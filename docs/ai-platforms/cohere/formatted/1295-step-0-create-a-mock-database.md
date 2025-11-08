---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 0: Create a mock database

Before we can illustrate tool use, we first need to do some setup. Here, we'll define the mock data that our tools will query. This data represents sales reports and a product catalog.
```python PYTHON
sales_database = {
    '2023-09-28': {
        'total_sales_amount': 5000,
        'total_units_sold': 100,
    },
    '2023-09-29': {
        'total_sales_amount': 10000,
        'total_units_sold': 250,
    },
    '2023-09-30': {
        'total_sales_amount': 8000,
        'total_units_sold': 200,
    }
}

product_catalog = {
    'Electronics': [
        {'product_id': 'E1001', 'name': 'Smartphone', 'price': 500, 'stock_level': 20},
        {'product_id': 'E1002', 'name': 'Laptop', 'price': 1000, 'stock_level': 15},
        {'product_id': 'E1003', 'name': 'Tablet', 'price': 300, 'stock_level': 25},
    ],
    'Clothing': [
        {'product_id': 'C1001', 'name': 'T-Shirt', 'price': 20, 'stock_level': 100},
        {'product_id': 'C1002', 'name': 'Jeans', 'price': 50, 'stock_level': 80},
        {'product_id': 'C1003', 'name': 'Jacket', 'price': 100, 'stock_level': 40},
    ]
}
```
Now, we'll define the tools that simulate querying this database.\
For example, you could use the API of an enterprise sales platform.
```python PYTHON
def query_daily_sales_report(day: str) -> dict:
    """
    Function to retrieve the sales report for the given day
    """
    report = sales_database.get(day, {})
    if report:
        return {
            'date': day,
            'summary': f"Total Sales Amount: {report['total_sales_amount']}, Total Units Sold: {report['total_units_sold']}"
        }
    else:
        return {'date': day, 'summary': 'No sales data available for this day.'}


def query_product_catalog(category: str) -> dict:
    """
    Function to retrieve products for the given category
    """
    products = product_catalog.get(category, [])
    return {
        'category': category,
        'products': products
    }


functions_map = {
    "query_daily_sales_report": query_daily_sales_report,
    "query_product_catalog": query_product_catalog
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
