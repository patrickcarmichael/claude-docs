---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Filtering by language

If we're interested in results in only one language, we can specify it.
```python PYTHON
query_result = semantic_serch("time travel plot twist", results_lang='ja')

print_result(query_result)
```
```txt title="Output"
[95m時空の旅人 (500) -144.16002[0m
[4mhttps://ja.wikipedia.org/wiki?curid=523464[0m
バスは1868年の攘夷戦争で娘と夫を亡くした老婆の営む茶店に降り立つ。一時は老婆は一行を盗人と間違えて襲い掛かるも、ホクベンを亡き夫だと思い込んだことで一転して歓迎する。しかしそこへジロを追うタイムマシンがあらわれ、やむなく一行はバスに乗って走り去る。追い縋る老婆を見捨てられずバスを飛び降りたホクベンだが、直後にタイムマシンに攫われてしまった。

[95m親殺しのパラドックス (700) -144.11864[0m
[4mhttps://ja.wikipedia.org/wiki?curid=71910[0m
パラドックスを防ぐアイデアとして、時間旅行者は元々の歴史とは異なる並行宇宙に行くのだと解釈するもので、上の科学的理論で述べたのと同じ考え方であり、SFにもよく見られる。歴史改変SFにあるタイムトラベル参照。

[95mタイムトラベル (1000) -143.70331[0m
[4mhttps://ja.wikipedia.org/wiki?curid=1971274[0m
タイムパラドックスの矛盾を説明するため、タイムトラベル者による歴史の改変で時間軸が分岐し元の世界と並行した別の世界が生まれるとするパラレルワールドの概念がある。この概念を発展させ、タイムトラベル者の介在がなくとも歴史上の重要なポイントで世界が枝分かれしていると解釈する立場もある。この概念を大幅に作品に取り入れた最初期の小説に、可能性として存在する二つの歴史「ジョンバール」と「ギロンチ」の抗争を描いた、ジャック・ウィリアムスンの『航時軍団』（The Legion of Time、1938年）がある。

[95mタイムトラベル (1000) -143.69884[0m
[4mhttps://ja.wikipedia.org/wiki?curid=1971274[0m
タイムトラベラーが主人公であるマーク・トウェインの「アーサー王宮廷のコネチカット・ヤンキー」や、天使が未来の書物を携えて現れるサミュエル・マッデンの「20世紀回想」など、SFというカテゴリが明確なものとして育つ以前から、タイムトラベルをテーマにした物語は創られている。

[95mタイムトラベル (1000) -143.61562[0m
[4mhttps://ja.wikipedia.org/wiki?curid=1971274[0m
タイムパラドックス（Time Paradox / 時間の逆説）は、タイムトラベルに伴う矛盾や変化のことであり、物語のテーマとしてしばしば扱われる。具体的には、タイムトラベルした過去で現代（相対的未来）に存在する事象を改変した場合、その事象における過去と現代の存在や状況、因果関係の不一致という逆説が生じることに着目したものである。
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
