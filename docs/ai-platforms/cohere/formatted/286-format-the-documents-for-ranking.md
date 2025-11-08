---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Format the documents for ranking

documents = []
for hit in response["hits"]["hits"]:
    documents.append(hit["_source"]["text"])
```
Here's what that might look like:
```
Title: 2022 FIFA World Cup
Text: The 2022 FIFA World Cup was an international football tournament contested by the men's national teams of FIFA's member associations and 22nd edition of the FIFA World Cup. It took place in Qatar from 20 November to 18 December 2022, making it the first World Cup held in the Arab world and Muslim world, and the second held entirely in Asia after the 2002 tournament in South Korea and Japan. France were the defending champions, having defeated Croatia 4–2 in the 2018 final. At an estimated cost of over $220 billion, it is the most expensive World Cup ever held to date; this figure is disputed by Qatari officials, including organising CEO Nasser Al Khater, who said the true cost was $8 billion, and other figures related to overall infrastructure development since the World Cup was awarded to Qatar in 2010.

Title: 2022 FIFA World Cup
Text: The semi-finals were played on 13 and 14 December. Messi scored a penalty kick before Julián Álvarez scored twice to give Argentina a 3–0 victory over Croatia. Théo Hernandez scored after five minutes as France led Morocco for most of the game and later Randal Kolo Muani scored on 78 minutes to complete a 2–0 victory for France over Morocco as they reached a second consecutive final.

Title: 2022 FIFA World Cup
Text: The quarter-finals were played on 9 and 10 December. Croatia and Brazil ended 0–0 after 90 minutes and went to extra time. Neymar scored for Brazil in the 15th minute of extra time. Croatia, however, equalised through Bruno Petković in the second period of extra time. With the match tied, a penalty shootout decided the contest, with Croatia winning the shoot-out 4–2. In the second quarter-final match, Nahuel Molina and Messi scored for Argentina before Wout Weghorst equalised with two goals shortly before the end of the game. The match went to extra time and then penalties, where Argentina would go on to win 4–3. Morocco defeated Portugal 1–0, with Youssef En-Nesyri scoring at the end of the first half. Morocco became the first African and the first Arab nation to advance as far as the semi-finals of the competition. Despite Harry Kane scoring a penalty for England, it was not enough to beat France, who won 2–1 by virtue of goals from Aurélien Tchouaméni and Olivier Giroud, sending them to their second consecutive World Cup semi-final and becoming the first defending champions to reach this stage since Brazil in 1998.

Title: 2022 FIFA World Cup
Text: Unlike previous FIFA World Cups, which are typically played in June and July, because of Qatar's intense summer heat and often fairly high humidity, the 2022 World Cup was played in November and December. As a result, the World Cup was unusually staged in the middle of the seasons of domestic association football leagues, which started in late July or August, including all of the major European leagues, which had been obliged to incorporate extended breaks into their domestic schedules to accommodate the World Cup. Major European competitions had scheduled their respective competitions group matches to be played before the World Cup, to avoid playing group matches the following year.

Title: 2022 FIFA World Cup
Text: The match schedule was confirmed by FIFA in July 2020. The group stage was set to begin on 21 November, with four matches every day. Later, the schedule was tweaked by moving the Qatar vs Ecuador game to 20 November, after Qatar lobbied FIFA to allow their team to open the tournament. The final was played on 18 December 2022, National Day, at Lusail Stadium.

Title: 2022 FIFA World Cup
Text: Owing to the climate in Qatar, concerns were expressed over holding the World Cup in its traditional time frame of June and July. In October 2013, a task force was commissioned to consider alternative dates and report after the 2014 FIFA World Cup in Brazil. On 24 February 2015, the FIFA Task Force proposed that the tournament be played from late November to late December 2022, to avoid the summer heat between May and September and also avoid clashing with the 2022 Winter Olympics in February, the 2022 Winter Paralympics in March and Ramadan in April.

Title: 2022 FIFA World Cup
Text: Of the 32 nations qualified to play at the 2022 FIFA World Cup, 24 countries competed at the previous tournament in 2018. Qatar were the only team making their debut in the FIFA World Cup, becoming the first hosts to make their tournament debut since Italy in 1934. As a result, the 2022 tournament was the first World Cup in which none of the teams that earned a spot through qualification were making their debut. The Netherlands, Ecuador, Ghana, Cameroon, and the United States returned to the tournament after missing the 2018 tournament. Canada returned after 36 years, their only prior appearance being in 1986. Wales made their first appearance in 64 years – the longest ever gap for any team, their only previous participation having been in 1958.

Title: 2022 FIFA World Cup
Text: After UEFA were guaranteed to host the 2018 event, members of UEFA were no longer in contention to host in 2022. There were five bids remaining for the 2022 FIFA World Cup: Australia, Japan, Qatar, South Korea, and the United States.

Title: Cristiano Ronaldo
Text: Ronaldo was named in Portugal's squad for the 2022 FIFA World Cup in Qatar, making it his fifth World Cup. On 24 November, in Portugal's opening match against Ghana, Ronaldo scored a penalty kick and became the first male player to score in five different World Cups. In the last group game against South Korea, Ronaldo received criticism from his own coach for his reaction at being substituted. He was dropped from the starting line-up for Portugal's last 16 match against Switzerland, marking the first time since Euro 2008 that he had not started a game for Portugal in a major international tournament, and the first time Portugal had started a knockout game without Ronaldo in the starting line-up at an international tournament since Euro 2000. He came off the bench late on as Portugal won 6–1, their highest tally in a World Cup knockout game since the 1966 World Cup, with Ronaldo's replacement Gonçalo Ramos scoring a hat-trick. Portugal employed the same strategy in the quarter-finals against Morocco, with Ronaldo once again coming off the bench; in the process, he equalled Bader Al-Mutawa's international appearance record, becoming the joint–most capped male footballer of all time, with 196 caps. Portugal lost 1–0, however, with Morocco becoming the first CAF nation ever to reach the World Cup semi-finals.

Title: 2022 FIFA World Cup
Text: The final draw was held at the Doha Exhibition and Convention Center in Doha, Qatar, on 1 April 2022, 19:00 AST, prior to the completion of qualification. The two winners of the inter-confederation play-offs and the winner of the Path A of the UEFA play-offs were not known at the time of the draw. The draw was attended by 2,000 guests and was led by Carli Lloyd, Jermaine Jenas and sports broadcaster Samantha Johnson, assisted by the likes of Cafu (Brazil), Lothar Matthäus (Germany), Adel Ahmed Malalla (Qatar), Ali Daei (Iran), Bora Milutinović (Serbia/Mexico), Jay-Jay Okocha (Nigeria), Rabah Madjer (Algeria), and Tim Cahill (Australia).
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
