---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 2.2: Measure its performance

Before actually using the classifier, let's first test its performance. Here we take another 100 data points as the test dataset and the classifier will predict its class i.e. news category.
```python PYTHON
TEST_START = 200
TEST_END = 300
df_test = df.iloc[TEST_START:TEST_END]
df_test = df_test.copy()

df_test.drop(['ArticleId'],axis=1,inplace=True)

df_test['Text'] = df_test['Text'].apply(shorten_text)

df_test.head()
```
<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          Text
        </th>

        <th>
          Category
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          200
        </th>

        <td>
          sa return to mauritius top seeds south africa ...
        </td>

        <td>
          sport
        </td>
      </tr>

      <tr>
        <th>
          201
        </th>

        <td>
          snow patrol feted at irish awards snow patrol ...
        </td>

        <td>
          entertainment
        </td>
      </tr>

      <tr>
        <th>
          202
        </th>

        <td>
          clyde 0-5 celtic celtic brushed aside clyde to...
        </td>

        <td>
          sport
        </td>
      </tr>

      <tr>
        <th>
          203
        </th>

        <td>
          bad weather hits nestle sales a combination of...
        </td>

        <td>
          business
        </td>
      </tr>

      <tr>
        <th>
          204
        </th>

        <td>
          net fingerprints combat attacks eighty large n...
        </td>

        <td>
          tech
        </td>
      </tr>
    </tbody>
  </table>
</div>
```python PYTHON
predictions = []
BATCH_SIZE = 90 # The API accepts a maximum of 96 inputs

for i in range(0, len(df_test['Text']), BATCH_SIZE):
    batch_texts = df_test['Text'][i:i+BATCH_SIZE].tolist()
    predictions.extend(classify_text(batch_texts, examples))

actual = df_test['Category'].tolist()
```
```python PYTHON
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(actual, predictions)
print(f'Accuracy: {accuracy*100}')
```
```
Accuracy: 89.0
```
We get a good accuracy score of 91%, so the classifier is ready to be
implemented in our recommender system.

<img alt="Step 3 - Extract" src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/article-recommender/article-rec-4.png" />

We now proceed to the tags extraction step. Compared to the previous two steps, this step is not about sorting or filtering articles, but rather enriching them with more information.

We do this with the Chat endpoint.

We call the endpoint by specifying a few settings, and it will generate the corresponding extractions.
```python PYTHON
def extract_tags(article):
  prompt = f"""Given an article, extract a list of tags containing keywords of that article.

Article: japanese banking battle at an end japan s sumitomo mitsui \
financial has withdrawn its takeover offer for rival bank ufj holdings enabling the \
latter to merge with mitsubishi tokyo.  sumitomo bosses told counterparts at ufj of its \
decision on friday  clearing the way for it to conclude a 3 trillion

Tags: sumitomo mitsui financial, ufj holdings, mitsubishi tokyo, japanese banking

Article:france starts digital terrestrial france has become the last big european country to \
launch a digital terrestrial tv (dtt) service.  initially  more than a third of the \
population will be able to receive 14 free-to-air channels. despite the long wait for a \
french dtt roll-out  the new platform s bac

Tags: france, digital terrestrial

Article: apple laptop is  greatest gadget  the apple powerbook 100 has been chosen as the greatest \
gadget of all time  by us magazine mobile pc.  the 1991 laptop was chosen because it was \
one of the first  lightweight  portable computers and helped define the layout of all future \
notebook pcs. the magazine h

Tags: apple, apple powerbook 100, laptop


Article:{article}

Tags:"""


  response = co.chat(
    model='command-r',
    message=prompt,
    preamble="")

  return response.text
```
<img alt="Complete all steps" src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/article-recommender/article-rec-5.png" />

Let's now put everything together for our article recommender system.

