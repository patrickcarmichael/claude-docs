**Navigation:** [← Previous](./05-create-a-completion.md) | [Index](./index.md) | Next →

---

# Crypto API

> Learn how to purchase OpenRouter credits using cryptocurrency. Complete guide to Coinbase integration, supported chains, and automated credit purchases.

You can purchase credits using cryptocurrency through our Coinbase integration. This can either happen through the UI, on your [credits page](https://openrouter.ai/settings/credits), or through our API as described below. While other forms of payment are possible, this guide specifically shows how to pay with the chain's native token.

Headless credit purchases involve three steps:

1. Getting the calldata for a new credit purchase
2. Sending a transaction on-chain using that data
3. Detecting low account balance, and purchasing more

## Getting Credit Purchase Calldata

Make a POST request to `/api/v1/credits/coinbase` to create a new charge. You'll include the amount of credits you want to purchase (in USD, up to \${maxCryptoDollarPurchase}), the address you'll be sending the transaction from, and the EVM chain ID of the network you'll be sending on.

Currently, we only support the following chains (mainnet only):

* Ethereum ({SupportedChainIDs.Ethereum})
* Polygon ({SupportedChainIDs.Polygon})
* Base ({SupportedChainIDs.Base}) ***recommended***

```typescript
const response = await fetch('https://openrouter.ai/api/v1/credits/coinbase', {
  method: 'POST',
  headers: {
    Authorization: 'Bearer <OPENROUTER_API_KEY>',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    amount: 10, // Target credit amount in USD
    sender: '0x9a85CB3bfd494Ea3a8C9E50aA6a3c1a7E8BACE11',
    chain_id: 8453,
  }),
});
const responseJSON = await response.json();
```

The response includes the charge details and transaction data needed to execute the on-chain payment:

```json
{
  "data": {
    "id": "...",
    "created_at": "2024-01-01T00:00:00Z",
    "expires_at": "2024-01-01T01:00:00Z",
    "web3_data": {
      "transfer_intent": {
        "metadata": {
          "chain_id": 8453,
          "contract_address": "0x03059433bcdb6144624cc2443159d9445c32b7a8",
          "sender": "0x9a85CB3bfd494Ea3a8C9E50aA6a3c1a7E8BACE11"
        },
        "call_data": {
          "recipient_amount": "...",
          "deadline": "...",
          "recipient": "...",
          "recipient_currency": "...",
          "refund_destination": "...",
          "fee_amount": "...",
          "id": "...",
          "operator": "...",
          "signature": "...",
          "prefix": "..."
        }
      }
    }
  }
}
```

## Sending the Transaction

You can use [viem](https://viem.sh) (or another similar evm client) to execute the transaction on-chain.

In this example, we'll be fulfilling the charge using the [swapAndTransferUniswapV3Native()](https://github.com/coinbase/commerce-onchain-payment-protocol/blob/d891289bd1f41bb95f749af537f2b6a36b17f889/contracts/interfaces/ITransfers.sol#L168-L171) function. Other methods of swapping are also available, and you can learn more by checking out Coinbase's [onchain payment protocol here](https://github.com/coinbase/commerce-onchain-payment-protocol/tree/master). Note, if you are trying to pay in a less common ERC-20, there is added complexity in needing to make sure that there is sufficient liquidity in the pool to swap the tokens.

```typescript
import { createPublicClient, createWalletClient, http, parseEther } from 'viem';
import { privateKeyToAccount } from 'viem/accounts';
import { base } from 'viem/chains';

// The ABI for Coinbase's onchain payment protocol
const abi = [
  {
    inputs: [
      {
        internalType: 'contract IUniversalRouter',
        name: '_uniswap',
        type: 'address',
      },
      { internalType: 'contract Permit2', name: '_permit2', type: 'address' },
      { internalType: 'address', name: '_initialOperator', type: 'address' },
      {
        internalType: 'address',
        name: '_initialFeeDestination',
        type: 'address',
      },
      {
        internalType: 'contract IWrappedNativeCurrency',
        name: '_wrappedNativeCurrency',
        type: 'address',
      },
    ],
    stateMutability: 'nonpayable',
    type: 'constructor',
  },
  { inputs: [], name: 'AlreadyProcessed', type: 'error' },
  { inputs: [], name: 'ExpiredIntent', type: 'error' },
  {
    inputs: [
      { internalType: 'address', name: 'attemptedCurrency', type: 'address' },
    ],
    name: 'IncorrectCurrency',
    type: 'error',
  },
  { inputs: [], name: 'InexactTransfer', type: 'error' },
  {
    inputs: [{ internalType: 'uint256', name: 'difference', type: 'uint256' }],
    name: 'InsufficientAllowance',
    type: 'error',
  },
  {
    inputs: [{ internalType: 'uint256', name: 'difference', type: 'uint256' }],
    name: 'InsufficientBalance',
    type: 'error',
  },
  {
    inputs: [{ internalType: 'int256', name: 'difference', type: 'int256' }],
    name: 'InvalidNativeAmount',
    type: 'error',
  },
  { inputs: [], name: 'InvalidSignature', type: 'error' },
  { inputs: [], name: 'InvalidTransferDetails', type: 'error' },
  {
    inputs: [
      { internalType: 'address', name: 'recipient', type: 'address' },
      { internalType: 'uint256', name: 'amount', type: 'uint256' },
      { internalType: 'bool', name: 'isRefund', type: 'bool' },
      { internalType: 'bytes', name: 'data', type: 'bytes' },
    ],
    name: 'NativeTransferFailed',
    type: 'error',
  },
  { inputs: [], name: 'NullRecipient', type: 'error' },
  { inputs: [], name: 'OperatorNotRegistered', type: 'error' },
  { inputs: [], name: 'PermitCallFailed', type: 'error' },
  {
    inputs: [{ internalType: 'bytes', name: 'reason', type: 'bytes' }],
    name: 'SwapFailedBytes',
    type: 'error',
  },
  {
    inputs: [{ internalType: 'string', name: 'reason', type: 'string' }],
    name: 'SwapFailedString',
    type: 'error',
  },
  {
    anonymous: false,
    inputs: [
      {
        indexed: false,
        internalType: 'address',
        name: 'operator',
        type: 'address',
      },
      {
        indexed: false,
        internalType: 'address',
        name: 'feeDestination',
        type: 'address',
      },
    ],
    name: 'OperatorRegistered',
    type: 'event',
  },
  {
    anonymous: false,
    inputs: [
      {
        indexed: false,
        internalType: 'address',
        name: 'operator',
        type: 'address',
      },
    ],
    name: 'OperatorUnregistered',
    type: 'event',
  },
  {
    anonymous: false,
    inputs: [
      {
        indexed: true,
        internalType: 'address',
        name: 'previousOwner',
        type: 'address',
      },
      {
        indexed: true,
        internalType: 'address',
        name: 'newOwner',
        type: 'address',
      },
    ],
    name: 'OwnershipTransferred',
    type: 'event',
  },
  {
    anonymous: false,
    inputs: [
      {
        indexed: false,
        internalType: 'address',
        name: 'account',
        type: 'address',
      },
    ],
    name: 'Paused',
    type: 'event',
  },
  {
    anonymous: false,
    inputs: [
      {
        indexed: true,
        internalType: 'address',
        name: 'operator',
        type: 'address',
      },
      { indexed: false, internalType: 'bytes16', name: 'id', type: 'bytes16' },
      {
        indexed: false,
        internalType: 'address',
        name: 'recipient',
        type: 'address',
      },
      {
        indexed: false,
        internalType: 'address',
        name: 'sender',
        type: 'address',
      },
      {
        indexed: false,
        internalType: 'uint256',
        name: 'spentAmount',
        type: 'uint256',
      },
      {
        indexed: false,
        internalType: 'address',
        name: 'spentCurrency',
        type: 'address',
      },
    ],
    name: 'Transferred',
    type: 'event',
  },
  {
    anonymous: false,
    inputs: [
      {
        indexed: false,
        internalType: 'address',
        name: 'account',
        type: 'address',
      },
    ],
    name: 'Unpaused',
    type: 'event',
  },
  {
    inputs: [],
    name: 'owner',
    outputs: [{ internalType: 'address', name: '', type: 'address' }],
    stateMutability: 'view',
    type: 'function',
  },
  {
    inputs: [],
    name: 'pause',
    outputs: [],
    stateMutability: 'nonpayable',
    type: 'function',
  },
  {
    inputs: [],
    name: 'paused',
    outputs: [{ internalType: 'bool', name: '', type: 'bool' }],
    stateMutability: 'view',
    type: 'function',
  },
  {
    inputs: [],
    name: 'permit2',
    outputs: [{ internalType: 'contract Permit2', name: '', type: 'address' }],
    stateMutability: 'view',
    type: 'function',
  },
  {
    inputs: [],
    name: 'registerOperator',
    outputs: [],
    stateMutability: 'nonpayable',
    type: 'function',
  },
  {
    inputs: [
      { internalType: 'address', name: '_feeDestination', type: 'address' },
    ],
    name: 'registerOperatorWithFeeDestination',
    outputs: [],
    stateMutability: 'nonpayable',
    type: 'function',
  },
  {
    inputs: [],
    name: 'renounceOwnership',
    outputs: [],
    stateMutability: 'nonpayable',
    type: 'function',
  },
  {
    inputs: [{ internalType: 'address', name: 'newSweeper', type: 'address' }],
    name: 'setSweeper',
    outputs: [],
    stateMutability: 'nonpayable',
    type: 'function',
  },
  {
    inputs: [
      {
        components: [
          { internalType: 'uint256', name: 'recipientAmount', type: 'uint256' },
          { internalType: 'uint256', name: 'deadline', type: 'uint256' },
          {
            internalType: 'address payable',
            name: 'recipient',
            type: 'address',
          },
          {
            internalType: 'address',
            name: 'recipientCurrency',
            type: 'address',
          },
          {
            internalType: 'address',
            name: 'refundDestination',
            type: 'address',
          },
          { internalType: 'uint256', name: 'feeAmount', type: 'uint256' },
          { internalType: 'bytes16', name: 'id', type: 'bytes16' },
          { internalType: 'address', name: 'operator', type: 'address' },
          { internalType: 'bytes', name: 'signature', type: 'bytes' },
          { internalType: 'bytes', name: 'prefix', type: 'bytes' },
        ],
        internalType: 'struct TransferIntent',
        name: '_intent',
        type: 'tuple',
      },
      {
        components: [
          { internalType: 'address', name: 'owner', type: 'address' },
          { internalType: 'bytes', name: 'signature', type: 'bytes' },
        ],
        internalType: 'struct EIP2612SignatureTransferData',
        name: '_signatureTransferData',
        type: 'tuple',
      },
    ],
    name: 'subsidizedTransferToken',
    outputs: [],
    stateMutability: 'nonpayable',
    type: 'function',
  },
  {
    inputs: [
      {
        components: [
          { internalType: 'uint256', name: 'recipientAmount', type: 'uint256' },
          { internalType: 'uint256', name: 'deadline', type: 'uint256' },
          {
            internalType: 'address payable',
            name: 'recipient',
            type: 'address',
          },
          {
            internalType: 'address',
            name: 'recipientCurrency',
            type: 'address',
          },
          {
            internalType: 'address',
            name: 'refundDestination',
            type: 'address',
          },
          { internalType: 'uint256', name: 'feeAmount', type: 'uint256' },
          { internalType: 'bytes16', name: 'id', type: 'bytes16' },
          { internalType: 'address', name: 'operator', type: 'address' },
          { internalType: 'bytes', name: 'signature', type: 'bytes' },
          { internalType: 'bytes', name: 'prefix', type: 'bytes' },
        ],
        internalType: 'struct TransferIntent',
        name: '_intent',
        type: 'tuple',
      },
      { internalType: 'uint24', name: 'poolFeesTier', type: 'uint24' },
    ],
    name: 'swapAndTransferUniswapV3Native',
    outputs: [],
    stateMutability: 'payable',
    type: 'function',
  },
  {
    inputs: [
      {
        components: [
          { internalType: 'uint256', name: 'recipientAmount', type: 'uint256' },
          { internalType: 'uint256', name: 'deadline', type: 'uint256' },
          {
            internalType: 'address payable',
            name: 'recipient',
            type: 'address',
          },
          {
            internalType: 'address',
            name: 'recipientCurrency',
            type: 'address',
          },
          {
            internalType: 'address',
            name: 'refundDestination',
            type: 'address',
          },
          { internalType: 'uint256', name: 'feeAmount', type: 'uint256' },
          { internalType: 'bytes16', name: 'id', type: 'bytes16' },
          { internalType: 'address', name: 'operator', type: 'address' },
          { internalType: 'bytes', name: 'signature', type: 'bytes' },
          { internalType: 'bytes', name: 'prefix', type: 'bytes' },
        ],
        internalType: 'struct TransferIntent',
        name: '_intent',
        type: 'tuple',
      },
      {
        components: [
          {
            components: [
              {
                components: [
                  { internalType: 'address', name: 'token', type: 'address' },
                  { internalType: 'uint256', name: 'amount', type: 'uint256' },
                ],
                internalType: 'struct ISignatureTransfer.TokenPermissions',
                name: 'permitted',
                type: 'tuple',
              },
              { internalType: 'uint256', name: 'nonce', type: 'uint256' },
              { internalType: 'uint256', name: 'deadline', type: 'uint256' },
            ],
            internalType: 'struct ISignatureTransfer.PermitTransferFrom',
            name: 'permit',
            type: 'tuple',
          },
          {
            components: [
              { internalType: 'address', name: 'to', type: 'address' },
              {
                internalType: 'uint256',
                name: 'requestedAmount',
                type: 'uint256',
              },
            ],
            internalType: 'struct ISignatureTransfer.SignatureTransferDetails',
            name: 'transferDetails',
            type: 'tuple',
          },
          { internalType: 'bytes', name: 'signature', type: 'bytes' },
        ],
        internalType: 'struct Permit2SignatureTransferData',
        name: '_signatureTransferData',
        type: 'tuple',
      },
      { internalType: 'uint24', name: 'poolFeesTier', type: 'uint24' },
    ],
    name: 'swapAndTransferUniswapV3Token',
    outputs: [],
    stateMutability: 'nonpayable',
    type: 'function',
  },
  {
    inputs: [
      {
        components: [
          { internalType: 'uint256', name: 'recipientAmount', type: 'uint256' },
          { internalType: 'uint256', name: 'deadline', type: 'uint256' },
          {
            internalType: 'address payable',
            name: 'recipient',
            type: 'address',
          },
          {
            internalType: 'address',
            name: 'recipientCurrency',
            type: 'address',
          },
          {
            internalType: 'address',
            name: 'refundDestination',
            type: 'address',
          },
          { internalType: 'uint256', name: 'feeAmount', type: 'uint256' },
          { internalType: 'bytes16', name: 'id', type: 'bytes16' },
          { internalType: 'address', name: 'operator', type: 'address' },
          { internalType: 'bytes', name: 'signature', type: 'bytes' },
          { internalType: 'bytes', name: 'prefix', type: 'bytes' },
        ],
        internalType: 'struct TransferIntent',
        name: '_intent',
        type: 'tuple',
      },
      { internalType: 'address', name: '_tokenIn', type: 'address' },
      { internalType: 'uint256', name: 'maxWillingToPay', type: 'uint256' },
      { internalType: 'uint24', name: 'poolFeesTier', type: 'uint24' },
    ],
    name: 'swapAndTransferUniswapV3TokenPreApproved',
    outputs: [],
    stateMutability: 'nonpayable',
    type: 'function',
  },
  {
    inputs: [
      { internalType: 'address payable', name: 'destination', type: 'address' },
    ],
    name: 'sweepETH',
    outputs: [],
    stateMutability: 'nonpayable',
    type: 'function',
  },
  {
    inputs: [
      { internalType: 'address payable', name: 'destination', type: 'address' },
      { internalType: 'uint256', name: 'amount', type: 'uint256' },
    ],
    name: 'sweepETHAmount',
    outputs: [],
    stateMutability: 'nonpayable',
    type: 'function',
  },
  {
    inputs: [
      { internalType: 'address', name: '_token', type: 'address' },
      { internalType: 'address', name: 'destination', type: 'address' },
    ],
    name: 'sweepToken',
    outputs: [],
    stateMutability: 'nonpayable',
    type: 'function',
  },
  {
    inputs: [
      { internalType: 'address', name: '_token', type: 'address' },
      { internalType: 'address', name: 'destination', type: 'address' },
      { internalType: 'uint256', name: 'amount', type: 'uint256' },
    ],
    name: 'sweepTokenAmount',
    outputs: [],
    stateMutability: 'nonpayable',
    type: 'function',
  },
  {
    inputs: [],
    name: 'sweeper',
    outputs: [{ internalType: 'address', name: '', type: 'address' }],
    stateMutability: 'view',
    type: 'function',
  },
  {
    inputs: [
      {
        components: [
          { internalType: 'uint256', name: 'recipientAmount', type: 'uint256' },
          { internalType: 'uint256', name: 'deadline', type: 'uint256' },
          {
            internalType: 'address payable',
            name: 'recipient',
            type: 'address',
          },
          {
            internalType: 'address',
            name: 'recipientCurrency',
            type: 'address',
          },
          {
            internalType: 'address',
            name: 'refundDestination',
            type: 'address',
          },
          { internalType: 'uint256', name: 'feeAmount', type: 'uint256' },
          { internalType: 'bytes16', name: 'id', type: 'bytes16' },
          { internalType: 'address', name: 'operator', type: 'address' },
          { internalType: 'bytes', name: 'signature', type: 'bytes' },
          { internalType: 'bytes', name: 'prefix', type: 'bytes' },
        ],
        internalType: 'struct TransferIntent',
        name: '_intent',
        type: 'tuple',
      },
    ],
    name: 'transferNative',
    outputs: [],
    stateMutability: 'payable',
    type: 'function',
  },
  {
    inputs: [{ internalType: 'address', name: 'newOwner', type: 'address' }],
    name: 'transferOwnership',
    outputs: [],
    stateMutability: 'nonpayable',
    type: 'function',
  },
  {
    inputs: [
      {
        components: [
          { internalType: 'uint256', name: 'recipientAmount', type: 'uint256' },
          { internalType: 'uint256', name: 'deadline', type: 'uint256' },
          {
            internalType: 'address payable',
            name: 'recipient',
            type: 'address',
          },
          {
            internalType: 'address',
            name: 'recipientCurrency',
            type: 'address',
          },
          {
            internalType: 'address',
            name: 'refundDestination',
            type: 'address',
          },
          { internalType: 'uint256', name: 'feeAmount', type: 'uint256' },
          { internalType: 'bytes16', name: 'id', type: 'bytes16' },
          { internalType: 'address', name: 'operator', type: 'address' },
          { internalType: 'bytes', name: 'signature', type: 'bytes' },
          { internalType: 'bytes', name: 'prefix', type: 'bytes' },
        ],
        internalType: 'struct TransferIntent',
        name: '_intent',
        type: 'tuple',
      },
      {
        components: [
          {
            components: [
              {
                components: [
                  { internalType: 'address', name: 'token', type: 'address' },
                  { internalType: 'uint256', name: 'amount', type: 'uint256' },
                ],
                internalType: 'struct ISignatureTransfer.TokenPermissions',
                name: 'permitted',
                type: 'tuple',
              },
              { internalType: 'uint256', name: 'nonce', type: 'uint256' },
              { internalType: 'uint256', name: 'deadline', type: 'uint256' },
            ],
            internalType: 'struct ISignatureTransfer.PermitTransferFrom',
            name: 'permit',
            type: 'tuple',
          },
          {
            components: [
              { internalType: 'address', name: 'to', type: 'address' },
              {
                internalType: 'uint256',
                name: 'requestedAmount',
                type: 'uint256',
              },
            ],
            internalType: 'struct ISignatureTransfer.SignatureTransferDetails',
            name: 'transferDetails',
            type: 'tuple',
          },
          { internalType: 'bytes', name: 'signature', type: 'bytes' },
        ],
        internalType: 'struct Permit2SignatureTransferData',
        name: '_signatureTransferData',
        type: 'tuple',
      },
    ],
    name: 'transferToken',
    outputs: [],
    stateMutability: 'nonpayable',
    type: 'function',
  },
  {
    inputs: [
      {
        components: [
          { internalType: 'uint256', name: 'recipientAmount', type: 'uint256' },
          { internalType: 'uint256', name: 'deadline', type: 'uint256' },
          {
            internalType: 'address payable',
            name: 'recipient',
            type: 'address',
          },
          {
            internalType: 'address',
            name: 'recipientCurrency',
            type: 'address',
          },
          {
            internalType: 'address',
            name: 'refundDestination',
            type: 'address',
          },
          { internalType: 'uint256', name: 'feeAmount', type: 'uint256' },
          { internalType: 'bytes16', name: 'id', type: 'bytes16' },
          { internalType: 'address', name: 'operator', type: 'address' },
          { internalType: 'bytes', name: 'signature', type: 'bytes' },
          { internalType: 'bytes', name: 'prefix', type: 'bytes' },
        ],
        internalType: 'struct TransferIntent',
        name: '_intent',
        type: 'tuple',
      },
    ],
    name: 'transferTokenPreApproved',
    outputs: [],
    stateMutability: 'nonpayable',
    type: 'function',
  },
  {
    inputs: [],
    name: 'unpause',
    outputs: [],
    stateMutability: 'nonpayable',
    type: 'function',
  },
  {
    inputs: [],
    name: 'unregisterOperator',
    outputs: [],
    stateMutability: 'nonpayable',
    type: 'function',
  },
  {
    inputs: [
      {
        components: [
          { internalType: 'uint256', name: 'recipientAmount', type: 'uint256' },
          { internalType: 'uint256', name: 'deadline', type: 'uint256' },
          {
            internalType: 'address payable',
            name: 'recipient',
            type: 'address',
          },
          {
            internalType: 'address',
            name: 'recipientCurrency',
            type: 'address',
          },
          {
            internalType: 'address',
            name: 'refundDestination',
            type: 'address',
          },
          { internalType: 'uint256', name: 'feeAmount', type: 'uint256' },
          { internalType: 'bytes16', name: 'id', type: 'bytes16' },
          { internalType: 'address', name: 'operator', type: 'address' },
          { internalType: 'bytes', name: 'signature', type: 'bytes' },
          { internalType: 'bytes', name: 'prefix', type: 'bytes' },
        ],
        internalType: 'struct TransferIntent',
        name: '_intent',
        type: 'tuple',
      },
      {
        components: [
          {
            components: [
              {
                components: [
                  { internalType: 'address', name: 'token', type: 'address' },
                  { internalType: 'uint256', name: 'amount', type: 'uint256' },
                ],
                internalType: 'struct ISignatureTransfer.TokenPermissions',
                name: 'permitted',
                type: 'tuple',
              },
              { internalType: 'uint256', name: 'nonce', type: 'uint256' },
              { internalType: 'uint256', name: 'deadline', type: 'uint256' },
            ],
            internalType: 'struct ISignatureTransfer.PermitTransferFrom',
            name: 'permit',
            type: 'tuple',
          },
          {
            components: [
              { internalType: 'address', name: 'to', type: 'address' },
              {
                internalType: 'uint256',
                name: 'requestedAmount',
                type: 'uint256',
              },
            ],
            internalType: 'struct ISignatureTransfer.SignatureTransferDetails',
            name: 'transferDetails',
            type: 'tuple',
          },
          { internalType: 'bytes', name: 'signature', type: 'bytes' },
        ],
        internalType: 'struct Permit2SignatureTransferData',
        name: '_signatureTransferData',
        type: 'tuple',
      },
    ],
    name: 'unwrapAndTransfer',
    outputs: [],
    stateMutability: 'nonpayable',
    type: 'function',
  },
  {
    inputs: [
      {
        components: [
          { internalType: 'uint256', name: 'recipientAmount', type: 'uint256' },
          { internalType: 'uint256', name: 'deadline', type: 'uint256' },
          {
            internalType: 'address payable',
            name: 'recipient',
            type: 'address',
          },
          {
            internalType: 'address',
            name: 'recipientCurrency',
            type: 'address',
          },
          {
            internalType: 'address',
            name: 'refundDestination',
            type: 'address',
          },
          { internalType: 'uint256', name: 'feeAmount', type: 'uint256' },
          { internalType: 'bytes16', name: 'id', type: 'bytes16' },
          { internalType: 'address', name: 'operator', type: 'address' },
          { internalType: 'bytes', name: 'signature', type: 'bytes' },
          { internalType: 'bytes', name: 'prefix', type: 'bytes' },
        ],
        internalType: 'struct TransferIntent',
        name: '_intent',
        type: 'tuple',
      },
    ],
    name: 'unwrapAndTransferPreApproved',
    outputs: [],
    stateMutability: 'nonpayable',
    type: 'function',
  },
  {
    inputs: [
      {
        components: [
          { internalType: 'uint256', name: 'recipientAmount', type: 'uint256' },
          { internalType: 'uint256', name: 'deadline', type: 'uint256' },
          {
            internalType: 'address payable',
            name: 'recipient',
            type: 'address',
          },
          {
            internalType: 'address',
            name: 'recipientCurrency',
            type: 'address',
          },
          {
            internalType: 'address',
            name: 'refundDestination',
            type: 'address',
          },
          { internalType: 'uint256', name: 'feeAmount', type: 'uint256' },
          { internalType: 'bytes16', name: 'id', type: 'bytes16' },
          { internalType: 'address', name: 'operator', type: 'address' },
          { internalType: 'bytes', name: 'signature', type: 'bytes' },
          { internalType: 'bytes', name: 'prefix', type: 'bytes' },
        ],
        internalType: 'struct TransferIntent',
        name: '_intent',
        type: 'tuple',
      },
    ],
    name: 'wrapAndTransfer',
    outputs: [],
    stateMutability: 'payable',
    type: 'function',
  },
  { stateMutability: 'payable', type: 'receive' },
];

// Set up viem clients
const publicClient = createPublicClient({
  chain: base,
  transport: http(),
});
const account = privateKeyToAccount('0x...');
const walletClient = createWalletClient({
  chain: base,
  transport: http(),
  account,
});

// Use the calldata included in the charge response
const { contract_address } =
  responseJSON.data.web3_data.transfer_intent.metadata;
const call_data = responseJSON.data.web3_data.transfer_intent.call_data;

// When transacting in ETH, a pool fees tier of 500 (the lowest) is very
// likely to be sufficient. However, if you plan to swap with a different
// contract method, using less-common ERC-20 tokens, it is recommended to
// call that chain's Uniswap QuoterV2 contract to check its liquidity.
// Depending on the results, choose the lowest fee tier which has enough
// liquidity in the pool.
const poolFeesTier = 500;

// Simulate the transaction first to prevent most common revert reasons
const { request } = await publicClient.simulateContract({
  abi,
  account,
  address: contract_address,
  functionName: 'swapAndTransferUniswapV3Native',
  args: [
    {
      recipientAmount: BigInt(call_data.recipient_amount),
      deadline: BigInt(
        Math.floor(new Date(call_data.deadline).getTime() / 1000),
      ),
      recipient: call_data.recipient,
      recipientCurrency: call_data.recipient_currency,
      refundDestination: call_data.refund_destination,
      feeAmount: BigInt(call_data.fee_amount),
      id: call_data.id,
      operator: call_data.operator,
      signature: call_data.signature,
      prefix: call_data.prefix,
    },
    poolFeesTier,
  ],
  // Transaction value in ETH. You'll want to include a little extra to
  // ensure the transaction & swap is successful. All excess funds return
  // back to your sender address afterwards.
  value: parseEther('0.004'),
});

// Send the transaction on chain
const txHash = await walletClient.writeContract(request);
console.log('Transaction hash:', txHash);
```

Once the transaction succeeds on chain, we'll add credits to your account. You can track the transaction status using the returned transaction hash.

Credit purchases lower than \$500 will be immediately credited once the transaction is on chain. Above \$500, there is a \~15 minute confirmation delay, ensuring the chain does not re-org your purchase.

## Detecting Low Balance

While it is possible to simply run down the balance until your app starts receiving 402 error codes for insufficient credits, this gap in service while topping up might not be desirable.

To avoid this, you can periodically call the `GET /api/v1/credits` endpoint to check your available credits.

<CodeGroup>
  ```typescript title="TypeScript SDK"
  import { OpenRouter } from '@openrouter/sdk';

  const openRouter = new OpenRouter({
    apiKey: '<OPENROUTER_API_KEY>',
  });

  const credits = await openRouter.credits.get();
  console.log('Available credits:', credits.totalCredits - credits.totalUsage);
  ```

  ```typescript title="TypeScript (fetch)"
  const response = await fetch('https://openrouter.ai/api/v1/credits', {
    method: 'GET',
    headers: { Authorization: 'Bearer <OPENROUTER_API_KEY>' },
  });
  const { data } = await response.json();
  ```
</CodeGroup>

The response includes your total credits purchased and usage, where your current balance is the difference between the two:

```json
{
  "data": {
    "total_credits": 50.0,
    "total_usage": 42.0
  }
}
```

Note that these values are cached, and may be up to 60 seconds stale.


# OAuth PKCE

> Implement secure user authentication with OpenRouter using OAuth PKCE. Complete guide to setting up and managing OAuth authentication flows.

Users can connect to OpenRouter in one click using [Proof Key for Code Exchange (PKCE)](https://oauth.net/2/pkce/).

Here's a step-by-step guide:

## PKCE Guide

### Step 1: Send your user to OpenRouter

To start the PKCE flow, send your user to OpenRouter's `/auth` URL with a `callback_url` parameter pointing back to your site:

<CodeGroup>
  ```txt title="With S256 Code Challenge (Recommended)" wordWrap
  https://openrouter.ai/auth?callback_url=<YOUR_SITE_URL>&code_challenge=<CODE_CHALLENGE>&code_challenge_method=S256
  ```

  ```txt title="With Plain Code Challenge" wordWrap
  https://openrouter.ai/auth?callback_url=<YOUR_SITE_URL>&code_challenge=<CODE_CHALLENGE>&code_challenge_method=plain
  ```

  ```txt title="Without Code Challenge" wordWrap
  https://openrouter.ai/auth?callback_url=<YOUR_SITE_URL>
  ```
</CodeGroup>

The `code_challenge` parameter is optional but recommended.

Your user will be prompted to log in to OpenRouter and authorize your app. After authorization, they will be redirected back to your site with a `code` parameter in the URL:

![Alt text](file:22f4b2e3-1cfe-4419-a1c0-ae611c98040e)

<Tip title="Use SHA-256 for Maximum Security">
  For maximum security, set `code_challenge_method` to `S256`, and set `code_challenge` to the base64 encoding of the sha256 hash of `code_verifier`.

  For more info, [visit Auth0's docs](https://auth0.com/docs/get-started/authentication-and-authorization-flow/call-your-api-using-the-authorization-code-flow-with-pkce#parameters).
</Tip>

#### How to Generate a Code Challenge

The following example leverages the Web Crypto API and the Buffer API to generate a code challenge for the S256 method. You will need a bundler to use the Buffer API in the web browser:

<CodeGroup>
  ```typescript title="Generate Code Challenge"
  import { Buffer } from 'buffer';

  async function createSHA256CodeChallenge(input: string) {
    const encoder = new TextEncoder();
    const data = encoder.encode(input);
    const hash = await crypto.subtle.digest('SHA-256', data);
    return Buffer.from(hash).toString('base64url');
  }

  const codeVerifier = 'your-random-string';
  const generatedCodeChallenge = await createSHA256CodeChallenge(codeVerifier);
  ```
</CodeGroup>

#### Localhost Apps

If your app is a local-first app or otherwise doesn't have a public URL, it is recommended to test with `http://localhost:3000` as the callback and referrer URLs.

When moving to production, replace the localhost/private referrer URL with a public GitHub repo or a link to your project website.

### Step 2: Exchange the code for a user-controlled API key

After the user logs in with OpenRouter, they are redirected back to your site with a `code` parameter in the URL:

![Alt text](file:dd2980ed-1eea-4ed7-b37e-e4cc5cfaff5b)

Extract this code using the browser API:

<CodeGroup>
  ```typescript title="Extract Code"
  const urlParams = new URLSearchParams(window.location.search);
  const code = urlParams.get('code');
  ```
</CodeGroup>

Then use it to make an API call to `https://openrouter.ai/api/v1/auth/keys` to exchange the code for a user-controlled API key:

<CodeGroup>
  ```typescript title="Exchange Code"
  const response = await fetch('https://openrouter.ai/api/v1/auth/keys', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      code: '<CODE_FROM_QUERY_PARAM>',
      code_verifier: '<CODE_VERIFIER>', // If code_challenge was used
      code_challenge_method: '<CODE_CHALLENGE_METHOD>', // If code_challenge was used
    }),
  });

  const { key } = await response.json();
  ```
</CodeGroup>

And that's it for the PKCE flow!

### Step 3: Use the API key

Store the API key securely within the user's browser or in your own database, and use it to [make OpenRouter requests](/api-reference/completion).

<CodeGroup>
  ```typescript title="TypeScript SDK"
  import { OpenRouter } from '@openrouter/sdk';

  const openRouter = new OpenRouter({
    apiKey: key, // The key from Step 2
  });

  const completion = await openRouter.chat.send({
    model: 'openai/gpt-4o',
    messages: [
      {
        role: 'user',
        content: 'Hello!',
      },
    ],
    stream: false,
  });

  console.log(completion.choices[0].message);
  ```

  ```typescript title="TypeScript (fetch)"
  fetch('https://openrouter.ai/api/v1/chat/completions', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${key}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/gpt-4o',
      messages: [
        {
          role: 'user',
          content: 'Hello!',
        },
      ],
    }),
  });
  ```
</CodeGroup>

## Error Codes

* `400 Invalid code_challenge_method`: Make sure you're using the same code challenge method in step 1 as in step 2.
* `403 Invalid code or code_verifier`: Make sure your user is logged in to OpenRouter, and that `code_verifier` and `code_challenge_method` are correct.
* `405 Method Not Allowed`: Make sure you're using `POST` and `HTTPS` for your request.

## External Tools

* [PKCE Tools](https://example-app.com/pkce)
* [Online PKCE Generator](https://tonyxu-io.github.io/pkce-generator/)


# Using MCP Servers with OpenRouter

> Learn how to use MCP Servers with OpenRouter

MCP servers are a popular way of providing LLMs with tool calling abilities, and are an alternative to using OpenAI-compatible tool calling.

By converting MCP (Anthropic) tool definitions to OpenAI-compatible tool definitions, you can use MCP servers with OpenRouter.

In this example, we'll use [Anthropic's MCP client SDK](https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#writing-mcp-clients) to interact with the File System MCP, all with OpenRouter under the hood.

<Warning>
  Note that interacting with MCP servers is more complex than calling a REST
  endpoint. The MCP protocol is stateful and requires session management. The
  example below uses the MCP client SDK, but is still somewhat complex.
</Warning>

First, some setup. In order to run this you will need to pip install the packages, and create a `.env` file with OPENAI\_API\_KEY set. This example also assumes the directory `/Applications` exists.

```python
import asyncio
from typing import Optional
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()  # load environment variables from .env

MODEL = "anthropic/claude-3-7-sonnet"

SERVER_CONFIG = {
    "command": "npx",
    "args": ["-y",
              "@modelcontextprotocol/server-filesystem",
              f"/Applications/"],
    "env": None
}
```

Next, our helper function to convert MCP tool definitions to OpenAI tool definitions:

```python

def convert_tool_format(tool):
    converted_tool = {
        "type": "function",
        "function": {
            "name": tool.name,
            "description": tool.description,
            "parameters": {
                "type": "object",
                "properties": tool.inputSchema["properties"],
                "required": tool.inputSchema["required"]
            }
        }
    }
    return converted_tool

```

And, the MCP client itself; a regrettable \~100 lines of code. Note that the SERVER\_CONFIG is hard-coded into the client, but of course could be parameterized for other MCP servers.

```python
class MCPClient:
    def __init__(self):
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.openai = OpenAI(
            base_url="https://openrouter.ai/api/v1"
        )

    async def connect_to_server(self, server_config):
        server_params = StdioServerParameters(**server_config)
        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        self.stdio, self.write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))

        await self.session.initialize()

        # List available tools from the MCP server
        response = await self.session.list_tools()
        print("\nConnected to server with tools:", [tool.name for tool in response.tools])

        self.messages = []

    async def process_query(self, query: str) -> str:

        self.messages.append({
            "role": "user",
            "content": query
        })

        response = await self.session.list_tools()
        available_tools = [convert_tool_format(tool) for tool in response.tools]

        response = self.openai.chat.completions.create(
            model=MODEL,
            tools=available_tools,
            messages=self.messages
        )
        self.messages.append(response.choices[0].message.model_dump())

        final_text = []
        content = response.choices[0].message
        if content.tool_calls is not None:
            tool_name = content.tool_calls[0].function.name
            tool_args = content.tool_calls[0].function.arguments
            tool_args = json.loads(tool_args) if tool_args else {}

            # Execute tool call
            try:
                result = await self.session.call_tool(tool_name, tool_args)
                final_text.append(f"[Calling tool {tool_name} with args {tool_args}]")
            except Exception as e:
                print(f"Error calling tool {tool_name}: {e}")
                result = None

            self.messages.append({
                "role": "tool",
                "tool_call_id": content.tool_calls[0].id,
                "name": tool_name,
                "content": result.content
            })

            response = self.openai.chat.completions.create(
                model=MODEL,
                max_tokens=1000,
                messages=self.messages,
            )

            final_text.append(response.choices[0].message.content)
        else:
            final_text.append(content.content)

        return "\n".join(final_text)

    async def chat_loop(self):
        """Run an interactive chat loop"""
        print("\nMCP Client Started!")
        print("Type your queries or 'quit' to exit.")

        while True:
            try:
                query = input("\nQuery: ").strip()
                result = await self.process_query(query)
                print("Result:")
                print(result)

            except Exception as e:
                print(f"Error: {str(e)}")

    async def cleanup(self):
        await self.exit_stack.aclose()

async def main():
    client = MCPClient()
    try:
        await client.connect_to_server(SERVER_CONFIG)
        await client.chat_loop()
    finally:
        await client.cleanup()

if __name__ == "__main__":
    import sys
    asyncio.run(main())
```

Assembling all of the above code into mcp-client.py, you get a client that behaves as follows (some outputs truncated for brevity):

```bash
% python mcp-client.py

Secure MCP Filesystem Server running on stdio
Allowed directories: [ '/Applications' ]

Connected to server with tools: ['read_file', 'read_multiple_files', 'write_file'...]

MCP Client Started!
Type your queries or 'quit' to exit.

Query: Do I have microsoft office installed?

Result:
[Calling tool list_allowed_directories with args {}]
I can check if Microsoft Office is installed in the Applications folder:

Query: continue

Result:
[Calling tool search_files with args {'path': '/Applications', 'pattern': 'Microsoft'}]
Now let me check specifically for Microsoft Office applications:

Query: continue

Result:
I can see from the search results that Microsoft Office is indeed installed on your system.
The search found the following main Microsoft Office applications:

1. Microsoft Excel - /Applications/Microsoft Excel.app
2. Microsoft PowerPoint - /Applications/Microsoft PowerPoint.app
3. Microsoft Word - /Applications/Microsoft Word.app
4. OneDrive - /Applications/OneDrive.app (which includes Microsoft SharePoint integration)
```


# Organization Management

> Learn how to create and manage organizations on OpenRouter for team collaboration, shared credits, and centralized API management.

OpenRouter organizations enable teams and companies to collaborate effectively by sharing credits, managing API keys centrally, and tracking usage across all team members. Organizations are ideal for companies that want to pool resources, manage inference costs centrally, and maintain oversight of AI usage across their team.

## Getting Started with Organizations

### Creating an Organization

To create an organization:

1. Navigate to [Settings > Preferences](https://openrouter.ai/settings/preferences)
2. In the Organization section, click **Create Organization**
3. Follow the setup process to configure your organization details
4. Invite team members to join your organization

<Tip>
  You must have a verified email address to create an organization.
</Tip>

### Switching Between Personal and Organization Accounts

Once you're part of an organization, you can easily switch between your personal account and organization context:

* Use the **organization switcher** at the top of the web application
* When in organization mode, all actions (API usage, credit purchases, key management) are performed on behalf of the organization
* When in personal mode, you're working with your individual account resources

## Credit Management

### Shared Credit Pool

Organizations maintain a shared credit pool that offers several advantages:

* **Centralized Billing**: All credits purchased in the organization account can be used by any organization member
* **Simplified Accounting**: Track all AI inference costs in one place
* **Budget Control**: Administrators can manage spending and monitor usage across the entire team

### Admin-Only Credit Management

Only organization administrators can:

* Purchase credits for the organization
* View detailed billing information
* Manage payment methods and invoicing settings

<Warning>
  Regular organization members cannot purchase credits or access billing information. Contact your organization administrator for credit-related requests.
</Warning>

### Transferring Credits from Personal to Organization

If you need to transfer credits from your personal account to your organization account:

1. Email [support@openrouter.ai](mailto:support@openrouter.ai) with your request
2. Include your organization details and the amount you wish to transfer
3. Our support team will process the transfer manually

<Info>
  Credit transfers from personal to organization accounts require manual processing by our support team and cannot be done automatically through the interface.
</Info>

## API Key Management

Organizations provide flexible API key management with role-based permissions:

### Member Permissions

* **Create API Keys**: All organization members can create API keys
* **View Own Keys**: Members can only view and manage API keys they created
* **Use Organization Keys**: Keys created by any organization member can be used by all members
* **Shared Usage**: API usage from any organization key is billed to the organization's credit pool

### Administrator Permissions

* **View All Keys**: Administrators can view all API keys created within the organization
* **Manage All Keys**: Full access to edit, disable, or delete any organization API key
* **Monitor Usage**: Access to detailed usage analytics for all organization keys

<Tip>
  When creating API keys within an organization, consider using descriptive names that indicate the key's purpose or the team member responsible for it.
</Tip>

## Activity and Usage Tracking

### Organization-Wide Activity Feed

When viewing your activity feed while in organization context, you'll see:

* **All Member Activity**: Usage data from all organization members appears in the activity feed
* **Metadata Only**: Activity shows model usage, costs, and request metadata
* **Key Filtering**: Activity can be filtered by a specific API key to view usage for that key only

<Warning>
  **Known Limitation**: The activity feed currently shows all organization member activity when in organization context, not just your individual activity. Usage metadata (model used, cost, timing) is visible to all organization members.
</Warning>

### Usage Analytics

Organizations benefit from comprehensive usage analytics:

* Track spending across all team members
* Monitor model usage patterns
* Identify cost optimization opportunities
* Generate reports for budget planning

## Administrative Controls

### Admin-Only Settings

Organization administrators have exclusive access to:

* **Provider Settings**: Configure preferred model providers and routing preferences
* **Privacy Settings**: Manage data retention and privacy policies for the organization
* **Member Management**: Add, remove, and manage member roles
* **Billing Configuration**: Set up invoicing, payment methods, and billing contacts

### Member Role Management

Organizations support role-based access control:

* **Admin**: Full access to all organization features and settings
* **Member**: Access to create keys, use organization resources, and view own activity

## Use Cases and Benefits

### For Development Teams

* **Shared Resources**: Pool credits across multiple developers and projects
* **Centralized Management**: Manage all API keys and usage from a single dashboard
* **Cost Tracking**: Monitor spending per project or team member
* **Simplified Onboarding**: New team members can immediately access organization resources

### For Companies

* **Budget Control**: Administrators control spending and resource allocation
* **Compliance**: Centralized logging and usage tracking for audit purposes
* **Scalability**: Easy to add new team members and projects
* **Cost Optimization**: Identify usage patterns and optimize model selection

### For Research Organizations

* **Resource Sharing**: Share expensive model access across research teams
* **Usage Monitoring**: Track research spending and resource utilization
* **Collaboration**: Enable seamless collaboration on AI projects
* **Reporting**: Generate usage reports for grant applications and budget planning

## Frequently Asked Questions

<AccordionGroup>
  <Accordion title="Can I convert my personal account to an organization?">
    No, organizations are separate entities. You'll need to create a new organization and transfer resources as needed. Contact [support@openrouter.ai](mailto:support@openrouter.ai) for assistance with credit transfers.
  </Accordion>

  <Accordion title="How many members can an organization have?">
    An organization can only have 10 members. Contact support if you need more.
  </Accordion>

  <Accordion title="Can organization members see each other's usage data?">
    Organization members can see usage metadata (model used, cost, timing) for all organization activity in the activity feed. OpenRouter does not store prompts or responses.
  </Accordion>

  <Accordion title="What happens if I leave an organization?">
    When you leave an organization, you lose access to organization resources, credits, and API keys. Your personal account remains unaffected.
  </Accordion>

  <Accordion title="Can I be a member of multiple organizations?">
    Yes, you can be a member of multiple organizations and switch between them using the organization switcher.
  </Accordion>
</AccordionGroup>

## Getting Help

If you need assistance with organization management:

* **General Questions**: Check our [FAQ](/docs/faq) for common questions
* **Technical Support**: Email [support@openrouter.ai](mailto:support@openrouter.ai)
* **Credit Transfers**: Email [support@openrouter.ai](mailto:support@openrouter.ai) with transfer requests
* **Enterprise Sales**: Contact our sales team for large organization needs

Organizations make it easy to collaborate on AI projects while maintaining control over costs and resources. Get started by creating your organization today!


# Provider Integration

> Learn how to integrate your AI models with OpenRouter. Complete guide for providers to make their models available through OpenRouter's unified API.

## For Providers

If you'd like to be a model provider and sell inference on OpenRouter, [fill out our form](https://openrouter.ai/how-to-list) to get started.

To be eligible to provide inference on OpenRouter you must have the following:

### 1. List Models Endpoint

You must implement an endpoint that returns all models that should be served by OpenRouter. At this endpoint, please return a list of all available models on your platform. Below is an example of the response format:

```json
{
  "data": [
    {
      // Required
      "id": "anthropic/claude-sonnet-4",
      "hugging_face_id": "", // required if the model is on Hugging Face
      "name": "Anthropic: Claude Sonnet 4",
      "created": 1690502400,
      "input_modalities": ["text", "image", "file"],
      "output_modalities": ["text", "image", "file"],
      "quantization": "fp8",
      "context_length": 1000000,
      "max_output_length": 128000,
      "pricing": {
        "prompt": "0.000008", // pricing per 1 token
        "completion": "0.000024", // pricing per 1 token
        "image": "0", // pricing per 1 image
        "request": "0", // pricing per 1 request
        "input_cache_reads": "0", // pricing per 1 token
        "input_cache_writes": "0" // pricing per 1 token
      },
      "supported_sampling_parameters": ["temperature", "stop"],
      "supported_features": [
        "tools",
        "json_mode",
        "structured_outputs",
        "web_search",
        "reasoning"
      ],
      // Optional
      "description": "Anthropic's flagship model...",
      "openrouter": {
        "slug": "anthropic/claude-sonnet-4"
      },
      "datacenters": [
        {
          "country_code": "US" // `Iso3166Alpha2Code`
        }
      ]
    }
  ]
}
```

NOTE: `pricing` fields are in string format to avoid floating point precision issues, and must be in USD.

Valid quantization values are: `int4`, `int8`, `fp4`, `fp6`, `fp8`, `fp16`, `bf16`, `fp32`.

Valid sampling parameters are: `temperature`, `top_p`, `top_k`, `repetition_penalty`, `frequency_penalty`, `presence_penalty`, `stop`, `seed`.

Valid features are: `tools`, `json_mode`, `structured_outputs`, `web_search`, `reasoning`.

### 2. Auto Top Up or Invoicing

For OpenRouter to use the provider we must be able to pay for inference automatically. This can be done via auto top up or invoicing.

### 3. Uptime Monitoring & Traffic Routing

OpenRouter automatically monitors provider reliability and adjusts traffic routing based on uptime metrics. Your endpoint's uptime is calculated as: **successful requests ÷ total requests** (excluding user errors).

**Errors that affect your uptime:**

* Authentication issues (401)
* Payment failures (402)
* Model not found (404)
* All server errors (500+)
* Mid-stream errors
* Successful requests with error finish reasons

**Errors that DON'T affect uptime:**

* Bad requests (400) - user input errors
* Oversized payloads (413) - user input errors
* Rate limiting (429) - tracked separately
* Geographic restrictions (403) - tracked separately

**Traffic routing thresholds:**

* **Minimum data**: 100+ requests required before uptime calculation begins
* **Normal routing**: 95%+ uptime
* **Degraded status**: 80-94% uptime → receives lower priority
* **Down status**: \<80% uptime → only used as fallback

This system ensures traffic automatically flows to the most reliable providers while giving temporary issues time to resolve.


# Reasoning Tokens

> Learn how to use reasoning tokens to enhance AI model outputs. Implement step-by-step reasoning traces for better decision making and transparency.

For models that support it, the OpenRouter API can return **Reasoning Tokens**, also known as thinking tokens. OpenRouter normalizes the different ways of customizing the amount of reasoning tokens that the model will use, providing a unified interface across different providers.

Reasoning tokens provide a transparent look into the reasoning steps taken by a model. Reasoning tokens are considered output tokens and charged accordingly.

Reasoning tokens are included in the response by default if the model decides to output them. Reasoning tokens will appear in the `reasoning` field of each message, unless you decide to exclude them.

<Note title="Some reasoning models do not return their reasoning tokens">
  While most models and providers make reasoning tokens available in the
  response, some (like the OpenAI o-series and Gemini Flash Thinking) do not.
</Note>

## Controlling Reasoning Tokens

You can control reasoning tokens in your requests using the `reasoning` parameter:

```json
{
  "model": "your-model",
  "messages": [],
  "reasoning": {
    // One of the following (not both):
    "effort": "high", // Can be "high", "medium", or "low" (OpenAI-style)
    "max_tokens": 2000, // Specific token limit (Anthropic-style)

    // Optional: Default is false. All models support this.
    "exclude": false, // Set to true to exclude reasoning tokens from response

    // Or enable reasoning with the default parameters:
    "enabled": true // Default: inferred from `effort` or `max_tokens`
  }
}
```

The `reasoning` config object consolidates settings for controlling reasoning strength across different models. See the Note for each option below to see which models are supported and how other models will behave.

### Max Tokens for Reasoning

<Note title="Supported models">
  Currently supported by:

  <ul>
    <li>
      Gemini thinking models
    </li>

    <li>
      Anthropic reasoning models (by using the <code>reasoning.max\_tokens</code>{' '}
      parameter)
    </li>

    <li>
      Some Alibaba Qwen thinking models (mapped to 

      <code>thinking_budget</code>

      )
    </li>
  </ul>

  For Alibaba, support varies by model — please check the individual model descriptions to confirm
  whether <code>reasoning.max\_tokens</code> (via <code>thinking\_budget</code>) is available.
</Note>

For models that support reasoning token allocation, you can control it like this:

* `"max_tokens": 2000` - Directly specifies the maximum number of tokens to use for reasoning

For models that only support `reasoning.effort` (see below), the `max_tokens` value will be used to determine the effort level.

### Reasoning Effort Level

<Note title="Supported models">
  Currently supported by OpenAI reasoning models (o1 series, o3 series, GPT-5 series) and Grok models
</Note>

* `"effort": "high"` - Allocates a large portion of tokens for reasoning (approximately 80% of max\_tokens)
* `"effort": "medium"` - Allocates a moderate portion of tokens (approximately 50% of max\_tokens)
* `"effort": "low"` - Allocates a smaller portion of tokens (approximately 20% of max\_tokens)

For models that only support `reasoning.max_tokens`, the effort level will be set based on the percentages above.

### Excluding Reasoning Tokens

If you want the model to use reasoning internally but not include it in the response:

* `"exclude": true` - The model will still use reasoning, but it won't be returned in the response

Reasoning tokens will appear in the `reasoning` field of each message.

### Enable Reasoning with Default Config

To enable reasoning with the default parameters:

* `"enabled": true` - Enables reasoning at the "medium" effort level with no exclusions.

## Legacy Parameters

For backward compatibility, OpenRouter still supports the following legacy parameters:

* `include_reasoning: true` - Equivalent to `reasoning: {}`
* `include_reasoning: false` - Equivalent to `reasoning: { exclude: true }`

However, we recommend using the new unified `reasoning` parameter for better control and future compatibility.

## Examples

### Basic Usage with Reasoning Tokens

<Template
  data={{
  API_KEY_REF,
  MODEL: "openai/o3-mini"
}}
>
  <CodeGroup>
    ```typescript title="TypeScript SDK"
    import { OpenRouter } from '@openrouter/sdk';

    const openRouter = new OpenRouter({
      apiKey: '{{API_KEY_REF}}',
    });

    const response = await openRouter.chat.send({
      model: '{{MODEL}}',
      messages: [
        {
          role: 'user',
          content: "How would you build the world's tallest skyscraper?",
        },
      ],
      reasoning: {
        effort: 'high',
      },
      stream: false,
    });

    console.log('REASONING:', response.choices[0].message.reasoning);
    console.log('CONTENT:', response.choices[0].message.content);
    ```

    ```python title="Python (OpenAI SDK)"
    from openai import OpenAI

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="{{API_KEY_REF}}",
    )

    response = client.chat.completions.create(
        model="{{MODEL}}",
        messages=[
            {"role": "user", "content": "How would you build the world's tallest skyscraper?"}
        ],
        extra_body={
            "reasoning": {
                "effort": "high"
            }
        },
    )

    msg = response.choices[0].message
    print(getattr(msg, "reasoning", None))
    ```

    ```typescript title="TypeScript (OpenAI SDK)"
    import OpenAI from 'openai';

    const openai = new OpenAI({
      baseURL: 'https://openrouter.ai/api/v1',
      apiKey: '{{API_KEY_REF}}',
    });

    async function getResponseWithReasoning() {
      const response = await openai.chat.completions.create({
        model: '{{MODEL}}',
        messages: [
          {
            role: 'user',
            content: "How would you build the world's tallest skyscraper?",
          },
        ],
        reasoning: {
          effort: 'high',
        },
      });

      type ORChatMessage = (typeof response)['choices'][number]['message'] & {
        reasoning?: string;
        reasoning_details?: unknown;
      };

      const msg = response.choices[0].message as ORChatMessage;
      console.log('REASONING:', msg.reasoning);
      console.log('CONTENT:', msg.content);
    }

    getResponseWithReasoning();
    ```
  </CodeGroup>
</Template>

### Using Max Tokens for Reasoning

For models that support direct token allocation (like Anthropic models), you can specify the exact number of tokens to use for reasoning:

<Template
  data={{
  API_KEY_REF,
  MODEL: "anthropic/claude-3.7-sonnet"
}}
>
  <CodeGroup>
    ```python Python
    from openai import OpenAI

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="{{API_KEY_REF}}",
    )

    response = client.chat.completions.create(
        model="{{MODEL}}",
        messages=[
            {"role": "user", "content": "What's the most efficient algorithm for sorting a large dataset?"}
        ],
        extra_body={
            "reasoning": {
                "max_tokens": 2000
            }
        },
    )

    msg = response.choices[0].message
    print(getattr(msg, "reasoning", None))
    print(getattr(msg, "content", None))
    ```

    ```typescript TypeScript
    import OpenAI from 'openai';

    const openai = new OpenAI({
      baseURL: 'https://openrouter.ai/api/v1',
      apiKey: '{{API_KEY_REF}}',
    });

    async function getResponseWithReasoning() {
      const response = await openai.chat.completions.create({
        model: '{{MODEL}}',
        messages: [
          {
            role: 'user',
            content: "How would you build the world's tallest skyscraper?",
          },
        ],
        reasoning: {
          max_tokens: 2000,
        },
      });

      type ORChatMessage = (typeof response)['choices'][number]['message'] & {
        reasoning?: string;
      };
      const msg = response.choices[0].message as ORChatMessage;

      console.log('REASONING:', msg.reasoning);
      console.log('CONTENT:', msg.content);
    }

    getResponseWithReasoning();
    ```
  </CodeGroup>
</Template>

### Excluding Reasoning Tokens from Response

If you want the model to use reasoning internally but not include it in the response:

<Template
  data={{
  API_KEY_REF,
  MODEL: "deepseek/deepseek-r1"
}}
>
  <CodeGroup>
    ```python Python
    from openai import OpenAI

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="{{API_KEY_REF}}",
    )

    response = client.chat.completions.create(
        model="{{MODEL}}",
        messages=[
            {"role": "user", "content": "Explain quantum computing in simple terms."}
        ],
        extra_body={
            "reasoning": {
                "effort": "high",
                "exclude": True
            }
        },
    )

    msg = response.choices[0].message
    print(getattr(msg, "content", None))
    ```

    ```typescript TypeScript
    import OpenAI from 'openai';

    const openai = new OpenAI({
      baseURL: 'https://openrouter.ai/api/v1',
      apiKey: '{{API_KEY_REF}}',
    });

    async function getResponseWithReasoning() {
      const response = await openai.chat.completions.create({
        model: '{{MODEL}}',
        messages: [
          {
            role: 'user',
            content: "How would you build the world's tallest skyscraper?",
          },
        ],
        reasoning: {
          effort: 'high',
          exclude: true,
        },
      });

      const msg = response.choices[0].message as {
        content?: string | null;
      };
      console.log('CONTENT:', msg.content);
    }

    getResponseWithReasoning();
    ```
  </CodeGroup>
</Template>

### Advanced Usage: Reasoning Chain-of-Thought

This example shows how to use reasoning tokens in a more complex workflow. It injects one model's reasoning into another model to improve its response quality:

<Template
  data={{
  API_KEY_REF,
}}
>
  <CodeGroup>
    ```python Python
    from openai import OpenAI

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="{{API_KEY_REF}}",
    )

    question = "Which is bigger: 9.11 or 9.9?"

    def do_req(model: str, content: str, reasoning_config: dict | None = None):
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": content}],
            "stop": "</think>",
        }
        if reasoning_config:
            payload.update(reasoning_config)
        return client.chat.completions.create(**payload)

    # Get reasoning from a capable model
    content = f"{question} Please think this through, but don't output an answer"
    reasoning_response = do_req("deepseek/deepseek-r1", content)
    reasoning = getattr(reasoning_response.choices[0].message, "reasoning", "")

    # Let's test! Here's the naive response:
    simple_response = do_req("openai/gpt-4o-mini", question)
    print(getattr(simple_response.choices[0].message, "content", None))

    # Here's the response with the reasoning token injected:
    content = f"{question}. Here is some context to help you: {reasoning}"
    smart_response = do_req("openai/gpt-4o-mini", content)
    print(getattr(smart_response.choices[0].message, "content", None))
    ```

    ```typescript TypeScript
    import OpenAI from 'openai';

    const openai = new OpenAI({
      baseURL: 'https://openrouter.ai/api/v1',
      apiKey: '{{API_KEY_REF}}',
    });

    async function doReq(model, content, reasoningConfig) {
      const payload = {
        model,
        messages: [{ role: 'user', content }],
        stop: '</think>',
        ...reasoningConfig,
      };

      return openai.chat.completions.create(payload);
    }

    async function getResponseWithReasoning() {
      const question = 'Which is bigger: 9.11 or 9.9?';
      const reasoningResponse = await doReq(
        'deepseek/deepseek-r1',
        `${question} Please think this through, but don't output an answer`,
      );
      const reasoning = reasoningResponse.choices[0].message.reasoning;

      // Let's test! Here's the naive response:
      const simpleResponse = await doReq('openai/gpt-4o-mini', question);
      console.log(simpleResponse.choices[0].message.content);

      // Here's the response with the reasoning token injected:
      const content = `${question}. Here is some context to help you: ${reasoning}`;
      const smartResponse = await doReq('openai/gpt-4o-mini', content);
      console.log(smartResponse.choices[0].message.content);
    }

    getResponseWithReasoning();
    ```
  </CodeGroup>
</Template>

## Provider-Specific Reasoning Implementation

### Anthropic Models with Reasoning Tokens

The latest Claude models, such as [anthropic/claude-3.7-sonnet](https://openrouter.ai/anthropic/claude-3.7-sonnet), support working with and returning reasoning tokens.

You can enable reasoning on Anthropic models **only** using the unified `reasoning` parameter with either `effort` or `max_tokens`.

**Note:** The `:thinking` variant is no longer supported for Anthropic models. Use the `reasoning` parameter instead.

#### Reasoning Max Tokens for Anthropic Models

When using Anthropic models with reasoning:

* When using the `reasoning.max_tokens` parameter, that value is used directly with a minimum of 1024 tokens.
* When using the `reasoning.effort` parameter, the budget\_tokens are calculated based on the `max_tokens` value.

The reasoning token allocation is capped at 32,000 tokens maximum and 1024 tokens minimum. The formula for calculating the budget\_tokens is: `budget_tokens = max(min(max_tokens * {effort_ratio}, 32000), 1024)`

effort\_ratio is 0.8 for high effort, 0.5 for medium effort, and 0.2 for low effort.

**Important**: `max_tokens` must be strictly higher than the reasoning budget to ensure there are tokens available for the final response after thinking.

<Note title="Token Usage and Billing">
  Please note that reasoning tokens are counted as output tokens for billing
  purposes. Using reasoning tokens will increase your token usage but can
  significantly improve the quality of model responses.
</Note>

### Examples with Anthropic Models

#### Example 1: Streaming mode with reasoning tokens

<Template
  data={{
  API_KEY_REF,
  MODEL: "anthropic/claude-3.7-sonnet"
}}
>
  <CodeGroup>
    ```python Python
    from openai import OpenAI

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="{{API_KEY_REF}}",
    )

    def chat_completion_with_reasoning(messages):
        response = client.chat.completions.create(
            model="{{MODEL}}",
            messages=messages,
            max_tokens=10000,
            extra_body={
                "reasoning": {
                    "max_tokens": 8000
                }
            },
            stream=True
        )
        return response

    for chunk in chat_completion_with_reasoning([
        {"role": "user", "content": "What's bigger, 9.9 or 9.11?"}
    ]):
        if hasattr(chunk.choices[0].delta, 'reasoning_details') and chunk.choices[0].delta.reasoning_details:
            print(f"REASONING_DETAILS: {chunk.choices[0].delta.reasoning_details}")
        elif getattr(chunk.choices[0].delta, 'content', None):
            print(f"CONTENT: {chunk.choices[0].delta.content}")
    ```

    ```typescript TypeScript
    import OpenAI from 'openai';

    const openai = new OpenAI({
      baseURL: 'https://openrouter.ai/api/v1',
      apiKey: '{{API_KEY_REF}}',
    });

    async function chatCompletionWithReasoning(messages) {
      const response = await openai.chat.completions.create({
        model: '{{MODEL}}',
        messages,
        max_tokens: 10000,
        reasoning: {
          max_tokens: 8000,
        },
        stream: true,
      });

      return response;
    }

    (async () => {
      for await (const chunk of chatCompletionWithReasoning([
        { role: 'user', content: "What's bigger, 9.9 or 9.11?" },
      ])) {
        if (chunk.choices[0].delta?.reasoning_details) {
          console.log(`REASONING_DETAILS:`, chunk.choices[0].delta.reasoning_details);
        } else if (chunk.choices[0].delta?.content) {
          console.log(`CONTENT: ${chunk.choices[0].delta.content}`);
        }
      }
    })();
    ```
  </CodeGroup>
</Template>

## Preserving Reasoning Blocks

<Note title="Model Support">
  Preserving reasoning with reasoning\_details is currently supported by:

  <ul>
    <li>
      All OpenAI reasoning models (o1 series, o3 series, GPT-5 series)
    </li>

    <li>
      All Anthropic reasoning models (Claude 3.7, Claude 4, and Claude 4.1 series)
    </li>

    <li>
      All xAI reasoning models
    </li>

    <li>
      MiniMax M2
    </li>

    <li>
      Kimi K2 Thinking
    </li>
  </ul>
</Note>

The reasoning\_details functionality works identically across all supported reasoning models. You can easily switch between OpenAI reasoning models (like `openai/gpt-5-mini`) and Anthropic reasoning models (like `anthropic/claude-sonnet-4`) without changing your code structure.

If you want to pass reasoning back in context, you must pass reasoning blocks back to the API. This is useful for maintaining the model's reasoning flow and conversation integrity.

Preserving reasoning blocks is useful specifically for tool calling. When models like Claude invoke tools, it is pausing its construction of a response to await external information. When tool results are returned, the model will continue building that existing response. This necessitates preserving reasoning blocks during tool use, for a couple of reasons:

**Reasoning continuity**: The reasoning blocks capture the model's step-by-step reasoning that led to tool requests. When you post tool results, including the original reasoning ensures the model can continue its reasoning from where it left off.

**Context maintenance**: While tool results appear as user messages in the API structure, they're part of a continuous reasoning flow. Preserving reasoning blocks maintains this conceptual flow across multiple API calls.

<Note title="Important for Reasoning Models">
  When providing reasoning\_details blocks, the entire sequence of consecutive
  reasoning blocks must match the outputs generated by the model during the
  original request; you cannot rearrange or modify the sequence of these blocks.
</Note>

## Responses API Shape

When reasoning models generate responses, the reasoning information is structured in a standardized format through the `reasoning_details` array. This section documents the API response structure for reasoning details in both streaming and non-streaming responses.

### reasoning\_details Array Structure

The `reasoning_details` field contains an array of reasoning detail objects. Each object in the array represents a specific piece of reasoning information and follows one of three possible types. The location of this array differs between streaming and non-streaming responses:

* **Non-streaming responses**: `reasoning_details` appears in `choices[].message.reasoning_details`
* **Streaming responses**: `reasoning_details` appears in `choices[].delta.reasoning_details` for each chunk

#### Common Fields

All reasoning detail objects share these common fields:

* `id` (string | null): Unique identifier for the reasoning detail
* `format` (string): The format of the reasoning detail, with possible values:
  * `"unknown"` - Format is not specified
  * `"openai-responses-v1"` - OpenAI responses format version 1
  * `"xai-responses-v1"` - xAI responses format version 1
  * `"anthropic-claude-v1"` - Anthropic Claude format version 1 (default)
* `index` (number, optional): Sequential index of the reasoning detail

#### Reasoning Detail Types

**1. Summary Type (`reasoning.summary`)**

Contains a high-level summary of the reasoning process:

```json
{
  "type": "reasoning.summary",
  "summary": "The model analyzed the problem by first identifying key constraints, then evaluating possible solutions...",
  "id": "reasoning-summary-1",
  "format": "anthropic-claude-v1",
  "index": 0
}
```

**2. Encrypted Type (`reasoning.encrypted`)**

Contains encrypted reasoning data that may be redacted or protected:

```json
{
  "type": "reasoning.encrypted",
  "data": "eyJlbmNyeXB0ZWQiOiJ0cnVlIiwiY29udGVudCI6IltSRURBQ1RFRF0ifQ==",
  "id": "reasoning-encrypted-1",
  "format": "anthropic-claude-v1",
  "index": 1
}
```

**3. Text Type (`reasoning.text`)**

Contains raw text reasoning with optional signature verification:

```json
{
  "type": "reasoning.text",
  "text": "Let me think through this step by step:\n1. First, I need to understand the user's question...",
  "signature": "sha256:abc123def456...",
  "id": "reasoning-text-1",
  "format": "anthropic-claude-v1",
  "index": 2
}
```

### Response Examples

#### Non-Streaming Response

In non-streaming responses, `reasoning_details` appears in the message:

```json
{
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "Based on my analysis, I recommend the following approach...",
        "reasoning_details": [
          {
            "type": "reasoning.summary",
            "summary": "Analyzed the problem by breaking it into components",
            "id": "reasoning-summary-1",
            "format": "anthropic-claude-v1",
            "index": 0
          },
          {
            "type": "reasoning.text",
            "text": "Let me work through this systematically:\n1. First consideration...\n2. Second consideration...",
            "signature": null,
            "id": "reasoning-text-1",
            "format": "anthropic-claude-v1",
            "index": 1
          }
        ]
      }
    }
  ]
}
```

#### Streaming Response

In streaming responses, `reasoning_details` appears in delta chunks as the reasoning is generated:

```json
{
  "choices": [
    {
      "delta": {
        "reasoning_details": [
          {
            "type": "reasoning.text",
            "text": "Let me think about this step by step...",
            "signature": null,
            "id": "reasoning-text-1",
            "format": "anthropic-claude-v1",
            "index": 0
          }
        ]
      }
    }
  ]
}
```

**Streaming Behavior Notes:**

* Each reasoning detail chunk is sent as it becomes available
* The `reasoning_details` array in each chunk may contain one or more reasoning objects
* For encrypted reasoning, the content may appear as `[REDACTED]` in streaming responses
* The complete reasoning sequence is built by concatenating all chunks in order

### Example: Preserving Reasoning Blocks with OpenRouter and Claude

<Template
  data={{
  API_KEY_REF,
  MODEL: 'anthropic/claude-sonnet-4'
}}
>
  <CodeGroup>
    ```python
    from openai import OpenAI

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="{{API_KEY_REF}}",
    )

    # Define tools once and reuse
    tools = [{
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"}
                },
                "required": ["location"]
            }
        }
    }]

    # First API call with tools
    # Note: You can use 'openai/gpt-5-mini' instead of 'anthropic/claude-sonnet-4' - they're completely interchangeable
    response = client.chat.completions.create(
        model="{{MODEL}}",
        messages=[
            {"role": "user", "content": "What's the weather like in Boston? Then recommend what to wear."}
        ],
        tools=tools,
        extra_body={"reasoning": {"max_tokens": 2000}}
    )

    # Extract the assistant message with reasoning_details
    message = response.choices[0].message

    # Preserve the complete reasoning_details when passing back
    messages = [
        {"role": "user", "content": "What's the weather like in Boston? Then recommend what to wear."},
        {
            "role": "assistant",
            "content": message.content,
            "tool_calls": message.tool_calls,
            "reasoning_details": message.reasoning_details  # Pass back unmodified
        },
        {
            "role": "tool",
            "tool_call_id": message.tool_calls[0].id,
            "content": '{"temperature": 45, "condition": "rainy", "humidity": 85}'
        }
    ]

    # Second API call - Claude continues reasoning from where it left off
    response2 = client.chat.completions.create(
        model="{{MODEL}}",
        messages=messages,  # Includes preserved thinking blocks
        tools=tools
    )
    ```

    ```typescript
    import OpenAI from 'openai';

    const client = new OpenAI({
      baseURL: 'https://openrouter.ai/api/v1',
      apiKey: '{{API_KEY_REF}}',
    });

    // Define tools once and reuse
    const tools = [
      {
        type: 'function',
        function: {
          name: 'get_weather',
          description: 'Get current weather',
          parameters: {
            type: 'object',
            properties: {
              location: { type: 'string' },
            },
            required: ['location'],
          },
        },
      },
    ] as const;

    // First API call with tools
    // Note: You can use 'openai/gpt-5-mini' instead of 'anthropic/claude-sonnet-4' - they're completely interchangeable
    const response = await client.chat.completions.create({
      model: '{{MODEL}}',
      messages: [
        {
          role: 'user',
          content:
            "What's the weather like in Boston? Then recommend what to wear.",
        },
      ],
      tools,
      reasoning: { max_tokens: 2000 },
    });

    // Extract the assistant message with reasoning_details
    type ORChatMessage = (typeof response)['choices'][number]['message'] & {
      reasoning_details?: unknown;
    };
    const message = response.choices[0].message as ORChatMessage;

    // Preserve the complete reasoning_details when passing back
    const messages = [
      {
        role: 'user' as const,
        content: "What's the weather like in Boston? Then recommend what to wear.",
      },
      {
        role: 'assistant' as const,
        content: message.content,
        tool_calls: message.tool_calls,
        reasoning_details: message.reasoning_details, // Pass back unmodified
      },
      {
        role: 'tool' as const,
        tool_call_id: message.tool_calls?.[0]?.id,
        content: JSON.stringify({
          temperature: 45,
          condition: 'rainy',
          humidity: 85,
        }),
      },
    ];

    // Second API call - Claude continues reasoning from where it left off
    const response2 = await client.chat.completions.create({
      model: '{{MODEL}}',
      messages, // Includes preserved thinking blocks
      tools,
    });
    ```
  </CodeGroup>
</Template>

For more detailed information about thinking encryption, redacted blocks, and advanced use cases, see [Anthropic's documentation on extended thinking](https://docs.anthropic.com/en/docs/build-with-claude/tool-use#extended-thinking).

For more information about OpenAI reasoning models, see [OpenAI's reasoning documentation](https://platform.openai.com/docs/guides/reasoning#keeping-reasoning-items-in-context).


# Usage Accounting

> Learn how to track AI model usage including prompt tokens, completion tokens, and cached tokens without additional API calls.

The OpenRouter API provides built-in **Usage Accounting** that allows you to track AI model usage without making additional API calls. This feature provides detailed information about token counts, costs, and caching status directly in your API responses.

## Usage Information

When enabled, the API will return detailed usage information including:

1. Prompt and completion token counts using the model's native tokenizer
2. Cost in credits
3. Reasoning token counts (if applicable)
4. Cached token counts (if available)

This information is included in the last SSE message for streaming responses, or in the complete response for non-streaming requests.

## Enabling Usage Accounting

You can enable usage accounting in your requests by including the `usage` parameter:

```json
{
  "model": "your-model",
  "messages": [],
  "usage": {
    "include": true
  }
}
```

## Response Format

When usage accounting is enabled, the response will include a `usage` object with detailed token information:

```json
{
  "object": "chat.completion.chunk",
  "usage": {
    "completion_tokens": 2,
    "completion_tokens_details": {
      "reasoning_tokens": 0
    },
    "cost": 0.95,
    "cost_details": {
      "upstream_inference_cost": 19
    },
    "prompt_tokens": 194,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    },
    "total_tokens": 196
  }
}
```

`cached_tokens` is the number of tokens that were *read* from the cache. At this point in time, we do not support retrieving the number of tokens that were *written* to the cache.

## Cost Breakdown

The usage response includes detailed cost information:

* `cost`: The total amount charged to your account
* `cost_details.upstream_inference_cost`: The actual cost charged by the upstream AI provider

**Note:** The `upstream_inference_cost` field only applies to BYOK (Bring Your Own Key) requests.

<Note title="Performance Impact">
  Enabling usage accounting will add a few hundred milliseconds to the last
  response as the API calculates token counts and costs. This only affects the
  final message and does not impact overall streaming performance.
</Note>

## Benefits

1. **Efficiency**: Get usage information without making separate API calls
2. **Accuracy**: Token counts are calculated using the model's native tokenizer
3. **Transparency**: Track costs and cached token usage in real-time
4. **Detailed Breakdown**: Separate counts for prompt, completion, reasoning, and cached tokens

## Best Practices

1. Enable usage tracking when you need to monitor token consumption or costs
2. Account for the slight delay in the final response when usage accounting is enabled
3. Consider implementing usage tracking in development to optimize token usage before production
4. Use the cached token information to optimize your application's performance

## Alternative: Getting Usage via Generation ID

You can also retrieve usage information asynchronously by using the generation ID returned from your API calls. This is particularly useful when you want to fetch usage statistics after the completion has finished or when you need to audit historical usage.

To use this method:

1. Make your chat completion request as normal
2. Note the `id` field in the response
3. Use that ID to fetch usage information via the `/generation` endpoint

For more details on this approach, see the [Get a Generation](/docs/api-reference/get-a-generation) documentation.

## Examples

### Basic Usage with Token Tracking

<Template
  data={{
  API_KEY_REF,
  MODEL: "anthropic/claude-3-opus"
}}
>
  <CodeGroup>
    ```typescript title="TypeScript SDK"
    import { OpenRouter } from '@openrouter/sdk';

    const openRouter = new OpenRouter({
      apiKey: '{{API_KEY_REF}}',
    });

    const response = await openRouter.chat.send({
      model: '{{MODEL}}',
      messages: [
        {
          role: 'user',
          content: 'What is the capital of France?',
        },
      ],
      usage: {
        include: true,
      },
      stream: false,
    });

    console.log('Response:', response.choices[0].message.content);
    console.log('Usage Stats:', response.usage);
    ```

    ```python title="Python (OpenAI SDK)"
    from openai import OpenAI

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="{{API_KEY_REF}}",
    )

    response = client.chat.completions.create(
        model="{{MODEL}}",
        messages=[
            {"role": "user", "content": "What is the capital of France?"}
        ],
        extra_body={
            "usage": {
                "include": True
            }
        }
    )

    print("Response:", response.choices[0].message.content)
    print("Usage Stats:", getattr(response, "usage", None))
    ```

    ```typescript title="TypeScript (OpenAI SDK)"
    import OpenAI from 'openai';

    const openai = new OpenAI({
      baseURL: 'https://openrouter.ai/api/v1',
      apiKey: '{{API_KEY_REF}}',
    });

    async function getResponseWithUsage() {
      const response = await openai.chat.completions.create({
        model: '{{MODEL}}',
        messages: [
          {
            role: 'user',
            content: 'What is the capital of France?',
          },
        ],
        usage: {
          include: true,
        },
      });

      console.log('Response:', response.choices[0].message.content);
      console.log('Usage Stats:', response.usage);
    }

    getResponseWithUsage();
    ```
  </CodeGroup>
</Template>

### Streaming with Usage Information

This example shows how to handle usage information in streaming mode:

<Template
  data={{
  API_KEY_REF,
  MODEL: "anthropic/claude-3-opus"
}}
>
  <CodeGroup>
    ```python Python
    from openai import OpenAI

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="{{API_KEY_REF}}",
    )

    def chat_completion_with_usage(messages):
        response = client.chat.completions.create(
            model="{{MODEL}}",
            messages=messages,
            extra_body={
                "usage": {
                    "include": True
                }
            },
            stream=True
        )
        return response

    for chunk in chat_completion_with_usage([
        {"role": "user", "content": "Write a haiku about Paris."}
    ]):
        if hasattr(chunk, 'usage'):
            if hasattr(chunk.usage, 'total_tokens'):
                print(f"\nUsage Statistics:")
                print(f"Total Tokens: {chunk.usage.total_tokens}")
                print(f"Prompt Tokens: {chunk.usage.prompt_tokens}")
                print(f"Completion Tokens: {chunk.usage.completion_tokens}")
                print(f"Cost: {chunk.usage.cost} credits")
        elif chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="")
    ```

    ```typescript TypeScript
    import OpenAI from 'openai';

    const openai = new OpenAI({
      baseURL: 'https://openrouter.ai/api/v1',
      apiKey: '{{API_KEY_REF}}',
    });

    async function chatCompletionWithUsage(messages) {
      const response = await openai.chat.completions.create({
        model: '{{MODEL}}',
        messages,
        usage: {
          include: true,
        },
        stream: true,
      });

      return response;
    }

    (async () => {
      for await (const chunk of chatCompletionWithUsage([
        { role: 'user', content: 'Write a haiku about Paris.' },
      ])) {
        if (chunk.usage) {
          console.log('\nUsage Statistics:');
          console.log(`Total Tokens: ${chunk.usage.total_tokens}`);
          console.log(`Prompt Tokens: ${chunk.usage.prompt_tokens}`);
          console.log(`Completion Tokens: ${chunk.usage.completion_tokens}`);
          console.log(`Cost: ${chunk.usage.cost} credits`);
        } else if (chunk.choices[0].delta.content) {
          process.stdout.write(chunk.choices[0].delta.content);
        }
      }
    })();
    ```
  </CodeGroup>
</Template>


# User Tracking

> Learn how to use the user parameter to track your own user IDs with OpenRouter. Improve caching performance and get detailed reporting on your sub-users.

The OpenRouter API supports **User Tracking** through the optional `user` parameter, allowing you to track your own user IDs and improve your application's performance and reporting capabilities.

## What is User Tracking?

User tracking enables you to specify an arbitrary string identifier for your end-users in API requests. This optional metadata helps OpenRouter understand your sub-users, leading to several benefits:

1. **Improved Caching**: OpenRouter can make caches sticky to your individual users, improving load-balancing and throughput
2. **Enhanced Reporting**: View detailed analytics and activity feeds broken down by your user IDs

## How It Works

Simply include a `user` parameter in your API requests with any string identifier that represents your end-user. This could be a user ID, email hash, session identifier, or any other stable identifier you use in your application.

```json
{
  "model": "openai/gpt-4o",
  "messages": [
    {"role": "user", "content": "Hello, how are you?"}
  ],
  "user": "user_12345"
}
```

## Benefits

### Improved Caching Performance

When you consistently use the same user identifier for a specific user, OpenRouter can optimize caching to be "sticky" to that user. This means:

* A given user of your application (assuming you are using caching) will always get routed to the same provider and the cache will stay warm
* But separate users can be spread over different providers, improving load-balancing and throughput

### Enhanced Reporting and Analytics

The user parameter is available in the /activity page, in the exports from that page, and in the /generations API.

* **Activity Feed**: View requests broken down by user ID in your OpenRouter dashboard
* **Usage Analytics**: Understand which users are making the most requests
* **Export Data**: Get detailed exports that include user-level breakdowns

## Implementation Example

<Template
  data={{
  API_KEY_REF,
  MODEL: "openai/gpt-4o"
}}
>
  <CodeGroup>
    ```typescript title="TypeScript SDK"
    import { OpenRouter } from '@openrouter/sdk';

    const openRouter = new OpenRouter({
      apiKey: '{{API_KEY_REF}}',
    });

    const response = await openRouter.chat.send({
      model: '{{MODEL}}',
      messages: [
        {
          role: 'user',
          content: "What's the weather like today?",
        },
      ],
      user: 'user_12345', // Your user identifier
      stream: false,
    });

    console.log(response.choices[0].message.content);
    ```

    ```python title="Python (OpenAI SDK)"
    from openai import OpenAI

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="{{API_KEY_REF}}",
    )

    response = client.chat.completions.create(
        model="{{MODEL}}",
        messages=[
            {"role": "user", "content": "What's the weather like today?"}
        ],
        user="user_12345",  # Your user identifier
    )

    print(response.choices[0].message.content)
    ```

    ```typescript title="TypeScript (OpenAI SDK)"
    import OpenAI from 'openai';

    const openai = new OpenAI({
      baseURL: 'https://openrouter.ai/api/v1',
      apiKey: '{{API_KEY_REF}}',
    });

    async function chatWithUserTracking() {
      const response = await openai.chat.completions.create({
        model: '{{MODEL}}',
        messages: [
          {
            role: 'user',
            content: "What's the weather like today?",
          },
        ],
        user: 'user_12345', // Your user identifier
      });

      console.log(response.choices[0].message.content);
    }

    chatWithUserTracking();
    ```
  </CodeGroup>
</Template>

## Best Practices

### Choose Stable Identifiers

Use consistent, stable identifiers for the same user across requests:

* **Good**: `user_12345`, `customer_abc123`, `account_xyz789`
* **Avoid**: Random strings that change between requests

### Consider Privacy

When using user identifiers, consider privacy implications:

* Use internal user IDs rather than exposing personal information
* Avoid including personally identifiable information in user identifiers
* Consider using anonymized identifiers for better privacy protection

### Be Consistent

Use the same user identifier format throughout your application:

```python
# Consistent format
user_id = f"app_{internal_user_id}"
```


# Frameworks and Integrations Overview

> Integrate OpenRouter using popular frameworks and SDKs. Complete guides for OpenAI SDK, LangChain, PydanticAI, and Vercel AI SDK integration.

OpenRouter integrates seamlessly with popular AI frameworks and SDKs. Choose your preferred framework below for detailed integration guides:

## Available Framework Integrations

* **[Effect AI SDK](/docs/community/effect-ai-sdk)** - Integration with TypeScript Effect applications using the Effect AI SDK
* **[LangChain](/docs/community/lang-chain)** - Integration with LangChain for Python and JavaScript applications
* **[LlamaIndex](https://developers.llamaindex.ai/python/framework-api-reference/llms/openrouter/)** - Integration with LlamaIndex for Python and TypeScript RAG applications
* **[Mastra](/docs/community/mastra)** - Unified interface for AI model access through Mastra framework
* **[OpenAI SDK](/docs/community/open-ai-sdk)** - Direct integration using the official OpenAI SDK for Python and TypeScript
* **[PydanticAI](/docs/community/pydantic-ai)** - High-level interface for Python applications using PydanticAI
* **[Vercel AI SDK](/docs/community/vercel-ai-sdk)** - Integration with Next.js applications using the Vercel AI SDK

## Other Integrations:

* **[Aider](https://aider.chat/docs/llms/openrouter.html)** - Integration with Aider coding assistant
* **[Cline](https://docs.cline.bot/provider-config/openrouter)** - Integration with Cline coding assistant
* **[Kilo Code](https://kilocode.ai/docs/providers/openrouter)** - Integration with KiloCode coding assistant
* **[Langfuse](/docs/community/langfuse)** - Integration with Langfuse Observability and Tracing
* **[Roo Code](https://docs.roocode.com/providers/openrouter?_highlight=openrouter)** - Integration with Roo Code coding assistant
* **[VSCode Copilot](https://code.visualstudio.com/docs/copilot/customization/language-models#_bring-your-own-language-model-key)** - Integration with VSCode Copilot
* **[Xcode](/docs/community/xcode)** - Integration with Xcode coding assistant

You can also find additional examples in our [GitHub repository](https://github.com/OpenRouterTeam/openrouter-examples).


# Effect AI SDK

> Integrate OpenRouter using the Effect AI SDK. Complete guide for integrating the Effect AI SDK with OpenRouter.

# Effect AI SDK

> Integrate OpenRouter using the Effect AI SDK. Complete guide for integrating the Effect AI SDK with OpenRouter.

## Effect AI SDK

You can use the [Effect AI SDK](https://www.npmjs.com/package/@effect/ai) to integrate OpenRouter with your Effect applications. To get started, install the following packages:

* [effect](https://www.npmjs.com/package/effect): the Effect core (if not already installed)
* [@effect/ai](https://www.npmjs.com/package/@effect/ai): the core Effect AI SDK abstractions
* [@effect/ai-openrouter](https://www.npmjs.com/package/@effect/ai-openrouter): the Effect AI provider integration for OpenRouter
* [@effect/platform](https://www.npmjs.com/package/@effect/platform): platform-agnostic abstractions for Effect

```bash
npm install effect @effect/ai @effect/ai-openrouter @effect/platform
```

Once that's done you can use the [LanguageModel](https://effect.website/docs/ai/getting-started/#define-an-interaction-with-a-language-model) module to define interactions with a large language model via OpenRouter.

<CodeGroup>
  ```typescript title="TypeScript"
  import { LanguageModel } from "@effect/ai"
  import { OpenRouterClient, OpenRouterLanguageModel } from "@effect/ai-openrouter"
  import { FetchHttpClient } from "@effect/platform"
  import { Config, Effect, Layer, Stream } from "effect"

  const Gpt4o = OpenRouterLanguageModel.model("openai/gpt-4o")

  const program = LanguageModel.streamText({
    prompt: [
      { role: "system", content: "You are a comedian with a penchant for groan-inducing puns" },
      { role: "user", content: [{ type: "text", text: "Tell me a dad joke" }] }
    ]
  }).pipe(
    Stream.filter((part) => part.type === "text-delta"),
    Stream.runForEach((part) => Effect.sync(() => process.stdout.write(part.delta))),
    Effect.provide(Gpt4o)
  )

  const OpenRouter = OpenRouterClient.layerConfig({
    apiKey: Config.redacted("OPENROUTER_API_KEY")
  }).pipe(Layer.provide(FetchHttpClient.layer))

  program.pipe(
    Effect.provide(OpenRouter),
    Effect.runPromise
  )
  ```
</CodeGroup>


# Arize

> Integrate OpenRouter using Arize for observability and tracing. Complete guide for Arize integration with OpenRouter for Python and JavaScript applications.

## Using Arize

[Arize](https://arize.com/) provides observability and tracing for LLM applications. Since OpenRouter uses the OpenAI API schema, you can utilize Arize's OpenInference auto-instrumentation with the OpenAI SDK to automatically trace and monitor your OpenRouter API calls.

### Installation

```bash
pip install openinference-instrumentation-openai openai arize-otel
```

### Prerequisites

* OpenRouter account and API key
* Arize account with Space ID and API Key

### Why OpenRouter Works with Arize

Arize's OpenInference auto-instrumentation works with OpenRouter because:

1. **OpenRouter provides a fully OpenAI-API-compatible endpoint** - The `/v1` endpoint mirrors OpenAI's schema
2. **Reuse official OpenAI SDKs** - Point the OpenAI client's `base_url` to OpenRouter
3. **Automatic instrumentation** - OpenInference hooks into OpenAI SDK calls seamlessly

### Configuration

Set up your environment variables:

<CodeGroup>
  ```python title="Environment Setup"
  import os

  # Set your OpenRouter API key
  os.environ["OPENAI_API_KEY"] = "${API_KEY_REF}"
  ```
</CodeGroup>

### Simple LLM Call

Initialize Arize and instrument your OpenAI client to automatically trace OpenRouter calls:

<CodeGroup>
  ```python title="Basic Integration"
  from arize.otel import register
  from openinference.instrumentation.openai import OpenAIInstrumentor
  import openai

  # Initialize Arize and register the tracer provider
  tracer_provider = register(
      space_id="your-space-id",
      api_key="your-arize-api-key",
      project_name="your-project-name",
  )

  # Instrument OpenAI SDK
  OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)

  # Configure OpenAI client for OpenRouter
  client = openai.OpenAI(
      base_url="https://openrouter.ai/api/v1",
      api_key="your_openrouter_api_key",
      default_headers={
          "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional: Your site URL
          "X-Title": "<YOUR_SITE_NAME>",      # Optional: Your site name
      }
  )

  # Make a traced chat completion request
  response = client.chat.completions.create(
      model="meta-llama/llama-3.1-8b-instruct:free",
      messages=[
          {"role": "user", "content": "Write a haiku about observability."}
      ],
  )

  # Print the assistant's reply
  print(response.choices[0].message.content)
  ```
</CodeGroup>

### What Gets Traced

All OpenRouter model calls are automatically traced and include:

* Request/response data and timing
* Model name and provider information
* Token usage and cost data (when supported)
* Error handling and debugging information

### JavaScript/TypeScript Support

OpenInference also provides instrumentation for the OpenAI JavaScript/TypeScript SDK, which works with OpenRouter. For setup and examples, please refer to the [OpenInference JavaScript examples for OpenAI](https://github.com/Arize-ai/openinference/tree/main/js).

### Common Issues

* **API Key**: Use your OpenRouter API key, not OpenAI's
* **Model Names**: Use exact model names from [OpenRouter's model list](https://openrouter.ai/models)
* **Rate Limits**: Check your OpenRouter dashboard for usage limits

### Learn More

* **Arize OpenRouter Integration**: [https://arize.com/docs/ax/integrations/llm-providers/openrouter/openrouter-tracing](https://arize.com/docs/ax/integrations/llm-providers/openrouter/openrouter-tracing)
* **OpenRouter Quick Start Guide**: [https://openrouter.ai/docs/quickstart](https://openrouter.ai/docs/quickstart)
* **OpenInference OpenAI Instrumentation**: [https://github.com/Arize-ai/openinference/tree/main/python/instrumentation/openinference-instrumentation-openai](https://github.com/Arize-ai/openinference/tree/main/python/instrumentation/openinference-instrumentation-openai)


# LangChain

> Integrate OpenRouter using LangChain framework. Complete guide for LangChain integration with OpenRouter for Python and JavaScript.

## Using LangChain

* Using [LangChain for Python](https://github.com/langchain-ai/langchain): [github](https://github.com/alexanderatallah/openrouter-streamlit/blob/main/pages/2_Langchain_Quickstart.py)
* Using [LangChain.js](https://github.com/langchain-ai/langchainjs): [github](https://github.com/OpenRouterTeam/openrouter-examples/blob/main/examples/langchain/index.ts)
* Using [Streamlit](https://streamlit.io/): [github](https://github.com/alexanderatallah/openrouter-streamlit)

<CodeGroup>
  ```typescript title="TypeScript"
  import { ChatOpenAI } from "@langchain/openai";
  import { HumanMessage, SystemMessage } from "@langchain/core/messages";

  const chat = new ChatOpenAI(
    {
      model: '<model_name>',
      temperature: 0.8,
      streaming: true,
      apiKey: '${API_KEY_REF}',
    },
    {
      baseURL: 'https://openrouter.ai/api/v1',
      defaultHeaders: {
        'HTTP-Referer': '<YOUR_SITE_URL>', // Optional. Site URL for rankings on openrouter.ai.
        'X-Title': '<YOUR_SITE_NAME>', // Optional. Site title for rankings on openrouter.ai.
      },
    },
  );

  // Example usage
  const response = await chat.invoke([
    new SystemMessage("You are a helpful assistant."),
    new HumanMessage("Hello, how are you?"),
  ]);
  ```

  ```python title="Python"
  from langchain_openai import ChatOpenAI
  from langchain_core.prompts import PromptTemplate
  from langchain.chains import LLMChain
  from os import getenv
  from dotenv import load_dotenv

  load_dotenv()

  template = """Question: {question}
  Answer: Let's think step by step."""

  prompt = PromptTemplate(template=template, input_variables=["question"])

  llm = ChatOpenAI(
    api_key=getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    model="<model_name>",
    default_headers={
      "HTTP-Referer": getenv("YOUR_SITE_URL"), # Optional. Site URL for rankings on openrouter.ai.
      "X-Title": getenv("YOUR_SITE_NAME"), # Optional. Site title for rankings on openrouter.ai.
    }
  )

  llm_chain = LLMChain(prompt=prompt, llm=llm)

  question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

  print(llm_chain.run(question))
  ```
</CodeGroup>


# LiveKit

> Integrate OpenRouter using LiveKit Agents framework. Complete guide for LiveKit integration with OpenRouter to build voice AI agents with access to 500+ models.

## Using LiveKit Agents

[LiveKit Agents](https://docs.livekit.io/agents/) is an open-source framework for building voice AI agents. The OpenRouter plugin allows you to access 500+ AI models from multiple providers through a unified API, with automatic fallback support and intelligent routing.

### Installation

Install the OpenAI plugin to add OpenRouter support:

```bash
uv add "livekit-agents[openai]~=1.2"
```

### Authentication

The OpenRouter plugin requires an [OpenRouter API key](https://openrouter.ai/settings/keys). Set `OPENROUTER_API_KEY` in your `.env` file.

### Basic Usage

Create an OpenRouter LLM using the `with_openrouter` method:

<CodeGroup>
  ```python title="Python"
  from livekit.plugins import openai

  session = AgentSession(
      llm=openai.LLM.with_openrouter(model="anthropic/claude-sonnet-4.5"),
      # ... tts, stt, vad, turn_detection, etc.
  )
  ```
</CodeGroup>

### Advanced Features

#### Fallback Models

Configure multiple fallback models to use if the primary model is unavailable:

<CodeGroup>
  ```python title="Python"
  from livekit.plugins import openai

  llm = openai.LLM.with_openrouter(
      model="openai/gpt-4o",
      fallback_models=[
          "anthropic/claude-sonnet-4",
          "openai/gpt-5-mini",
      ],
  )
  ```
</CodeGroup>

#### Provider Routing

Control which providers are used for model inference:

<CodeGroup>
  ```python title="Python"
  from livekit.plugins import openai

  llm = openai.LLM.with_openrouter(
      model="deepseek/deepseek-chat-v3.1",
      provider={
          "order": ["novita/fp8", "gmicloud/fp8", "google-vertex"],
          "allow_fallbacks": True,
          "sort": "latency",
      },
  )
  ```
</CodeGroup>

#### Web Search Plugin

Enable OpenRouter's web search capabilities:

<CodeGroup>
  ```python title="Python"
  from livekit.plugins import openai

  llm = openai.LLM.with_openrouter(
      model="google/gemini-2.5-flash-preview-09-2025",
      plugins=[
          openai.OpenRouterWebPlugin(
              max_results=5,
              search_prompt="Search for relevant information",
          )
      ],
  )
  ```
</CodeGroup>

#### Analytics Integration

Include site and app information for OpenRouter analytics:

<CodeGroup>
  ```python title="Python"
  from livekit.plugins import openai

  llm = openai.LLM.with_openrouter(
      model="openrouter/auto",
      site_url="https://myapp.com",
      app_name="My Voice Agent",
  )
  ```
</CodeGroup>

### Resources

* [LiveKit OpenRouter Plugin Documentation](https://docs.livekit.io/agents/models/llm/plugins/openrouter/)
* [LiveKit Agents GitHub](https://github.com/livekit/agents)
* [OpenRouter Models](https://openrouter.ai/models)


# Langfuse

> Integrate OpenRouter using Langfuse for observability and tracing. Complete guide for Langfuse integration with OpenRouter for Python applications.

## Using Langfuse

[Langfuse](https://langfuse.com/) provides observability and analytics for LLM applications. Since OpenRouter uses the OpenAI API schema, you can utilize Langfuse's native integration with the OpenAI SDK to automatically trace and monitor your OpenRouter API calls.

### Installation

```bash
pip install langfuse openai
```

### Configuration

Set up your environment variables:

<CodeGroup>
  ```python title="Environment Setup"
  import os

  # Set your Langfuse API keys
  LANGFUSE_SECRET_KEY="sk-lf-..."
  LANGFUSE_PUBLIC_KEY="pk-lf-..."
  # EU region
  LANGFUSE_HOST="https://cloud.langfuse.com"
  # US region
  # LANGFUSE_HOST="https://us.cloud.langfuse.com"

  # Set your OpenRouter API key
  os.environ["OPENAI_API_KEY"] = "${API_KEY_REF}"
  ```
</CodeGroup>

### Simple LLM Call

Since OpenRouter provides an OpenAI-compatible API, you can use the Langfuse OpenAI SDK wrapper to automatically log OpenRouter calls as generations in Langfuse:

<CodeGroup>
  ```python title="Basic Integration"
  # Import the Langfuse OpenAI SDK wrapper
  from langfuse.openai import openai

  # Create an OpenAI client with OpenRouter's base URL
  client = openai.OpenAI(
      base_url="https://openrouter.ai/api/v1",
      default_headers={
          "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional: Your site URL
          "X-Title": "<YOUR_SITE_NAME>",      # Optional: Your site name
      }
  )

  # Make a chat completion request
  response = client.chat.completions.create(
      model="anthropic/claude-3.5-sonnet",
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "Tell me a fun fact about space."}
      ],
      name="fun-fact-request"  # Optional: Name of the generation in Langfuse
  )

  # Print the assistant's reply
  print(response.choices[0].message.content)
  ```
</CodeGroup>

### Advanced Tracing with Nested Calls

Use the `@observe()` decorator to capture execution details of functions with nested LLM calls:

<CodeGroup>
  ```python title="Nested Function Tracing"
  from langfuse import observe
  from langfuse.openai import openai

  # Create an OpenAI client with OpenRouter's base URL
  client = openai.OpenAI(
      base_url="https://openrouter.ai/api/v1",
  )

  @observe()  # This decorator enables tracing of the function
  def analyze_text(text: str):
      # First LLM call: Summarize the text
      summary_response = summarize_text(text)
      summary = summary_response.choices[0].message.content

      # Second LLM call: Analyze the sentiment of the summary
      sentiment_response = analyze_sentiment(summary)
      sentiment = sentiment_response.choices[0].message.content

      return {
          "summary": summary,
          "sentiment": sentiment
      }

  @observe()  # Nested function to be traced
  def summarize_text(text: str):
      return client.chat.completions.create(
          model="openai/gpt-3.5-turbo",
          messages=[
              {"role": "system", "content": "You summarize texts in a concise manner."},
              {"role": "user", "content": f"Summarize the following text:\n{text}"}
          ],
          name="summarize-text"
      )

  @observe()  # Nested function to be traced
  def analyze_sentiment(summary: str):
      return client.chat.completions.create(
          model="openai/gpt-3.5-turbo",
          messages=[
              {"role": "system", "content": "You analyze the sentiment of texts."},
              {"role": "user", "content": f"Analyze the sentiment of the following summary:\n{summary}"}
          ],
          name="analyze-sentiment"
      )

  # Example usage
  text_to_analyze = "OpenRouter's unified API has significantly advanced the field of AI development, setting new standards for model accessibility."
  result = analyze_text(text_to_analyze)
  print(result)
  ```
</CodeGroup>

### Learn More

* **Langfuse OpenRouter Integration**: [https://langfuse.com/docs/integrations/other/openrouter](https://langfuse.com/docs/integrations/other/openrouter)
* **OpenRouter Quick Start Guide**: [https://openrouter.ai/docs/quickstart](https://openrouter.ai/docs/quickstart)
* **Langfuse `@observe()` Decorator**: [https://langfuse.com/docs/sdk/python/decorators](https://langfuse.com/docs/sdk/python/decorators)


# Mastra

> Integrate OpenRouter using Mastra framework. Complete guide for Mastra integration with OpenRouter for unified AI model access.

## Mastra

Integrate OpenRouter with Mastra to access a variety of AI models through a unified interface. This guide provides complete examples from basic setup to advanced configurations.

### Step 1: Initialize a new Mastra project

The simplest way to start is using the automatic project creation:

```bash
# Create a new project using create-mastra
npx create-mastra@latest
```

You'll be guided through prompts to set up your project. For this example, select:

* Name your project: my-mastra-openrouter-app
* Components: Agents (recommended)
* For default provider, select OpenAI (recommended) - we'll configure OpenRouter manually later
* Optionally include example code

For detailed instructions on setting up a Mastra project manually or adding Mastra to an existing project, refer to the [official Mastra documentation](https://mastra.ai/en/docs/getting-started/installation).

### Step 2: Configure your environment variables

After creating your project with `create-mastra`, you'll find a `.env.development` file in your project root. Since we selected OpenAI during setup but will be using OpenRouter instead:

1. Open the `.env.development` file
2. Remove or comment out the `OPENAI_API_KEY` line
3. Add your OpenRouter API key:

```
# .env.development
# OPENAI_API_KEY=your-openai-key  # Comment out or remove this line
OPENROUTER_API_KEY=sk-or-your-api-key-here
```

You can also remove the `@ai-sdk/openai` package since we'll be using OpenRouter instead:

```bash
npm uninstall @ai-sdk/openai
```

```bash
npm install @openrouter/ai-sdk-provider
```

### Step 3: Configure your agent to use OpenRouter

After setting up your Mastra project, you'll need to modify the agent files to use OpenRouter instead of the default OpenAI provider.

If you used `create-mastra`, you'll likely have a file at `src/mastra/agents/agent.ts` or similar. Replace its contents with:

```typescript
import { Agent } from '@mastra/core/agent';
import { createOpenRouter } from '@openrouter/ai-sdk-provider';

