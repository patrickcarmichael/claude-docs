---
title: "Crewai: Available Tools"
description: "Available Tools section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Tools


### **Customer Management**

<AccordionGroup>
  <Accordion title="shopify/get_customers">
    **Description:** Retrieve a list of customers from your Shopify store.

    **Parameters:**

    * `customerIds` (string, optional): Comma-separated list of customer IDs to filter by (example: "207119551, 207119552")
    * `createdAtMin` (string, optional): Only return customers created after this date (ISO or Unix timestamp)
    * `createdAtMax` (string, optional): Only return customers created before this date (ISO or Unix timestamp)
    * `updatedAtMin` (string, optional): Only return customers updated after this date (ISO or Unix timestamp)
    * `updatedAtMax` (string, optional): Only return customers updated before this date (ISO or Unix timestamp)
    * `limit` (string, optional): Maximum number of customers to return (defaults to 250)
  </Accordion>

  <Accordion title="shopify/search_customers">
    **Description:** Search for customers using advanced filtering criteria.

    **Parameters:**

    * `filterFormula` (object, optional): Advanced filter in disjunctive normal form with field-specific operators
    * `limit` (string, optional): Maximum number of customers to return (defaults to 250)
  </Accordion>

  <Accordion title="shopify/create_customer">
    **Description:** Create a new customer in your Shopify store.

    **Parameters:**

    * `firstName` (string, required): Customer's first name
    * `lastName` (string, required): Customer's last name
    * `email` (string, required): Customer's email address
    * `company` (string, optional): Company name
    * `streetAddressLine1` (string, optional): Street address
    * `streetAddressLine2` (string, optional): Street address line 2
    * `city` (string, optional): City
    * `state` (string, optional): State or province code
    * `country` (string, optional): Country
    * `zipCode` (string, optional): Zip code
    * `phone` (string, optional): Phone number
    * `tags` (string, optional): Tags as array or comma-separated list
    * `note` (string, optional): Customer note
    * `sendEmailInvite` (boolean, optional): Whether to send email invitation
    * `metafields` (object, optional): Additional metafields in JSON format
  </Accordion>

  <Accordion title="shopify/update_customer">
    **Description:** Update an existing customer in your Shopify store.

    **Parameters:**

    * `customerId` (string, required): The ID of the customer to update
    * `firstName` (string, optional): Customer's first name
    * `lastName` (string, optional): Customer's last name
    * `email` (string, optional): Customer's email address
    * `company` (string, optional): Company name
    * `streetAddressLine1` (string, optional): Street address
    * `streetAddressLine2` (string, optional): Street address line 2
    * `city` (string, optional): City
    * `state` (string, optional): State or province code
    * `country` (string, optional): Country
    * `zipCode` (string, optional): Zip code
    * `phone` (string, optional): Phone number
    * `tags` (string, optional): Tags as array or comma-separated list
    * `note` (string, optional): Customer note
    * `sendEmailInvite` (boolean, optional): Whether to send email invitation
    * `metafields` (object, optional): Additional metafields in JSON format
  </Accordion>
</AccordionGroup>

### **Order Management**

<AccordionGroup>
  <Accordion title="shopify/get_orders">
    **Description:** Retrieve a list of orders from your Shopify store.

    **Parameters:**

    * `orderIds` (string, optional): Comma-separated list of order IDs to filter by (example: "450789469, 450789470")
    * `createdAtMin` (string, optional): Only return orders created after this date (ISO or Unix timestamp)
    * `createdAtMax` (string, optional): Only return orders created before this date (ISO or Unix timestamp)
    * `updatedAtMin` (string, optional): Only return orders updated after this date (ISO or Unix timestamp)
    * `updatedAtMax` (string, optional): Only return orders updated before this date (ISO or Unix timestamp)
    * `limit` (string, optional): Maximum number of orders to return (defaults to 250)
  </Accordion>

  <Accordion title="shopify/create_order">
    **Description:** Create a new order in your Shopify store.

    **Parameters:**

    * `email` (string, required): Customer email address
    * `lineItems` (object, required): Order line items in JSON format with title, price, quantity, and variant\_id
    * `sendReceipt` (boolean, optional): Whether to send order receipt
    * `fulfillmentStatus` (string, optional): Fulfillment status - Options: fulfilled, null, partial, restocked
    * `financialStatus` (string, optional): Financial status - Options: pending, authorized, partially\_paid, paid, partially\_refunded, refunded, voided
    * `inventoryBehaviour` (string, optional): Inventory behavior - Options: bypass, decrement\_ignoring\_policy, decrement\_obeying\_policy
    * `note` (string, optional): Order note
  </Accordion>

  <Accordion title="shopify/update_order">
    **Description:** Update an existing order in your Shopify store.

    **Parameters:**

    * `orderId` (string, required): The ID of the order to update
    * `email` (string, optional): Customer email address
    * `lineItems` (object, optional): Updated order line items in JSON format
    * `sendReceipt` (boolean, optional): Whether to send order receipt
    * `fulfillmentStatus` (string, optional): Fulfillment status - Options: fulfilled, null, partial, restocked
    * `financialStatus` (string, optional): Financial status - Options: pending, authorized, partially\_paid, paid, partially\_refunded, refunded, voided
    * `inventoryBehaviour` (string, optional): Inventory behavior - Options: bypass, decrement\_ignoring\_policy, decrement\_obeying\_policy
    * `note` (string, optional): Order note
  </Accordion>

  <Accordion title="shopify/get_abandoned_carts">
    **Description:** Retrieve abandoned carts from your Shopify store.

    **Parameters:**

    * `createdWithInLast` (string, optional): Restrict results to checkouts created within specified time
    * `createdAfterId` (string, optional): Restrict results to after the specified ID
    * `status` (string, optional): Show checkouts with given status - Options: open, closed (defaults to open)
    * `createdAtMin` (string, optional): Only return carts created after this date (ISO or Unix timestamp)
    * `createdAtMax` (string, optional): Only return carts created before this date (ISO or Unix timestamp)
    * `limit` (string, optional): Maximum number of carts to return (defaults to 250)
  </Accordion>
