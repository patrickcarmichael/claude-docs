---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Paste in your Together AI API Key or load it

TOGETHER_API_KEY = os.environ.get("TOGETHER_API_KEY")
client = Together(api_key=TOGETHER_API_KEY)

with open("./datasets/movies.json", "r") as file:
    movies_data = json.load(file)

movies_data[10:13]
```

Our dataset contains information about popular movies:
```json
[{'title': 'Terminator Genisys',
  'overview': "The year is 2029. John Connor, leader of the resistance continues the war against the machines. At the Los Angeles offensive, John's fears of the unknown future begin to emerge when TECOM spies reveal a new plot by SkyNet that will attack him from both fronts; past and future, and will ultimately change warfare forever.",
  'director': 'Alan Taylor',
  'genres': 'Science Fiction Action Thriller Adventure',
  'tagline': 'Reset the future'},
 {'title': 'Captain America: Civil War',
  'overview': 'Following the events of Age of Ultron, the collective governments of the world pass an act designed to regulate all superhuman activity. This polarizes opinion amongst the Avengers, causing two factions to side with Iron Man or Captain America, which causes an epic battle between former allies.',
  'director': 'Anthony Russo',
  'genres': 'Adventure Action Science Fiction',
  'tagline': 'Divided We Fall'},
 {'title': 'Whiplash',
  'overview': 'Under the direction of a ruthless instructor, a talented young drummer begins to pursue perfection at any cost, even his humanity.',
  'director': 'Damien Chazelle',
  'genres': 'Drama',
  'tagline': 'The road to greatness can take you to the edge.'}]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