// Initialize OpenRouter provider
const openrouter = createOpenRouter({
  apiKey: process.env.OPENROUTER_API_KEY,
});

// Create an agent
export const assistant = new Agent({
  model: openrouter('anthropic/claude-3-opus'),
  name: 'Assistant',
  instructions:
    'You are a helpful assistant with expertise in technology and science.',
});
```

Also make sure to update your Mastra entry point at `src/mastra/index.ts` to use your renamed agent:

```typescript
import { Mastra } from '@mastra/core';

import { assistant } from './agents/agent'; // Update the import path if you used a different filename

export const mastra = new Mastra({
  agents: { assistant }, // Use the same name here as you exported from your agent file
});
```

### Step 4: Running the Application

Once you've configured your agent to use OpenRouter, you can run the Mastra development server:

```bash
npm run dev
```

This will start the Mastra development server and make your agent available at:

* REST API endpoint: `http://localhost:4111/api/agents/assistant/generate`
* Interactive playground: `http://localhost:4111`

The Mastra playground provides a user-friendly interface where you can interact with your agent and test its capabilities without writing any additional code.

You can also test the API endpoint using curl if needed:

```bash
curl -X POST http://localhost:4111/api/agents/assistant/generate \
-H "Content-Type: application/json" \
-d '{"messages": ["What are the latest advancements in quantum computing?"]}'
```

