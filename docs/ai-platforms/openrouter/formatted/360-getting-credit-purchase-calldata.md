---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

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

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
