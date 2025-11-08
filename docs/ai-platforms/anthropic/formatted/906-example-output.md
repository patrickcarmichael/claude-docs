---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example Output

Here's a Google Apps Script that translates all the text in a Google Slides presentation to Korean:
```JavaScript
function translateSlidesToKorean() {
  var presentation = SlidesApp.getActivePresentation();
  var slides = presentation.getSlides();

  for (var i = 0; i < slides.length; i++) {
    var slide = slides[i];
    var pageElements = slide.getPageElements();

    for (var j = 0; j < pageElements.length; j++) {
      var pageElement = pageElements[j];

      if (pageElement.getPageElementType() === SlidesApp.PageElementType.SHAPE) {
        var shape = pageElement.asShape();
        if (shape.getText() !== null) {
          var text = shape.getText().asString();
          var translatedText = LanguageApp.translate(text, '', 'ko');
          shape.getText().setText(translatedText);
        }
      } else if (pageElement.getPageElementType() === SlidesApp.PageElementType.TABLE) {
        var table = pageElement.asTable();
        var numRows = table.getNumRows();
        var numColumns = table.getNumColumns();

        for (var row = 0; row < numRows; row++) {
          for (var col = 0; col < numColumns; col++) {
            var tableCell = table.getCell(row, col);
            var text = tableCell.getText().asString();
            var translatedText = LanguageApp.translate(text, '', 'ko');
            tableCell.getText().setText(translatedText);
          }
        }
      }
    }
  }
}
```
Here's how the script works:

1. The `translateSlidesToKorean()` function retrieves the active Google Slides presentation using `SlidesApp.getActivePresentation()`.

2. It gets all the slides in the presentation using the `getSlides()` method.

3. We iterate over each slide in the presentation.

4. For each slide, we retrieve all the page elements (shapes, text boxes, tables, etc.) using the `getPageElements()` method.

5. We iterate over each page element on the slide.

6. We check the type of the page element using `getPageElementType()`:

   * If the page element is a shape (`SlidesApp.PageElementType.SHAPE`), we get the text content of the shape using `getText().asString()`. We then translate the text to Korean using `LanguageApp.translate(text, '', 'ko')`, where `''` represents the source language (auto-detect) and `'ko'` represents the target language (Korean). Finally, we set the translated text back to the shape using `setText()`.
   * If the page element is a table (`SlidesApp.PageElementType.TABLE`), we iterate over each cell in the table and translate the text within each cell similarly to how we handle shapes.

7. The script continues to process all the page elements on each slide until all the text in the presentation has been translated to Korean.

{' '}

>   **📝 Note**
>
>   **Note:** This script assumes that you have the necessary permissions to
  access and modify the Google Slides presentation. Make sure you have the
  required access rights before running the script.

Also, keep in mind that the translation is performed using the Google Translate
API, so the quality of the translation may vary depending on the complexity of
the text and the capabilities of the translation service.

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