### Basic Integration with Mastra

The simplest way to integrate OpenRouter with Mastra is by using the OpenRouter AI provider with Mastra's Agent system:

```typescript
import { Agent } from '@mastra/core/agent';
import { createOpenRouter } from '@openrouter/ai-sdk-provider';

// Initialize the OpenRouter provider
const openrouter = createOpenRouter({
  apiKey: process.env.OPENROUTER_API_KEY,
});

// Create an agent using OpenRouter
const assistant = new Agent({
  model: openrouter('anthropic/claude-3-opus'),
  name: 'Assistant',
  instructions: 'You are a helpful assistant.',
});

// Generate a response
const response = await assistant.generate([
  {
    role: 'user',
    content: 'Tell me about renewable energy sources.',
  },
]);

console.log(response.text);
```

### Advanced Configuration

For more control over your OpenRouter requests, you can pass additional configuration options:

```typescript
import { Agent } from '@mastra/core/agent';
import { createOpenRouter } from '@openrouter/ai-sdk-provider';

// Initialize with advanced options
const openrouter = createOpenRouter({
  apiKey: process.env.OPENROUTER_API_KEY,
  extraBody: {
    reasoning: {
      max_tokens: 10,
    },
  },
});

// Create an agent with model-specific options
const chefAgent = new Agent({
  model: openrouter('anthropic/claude-3.7-sonnet', {
    extraBody: {
      reasoning: {
        max_tokens: 10,
      },
    },
  }),
  name: 'Chef',
  instructions: 'You are a chef assistant specializing in French cuisine.',
});
```

