---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create a new collection named "Legal_Docs" in the Weaviate database

client.collections.create(
    name="Legal_Docs",
    properties=[
        # Define a property named "title" with data type TEXT

        Property(name="title", data_type=DataType.TEXT),
    ],
    # Configure the vectorizer to use Cohere's text2vec model

    vectorizer_config=Configure.Vectorizer.text2vec_cohere(
        model="embed-english-v3.0"  # Specify the Cohere model to use for vectorization

    ),
    # Configure the reranker to use Cohere's rerank model

    reranker_config=Configure.Reranker.cohere(
        model="rerank-english-v3.0"  # Specify the Cohere model to use for reranking

    ),
)
```
```python PYTHON
legal_documents = [
    {
        "title": "Contract Law Basics",
        "description": "An in-depth introduction to contract law, covering essential elements such as offer, acceptance, consideration, and mutual assent. Explores types of contracts, including express, implied, and unilateral contracts, as well as remedies for breach of contract, such as damages, specific performance, and rescission.",
    },
    {
        "title": "Intellectual Property Rights",
        "description": "Comprehensive overview of intellectual property laws, including patents, trademarks, copyrights, and trade secrets. Discusses the process of obtaining patents, trademark registration, and copyright protection, as well as strategies for enforcing intellectual property rights and defending against infringement claims.",
    },
    {
        "title": "Employment Law Guide",
        "description": "Detailed guide to employment laws, covering hiring practices, termination procedures, anti-discrimination laws, and workplace safety regulations. Includes information on employee rights, such as minimum wage, overtime pay, and family and medical leave, as well as employer obligations under federal and state laws.",
    },
    {
        "title": "Criminal Law Procedures",
        "description": "Step-by-step explanation of criminal law procedures, from arrest and booking to trial and sentencing. Covers the rights of the accused, including the right to counsel, the right to remain silent, and the right to a fair trial, as well as rules of evidence and burden of proof in criminal cases.",
    },
    {
        "title": "Real Estate Transactions",
        "description": "Comprehensive guide to real estate transactions, including purchase agreements, title searches, property inspections, and closing processes. Discusses common issues such as title defects, financing contingencies, and property disclosures, as well as the role of real estate agents and attorneys in the transaction process.",
    },
    {
        "title": "Corporate Governance",
        "description": "In-depth overview of corporate governance principles, including the roles and responsibilities of boards of directors, shareholder rights, and compliance with securities laws. Explores best practices for board composition, executive compensation, and risk management, as well as strategies for maintaining transparency and accountability in corporate decision-making.",
    },
    {
        "title": "Family Law Overview",
        "description": "Comprehensive introduction to family law, covering marriage, divorce, child custody, child support, and adoption processes. Discusses the legal requirements for marriage and divorce, factors considered in child custody determinations, and the rights and obligations of adoptive parents under state and federal laws.",
    },
    {
        "title": "Tax Law for Businesses",
        "description": "Detailed guide to tax laws affecting businesses, including corporate income tax, payroll taxes, sales and use taxes, and tax deductions. Explores tax planning strategies, such as deferring income and accelerating expenses, as well as compliance requirements and penalties for non-compliance with tax laws.",
    },
    {
        "title": "Immigration Law Basics",
        "description": "Comprehensive overview of immigration laws, including visa categories, citizenship requirements, and deportation processes. Discusses the rights and obligations of immigrants, including access to public benefits and protection from discrimination, as well as the role of immigration attorneys in navigating the immigration system.",
    },
    {
        "title": "Environmental Regulations",
        "description": "In-depth overview of environmental laws and regulations, including air and water quality standards, hazardous waste management, and endangered species protection. Explores the role of federal and state agencies in enforcing environmental laws, as well as strategies for businesses to achieve compliance and minimize environmental impact.",
    },
    {
        "title": "Consumer Protection Laws",
        "description": "Comprehensive guide to consumer protection laws, including truth in advertising, product safety, and debt collection practices. Discusses the rights of consumers under federal and state laws, such as the right to sue for damages and the right to cancel certain contracts, as well as the role of government agencies in enforcing consumer protection laws.",
    },
    {
        "title": "Estate Planning Essentials",
        "description": "Detailed overview of estate planning, including wills, trusts, powers of attorney, and advance healthcare directives. Explores strategies for minimizing estate taxes, protecting assets from creditors, and ensuring that assets are distributed according to the individual's wishes after death.",
    },
    {
        "title": "Bankruptcy Law Overview",
        "description": "Comprehensive introduction to bankruptcy law, including Chapter 7 and Chapter 13 bankruptcy proceedings. Discusses the eligibility requirements for filing bankruptcy, the process of liquidating assets and discharging debts, and the impact of bankruptcy on credit scores and future financial opportunities.",
    },
    {
        "title": "International Trade Law",
        "description": "In-depth overview of international trade laws, including tariffs, quotas, and trade agreements. Explores the role of international organizations such as the World Trade Organization (WTO) in regulating global trade, as well as strategies for businesses to navigate trade barriers and comply with international trade regulations.",
    },
    {
        "title": "Healthcare Law and Regulations",
        "description": "Comprehensive guide to healthcare laws and regulations, including patient privacy rights, healthcare provider licensing, and medical malpractice liability. Discusses the impact of laws such as the Affordable Care Act (ACA) and the Health Insurance Portability and Accountability Act (HIPAA) on healthcare providers and patients, as well as strategies for ensuring compliance with healthcare regulations.",
    },
]
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