</AccordionGroup>

### **Product Management (REST API)**

<AccordionGroup>
  <Accordion title="shopify/get_products">
    **Description:** Retrieve a list of products from your Shopify store using REST API.

    **Parameters:**

    * `productIds` (string, optional): Comma-separated list of product IDs to filter by (example: "632910392, 632910393")
    * `title` (string, optional): Filter by product title
    * `productType` (string, optional): Filter by product type
    * `vendor` (string, optional): Filter by vendor
    * `status` (string, optional): Filter by status - Options: active, archived, draft
    * `createdAtMin` (string, optional): Only return products created after this date (ISO or Unix timestamp)
    * `createdAtMax` (string, optional): Only return products created before this date (ISO or Unix timestamp)
    * `updatedAtMin` (string, optional): Only return products updated after this date (ISO or Unix timestamp)
    * `updatedAtMax` (string, optional): Only return products updated before this date (ISO or Unix timestamp)
    * `limit` (string, optional): Maximum number of products to return (defaults to 250)
  </Accordion>

  <Accordion title="shopify/create_product">
    **Description:** Create a new product in your Shopify store using REST API.

    **Parameters:**

    * `title` (string, required): Product title
    * `productType` (string, required): Product type/category
    * `vendor` (string, required): Product vendor
    * `productDescription` (string, optional): Product description (accepts plain text or HTML)
    * `tags` (string, optional): Product tags as array or comma-separated list
    * `price` (string, optional): Product price
    * `inventoryPolicy` (string, optional): Inventory policy - Options: deny, continue
    * `imageUrl` (string, optional): Product image URL
    * `isPublished` (boolean, optional): Whether product is published
    * `publishToPointToSale` (boolean, optional): Whether to publish to point of sale
  </Accordion>

  <Accordion title="shopify/update_product">
    **Description:** Update an existing product in your Shopify store using REST API.

    **Parameters:**

    * `productId` (string, required): The ID of the product to update
    * `title` (string, optional): Product title
    * `productType` (string, optional): Product type/category
    * `vendor` (string, optional): Product vendor
    * `productDescription` (string, optional): Product description (accepts plain text or HTML)
    * `tags` (string, optional): Product tags as array or comma-separated list
    * `price` (string, optional): Product price
    * `inventoryPolicy` (string, optional): Inventory policy - Options: deny, continue
    * `imageUrl` (string, optional): Product image URL
    * `isPublished` (boolean, optional): Whether product is published
    * `publishToPointToSale` (boolean, optional): Whether to publish to point of sale
  </Accordion>
</AccordionGroup>

### **Product Management (GraphQL)**

<AccordionGroup>
  <Accordion title="shopify/get_products_graphql">
    **Description:** Retrieve products using advanced GraphQL filtering capabilities.

    **Parameters:**

    * `productFilterFormula` (object, optional): Advanced filter in disjunctive normal form with support for fields like id, title, vendor, status, handle, tag, created\_at, updated\_at, published\_at
  </Accordion>

  <Accordion title="shopify/create_product_graphql">
    **Description:** Create a new product using GraphQL API with enhanced media support.

    **Parameters:**

    * `title` (string, required): Product title
    * `productType` (string, required): Product type/category
    * `vendor` (string, required): Product vendor
    * `productDescription` (string, optional): Product description (accepts plain text or HTML)
    * `tags` (string, optional): Product tags as array or comma-separated list
    * `media` (object, optional): Media objects with alt text, content type, and source URL
    * `additionalFields` (object, optional): Additional product fields like status, requiresSellingPlan, giftCard
  </Accordion>

  <Accordion title="shopify/update_product_graphql">
    **Description:** Update an existing product using GraphQL API with enhanced media support.

    **Parameters:**

    * `productId` (string, required): The GraphQL ID of the product to update (e.g., "gid://shopify/Product/913144112")
    * `title` (string, optional): Product title
    * `productType` (string, optional): Product type/category
    * `vendor` (string, optional): Product vendor
    * `productDescription` (string, optional): Product description (accepts plain text or HTML)
    * `tags` (string, optional): Product tags as array or comma-separated list
    * `media` (object, optional): Updated media objects with alt text, content type, and source URL
    * `additionalFields` (object, optional): Additional product fields like status, requiresSellingPlan, giftCard
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up Shopify Integration](./1909-setting-up-shopify-integration.md)

**Next:** [Usage Examples →](./1911-usage-examples.md)