### Provider-Specific Options

You can also pass provider-specific options in your requests:

```typescript
// Get a response with provider-specific options
const response = await chefAgent.generate([
  {
    role: 'system',
    content:
      'You are Chef Michel, a culinary expert specializing in ketogenic (keto) diet...',
    providerOptions: {
      // Provider-specific options - key can be 'anthropic' or 'openrouter'
      anthropic: {
        cacheControl: { type: 'ephemeral' },
      },
    },
  },
  {
    role: 'user',
    content: 'Can you suggest a keto breakfast?',
  },
]);
```

### Using Multiple Models with OpenRouter

OpenRouter gives you access to various models from different providers. Here's how to use multiple models:

```typescript
import { Agent } from '@mastra/core/agent';
import { createOpenRouter } from '@openrouter/ai-sdk-provider';

const openrouter = createOpenRouter({
  apiKey: process.env.OPENROUTER_API_KEY,
});

// Create agents using different models
const claudeAgent = new Agent({
  model: openrouter('anthropic/claude-3-opus'),
  name: 'ClaudeAssistant',
  instructions: 'You are a helpful assistant powered by Claude.',
});

const gptAgent = new Agent({
  model: openrouter('openai/gpt-4'),
  name: 'GPTAssistant',
  instructions: 'You are a helpful assistant powered by GPT-4.',
});

// Use different agents based on your needs
const claudeResponse = await claudeAgent.generate([
  {
    role: 'user',
    content: 'Explain quantum mechanics simply.',
  },
]);
console.log(claudeResponse.text);

const gptResponse = await gptAgent.generate([
  {
    role: 'user',
    content: 'Explain quantum mechanics simply.',
  },
]);
console.log(gptResponse.text);
```

