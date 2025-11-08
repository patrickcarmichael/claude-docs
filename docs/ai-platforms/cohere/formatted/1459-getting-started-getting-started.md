---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Getting Started \[#getting-started]

```python PYTHON
%%capture
!pip install cohere
!pip install python-dotenv
!pip install tokenizers
!pip install langchain
!pip install nltk
!pip install networkx
!pip install pypdf2
```
```python PYTHON
import os
import requests
from collections import deque
from typing import List, Tuple

import cohere

import numpy as np

import PyPDF2
from dotenv import load_dotenv

from tokenizers import Tokenizer

import nltk
nltk.download('punkt')  # Download the necessary data for sentence tokenization

from nltk.tokenize import sent_tokenize

import networkx as nx
from getpass import getpass
from IPython.display import HTML, display
```
```txt title="Output"
[nltk_data] Downloading package punkt to
[nltk_data]     /home/anna_cohere_com/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
