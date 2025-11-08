---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Dataset

[ConvFinQA](https://github.com/czyssrs/ConvFinQA) dataset is a conversational dataset comprising of multi-turn numerical question and answers based on a given financial report which includes text and tables. We process the original dataset to do a few things:

* We preprocess the financial reports to combine various fields in the original dataset to create a single text blurb from which the questions are to be answered. This involves concatenating various pieces of text, converting the tables to simple text with heuristic regex mappings, among other cosmetic things.
* For finetuning Command R models, the dataset needs to be a `jsonl` file, where each `json` object is a conversation. Each conversation has a list of messages, and each message has two properties: role and content. The role identifies the sender (Chatbot, System, or User), while the content contains the text content. You can find more detailed guide on preparing the dataset including the data validations we have, train/eval splits we recommend, etc. [here](https://docs.cohere.com/docs/chat-preparing-the-data). We format the conversations in the original dataset to conform to these requirements.

### ConvFinQA data example

Following is an example datapoint from the finetuning data.
```python
{
    "messages": [
        {
            "role": "System",
            "content": "stock-based awards under the plan stock options 2013 marathon grants stock options under the 2007 plan and previously granted options under the 2003 plan .\nmarathon 2019s stock options represent the right to purchase shares of common stock at the fair market value of the common stock on the date of grant .\nthrough 2004 , certain stock options were granted under the 2003 plan with a tandem stock appreciation right , which allows the recipient to instead elect to receive cash and/or common stock equal to the excess of the fair market value of shares of common stock , as determined in accordance with the 2003 plan , over the option price of the shares .\nin general , stock options granted under the 2007 plan and the 2003 plan vest ratably over a three-year period and have a maximum term of ten years from the date they are granted .\nstock appreciation rights 2013 prior to 2005 , marathon granted sars under the 2003 plan .\nno stock appreciation rights have been granted under the 2007 plan .\nsimilar to stock options , stock appreciation rights represent the right to receive a payment equal to the excess of the fair market value of shares of common stock on the date the right is exercised over the grant price .\nunder the 2003 plan , certain sars were granted as stock-settled sars and others were granted in tandem with stock options .\nin general , sars granted under the 2003 plan vest ratably over a three-year period and have a maximum term of ten years from the date they are granted .\nstock-based performance awards 2013 prior to 2005 , marathon granted stock-based performance awards under the 2003 plan .\nno stock-based performance awards have been granted under the 2007 plan .\nbeginning in 2005 , marathon discontinued granting stock-based performance awards and instead now grants cash-settled performance units to officers .\nall stock-based performance awards granted under the 2003 plan have either vested or been forfeited .\nas a result , there are no outstanding stock-based performance awards .\nrestricted stock 2013 marathon grants restricted stock and restricted stock units under the 2007 plan and previously granted such awards under the 2003 plan .\nin 2005 , the compensation committee began granting time-based restricted stock to certain u.s.-based officers of marathon and its consolidated subsidiaries as part of their annual long-term incentive package .\nthe restricted stock awards to officers vest three years from the date of grant , contingent on the recipient 2019s continued employment .\nmarathon also grants restricted stock to certain non-officer employees and restricted stock units to certain international employees ( 201crestricted stock awards 201d ) , based on their performance within certain guidelines and for retention purposes .\nthe restricted stock awards to non-officers generally vest in one-third increments over a three-year period , contingent on the recipient 2019s continued employment .\nprior to vesting , all restricted stock recipients have the right to vote such stock and receive dividends thereon .\nthe non-vested shares are not transferable and are held by marathon 2019s transfer agent .\ncommon stock units 2013 marathon maintains an equity compensation program for its non-employee directors under the 2007 plan and previously maintained such a program under the 2003 plan .\nall non-employee directors other than the chairman receive annual grants of common stock units , and they are required to hold those units until they leave the board of directors .\nwhen dividends are paid on marathon common stock , directors receive dividend equivalents in the form of additional common stock units .\nstock-based compensation expense 2013 total employee stock-based compensation expense was $ 80 million , $ 83 million and $ 111 million in 2007 , 2006 and 2005 .\nthe total related income tax benefits were $ 29 million , $ 31 million and $ 39 million .\nin 2007 and 2006 , cash received upon exercise of stock option awards was $ 27 million and $ 50 million .\ntax benefits realized for deductions during 2007 and 2006 that were in excess of the stock-based compensation expense recorded for options exercised and other stock-based awards vested during the period totaled $ 30 million and $ 36 million .\ncash settlements of stock option awards totaled $ 1 million and $ 3 million in 2007 and 2006 .\nstock option awards granted 2013 during 2007 , 2006 and 2005 , marathon granted stock option awards to both officer and non-officer employees .\nthe weighted average grant date fair value of these awards was based on the following black-scholes assumptions: .\nThe weighted average exercise price per share of 2007, 2006, 2005 are $ 60.94, $ 37.84, $ 25.14. The expected annual dividends per share of 2007, 2006, 2005 are $ 0.96, $ 0.80, $ 0.66. The expected life in years of 2007, 2006, 2005 are 5.0, 5.1, 5.5. The expected volatility of 2007, 2006, 2005 are 27% ( 27 % ), 28% ( 28 % ), 28% ( 28 % ). The risk-free interest rate of 2007, 2006, 2005 are 4.1% ( 4.1 % ), 5.0% ( 5.0 % ), 3.8% ( 3.8 % ). The weighted average grant date fair value of stock option awards granted of 2007, 2006, 2005 are $ 17.24, $ 10.19, $ 6.15.\n.",
        },
        {
            "role": "User",
            "content": "what was the weighted average exercise price per share in 2007?",
        },
        {"role": "Chatbot", "content": "60.94"},
        {"role": "User", "content": "and what was it in 2005?"},
        {"role": "Chatbot", "content": "25.14"},
        {
            "role": "User",
            "content": "what was, then, the change over the years?",
        },
        {"role": "Chatbot", "content": "subtract(60.94, 25.14)"},
        {
            "role": "User",
            "content": "what was the weighted average exercise price per share in 2005?",
        },
        {"role": "Chatbot", "content": "25.14"},
        {
            "role": "User",
            "content": "and how much does that change represent in relation to this 2005 weighted average exercise price?",
        },
        {
            "role": "Chatbot",
            "content": "subtract(60.94, 25.14), divide(#0, 25.14)",
        },
    ]
}
```
As you can see, the financial report based on which we answer the questions is put in as System role. This acts as the 'system prompt', which is part of the prompt used as context/instructions for the entire conversation. Since the information in the report is required and relevant to every user question in the conversation, we would want to put it as the overall context of the conversation.

Few things to note in the above example:

* Each datapoint has multiple turns alternating between `User` and `Chatbot`; during finetuning, we consume messages from all roles but only the `Chatbot` messages contribute to the model updates.
* We want the model to learn to strictly follow the domain specific language as represented by the desired Chatbot responses in this example.

### Upload the dataset

We use the [Datasets API](https://docs.cohere.com/reference/create-dataset) to upload the dataset required for finetuning. Note that we upload both training and evaluation files. The data in evaluation file is used for validation and early stopping as we will elaborate later.
```python
chat_dataset = co.datasets.create(
    name="cfqa-ft-dataset",
    data=open("data/convfinqa-train-chat.jsonl", "rb"),
    eval_data=open("data/convfinqa-eval-chat.jsonl", "rb"),
    type="chat-finetune-input",
)
print(
    chat_dataset.id
)  # we will use this id to refer to the dataset when creating a finetuning job

```
Whenever a dataset is created, the data is validated asynchronously. This validation is kicked off automatically on the backend, and must be completed before we can use this dataset for finetuning. You can find more info on interpreting the errors, if you get any, [here](https://docs.cohere.com/docs/datasets#dataset-validation).
```python
co.wait(
    chat_dataset
)  # wait for the dataset to be processed and validated

```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