### Resources

For more information and detailed documentation, check out these resources:

* [OpenRouter Documentation](https://openrouter.ai/docs) - Learn about OpenRouter's capabilities and available models
* [Mastra Documentation](https://mastra.ai/docs) - Comprehensive documentation for the Mastra framework
* [AI SDK Documentation](https://sdk.vercel.ai/docs) - Detailed information about the AI SDK that powers Mastra's model interactions


# OpenAI SDK

> Integrate OpenRouter using the official OpenAI SDK. Complete guide for OpenAI SDK integration with OpenRouter for Python and TypeScript.

## Using the OpenAI SDK

* Using `pip install openai`: [github](https://github.com/OpenRouterTeam/openrouter-examples-python/blob/main/src/openai_test.py).
* Using `npm i openai`: [github](https://github.com/OpenRouterTeam/openrouter-examples/blob/main/examples/openai/index.ts).
  <Tip>
    You can also use
    [Grit](https://app.grit.io/studio?key=RKC0n7ikOiTGTNVkI8uRS) to
    automatically migrate your code. Simply run `npx @getgrit/launcher
      openrouter`.
  </Tip>

<CodeGroup>
  ```typescript title="TypeScript"
  import OpenAI from "openai"

  const openai = new OpenAI({
    baseURL: "https://openrouter.ai/api/v1",
    apiKey: "${API_KEY_REF}",
    defaultHeaders: {
      ${getHeaderLines().join('\n        ')}
    },
  })

  async function main() {
    const completion = await openai.chat.completions.create({
      model: "${Model.GPT_4_Omni}",
      messages: [
        { role: "user", content: "Say this is a test" }
      ],
    })

    console.log(completion.choices[0].message)
  }
  main();
  ```

  ```python title="Python"
  from openai import OpenAI
  from os import getenv

  # gets API Key from environment variable OPENAI_API_KEY
  client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=getenv("OPENROUTER_API_KEY"),
  )

  completion = client.chat.completions.create(
    model="${Model.GPT_4_Omni}",
    extra_headers={
      "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
      "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    # pass extra_body to access OpenRouter-only arguments.
    # extra_body={
      # "models": [
      #   "${Model.GPT_4_Omni}",
      #   "${Model.Mixtral_8x_22B_Instruct}"
      # ]
    # },
    messages=[
      {
        "role": "user",
        "content": "Say this is a test",
      },
    ],
  )
  print(completion.choices[0].message.content)
  ```
</CodeGroup>


# PydanticAI

> Integrate OpenRouter using PydanticAI framework. Complete guide for PydanticAI integration with OpenRouter for Python applications.

## Using PydanticAI

[PydanticAI](https://github.com/pydantic/pydantic-ai) provides a high-level interface for working with various LLM providers, including OpenRouter.

### Installation

```bash
pip install 'pydantic-ai-slim[openai]'
```

### Configuration

You can use OpenRouter with PydanticAI through its OpenAI-compatible interface:

```python
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

model = OpenAIModel(
    "anthropic/claude-3.5-sonnet",  # or any other OpenRouter model
    base_url="https://openrouter.ai/api/v1",
    api_key="sk-or-...",
)

agent = Agent(model)
result = await agent.run("What is the meaning of life?")
print(result)
```

For more details about using PydanticAI with OpenRouter, see the [PydanticAI documentation](https://ai.pydantic.dev/models/#api_key-argument).


# Vercel AI SDK

> Integrate OpenRouter using Vercel AI SDK. Complete guide for Vercel AI SDK integration with OpenRouter for Next.js applications.

## Vercel AI SDK

You can use the [Vercel AI SDK](https://www.npmjs.com/package/ai) to integrate OpenRouter with your Next.js app. To get started, install [@openrouter/ai-sdk-provider](https://github.com/OpenRouterTeam/ai-sdk-provider):

```bash
npm install @openrouter/ai-sdk-provider
```

And then you can use [streamText()](https://sdk.vercel.ai/docs/reference/ai-sdk-core/stream-text) API to stream text from OpenRouter.

<CodeGroup>
  ```typescript title="TypeScript"
  import { createOpenRouter } from '@openrouter/ai-sdk-provider';
  import { streamText } from 'ai';
  import { z } from 'zod';

  export const getLasagnaRecipe = async (modelName: string) => {
    const openrouter = createOpenRouter({
      apiKey: '${API_KEY_REF}',
    });

    const response = streamText({
      model: openrouter(modelName),
      prompt: 'Write a vegetarian lasagna recipe for 4 people.',
    });

    await response.consumeStream();
    return response.text;
  };

  export const getWeather = async (modelName: string) => {
    const openrouter = createOpenRouter({
      apiKey: '${API_KEY_REF}',
    });

    const response = streamText({
      model: openrouter(modelName),
      prompt: 'What is the weather in San Francisco, CA in Fahrenheit?',
      tools: {
        getCurrentWeather: {
          description: 'Get the current weather in a given location',
          parameters: z.object({
            location: z
              .string()
              .describe('The city and state, e.g. San Francisco, CA'),
            unit: z.enum(['celsius', 'fahrenheit']).optional(),
          }),
          execute: async ({ location, unit = 'celsius' }) => {
            // Mock response for the weather
            const weatherData = {
              'Boston, MA': {
                celsius: '15°C',
                fahrenheit: '59°F',
              },
              'San Francisco, CA': {
                celsius: '18°C',
                fahrenheit: '64°F',
              },
            };

            const weather = weatherData[location];
            if (!weather) {
              return `Weather data for ${location} is not available.`;
            }

            return `The current weather in ${location} is ${weather[unit]}.`;
          },
        },
      },
    });

    await response.consumeStream();
    return response.text;
  };
  ```
</CodeGroup>


# Xcode

> Integrate OpenRouter with Apple Intelligence in Xcode 26. Complete setup guide for accessing hundreds of AI models directly in your Xcode development environment.

## Using Xcode with Apple Intelligence

[Apple Intelligence](https://developer.apple.com/apple-intelligence/) in Xcode 26 provides built-in AI assistance for coding. By integrating OpenRouter, you can access hundreds of AI models directly in your Xcode development environment, going far beyond the default ChatGPT integration.

This integration allows you to use models from Anthropic, Google, Meta, and many other providers without leaving your development environment.

### Prerequisites

<Callout intent="warn">
  Apple Intelligence on Xcode is currently in Beta and requires:

  * **macOS Tahoe 26.0 Beta** or later
  * **[Xcode 26 beta 4](https://developer.apple.com/download/applications/)** or later
</Callout>

### Setup Instructions

#### Step 1: Access Intelligence Settings

Navigate to **Settings > Intelligence > Add a Model Provider** in your macOS system preferences.

![Xcode Intelligence Settings](file:c112a5b4-b2e7-4c92-a625-70dba603de90)

#### Step 2: Configure OpenRouter Provider

In the "Add a Model Provider" dialog, enter the following details:

* **URL**: `https://openrouter.ai/api`
  * **Important**: Do not add `/v1` at the end of the endpoint like you typically would for direct API calls
* **API Key Header**: `api_key`
* **API Key**: Your OpenRouter API key (starts with `sk-or-v1-`)
* **Description**: `OpenRouter` (or any name you prefer)

Click **Add** to save the configuration.

![OpenRouter Configuration](file:a2f081e5-3d93-4759-83c4-9fe2bb9a6e7b)

#### Step 3: Browse Available Models

Once configured, click on **OpenRouter** to see all available models. Since OpenRouter offers hundreds of models, you should bookmark your favorite models for quick access. Bookmarked models will appear at the top of the list, making them easily accessible from within the pane whenever you need them.

![Available Models](file:d94af3d5-6fdb-47ab-88d8-f22e7eb13454)

You'll have access to models from various providers including:

* Anthropic Claude models
* Google Gemini models
* Meta Llama models
* OpenAI GPT models
* And hundreds more

![Extended Model List](file:aaa5de51-c260-438a-b350-c5e3b71b96f4)

#### Step 4: Start Using AI in Xcode

Head back to the chat interface (icon at the top) and start chatting with your selected models directly in Xcode.

![Xcode Chat Interface](file:feefc0c9-1dd7-4d7f-b7e4-d27e3d12b5bc)

### Using Apple Intelligence Features

Once configured, you can use Apple Intelligence features in Xcode with OpenRouter models:

* **Code Completion**: Get intelligent code suggestions
* **Code Explanation**: Ask questions about your code
* **Refactoring Assistance**: Get help improving your code structure
* **Documentation Generation**: Generate comments and documentation

![Apple Intelligence Interface](file:e874785a-8218-4312-88d8-02bdf4d3a81c)

*Image credit: [Apple Developer Documentation](https://developer.apple.com/documentation/Xcode/writing-code-with-intelligence-in-xcode)*

### Learn More

* **Apple Intelligence Documentation**: [Writing Code with Intelligence in Xcode](https://developer.apple.com/documentation/Xcode/writing-code-with-intelligence-in-xcode)
* **OpenRouter Quick Start**: [Getting Started with OpenRouter](https://openrouter.ai/docs/quickstart)
* **Available Models**: [Browse OpenRouter Models](https://openrouter.ai/models)


# Zapier

> Build powerful AI automations by connecting OpenRouter with 8000+ apps through Zapier. Access 500+ AI models in your workflows.

With OpenRouter you have access to over 500+ AI models through one API, and with Zapier you can connect to 8000+ apps to automate workflows, no coding required!

This page embeds Zapier Elements so your users can create Zaps that use OpenRouter-powered AI.

<Tip>
  Combine OpenRouter's model routing with Zapier's integrations to automate tasks across CRMs, spreadsheets, messaging, and more.
</Tip>

## Set up your Integration

Get started by exploring available automations and creating your first Zap with OpenRouter. The integration supports all OpenRouter models and features, including streaming responses, function calling, and multimodal capabilities.

<ZapierIframe />

## Using OpenRouter in Zapier

Once you've set up the integration, you can use OpenRouter in your Zaps to:

* **Generate content** with models like GPT-4, Claude, or Gemini
* **Analyze data** using specialized models for different domains
* **Process images** with vision-capable models
* **Create structured outputs** with JSON mode and function calling
* **Stream responses** for real-time applications

The OpenRouter Zapier integration automatically handles authentication, model routing, and error handling, so you can focus on building your automation logic.

For more advanced use cases and detailed documentation, visit the [OpenRouter Zapier integration page](https://zapier.com/apps/openrouter/integrations).

![Zapier Integration Screenshot](file:c8030a9f-c816-4042-92c0-62b609b7f876)



---

**Navigation:** [← Previous](./05-create-a-completion.md) | [Index](./index.md) | Next →
