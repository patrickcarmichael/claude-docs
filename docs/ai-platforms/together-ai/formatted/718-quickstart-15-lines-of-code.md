---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## QuickStart: 15 lines of code

1. Install both the Vercel AI SDK and Together.ai's Vercel package.
```bash
  npm i ai @ai-sdk/togetherai
```
```bash
  yarn add ai @ai-sdk/togetherai
```
```bash
  pnpm add ai @ai-sdk/togetherai
```

2. Import the Together.ai provider and call the `generateText` function with Kimi K2 to generate some text.
```js
import { generateText } from "ai";
import { createTogetherAI } from '@ai-sdk/togetherai';

const together = createTogetherAI({
  apiKey: process.env.TOGETHER_API_KEY ?? '',
});

async function main() {
  const { text } = await generateText({
    model: together("moonshotai/Kimi-K2-Instruct-0905"),
    prompt: "Write a vegetarian lasagna recipe for 4 people.",
  });

  console.log(text);
}

main();
```

### Output

```
Here's a delicious vegetarian lasagna recipe for 4 people:

**Ingredients:**

- 8-10 lasagna noodles
- 2 cups marinara sauce (homemade or store-bought)
- 1 cup ricotta cheese
- 1 cup shredded mozzarella cheese
- 1 cup grated Parmesan cheese
- 1 cup frozen spinach, thawed and drained
- 1 cup sliced mushrooms
- 1 cup sliced bell peppers
- 1 cup sliced zucchini
- 1 small onion, chopped
- 2 cloves garlic, minced
- 1 cup chopped fresh basil
- Salt and pepper to taste
- Olive oil for greasing the baking dish

**Instructions:**

1. **Preheat the oven:** Preheat the oven to 375°F (190°C).
2. **Prepare the vegetables:** Sauté the mushrooms, bell peppers, zucchini, and onion in a little olive oil until they're tender. Add the garlic and cook for another minute.
3. **Prepare the spinach:** Squeeze out as much water as possible from the thawed spinach. Mix it with the ricotta cheese and a pinch of salt and pepper.
4. **Assemble the lasagna:** Grease a 9x13-inch baking dish with olive oil. Spread a layer of marinara sauce on the bottom. Arrange 4 lasagna noodles on top.
5. **Layer 1:** Spread half of the spinach-ricotta mixture on top of the noodles. Add half of the sautéed vegetables and half of the shredded mozzarella cheese.
6. **Layer 2:** Repeat the layers: marinara sauce, noodles, spinach-ricotta mixture, sautéed vegetables, and mozzarella cheese.
7. **Top layer:** Spread the remaining marinara sauce on top of the noodles. Sprinkle with Parmesan cheese and a pinch of salt and pepper.
8. **Bake the lasagna:** Cover the baking dish with aluminum foil and bake for 30 minutes. Remove the foil and bake for another 10-15 minutes, or until the cheese is melted and bubbly.
9. **Let it rest:** Remove the lasagna from the oven and let it rest for 10-15 minutes before slicing and serving.

**Tips and Variations:**

- Use a variety of vegetables to suit your taste and dietary preferences.
- Add some chopped olives or artichoke hearts for extra flavor.
- Use a mixture of mozzarella and Parmesan cheese for a richer flavor.
- Serve with a side salad or garlic bread for a complete meal.

**Nutrition Information (approximate):**

Per serving (serves 4):

- Calories: 450
- Protein: 25g
- Fat: 20g
- Saturated fat: 8g
- Cholesterol: 30mg
- Carbohydrates: 40g
- Fiber: 5g
- Sugar: 10g
- Sodium: 400mg

Enjoy your delicious vegetarian lasagna!
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