First, we select the target article and compute the similarity scores against the candidate articles.
```python PYTHON
print(f'Choose one article ID between {INP_START} and {INP_END-1} below...')
```
```
Choose one article ID between 0 and 99 below...
```
```python PYTHON
READING_IDX = 70

reading = embeds[READING_IDX]

similarity = get_similarity(reading,embeds)
```
Next, we filter the articles via classification. Finally, we extract the keywords from each article and show the recommendations.
```python PYTHON
SHOW_TOP = 5

df_inputs = df_inputs.copy()
df_inputs['Text'] = df_inputs['Text'].apply(shorten_text)

def get_recommendations(reading_idx,similarity,show_top):

  # Show the current article

  print('------  You are reading...  ------')
  print(f'[ID {READING_IDX}] Article:',df_inputs['Text'][reading_idx][:MAX_CHARS]+'...\n')

  # Show the recommended articles

  print('------  You might also like...  ------')

  # Classify the target article

  target_class = classify_text([df_inputs['Text'][reading_idx]],examples)
  print(target_class)

  count = 0
  for idx,score in similarity:

    # Classify each candidate article

    candidate_class = classify_text([df_inputs['Text'][idx]],examples)

    # Show recommendations

    if target_class == candidate_class and idx != reading_idx:
      selection = df_inputs['Text'][idx][:MAX_CHARS]
      print(f'[ID {idx}] Article:',selection+'...')

      # Extract and show tags

      tags = extract_tags(selection)
      if tags:
          print(f'Tags: {tags.strip()}\n')
      else:
          print(f'Tags: none\n')

      # Increment the article count

      count += 1

      # Stop once articles reach the SHOW_TOP number

      if count == show_top:
        break
```
```python PYTHON
get_recommendations(READING_IDX,similarity,SHOW_TOP)
```
```
------  You are reading...  ------
[ID 70] Article: aragones angered by racism fine spain coach luis aragones is furious after being fined by the spanish football federation for his comments about thierry henry.  the 66-year-old criticised his 3000 euros (£2 060) punishment even though it was far below the maximum penalty.  i am not guilty  nor do i ...

------  You might also like...  ------
[ID 23] Article: ferguson urges henry punishment sir alex ferguson has called on the football association to punish arsenal s thierry henry for an incident involving gabriel heinze.  ferguson believes henry deliberately caught heinze on the head with his knee during united s controversial win. the united boss said i...
Tags: football, sir alex ferguson, thierry henry, arsenal, manchester united

[ID 51] Article: mourinho defiant on chelsea form chelsea boss jose mourinho has insisted that sir alex ferguson and arsene wenger would swap places with him.  mourinho s side were knocked out of the fa cup by newcastle last sunday before seeing barcelona secure a 2-1 champions league first-leg lead in the nou camp....
Tags: chelsea, jose mourinho, sir alex ferguson, arsene wenger, fa cup, newcastle, barcelona, champions league

[ID 41] Article: mcleish ready for criticism rangers manager alex mcleish accepts he is going to be criticised after their disastrous uefa cup exit at the hands of auxerre at ibrox on wednesday.  mcleish told bbc radio five live:  we were in pole position to get through to the next stage but we blew it  we absolutel...
Tags: rangers, alex mcleish, auxerre, uefa cup, ibrox

[ID 42] Article: premier league planning cole date the premier league is attempting to find a mutually convenient date to investigate allegations chelsea made an illegal approach for ashley cole.  both chelsea and arsenal will be asked to give evidence to a premier league commission  but no deadline has been put on ...
Tags: premier league, chelsea, arsenal, ashley cole

[ID 14] Article: ireland 21-19 argentina an injury-time dropped goal by ronan o gara stole victory for ireland from underneath the noses of argentina at lansdowne road on saturday.  o gara kicked all of ireland s points  with two dropped goals and five penalties  to give the home side a 100% record in their autumn i...
Tags: rugby, ireland, argentina, ronan o gara
```
Keeping to the Section 1.3 example, here we see how the classification and extraction steps have improved our recommendation outcome.

First, now the article with ID 73 (non sport) doesn't get recommended anymore. And now we have the tags related to each article being generated.

Let's try a couple of other articles in business and tech and see the output...

