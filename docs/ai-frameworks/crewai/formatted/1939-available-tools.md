---
title: "Crewai: Available Tools"
description: "Available Tools section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Tools


### **Customer Management**

<AccordionGroup>
  <Accordion title="stripe/create_customer">
    **Description:** Create a new customer in your Stripe account.

    **Parameters:**

    * `emailCreateCustomer` (string, required): Customer's email address
    * `name` (string, optional): Customer's full name
    * `description` (string, optional): Customer description for internal reference
    * `metadataCreateCustomer` (object, optional): Additional metadata as key-value pairs (e.g., `{"field1": 1, "field2": 2}`)
  </Accordion>

  <Accordion title="stripe/get_customer_by_id">
    **Description:** Retrieve a specific customer by their Stripe customer ID.

    **Parameters:**

    * `idGetCustomer` (string, required): The Stripe customer ID to retrieve
  </Accordion>

  <Accordion title="stripe/get_customers">
    **Description:** Retrieve a list of customers with optional filtering.

    **Parameters:**

    * `emailGetCustomers` (string, optional): Filter customers by email address
    * `createdAfter` (string, optional): Filter customers created after this date (Unix timestamp)
    * `createdBefore` (string, optional): Filter customers created before this date (Unix timestamp)
    * `limitGetCustomers` (string, optional): Maximum number of customers to return (defaults to 10)
  </Accordion>

  <Accordion title="stripe/update_customer">
    **Description:** Update an existing customer's information.

    **Parameters:**

    * `customerId` (string, required): The ID of the customer to update
    * `emailUpdateCustomer` (string, optional): Updated email address
    * `name` (string, optional): Updated customer name
    * `description` (string, optional): Updated customer description
    * `metadataUpdateCustomer` (object, optional): Updated metadata as key-value pairs
  </Accordion>
</AccordionGroup>

### **Subscription Management**

<AccordionGroup>
  <Accordion title="stripe/create_subscription">
    **Description:** Create a new subscription for a customer.

    **Parameters:**

    * `customerIdCreateSubscription` (string, required): The customer ID for whom the subscription will be created
    * `plan` (string, required): The plan ID for the subscription - Use Connect Portal Workflow Settings to allow users to select a plan
    * `metadataCreateSubscription` (object, optional): Additional metadata for the subscription
  </Accordion>

  <Accordion title="stripe/get_subscriptions">
    **Description:** Retrieve subscriptions with optional filtering.

    **Parameters:**

    * `customerIdGetSubscriptions` (string, optional): Filter subscriptions by customer ID
    * `subscriptionStatus` (string, optional): Filter by subscription status - Options: incomplete, incomplete\_expired, trialing, active, past\_due, canceled, unpaid
    * `limitGetSubscriptions` (string, optional): Maximum number of subscriptions to return (defaults to 10)
  </Accordion>
</AccordionGroup>

### **Product Management**

<AccordionGroup>
  <Accordion title="stripe/create_product">
    **Description:** Create a new product in your Stripe catalog.

    **Parameters:**

    * `productName` (string, required): The product name
    * `description` (string, optional): Product description
    * `metadataProduct` (object, optional): Additional product metadata as key-value pairs
  </Accordion>

  <Accordion title="stripe/get_product_by_id">
    **Description:** Retrieve a specific product by its Stripe product ID.

    **Parameters:**

    * `productId` (string, required): The Stripe product ID to retrieve
  </Accordion>

  <Accordion title="stripe/get_products">
    **Description:** Retrieve a list of products with optional filtering.

    **Parameters:**

    * `createdAfter` (string, optional): Filter products created after this date (Unix timestamp)
    * `createdBefore` (string, optional): Filter products created before this date (Unix timestamp)
    * `limitGetProducts` (string, optional): Maximum number of products to return (defaults to 10)
  </Accordion>
</AccordionGroup>

### **Financial Operations**

<AccordionGroup>
  <Accordion title="stripe/get_balance_transactions">
    **Description:** Retrieve balance transactions from your Stripe account.

    **Parameters:**

    * `balanceTransactionType` (string, optional): Filter by transaction type - Options: charge, refund, payment, payment\_refund
    * `paginationParameters` (object, optional): Pagination settings
      * `pageCursor` (string, optional): Page cursor for pagination
  </Accordion>

  <Accordion title="stripe/get_plans">
    **Description:** Retrieve subscription plans from your Stripe account.

    **Parameters:**

    * `isPlanActive` (boolean, optional): Filter by plan status - true for active plans, false for inactive plans
    * `paginationParameters` (object, optional): Pagination settings
      * `pageCursor` (string, optional): Page cursor for pagination
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up Stripe Integration](./1938-setting-up-stripe-integration.md)

**Next:** [Usage Examples →](./1940-usage-examples.md)
