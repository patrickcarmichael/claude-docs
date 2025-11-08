---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Multilingual multimodal understanding

Aya Vision can process and respond to prompts in multiple languages, demonstrating its multilingual capabilities. This feature allows users to interact with the model in their preferred language, making it accessible to a global audience. The model can analyze images and provide relevant responses based on the visual content, regardless of the language used in the query.

Here is an example in Persian:
```python PYTHON
image_path = "image2.jpg"
render_image(image_path)
```
<img src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/aya-vision/image2.jpg" />
```python PYTHON
message = "آیا این یک هدیه مناسب برای یک کودک 3 ساله است؟"
generate_text(image_path, message)
```
```mdx wordWrap
بله، این یک هدیه مناسب برای یک کودک سه ساله است. این مجموعه لگو دوپلوی "پل آهنی و مسیر قطار" به طور خاص برای کودکان دو تا چهار ساله طراحی شده است. قطعات بزرگ و رنگارنگ آن برای دست‌های کوچک راحت است و به کودکان کمک می‌کند تا مهارت‌های حرکتی ظریف خود را توسعه دهند. این مجموعه همچنین خلاقیت و بازی تخیلی را تشویق می‌کند، زیرا کودکان می‌توانند با قطعات مختلف برای ساختن پل و مسیر قطار بازی کنند. علاوه بر این، لگو دوپلو به دلیل ایمنی و سازگاری با کودکان خردسال شناخته شده است، که آن را به انتخابی ایده‌آل برای هدیه دادن به کودکان سه ساله تبدیل می‌کند.
```
And here's an example in Indonesian:
```python PYTHON
image_path = "image3.jpg"
render_image(image_path)
```
<img src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/aya-vision/image3.jpg" />
```python PYTHON
message = "Gambar ini berisikan kutipan dari tokoh nasional di Indonesia, siapakah tokoh itu?"
generate_text(image_path, message)
```
```mdx wordWrap
Gambar ini berisikan kutipan dari Soekarno, salah satu tokoh nasional Indonesia yang terkenal. Ia adalah Presiden pertama Indonesia dan dikenal sebagai salah satu pemimpin pergerakan kemerdekaan Indonesia. Kutipan dalam gambar tersebut mencerminkan pemikiran dan visi Soekarno tentang pembangunan bangsa dan pentingnya kontribusi generasi muda dalam menciptakan masa depan yang lebih baik.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
