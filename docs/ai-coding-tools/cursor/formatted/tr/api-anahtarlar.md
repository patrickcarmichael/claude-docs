---
title: "API Anahtarları"
source: "https://docs.cursor.com/tr/settings/api-keys"
language: "tr"
language_name: "Turkish"
---

# API Anahtarları
Source: https://docs.cursor.com/tr/settings/api-keys

Kendi LLM sağlayıcını kullan

Kendi API anahtarlarını kullanarak, maliyeti sana ait olacak şekilde sınırsız AI mesajı gönderebilirsin. Yapılandırdığında, Cursor LLM sağlayıcılarını doğrudan çağırmak için senin API anahtarlarını kullanır.

API anahtarını kullanmak için `Cursor Settings` > `Models` bölümüne git ve anahtarını gir. **Verify**’a tıkla. Doğrulandıktan sonra API anahtarın etkinleşir.

<Warning>
  Özel API anahtarları yalnızca standart sohbet modelleriyle çalışır. Özel modeller gerektiren özellikler (ör. Tab Completion) Cursor’un yerleşik modellerini kullanmaya devam eder.
</Warning>

<div id="supported-providers">
  ## Desteklenen sağlayıcılar
</div>

* **OpenAI** - Yalnızca standart, akıl yürütme içermeyen sohbet modelleri. Model seçicide kullanılabilir OpenAI modellerini göreceksin.
* **Anthropic** - Anthropic API üzerinden sunulan tüm Claude modelleri.
* **Google** - Google AI API üzerinden sunulan Gemini modelleri.
* **Azure OpenAI** - Azure OpenAI Service örneğinde dağıtılmış modeller.
* **AWS Bedrock** - AWS access key, secret key veya IAM role’leri kullan. Bedrock yapılandırmandaki mevcut modellerle çalışır.

Bedrock IAM role’un doğrulandıktan sonra benzersiz bir external ID oluşturulur; ek güvenlik için bunu IAM role trust policy’ne ekleyebilirsin.

<div id="faq">
  ## SSS
</div>

<AccordionGroup>
  <Accordion title="API anahtarım cihazımda saklanacak mı ya da cihazımdan çıkacak mı?">
    API anahtarın saklanmaz ama her istekte sunucumuza gönderilir. Tüm istekler, son prompt oluşturma aşaması için backend’imiz üzerinden yönlendirilir.
  </Accordion>
</AccordionGroup>

---

← Previous: [Modeller](./modeller.md) | [Index](./index.md) | Next: [Sekme](./sekme.md) →