Business article (returning recommendations around German economy and economic growth/slump):
```python PYTHON

READING_IDX = 1

reading = embeds[READING_IDX]

similarity = get_similarity(reading,embeds)

get_recommendations(READING_IDX,similarity,SHOW_TOP)
```
```
------  You are reading...  ------
[ID 1] Article: german business confidence slides german business confidence fell in february knocking hopes of a speedy recovery in europe s largest economy.  munich-based research institute ifo said that its confidence index fell to 95.5 in february from 97.5 in january  its first decline in three months. the stu...

------  You might also like...  ------
[ID 56] Article: borussia dortmund near bust german football club and former european champion borussia dortmund has warned it will go bankrupt if rescue talks with creditors fail.  the company s shares tumbled after it said it has  entered a life-threatening profitability and financial situation . borussia dortmund...
Tags: borussia dortmund, german football, bankruptcy

[ID 2] Article: bbc poll indicates economic gloom citizens in a majority of nations surveyed in a bbc world service poll believe the world economy is worsening.  most respondents also said their national economy was getting worse. but when asked about their own family s financial outlook  a majority in 14 countries...
Tags: bbc, economy, financial outlook

[ID 8] Article: car giant hit by mercedes slump a slump in profitability at luxury car maker mercedes has prompted a big drop in profits at parent daimlerchrysler.  the german-us carmaker saw fourth quarter operating profits fall to 785m euros ($1bn) from 2.4bn euros in 2003. mercedes-benz s woes - its profits slid...
Tags: daimlerchrysler, mercedes, luxury car, profitability

[ID 32] Article: china continues rapid growth china s economy has expanded by a breakneck 9.5% during 2004  faster than predicted and well above 2003 s 9.1%.  the news may mean more limits on investment and lending as beijing tries to take the economy off the boil. china has sucked in raw materials and energy to fee...
Tags: china, economy, beijing

[ID 96] Article: bmw to recall faulty diesel cars bmw is to recall all cars equipped with a faulty diesel fuel-injection pump supplied by parts maker robert bosch.  the faulty part does not represent a safety risk and the recall only affects pumps made in december and january. bmw said that it was too early to say h...
Tags: bmw, diesel cars, robert bosch, fuel injection pump
```
Tech article (returning recommendations around consumer devices):
```python PYTHON

READING_IDX = 71

reading = embeds[READING_IDX]

similarity = get_similarity(reading,embeds)

get_recommendations(READING_IDX,similarity,SHOW_TOP)
```
```txt title="Output"
------  You are reading...  ------
[ID 71] Article: camera phones are  must-haves  four times more mobiles with cameras in them will be sold in europe by the end of 2004 than last year  says a report from analysts gartner.  globally  the number sold will reach 159 million  an increase of 104%. the report predicts that nearly 70% of all mobile phones ...

------  You might also like...  ------
[ID 3] Article: lifestyle  governs mobile choice  faster  better or funkier hardware alone is not going to help phone firms sell more handsets  research suggests.  instead  phone firms keen to get more out of their customers should not just be pushing the technology for its own sake. consumers are far more interest...
Tags: mobile, lifestyle, phone firms, handsets

[ID 69] Article: gates opens biggest gadget fair bill gates has opened the consumer electronics show (ces) in las vegas  saying that gadgets are working together more to help people manage multimedia content around the home and on the move.  mr gates made no announcement about the next generation xbox games console ...
Tags: bill gates, consumer electronics show, gadgets, xbox

[ID 46] Article: china  ripe  for media explosion asia is set to drive global media growth to 2008 and beyond  with china and india filling the two top spots  analysts have predicted.  japan  south korea and singapore will also be strong players  but china s demographics give it the edge  a media conference in londo...
Tags: china, india, japan, south korea, singapore, global media growth

[ID 19] Article: moving mobile improves golf swing a mobile phone that recognises and responds to movements has been launched in japan.  the motion-sensitive phone - officially titled the v603sh - was developed by sharp and launched by vodafone s japanese division. devised mainly for mobile gaming  users can also ac...
Tags: mobile phone, japan, sharp, vodafone, golf swing

[ID 63] Article: what high-definition will do to dvds first it was the humble home video  then it was the dvd  and now hollywood is preparing for the next revolution in home entertainment - high-definition.  high-definition gives incredible  3d-like pictures and surround sound. the dvd disks and the gear to play the...
Tags: high-definition, dvd, hollywood, home entertainment
```
In conclusion, this demonstrates an example of how we can stack multiple NLP endpoints together to get an output much closer to our desired outcome.

In practice, hosting and maintaining multiple models can turn quickly into a complex activity. But by leveraging Cohere endpoints, this task is reduced to a simple API call.
```
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
