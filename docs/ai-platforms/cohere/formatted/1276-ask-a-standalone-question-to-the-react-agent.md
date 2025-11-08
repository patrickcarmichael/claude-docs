---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Ask a standalone question to the ReAct agent

A question that requires using a predefined tool from Langchain
```python PYTHON
response = agent_executor.invoke({
    "input": "I want to write an essay about the Roman Empire. Any tips for writing an essay? Any fun facts?",
    "preamble": preamble,
})

response['output']
```
```txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will search for tips on writing an essay and fun facts about the Roman Empire.
{'tool_name': 'vectorstore_search', 'parameters': {'query': 'tips for writing an essay'}}
[0m[33;1m[1;3mbe? I should have asked how do you write essays well? Though
these seem only phrasing apart, their answers diverge. The answer
to the first question, as we've seen, isn't really about essay
writing. The second question forces it to be.Writing essays, at its best, is a way of discovering ideas. How do
you do that well? How do you discover by writing?An essay should ordinarily start with what I'm going to call a
question, though I mean this in a very general sense: it doesn't
have to be a question grammatically, just something that acts like
one in the sense that it spurs some response.How do you get this initial question? It probably won't work to
choose some important-sounding topic at random and go at it.
Professional traders won't even trade unless they have what they
call an edge — a convincing story about why in some class of
trades they'll win more than they lose. Similarly, you shouldn't
attack a topic unless you have a way in — some new insight about
it or way of approaching it.You don't need to have a complete thesis; you just need some kind
of gap you can explore. In fact, merely having questions about
something other people take for granted can be edge enough.If you come across a question that's sufficiently puzzling, it could
be worth exploring even if it doesn't seem very momentous. Many an
important discovery has been made by pulling on a thread that seemed
insignificant at first. How can they all be finches?
[2]Once you've got a question, then what? You start thinking out loud
about it. Not literally out loud, but you commit to a specific
string of words in response, as you would if you were talking. This
initial response is usually mistaken or incomplete. Writing converts
your ideas from vague to bad. But that's a step forward, because
once you can see the brokenness, you can fix it.Perhaps beginning writers are alarmed at the thought of starting
with something mistaken or incomplete, but you shouldn't be, because
this is why essay writing works. Forcing yourself to commit to some
specific string of words gives you a starting point, and if it's
wrong, you'll see that when you reread it. At least half of essay
writing is rereading what you've written and asking is this correct

didn't have edge with any of them. To start writing an essay, you
need a topic plus some initial insight about it, and you can't
generate those systematically. If only.
[9]You can probably cause yourself to have more of them, though. The
quality of the ideas that come out of your head depends on what goes
in, and you can improve that in two dimensions, breadth and depth.You can't learn everything, so getting breadth implies learning
about topics that are very different from one another. When I tell
people about my book-buying trips to Hay and they ask what I buy
books about, I usually feel a bit sheepish answering, because the
topics seem like a laundry list of unrelated subjects. But perhaps
that's actually optimal in this business.You can also get ideas by talking to people, by doing and building
things, and by going places and seeing things. I don't think it's
important to talk to new people so much as the sort of people who
make you have new ideas. I get more new ideas after talking for an
afternoon with Robert Morris than from talking to 20 new smart
people. I know because that's what a block of office hours at Y
Combinator consists of.While breadth comes from reading and talking and seeing, depth comes
from doing. The way to really learn about some domain is to have
to solve problems in it. Though this could take the form of writing,
I suspect that to be a good essayist you also have to do, or have
done, some other kind of work. That may not be true for most other
fields, but essay writing is different. You could spend half your
time working on something else and be net ahead, so long as it was
hard.I'm not proposing that as a recipe so much as an encouragement to
those already doing it. If you've spent all your life so far working
on other things, you're already halfway there. Though of course to
be good at writing you have to like it, and if you like writing
you'd probably have spent at least some time doing it.Everything I've said about initial questions applies also to the
questions you encounter in writing the essay. They're the same
thing; every subtree of an essay is usually a shorter essay, just
as every subtree of a Calder mobile is a smaller mobile. So any

You don't have to get an answer right the first time, but there's
no excuse for not getting it right eventually, because you can keep
rewriting till you do. And this is not just a theoretical possibility.
It's a pretty accurate description of the way I work. I'm rewriting
as we speak.But although I wish I could say that writing great essays depends mostly
on effort, in the limit case it's inspiration that makes the
difference. In the limit case, the questions are the harder thing
to get. That pool has no bottom.How to get more questions? That is the most important question of
all.Notes[1]
There might be some resistance to this conclusion on the
grounds that some of these discoveries could only be understood by
a small number of readers. But you get into all sorts of difficulties
if you want to disqualify essays on this account. How do you decide
where the cutoff should be? If a virus kills off everyone except a
handful of people sequestered at Los Alamos,
could an essay that had been disqualified now be eligible? Etc.Darwin's 1844 essay was derived from an earlier version written in 1839.
Extracts from it were published in 1858.[2]
When you find yourself very curious about an apparently minor
question, that's an exciting sign. Evolution has designed you to
pay attention to things that matter. So when you're very curious
about something random, that could mean you've unconsciously noticed
it's less random than it seems.[3]
Corollary: If you're not intellectually honest, your writing
won't just be biased, but also boring, because you'll miss all the
ideas you'd have discovered if you pushed for the truth.[4]
Sometimes this process begins before you start writing.
Sometimes you've already figured out the first few things you want
to say. Schoolchildren are often taught they should decide everything
they want to say, and write this down as an outline before they
start writing the essay itself. Maybe that's a good way to get them
started — or not, I don't know — but it's antithetical to the
spirit of essay writing. The more detailed your outline, the less
your ideas can benefit from the sort of discovery that essays are for.[5]
The problem with this type of "greedy" algorithm is that you

technique that gets you good initial questions also gets you good
whole essays.At some point the cycle of question and response reaches what feels
like a natural end. Which is a little suspicious; shouldn't every
answer suggest more questions? I think what happens is that you
start to feel sated. Once you've covered enough interesting ground,
you start to lose your appetite for new questions. Which is just
as well, because the reader is probably feeling sated too. And it's
not lazy to stop asking questions, because you could instead be
asking the initial question of a new essay.That's the ultimate source of drag on the connectedness of ideas:
the discoveries you make along the way. If you discover enough
starting from question A, you'll never make it to question B. Though
if you keep writing essays you'll gradually fix this problem by
burning off such discoveries. So bizarrely enough, writing lots of
essays makes it as if the space of ideas were more highly connected.When a subtree comes to an end, you can do one of two things. You
can either stop, or pull the Cubist trick of laying separate subtrees
end to end by returning to a question you skipped earlier. Usually
it requires some sleight of hand to make the essay flow continuously
at this point, but not this time. This time I actually need an
example of the phenomenon. For example, we discovered earlier that
the best possible essay wouldn't usually be timeless in the way the
best painting would. This seems surprising enough to be
worth investigating further.There are two senses in which an essay can be timeless: to be about
a matter of permanent importance, and always to have the same effect
on readers. With art these two senses blend together. Art that
looked beautiful to the ancient Greeks still looks beautiful to us.
But with essays the two senses diverge, because essays
teach, and you can't teach people something they already know.
Natural selection is certainly a matter of permanent importance,
but an essay explaining it couldn't have the same effect on us that
it would have had on Darwin's contemporaries, precisely because his
ideas were so successful that everyone already knows about them.
[10]I imagined when I started writing this that the best possible essay
would be timeless in the stricter, evergreen sense: that it would[0m[32;1m[1;3m
{'tool_name': 'internet_search', 'parameters': {'query': 'fun facts about the roman empire'}}
[0m[36;1m[1;3m[{'url': 'https://www.natgeokids.com/uk/discover/history/romans/10-facts-about-the-ancient-romans/', 'content': 'i love this website\nBIG BOBBY\nbooby\nI love shell my bae;)\ni like bobby fishes ;0\nI like turtles\nOmg soy cool\ngreeeeeeeeeeeeaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaatttttttttttttttttttttttt\nbest fact ever\nthis artical is cool\nHANDY\nrubbish did not help what so ever\nha\nRocking\nTHIS IS THE BEST\nproper rad in it cool\nthis is cool\nawesomeness\nawsome\nawsome\nthank you captain\nit is a lot of help\ni like this\nwebsite it helps me on my projects and isabel likes munier\nmark uses this for research\nlot of help\nthis is awsome\nTHE BEST BOOBOO\nCool webpage helped me get 4 housepoints\n This helped me A LOT on a school project\ncool wow awesomoe\nCOOL WEBSITE LOL\nthis helped me with a school project :)\nthat was awesome\ncool\nthat helped me out for my research test\nReally its very cool really COOL\nLIKE COOL best website so far its nice\nI love it\nnice facts\nIt help with my history\n i mean u made animaljam a awesome nice safe place for kids and this site to have kids a safe website to get facts for reports and stuff\nLots of Love ,\nRose\npretty good website if u ask me\nbut definently not gonna use it on a daily basis\nIll try it again another time\ngood\nCool webcite\nterrible\nquite impressive\nAwesome website it real helps\nits good\nthis is a great website! You really a lot with my project!:)\nthis has helleped\nme get\nmy progect\ndone\nthank you\nsoooooooooooooooooo\nmuchchchchchch\nthis helleped me\nsooooooooo much with my progect thank you\nvery good website\nthank us very much your nice one today!!\n'}, {'url': 'https://ohfact.com/roman-empire-facts/', 'content': 'Learn about the ancient Roman Civilization, its history, culture, army, architecture, food and more from this list of 27 facts. Discover how the Romans started, conquered, lived, died and influenced the world with their legends, myths and facts.'}, {'url': 'https://factnight.com/fun-facts-about-the-roman-empire/', 'content': 'The Roman Empire was one of the most influential and significant civilizations in world history. At its peak, the empire stretched from North Africa to Britain, reigning over 60 million people. From its legendary beginnings and remarkable achievements to its eventual decline and fall, the Roman Empire is a fascinating topic full of little-known facts and intriguing trivia.'}, {'url': 'https://www.historyhit.com/facts-about-ancient-rome-and-the-romans/', 'content': 'The Enduring Legacy of C.S. Lewis\nMargaret J. Winkler: A Forgotten Pioneer in Disney’s Success\n10 Facts About Harper Lee\nAntarctica Expedition Cruise\nUncover Pompeii\nSophie Hay and Tristan Hughes\nRediscovering Richard III with Matt Lewis\nOrder the History Hit Miscellany\nHistory Hit Holidays\nGift Subscriptions\n100 Facts About Ancient Rome and the Romans\nRome wasn’t built in a day, as the cliché reminds us. The Crossing of the Rhine in 405/6 AD brought around 100,000 barbarians into the Empire\nBarbarian factions, tribes and war leaders were now a factor in the power struggles at the top of Roman politics and one of the once-strong boundaries of the Empire had proved to be permeable.\n Related Articles\n10 Facts About Saint Andrew\nThe Rise of Pompey the Great, the ‘Roman Alexander’\nWatch and Listen\nCleopatra\nSex in Ancient Rome\nRelated Locations\nBaelo Claudia\nMausoleum of Cecilia Metella\nColin Ricketts\n30 July 2021\n By the fourth century BC, the story was accepted by Romans who were proud of their warrior founder\nThe story was included in the first history of the city, by the Greek writer Diocles of Peparethus, and the twins and their wolf step-mother were depicted on Rome’s first coins.\n The History Hit Miscellany of Facts, Figures and Fascinating Finds\nA History of England: Part One\nDragons: Myth &amp; Reality\nA Tudor Wonder - Hardwick Hall\nThe Battle of Shrewsbury\nEurope’s 1848 Revolutions\nThe Boston Tea Party\nHow Did 3 People Seemingly Escape From Alcatraz?\n'}, {'url': 'https://www.countryfaq.com/facts-about-the-roman-empire/', 'content': 'Facts about the Roman Empire. Explore some of the interesting, fun, cool facts bout the Roman Empire: 1. The Magnificent Roman Empire. The Roman Empire, a colossal entity of unparalleled grandeur, occupies an indomitable position within the annals of human history, a name that resonates resoundingly across the eons.'}][0m[32;1m[1;3mRelevant Documents: 0,3,4,5
Cited Documents: 0,3,4,5
Answer: Here are some tips for writing an essay:
- Start with a question that spurs some response.
- Don't choose a topic at random, make sure you have a way in, a new insight or approach.
- You don't need a complete thesis, just a gap to explore.
- You can get ideas by talking to people, reading, doing and building things, and going places and seeing things.
- You can improve the quality of your ideas by increasing the breadth and depth of what goes in.
- You can get breadth by reading and talking about a wide range of topics.
- You can get depth by doing and having to solve problems.
- You can also get ideas by talking to people who make you have new ideas.

Here are some fun facts about the Roman Empire:
- At its peak, the empire stretched from North Africa to Britain, reigning over 60 million people.
- The story of Rome's warrior founder and the twins and their wolf step-mother was depicted on Rome's first coins.
- The Crossing of the Rhine in 405/6 AD brought around 100,000 barbarians into the Empire.
Grounded answer: Here are some tips for writing an essay:
- <co: 0="">Start with a question that spurs some response</co:>.
- <co: 0="">Don't choose a topic at random, make sure you have a way in, a new insight or approach</co:>.
- <co: 0="">You don't need a complete thesis, just a gap to explore</co:>.
- <co: 0="">You can get ideas by talking to people, reading, doing and building things, and going places and seeing things</co:>.
- <co: 0="">You can improve the quality of your ideas by increasing the breadth and depth of what goes in</co:>.
- <co: 0="">You can get breadth by reading and talking about a wide range of topics</co:>.
- <co: 0="">You can get depth by doing and having to solve problems</co:>.
- <co: 0="">You can also get ideas by talking to people who make you have new ideas</co:>.

Here are some fun facts about the Roman Empire:
- <co: 3="">At its peak, the empire stretched from North Africa to Britain, reigning over 60 million people</co:>.
- <co: 4="">The story of Rome's warrior founder and the twins and their wolf step-mother was depicted on Rome's first coins</co:>.
- <co: 4="">The Crossing of the Rhine in 405/6 AD brought around 100,000 barbarians into the Empire</co:>.[0m

[1m> Finished chain.[0m


"Here are some tips for writing an essay:\n- Start with a question that spurs some response.\n- Don't choose a topic at random, make sure you have a way in, a new insight or approach.\n- You don't need a complete thesis, just a gap to explore.\n- You can get ideas by talking to people, reading, doing and building things, and going places and seeing things.\n- You can improve the quality of your ideas by increasing the breadth and depth of what goes in.\n- You can get breadth by reading and talking about a wide range of topics.\n- You can get depth by doing and having to solve problems.\n- You can also get ideas by talking to people who make you have new ideas.\n\nHere are some fun facts about the Roman Empire:\n- At its peak, the empire stretched from North Africa to Britain, reigning over 60 million people.\n- The story of Rome's warrior founder and the twins and their wolf step-mother was depicted on Rome's first coins.\n- The Crossing of the Rhine in 405/6 AD brought around 100,000 barbarians into the Empire."
```
A question that requires the large language model to use a custom tool.
```python PYTHON
response = agent_executor.invoke({
    "input": "Calculate the result of the random operation of 10 and 20. Then find a few fun facts about that number, as well as its prime factors.",
    "preamble": preamble,
})

response['output']
```
```txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
First, I will calculate the result of the random operation between 10 and 20. Then, I will search for fun facts about that number and its prime factors.
{'tool_name': 'random_operation_tool', 'parameters': {'a': 10, 'b': 20}}
[0mrandom_operation_tool is not a valid tool, try one of [internet_search, vectorstore_search, python_interpreter, random_operation].[32;1m[1;3m
I received an error message when trying to use the random_operation_tool. I will now try using the python_interpreter tool to calculate the random operation between 10 and 20.
{'tool_name': 'python_interpreter', 'parameters': {'code': "import random\n\n# Define the two numbers\na = 10\nb = 20\n\n# Calculate the random operation\nresult = random.choice(['+', '-', '*', '/'])\n\n# Perform the operation\nif result == '+':\n    answer = a + b\nelif result == '-':\n    answer = a - b\nelif result == '*':\n    answer = a * b\nelif result == '/':\n    answer = a / b\n\nprint(f'The result of the random operation is {answer:.0f}')"}}

[0m[38;5;200m[1;3mThe result of the random operation is 200
[0m[32;1m[1;3m
The result of the random operation is 200. Now I will search for fun facts about the number 200 and its prime factors.
{'tool_name': 'internet_search', 'parameters': {'query': 'fun facts about the number 200'}}
[0m[36;1m[1;3m[{'url': 'https://www.express.co.uk/life-style/top10facts/690340/Top-10-facts-number-200', 'content': "Top 10 facts about the number 200 TODAY is the 200th day of 2016, so to celebrate let's have some facts about the number 200. By WILLIAM HARTSTON. 00:01, Mon, Jul 18, 2016."}, {'url': 'https://en.wikipedia.org/wiki/200_(number)', 'content': "The number appears in the Padovan sequence, preceded by 86, 114, 151 (it is the sum of the first two of these). The sum of Euler's totient function φ(x) over the first twenty-five integers is 200. 200 is the smallest base 10 unprimeable number - it cannot be turned into a prime number by changing just one of its digits to any other digit."}, {'url': 'https://www.archimedes-lab.org/numbers/Num70_200.html', 'content': "With 189 pages filled with an incredible variety of fun facts on numbers (and their peculiar properties), both mathematical and cultural, as well as tantalizing problems and anecdotes, there is much to learn for everyone. ... The number 200, according to Bullinger's study of biblical literature, signifies 'insufficiency'. The word 200 (ducenti) ..."}, {'url': 'https://owlcation.com/misc/Over-200-Odd-Facts-Did-You-Know-Them', 'content': "Over 200 odd facts about science, sports, history and more that you and your friends probably don't already know! ... Strange and Interesting Facts. ... Average number of people airborne over the U.S. at any given hour: 61,000. Portion of land in the U.S. owned by the government: 1/3. Ninety percent of New York City cabbies are recently arrived ..."}, {'url': 'https://numbermatics.com/n/200/', 'content': 'Mathematical info, prime factorization, fun facts and numerical data for STEM, education and fun. Your guide to the number 200, an even composite number composed of two distinct primes. Mathematical info, prime factorization, fun facts and numerical data for STEM, education and fun. ... Number 200 - Facts about the integer. Retrieved 2 April ...'}][0m[32;1m[1;3m
{'tool_name': 'internet_search', 'parameters': {'query': 'prime factors of 200'}}
[0m[36;1m[1;3m[{'url': 'https://www.cuemath.com/numbers/factors-of-200/', 'content': 'Therefore, the factors of 200 are 1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, and 200. Which means the number 200 is an even composite number.'}, {'url': 'https://byjus.com/maths/factors-of-200/', 'content': "The factors of 200 are 1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100 and 200. Visit BYJU'S to learn the pair factors and the prime factors of 200 with complete\xa0..."}, {'url': 'https://byjus.com/us/math/factors-of-200/', 'content': 'The factors of 200 are 1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100 and 200 because all these numbers divide the number 200 evenly.'}, {'url': 'https://homework.study.com/explanation/what-is-the-prime-factorization-of-200-using-exponents.html', 'content': 'The prime factorization of 200 using exponents is 2 3 ∗ 5 2 . First, we need to find the prime factorization of 200. 200 = 2 ∗ 100. 200 = 2 ∗ 2 ∗ 50.'}][0m[32;1m[1;3mRelevant Documents: 1,3,4,6,7,8,9,10
Cited Documents: 1,3,4,6,7,8,9,10
Answer: The result of the random operation is **200**. Here are some fun facts about the number 200:
- It is the smallest base 10 unprimeable number, meaning it cannot be turned into a prime number by changing just one of its digits to any other digit.
- According to Bullinger's study of biblical literature, the number 200 signifies 'insufficiency'.
- The number 200 is an even composite number composed of two distinct primes.

The prime factors of 200 are 2 and 5.
Grounded answer: The result of the random operation is *<co: 1="">*200</co:>**. Here are some fun facts about the number 200:
- It is the <co: 3="">smallest base 10 unprimeable number</co:>, meaning it <co: 3="">cannot be turned into a prime number by changing just one of its digits to any other digit</co:>.
- According to <co: 4="">Bullinger's study of biblical literature</co:>, the number 200 signifies <co: 4="">'insufficiency</co:>'.
- The number 200 is an <co: 6,7="">even</co:> <co: 6,7,9="">composite number</co:> composed of <co: 6="">two distinct primes</co:>.

The prime factors of 200 are <co: 10="">2 and 5</co:>.[0m

[1m> Finished chain.[0m


"The result of the random operation is **200**. Here are some fun facts about the number 200:\n- It is the smallest base 10 unprimeable number, meaning it cannot be turned into a prime number by changing just one of its digits to any other digit.\n- According to Bullinger's study of biblical literature, the number 200 signifies 'insufficiency'.\n- The number 200 is an even composite number composed of two distinct primes.\n\nThe prime factors of 200 are 2 and 5."
```
A question that requires the large language model to directly answer.
```python PYTHON
response = agent_executor.invoke({
    "input": "Hey how are you?",
    "preamble": preamble,
})

response['output']
```
```txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will respond to the user's greeting.
{'tool_name': 'directly_answer', 'parameters': {}}
[0mdirectly_answer is not a valid tool, try one of [internet_search, vectorstore_search, python_interpreter, random_operation].[32;1m[1;3mRelevant Documents: None
Cited Documents: None
Answer: I'm an AI chatbot, so I don't have feelings as such, but I'm here to help you with your queries. How can I help?
Grounded answer: I'm an AI chatbot, so I don't have feelings as such, but I'm here to help you with your queries. How can I help?[0m

[1m> Finished chain.[0m


"I'm an AI chatbot, so I don't have feelings as such, but I'm here to help you with your queries. How can I help?"
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
