---
title: "Crewai: Option 3: Accessing Properties Using the to_dict() Method"
description: "Option 3: Accessing Properties Using the to_dict() Method section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Option 3: Accessing Properties Using the to_dict() Method

print("Accessing Properties - Option 3")
output_dict = result.to_dict()
title = output_dict["title"]
content = output_dict["content"]
print("Title:", title)
print("Content:", content)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Option 2: Accessing Properties Directly from the Pydantic Model](./302-option-2-accessing-properties-directly-from-the-py.md)

**Next:** [Option 4: Printing the Entire Blog Object →](./304-option-4-printing-the-entire-blog-object.md)
