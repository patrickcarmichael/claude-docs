**Navigation:** [← Previous](./14-step-4-conversation-with-memory-using-ai-messages-.md) | [Index](./index.md) | [Next →](./16-creating-a-qa-bot-from-technical-documentation.md)

---

# Multi-Step Tool Use with Cohere

> This page describes how to create a multi-step, tool-using AI agent with Cohere's tool use functionality.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/agents/Vanilla_Multi_Step_Tool_Use.ipynb" />

Tool use allows developers to connect Cohere's models to external tools like search engines, APIs, functions, databases, etc.

Multi-step tool use is an extension of this basic idea, and allows the model to call more than one tool in a sequence of steps, using the results from one tool call in a subsequent step. This process allows the language model to reason, perform dynamic actions, and quickly adapt on the basis of information coming from external sources.

The recommended way to achieve [multi-step tool use with Cohere](https://docs.cohere.com/docs/multi-step-tool-use) is by leveraging the [Langchain framework](https://python.langchain.com/docs/integrations/providers/cohere#react-agent) in Python.

## Install Dependencies

```python PYTHON
! pip install --quiet langchain langchain_cohere langchain_experimental
```

```txt title="Output"
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m812.8/812.8 kB[0m [31m6.5 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m194.1/194.1 kB[0m [31m4.7 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m1.9/1.9 MB[0m [31m9.6 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m276.8/276.8 kB[0m [31m7.7 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m87.5/87.5 kB[0m [31m3.7 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m145.9/145.9 kB[0m [31m2.8 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m3.1/3.1 MB[0m [31m21.7 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m75.6/75.6 kB[0m [31m7.1 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m49.4/49.4 kB[0m [31m4.1 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m53.0/53.0 kB[0m [31m4.8 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m144.8/144.8 kB[0m [31m4.9 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m77.9/77.9 kB[0m [31m1.9 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m58.3/58.3 kB[0m [31m5.5 MB/s[0m eta [36m0:00:00[0m
[?25h
```

```python PYTHON
import os
os.environ['COHERE_API_KEY'] = <your-api-key>
```

## Define tools

Your agent will be equipped with the following tools. The model can pick between

* doing a search on the web
* and/or retrieving data from a vector store
* and/or using a python interpreter
* and/or directly answering \[ this tool comes out of the box! ]

Plus the model can self-reflect.

#### Web search

You can easily equip your agent with web search!

```python PYTHON
from langchain_community.tools.tavily_search import TavilySearchResults

os.environ["TAVILY_API_KEY"] = <your-api-key> # you can create an API key for free on Tavily's website

internet_search = TavilySearchResults()
internet_search.name = "internet_search"
internet_search.description = "Returns a list of relevant document snippets for a textual query retrieved from the internet."


from langchain_core.pydantic_v1 import BaseModel, Field
class TavilySearchInput(BaseModel):
    query: str = Field(description="Query to search the internet with")
internet_search.args_schema = TavilySearchInput
```

#### Vector store

You can easily equip your agent with a vector store!

```python PYTHON
!pip --quiet install faiss-cpu tiktoken
```

```txt title="Output"
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m27.0/27.0 MB[0m [31m41.4 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m1.8/1.8 MB[0m [31m58.3 MB/s[0m eta [36m0:00:00[0m
[?25h
```

```python PYTHON
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_cohere import CohereEmbeddings

embd = CohereEmbeddings()

urls = [
    "https://paulgraham.com/best.html",
]

docs = [WebBaseLoader(url).load() for url in urls]
docs_list = [item for sublist in docs for item in sublist]

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=512, chunk_overlap=0
)
doc_splits = text_splitter.split_documents(docs_list)

vectorstore = FAISS.from_documents(
    documents=doc_splits,
    embedding=embd,
)

vectorstore_retriever = vectorstore.as_retriever()

```

```python PYTHON
from langchain.tools.retriever import create_retriever_tool

vectorstore_search = create_retriever_tool(
    retriever=vectorstore_retriever,
    name="vectorstore_search",
    description="Retrieve relevant info from a vectorstore that contains information from Paul Graham about how to write good essays."
)
```

#### Python interpreter tool

You can easily equip your agent with a python interpreter!

```python PYTHON
from langchain.agents import Tool
from langchain_experimental.utilities import PythonREPL

python_repl = PythonREPL()
python_tool = Tool(
    name="python_repl",
    description="Executes python code and returns the result. The code runs in a static sandbox without interactive mode, so print output or save output to a file.",
    func=python_repl.run,
)
python_tool.name = "python_interpreter"

class ToolInput(BaseModel):
    code: str = Field(description="Python code to execute.")
python_tool.args_schema = ToolInput
```

#### Transform any Python function in a Tool

You can easily equip your agent with any Python function!

```python PYTHON
from langchain_core.tools import tool
import random

@tool
def random_operation_tool(a: int, b: int):
  """Calculates a random operation between the inputs."""
  coin_toss = random.uniform(0, 1)
  if coin_toss > 0.5:
    return {'output': a*b}
  else:
    return {'output': a+b}

random_operation_tool.name = "random_operation" # use python case
random_operation_tool.description = "Calculates a random operation between the inputs."

from langchain_core.pydantic_v1 import BaseModel, Field
class random_operation_inputs(BaseModel):
    a: int = Field(description="First input")
    b: int = Field(description="Second input")
random_operation_tool.args_schema = random_operation_inputs
```

## Create ReAct Agent

The model can smartly pick the right tool(s) for the user query, call them in any sequence, analyze the results and self-reflect.
Once the model considers it has enough information to answer the user question, it generates the final answer.

```python PYTHON
from langchain.agents import AgentExecutor
from langchain_cohere.react_multi_hop.agent import create_cohere_react_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_cohere.chat_models import ChatCohere

llm = ChatCohere(model="command-a-03-2025", temperature=0.3)

preamble = """
You are an expert who answers the user's question with the most relevant datasource. You are equipped with an internet search tool and a special vectorstore of information about how to write good essays.
You also have a 'random_operation_tool' tool, you must use it to compute the random operation between two numbers.
"""


prompt = ChatPromptTemplate.from_template("{input}")

agent = create_cohere_react_agent(
    llm=llm,
    tools=[internet_search, vectorstore_search, python_tool, random_operation_tool],
    prompt=prompt,
)

agent_executor = AgentExecutor(agent=agent, tools=[internet_search, vectorstore_search, python_tool, random_operation_tool], verbose=True)
```

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

## Ask a more complex question to the ReAct agent

A question that requires using multipe tools, in sequence

```python PYTHON
response = agent_executor.invoke({
    "input": "In what year was the company that was founded as Sound of Music went public? What was its stock price in 2000 and 2010.",
    "preamble": preamble,
})

response['output']
```

```txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will search for the company that was founded as Sound of Music. Then, I will search for the year it went public. Finally, I will search for its stock price in 2000 and 2010.
{'tool_name': 'internet_search', 'parameters': {'query': 'company founded as Sound of Music'}}
[0m[36;1m[1;3m[{'url': 'https://www.mprnews.org/story/2012/05/15/best-buy-richard-schulze-legacy', 'content': 'Amazon is taking a piece of everyone\'s business,"\nSome analysts have questioned the extent to which Schulze\'s strong hand over the company has held it back in the face of digital competition. "\nSchulze hit on the "Best Buy" strategy when a twister ripped open a store and the company held a huge sale with low prices and lots of promotion. And Richard Schulz was able to outthink and outmaneuver the competition to put up Best Buy as the definitive place in the brick-and-mortar world to buy electronic equipment," Spector said.\n Best Buy\'s Richard Schulze: Stereo seller to retail giant\nShare\nIn 1966, Best Buy was a stereo specialty retailer called Sound of Music, founded by Richard Schulze in St. Paul.\n Former CEO Anderson said it is possible that Schulze\'s goals for the company were out of touch with the digital age, and that Schulze may have stuck around too long.\n'}, {'url': 'https://corporate.bestbuy.com/tag/sound-of-music/', 'content': 'As we celebrate Best Buy’s 50th anniversary, we sat down with founder and Chairman Emeritus Dick Schulze and current Chairman and CEO Hubert Joly to talk about how we got to where we are today and get a glimpse into where we’re going next.\n Sound of Music\n22 Aug: Best Buy at 50: A Q&amp;A with Founder Dick Schulze and CEO Hubert Joly\nTechnology has changed a lot over the past half century, and so has Best Buy.\n 14 Jun: 35 Years Ago Today, A Tornado Transformed Best Buy\nOn the afternoon of June 14, 1981, a tornado slammed into the Minneapolis suburbs, mere miles from where the Best Buy corporate headquarters now stands.\n Little did he know that it would become Best Buy, a nearly $40 billion company that now sells everything from TVs and laptops to drones and virtual-reality headsets.\n It was the most significant tornado to hit the Minneapolis-St. Paul area in 20 years — and its wake would change the path of our company.\n'}, {'url': 'https://historydraft.com/story/best-buy/timeline/841', 'content': "Best Buy announced the shutdown of the Future Shop chain in Canada\nOn March 28, 2015, Best Buy announced the shutdown of the Future Shop chain in Canada; 65 of its 131 former locations were converted into Best Buy locations, while the rest (primarily those in close proximity to an existing Best Buy) were closed permanently.\n Best Buy Company, Inc\nIn 1983, with seven stores and $10 million in annual sales, Sound of Music was renamed Best Buy Company, Inc.\nBest Buy debuted on the New York Stock Exchange\nBest Buy was taken public in 1985, and two years later it debuted on the New York Stock Exchange.\n The company closed all of its Best Buy-branded stores in China\nThe company closed all of its Best Buy-branded stores in China by February 2011, when it merged Best Buy China's operations with Jiangsu Five Star, which had become a wholly-owned subsidiary of Best Buy in 2009.\n Best Buy announced that it would start selling musical instruments and related gear in over 80 of its retail stores\nIn July 2008, Best Buy announced that it would start selling musical instruments and related gear in over 80 of its retail stores, making the company the second-largest musical-instrument distributor in the US.\n Best Buy hired Virtucom Group to revamp Best Buy's website and handle all of the company's online content\nIn January 2004, Best Buy hired Virtucom Group to revamp Best Buy's website and handle all of the company's online content.\n"}, {'url': 'https://en.wikipedia.org/wiki/Best_Buy', 'content': 'Under the Geek Squad brand, Best Buy offers computer repair, warranty service, and accidental service plans.[2] Best Buy provides an online community forum for members, where consumers can discuss product experiences, ask questions, and get answers from other members or retail product experts.[82]\nThe building exteriors of Best Buy-branded stores are typically light brown, with the entrance designed to look like a blue box emerging from the structure.[83] Corporate employees operated under a results only work environment from 2005 until March 2013, when the management style was abandoned by Best Buy CEO Hubert Joly.[84][85]\nAs of October 29, 2016, Best Buy operated 1,026 Best Buy, 331 Best Buy Mobile stand-alone stores, and 28 stand-alone Pacific Sales stores in the US.[2] Best Buy also operated: 135 Best Buy and 53 Best Buy Mobile stand-alone stores in Canada; and 18 Best Buy stores and 5 Best Buy Express stores in Mexico.[2] Best Buy exited the European market in April 2013, selling its stake in the business back to its partner Carphone Warehouse.[71][72]\nHouse brands[edit]\nBest Buy also produces products under eight house brands:[2]\nControversies[edit]\nWarranty[edit]\n The company, in announcing the result, said it was focusing more on digital media in its marketing, moving away from newspaper, magazine, and television advertising.[73]\nOn March 28, 2015, Best Buy announced the shutdown of the Future Shop chain in Canada; 65 of its 131 former locations were converted into Best Buy locations, while the rest (primarily those in close proximity to an existing Best Buy) were closed permanently.[74]\nOn March 1, 2018, the company announced that it would shut down its 250 standalone Best Buy Mobile stores in the United States by the end of May, due to low revenue and high costs. In August 2022, Best Buy said it would be laying off employees across the country after warnings of weaker sales, and the company cut its forecast for the remainder of 2022.[79]\nOn October 13, 2023, Best Buy announced that it would phase out the sale of physical home media in early 2024, citing changes in the market due to the prevalence of streaming video on demand services.[80][81]\nCorporate affairs[edit]\nBusiness operations[edit]\nBest Buy sells consumer electronics and a variety of related merchandise, including software, video games, music, mobile phones, digital cameras, car stereos, and video cameras, in addition to home appliances (washing machines, dryers, and refrigerators), in a noncommissioned sales environment.[2] The Best Buy Mobile stores were reported to account for 1% of the company\'s revenue.[75]\nOn May 9, 2018, the company unveiled a new logo for the first time in nearly three decades.[76]\nOn July 2, 2018, Best Buy announced it was cutting the amount of store space devoted to selling physical music, citing the popularity of streaming services as having reduced sales.[77]\nOn April 15, 2019, Best Buy announced that in June 2019, its current CFO, Corie Barry, would replace Hubert Joly[5] who held the position of CEO since August 2012. The customer was indicted for possession of child pornography, although the judge in the case later threw out nearly all the evidence against the defendant due to "false and misleading statements" made by an FBI agent while trying to secure a search warrant for the customer\'s house, and the government ultimately dropped the case.[97]\nPrivacy[edit]\nOn October 20, 2023, CBC News released the results of a Marketplace investigation which found that that Best Buy technicians had viewed private files, such as intimate photos, on customer devices.'}, {'url': 'https://www.company-histories.com/Best-Buy-Co-Inc-Company-History.html', 'content': 'As the Best Buy chain pushed past the 500-store mark in 2003 with the opening of 67 new stores in the United States, including the first stores in Alaska, Idaho, Utah, and West Virginia, the situation at the Musicland chains was deteriorating. Returning to the Core: 2003 and Beyond\nDespite the completion of this acquisition, Best Buy pushed ahead with a previously planned expansion of the Best Buy chain into Canada, opening eight stores in the Toronto area in the fall of 2002. Significant changes were made to the product mix, particularly by eliminating slower selling product lines and models; a greater emphasis was placed on selling service plans to customers; and "high touch" areas were added to the stores to help sell the burgeoning array of digital consumer products, such as cameras, cellular phones, satellite systems, and the fast-selling DVD player (first introduced in 1996) for which customers often needed more assistance. This rapid growth in digital product sales also inspired a shift in the overall product mix: sales of consumer electronics products (33 percent of the total) surpassed the sales of home office products (31 percent) for the first time (in 1999 these figures were 27 percent and 36 percent, respectively). Magnolia was founded in 1954 by Len Tweten, who built the firm into one of the most respected audio-video retailers in the nation based on the high quality of its merchandise, its dedication to exceptional customer service, and its renowned in-house repair/installation department.'}][0m[32;1m[1;3m
I have found that Best Buy was founded as Sound of Music. Now, I will search for the year it went public and its stock price in 2000 and 2010.
{'tool_name': 'internet_search', 'parameters': {'query': 'Best Buy went public'}}
[0m[36;1m[1;3m[{'url': 'https://www.zippia.com/best-buy-careers-1455/history/', 'content': 'Meantime, Best Buy was taken public in 1985, raising $8 million through an IPO, and two years later gained a listing on the New York Stock Exchange (NYSE). ... Best Buy may also be known as or be related to Best Buy, Best Buy Co Inc, Best Buy Co., Inc., Sound of Music (1966-1983) Best Buy Co. Superstores (1983-1984) Best Buy Superstores ...'}, {'url': 'https://atouchofbusiness.com/companies/best-buy/', 'content': 'Public Listing and IPO: Best Buy went public in 1985 and listed on the NYSE in 1987. Conceptual Changes: The late 1980s and 1990s brought new store formats and growth, with revenues surpassing $1 billion. Overcoming Market Challenges. Supplier Relations: Mid-1990s challenges led to a merchandising revamp.'}, {'url': 'https://www.encyclopedia.com/social-sciences-and-law/economics-business-and-labor/businesses-and-occupations/best-buy-co-inc', 'content': 'Best Buy grew rapidly with $28.5 million in sales in 1984—compared to $9.9 million in 1983. In 1985, with 9 stores, Best Buy became a public company. By 1987, Best Buy had 24 stores and sales of $240 million, but it was beginning to feel the crunch as other rapidly expanding consumer electronics retailers pushed their way into the market.'}, {'url': 'https://www.company-histories.com/Best-Buy-Co-Inc-Company-History.html', 'content': 'As the Best Buy chain pushed past the 500-store mark in 2003 with the opening of 67 new stores in the United States, including the first stores in Alaska, Idaho, Utah, and West Virginia, the situation at the Musicland chains was deteriorating. Returning to the Core: 2003 and Beyond\nDespite the completion of this acquisition, Best Buy pushed ahead with a previously planned expansion of the Best Buy chain into Canada, opening eight stores in the Toronto area in the fall of 2002. Significant changes were made to the product mix, particularly by eliminating slower selling product lines and models; a greater emphasis was placed on selling service plans to customers; and "high touch" areas were added to the stores to help sell the burgeoning array of digital consumer products, such as cameras, cellular phones, satellite systems, and the fast-selling DVD player (first introduced in 1996) for which customers often needed more assistance. This rapid growth in digital product sales also inspired a shift in the overall product mix: sales of consumer electronics products (33 percent of the total) surpassed the sales of home office products (31 percent) for the first time (in 1999 these figures were 27 percent and 36 percent, respectively). Magnolia was founded in 1954 by Len Tweten, who built the firm into one of the most respected audio-video retailers in the nation based on the high quality of its merchandise, its dedication to exceptional customer service, and its renowned in-house repair/installation department.'}, {'url': 'https://en.wikipedia.org/wiki/Best_Buy', 'content': 'Under the Geek Squad brand, Best Buy offers computer repair, warranty service, and accidental service plans.[2] Best Buy provides an online community forum for members, where consumers can discuss product experiences, ask questions, and get answers from other members or retail product experts.[82]\nThe building exteriors of Best Buy-branded stores are typically light brown, with the entrance designed to look like a blue box emerging from the structure.[83] Corporate employees operated under a results only work environment from 2005 until March 2013, when the management style was abandoned by Best Buy CEO Hubert Joly.[84][85]\nAs of October 29, 2016, Best Buy operated 1,026 Best Buy, 331 Best Buy Mobile stand-alone stores, and 28 stand-alone Pacific Sales stores in the US.[2] Best Buy also operated: 135 Best Buy and 53 Best Buy Mobile stand-alone stores in Canada; and 18 Best Buy stores and 5 Best Buy Express stores in Mexico.[2] Best Buy exited the European market in April 2013, selling its stake in the business back to its partner Carphone Warehouse.[71][72]\nHouse brands[edit]\nBest Buy also produces products under eight house brands:[2]\nControversies[edit]\nWarranty[edit]\n The company, in announcing the result, said it was focusing more on digital media in its marketing, moving away from newspaper, magazine, and television advertising.[73]\nOn March 28, 2015, Best Buy announced the shutdown of the Future Shop chain in Canada; 65 of its 131 former locations were converted into Best Buy locations, while the rest (primarily those in close proximity to an existing Best Buy) were closed permanently.[74]\nOn March 1, 2018, the company announced that it would shut down its 250 standalone Best Buy Mobile stores in the United States by the end of May, due to low revenue and high costs. In August 2022, Best Buy said it would be laying off employees across the country after warnings of weaker sales, and the company cut its forecast for the remainder of 2022.[79]\nOn October 13, 2023, Best Buy announced that it would phase out the sale of physical home media in early 2024, citing changes in the market due to the prevalence of streaming video on demand services.[80][81]\nCorporate affairs[edit]\nBusiness operations[edit]\nBest Buy sells consumer electronics and a variety of related merchandise, including software, video games, music, mobile phones, digital cameras, car stereos, and video cameras, in addition to home appliances (washing machines, dryers, and refrigerators), in a noncommissioned sales environment.[2] The Best Buy Mobile stores were reported to account for 1% of the company\'s revenue.[75]\nOn May 9, 2018, the company unveiled a new logo for the first time in nearly three decades.[76]\nOn July 2, 2018, Best Buy announced it was cutting the amount of store space devoted to selling physical music, citing the popularity of streaming services as having reduced sales.[77]\nOn April 15, 2019, Best Buy announced that in June 2019, its current CFO, Corie Barry, would replace Hubert Joly[5] who held the position of CEO since August 2012. The customer was indicted for possession of child pornography, although the judge in the case later threw out nearly all the evidence against the defendant due to "false and misleading statements" made by an FBI agent while trying to secure a search warrant for the customer\'s house, and the government ultimately dropped the case.[97]\nPrivacy[edit]\nOn October 20, 2023, CBC News released the results of a Marketplace investigation which found that that Best Buy technicians had viewed private files, such as intimate photos, on customer devices.'}][0m[32;1m[1;3m
{'tool_name': 'internet_search', 'parameters': {'query': 'Best Buy stock price in 2000 and 2010'}}
[0m[36;1m[1;3m[{'url': 'https://finance.yahoo.com/quote/BBY/history/', 'content': 'Discover historical prices for BBY stock on Yahoo Finance. View daily, weekly or monthly format back to when Best Buy Co., Inc. stock was issued.'}, {'url': 'https://www.macrotrends.net/stocks/charts/BBY/best-buy/stock-price-history', 'content': 'Best Buy - 39 Year Stock Price History | BBY. Prices ... 2010, 25.1877, 25.7674, 31.2441, 20.2713, 22.3228 ... 2000, 16.0083, 15.2882, 22.8658, 5.9318, 7.8595, -\xa0...'}, {'url': 'https://investors.bestbuy.com/investor-relations/stock-info/quote-and-chart/', 'content': 'Price 79.30. Change -0.88. Volume 666,622.'}, {'url': 'https://companiesmarketcap.com/best-buy/stock-price-history/', 'content': 'Stock price history for Best Buy (BBY). Highest end of day price: $138.00 USD on 2021-11-22. Lowest end of day price: $0.14 USD on 1985-05-02\xa0...'}, {'url': 'https://www.netcials.com/stock-price-chart-history-nyse/BBY-Best-Buy-Co-Inc/', 'content': '1 Best Buy Co Inc (BBY) 20 Years Stock Chart History ; 2000, 16.24 (17.6%), 23.199 (29.07%) ; 2001, 14.80 (-8.87%), 20.1319 (-13.22%) ; 2002, 14.59 (-1.42%)\xa0...'}][0m[32;1m[1;3mRelevant Documents: 0,1,2,3,4,5,6,7,11,13,14
Cited Documents: 0,1,2,3,4,5,6,7,11,14
Answer: Best Buy, which was founded as Sound of Music, went public in 1985. Its stock price in 2000 was between $5.93 and $16.24 and in 2010, it was between $20.27 and $31.24.
Grounded answer: <co: 0,1,2,3,4="">Best Buy</co:>, which was founded as Sound of Music, went public in <co: 2,5,6,7="">1985</co:>. Its stock price in <co: 11,14="">2000</co:> was between <co: 11="">$5.93</co:> and <co: 14="">$16.24</co:> and in <co: 11="">2010</co:>, it was between <co: 11="">$20.27</co:> and <co: 11="">$31.24</co:>.[0m

[1m> Finished chain.[0m





'Best Buy, which was founded as Sound of Music, went public in 1985. Its stock price in 2000 was between $5.93 and $16.24 and in 2010, it was between $20.27 and $31.24.'
```

## Have a multi-turn conversation with the ReAct agent

The chat history enables you to have multi-turn conversations with the ReAct agent.

```python PYTHON
from langchain_core.messages import HumanMessage, AIMessage

chat_history = [
    HumanMessage(content="I'm considering switching to Oracle for my CRM."),
    AIMessage(content="That sounds like a good idea! How can I help you?"),
    HumanMessage(content="Recap me all the info you can find about their offering."),
]

prompt = ChatPromptTemplate.from_messages(chat_history)
```

```python PYTHON
agent = create_cohere_react_agent(
    llm=llm,
    tools=[internet_search, vectorstore_search, python_tool],
    prompt=prompt,
)

agent_executor = AgentExecutor(agent=agent, tools=[internet_search, vectorstore_search, python_tool], verbose=True)
```

```python PYTHON
response = agent_executor.invoke({
    "preamble": preamble,
})

response['output']
```

```txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will search for 'Oracle CRM offering' and relay the information I find to the user.
{'tool_name': 'internet_search', 'parameters': {'query': 'Oracle CRM offering'}}
[0m[36;1m[1;3m[{'url': 'https://docs.oracle.com/en/applications/siebel/', 'content': 'Siebel CRM delivers a combination of transactional, analytical, and engagement features to manage all customer-facing operations. With solutions tailored to more than 20 industries, Siebel CRM delivers comprehensive on-premise CRM solutions that are tailored industry solutions with role-based customer intelligence and pre-built integration.'}, {'url': 'https://www.softwareadvice.com/resources/breaking-down-oracle-crm/', 'content': "Oracle's Marketing Cloud provides a comprehensive set of tools that cover a range of digital marketing needs. This includes tools for cross-channel marketing, i.e., marketing automation for both B2B and B2C marketers, as well as data management, content marketing and social media marketing. Cross-Channel Marketing."}, {'url': 'https://www.trustradius.com/products/oracle-crm-on-demand/reviews?qs=pros-and-cons', 'content': "What is Oracle CRM On Demand?The basis of this offering is the Market2Lead product that Oracle acquired in 2010. It has now been fully integrated with Oracle's On Demand CRM product and is a full-featured marketing automation product with features from lead management and nurturing, to measuring marketing ROI."}, {'url': 'https://www.oracle.com/cx/siebel/', 'content': 'In addition to standard CRM functionality, this industry solution includes asset, premises, and contracts management; work orders; oil well management and oil field service; B2C and B2B web portals; and credit and fraud management capabilities.\nDesigned for pharmaceutical sales, Siebel CRM Life Sciences provides personalized content delivery tools to help sales and marketing teams deliver the right messages during each customer interaction.\n Marketing, sales, and customer service applications are fully integrated and designed to manage the complex interactions and relationships between brand owners, their partners (including brokers and distributors), their customers, and the end consumer.\n It leverages data and AI to transform CX–launching offers, acquiring and retaining customers, omnichannel ecommerce and customer care, and fulfilling and monetizing services.\n It leverages data and AI to transform CX–launching offers, acquiring and retaining customers, omnichannel ecommerce and customer care, and fulfilling and monetizing services.\n Provide world-class citizen services while delivering comprehensive, cost-efficient case management and policy management, including social services, justice and public safety, constituent services/311, self-service citizen portals, tax and revenue, and licensing and permitting.\n'}, {'url': 'https://www.suretysystems.com/insights/oracle-customer-relationship-management-a-complete-overview/', 'content': 'Effective CRM systems offer the following features for enterprise users: Simple, easy-to-use interface; ... Oracle CRM simplifies customer relationship management by enhancing customer interactions and improving customer satisfaction and sales growth. Oracle Client Experience (CX), a connected suite of tools that transcends standard CRM ...'}][0m[32;1m[1;3mRelevant Documents: 0,1,2,3,4
Cited Documents: 0,1,2,3,4
Answer: Oracle's CRM offering includes the following:
- Marketing Cloud, which provides a comprehensive set of tools that cover a range of digital marketing needs, including cross-channel marketing, marketing automation, data management, content marketing and social media marketing
- CRM On Demand, which is a full-featured marketing automation product with features from lead management and nurturing, to measuring marketing ROI
- Siebel CRM, which delivers a combination of transactional, analytical, and engagement features to manage all customer-facing operations, with solutions tailored to more than 20 industries
- Siebel CRM Life Sciences, which provides personalised content delivery tools to help sales and marketing teams deliver the right messages during each customer interaction
- Oracle Client Experience (CX), a connected suite of tools that transcends standard CRM
Grounded answer: Oracle's CRM offering includes the following:
- <co: 1="">Marketing Cloud</co:>, which provides a <co: 1="">comprehensive set of tools</co:> that cover a <co: 1="">range of digital marketing needs</co:>, including <co: 1="">cross-channel marketing</co:>, <co: 1="">marketing automation</co:>, <co: 1="">data management</co:>, <co: 1="">content marketing</co:> and <co: 1="">social media marketing</co:>
- <co: 2="">CRM On Demand</co:>, which is a <co: 2="">full-featured marketing automation product</co:> with features from <co: 2="">lead management and nurturing</co:>, to <co: 2="">measuring marketing ROI</co:>
- <co: 0,3="">Siebel CRM</co:>, which delivers a <co: 0="">combination of transactional, analytical, and engagement features</co:> to <co: 0="">manage all customer-facing operations</co:>, with <co: 0="">solutions tailored to more than 20 industries</co:>
- <co: 3="">Siebel CRM Life Sciences</co:>, which provides <co: 3="">personalised content delivery tools</co:> to help <co: 3="">sales and marketing teams deliver the right messages during each customer interaction</co:>
- <co: 4="">Oracle Client Experience (CX</co:>), a <co: 4="">connected suite of tools</co:> that <co: 4="">transcends standard CRM</co:>[0m

[1m> Finished chain.[0m





"Oracle's CRM offering includes the following:\n- Marketing Cloud, which provides a comprehensive set of tools that cover a range of digital marketing needs, including cross-channel marketing, marketing automation, data management, content marketing and social media marketing\n- CRM On Demand, which is a full-featured marketing automation product with features from lead management and nurturing, to measuring marketing ROI\n- Siebel CRM, which delivers a combination of transactional, analytical, and engagement features to manage all customer-facing operations, with solutions tailored to more than 20 industries\n- Siebel CRM Life Sciences, which provides personalised content delivery tools to help sales and marketing teams deliver the right messages during each customer interaction\n- Oracle Client Experience (CX), a connected suite of tools that transcends standard CRM"
```


# Basic RAG: Retrieval-Augmented Generation with Cohere

> This page describes how to work with Cohere's basic retrieval-augmented generation functionality.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/Vanilla_RAG.ipynb" />

Retrieval-Augmented Generation (RAG) is a technique that combines the strengths of pre-trained language models with the ability to retrieve information from a large corpus of documents. RAG **enables the language model to produce more informed, accurate, and contextually relevant answers** than by relying on its pre-trained knowledge alone.

At Cohere, all RAG calls come with... **precise citations**! 🎉
The model cites which groups of words, in the RAG chunks, were used to generate the final answer.\
These citations make it easy to check where the model’s generated response claims are coming from and they help users gain visibility into the model reasoning.

RAG consists of 3 steps:

* Step 1: Indexing and given a user query, retrieve the relevant chunks from the index
* Step 2: Optionally, rerank the retrieved chunks
* Step 3: Generate the model final answer with **precise citations**, given the retrieved and reranked chunks

## Step 0 - Imports & Getting some data

In this example, we'll use a recent piece of text, that wasn't in the training data: the Wikipedia page of the movie "Dune 2".

In practice, you would typically do RAG on much longer text, that doesn't fit in the context window of the model.

```python PYTHON
%pip install "cohere<5" --quiet
```

```txt title="Output"
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m52.8/52.8 kB[0m [31m1.6 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m3.1/3.1 MB[0m [31m33.6 MB/s[0m eta [36m0:00:00[0m
[?25h
```

```python PYTHON
import cohere
API_KEY = "..." # fill in your Cohere API key here
co = cohere.Client(API_KEY)
```

```python PYTHON
!pip install wikipedia --quiet
import wikipedia
```

```txt title="Output"
Preparing metadata (setup.py) ... [?25l[?25hdone
Building wheel for wikipedia (setup.py) ... [?25l[?25hdone
```

```python PYTHON
article = wikipedia.page('Dune Part Two')
text = article.content
print(f"The text has roughly {len(text.split())} words.")
```

```txt title="Output"
The text has roughly 5323 words.
```

## Step 1 - Indexing and given a user query, retrieve the relevant chunks from the index

We index the document in a vector database. This requires getting the documents, chunking them, embedding, and indexing them in a vector database. Then we retrieved relevant results based on the users' query.

### We split the document into chunks of roughly 512 words

```python PYTHON
%pip install -qU langchain-text-splitters --quiet
from langchain_text_splitters import RecursiveCharacterTextSplitter
```

```txt title="Output"
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m256.9/256.9 kB[0m [31m6.6 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m66.6/66.6 kB[0m [31m8.2 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m138.5/138.5 kB[0m [31m14.5 MB/s[0m eta [36m0:00:00[0m
[?25h
```

```python PYTHON
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=50,
    length_function=len,
    is_separator_regex=False,
)

chunks_ = text_splitter.create_documents([text])
chunks = [c.page_content for c in chunks_]
print(f"The text has been broken down in {len(chunks)} chunks.")
```

```txt title="Output"
The text has been broken down in 91 chunks.
```

### Embed every text chunk

Cohere embeddings are state-of-the-art.

```python PYTHON
model="embed-v4.0"
response = co.embed(
    texts= chunks,
    model=model,
    input_type="search_document",
    embedding_types=['float']
)
embeddings = response.embeddings.float
print(f"We just computed {len(embeddings)} embeddings.")
```

```txt title="Output"
We just computed 91 embeddings.
```

### Store the embeddings in a vector database

We use the simplest vector database ever: a python dictionary using `np.array()`.

```python PYTHON
!pip install numpy --quiet
```

```python PYTHON
import numpy as np
vector_database = {i: np.array(embedding) for i, embedding in enumerate(embeddings)}
```

## Given a user query, retrieve the relevant chunks from the vector database

### Define the user question

```python PYTHON
query = "Name everyone involved in writing the script, directing, and producing 'Dune: Part Two'?"

```

### Embed the user question

Cohere embeddings are state-of-the-art.

```python PYTHON
response = co.embed(
    texts=[query],
    model=model,
    input_type="search_query",
    embedding_types=['float']
)
query_embedding = response.embeddings.float[0]
print("query_embedding: ", query_embedding)
```

```txt title="Output"
query_embedding:  [-0.068603516, -0.02947998, -0.06274414, -0.015449524, -0.033294678, 0.0056877136, -0.047210693, 0.04714966, -0.024871826, 0.008148193, 0.0770874, 0.023880005, -0.058685303, -0.052520752, 0.012832642, 0.024398804, 0.0053215027, 0.035491943, 0.02961731, -0.0069847107, 0.01083374, -0.0011358261, -0.002199173, 0.018417358, 0.027389526, -0.002691269, -0.026535034, 0.015197754, 0.024368286, 0.03729248, 0.0057754517, -0.02229309, -0.014694214, 0.019989014, -0.0036315918, -0.013793945, 0.02835083, 0.006011963, 0.011428833, 0.008682251, 0.046142578, -0.040039062, -0.032196045, -0.002653122, -0.012580872, -0.0041618347, 0.03111267, -0.016799927, 0.014801025, -0.00030636787, -0.033050537, 0.033966064, -0.016021729, -0.025009155, -0.007534027, -0.017074585, 0.008415222, -0.10620117, 0.019195557, -0.015686035, -0.0043182373, -0.045440674, 0.05404663, 0.030776978, -0.014129639, -0.01499939, -0.007286072, 0.009933472, 0.06390381, 0.02444458, -0.010345459, 0.041931152, 0.032989502, -0.04522705, 0.056610107, 0.0068893433, -0.008911133, 0.012489319, 0.01675415, 0.020065308, 0.018753052, 0.022659302, -0.051849365, -0.04925537, 0.046325684, -0.005268097, 0.0026874542, -0.036712646, 0.009437561, -0.0037841797, -0.01473999, -0.034179688, -0.0011606216, 0.05026245, 0.0020771027, -0.016021729, -0.0044898987, 0.04168701, -0.015205383, 0.019210815, -0.012374878, -0.031311035, 0.03111267, -0.040100098, -0.016479492, 0.020446777, 0.010192871, 0.0037841797, -0.0023765564, 0.015220642, -0.016571045, -0.006454468, 0.037384033, -0.044555664, -0.008262634, 0.019546509, 0.009460449, 0.014701843, 0.02658081, -0.02078247, 0.015571594, 0.013153076, -0.010375977, 0.047912598, 0.005393982, -0.007911682, -0.019378662, 0.023529053, -0.0033550262, -0.04598999, -0.0052871704, 0.040252686, 0.011375427, 0.01550293, -0.004508972, 0.006515503, 0.003370285, -0.022766113, 0.00062561035, -0.0007596016, -0.0015277863, 0.0149002075, 0.061401367, 8.261204e-05, 0.06359863, -0.01537323, 0.007446289, 0.018814087, 0.02507019, 0.024215698, 0.006122589, 0.005886078, -0.03829956, 0.029037476, 0.07720947, 0.016921997, 0.022109985, 0.005958557, 0.028793335, 0.019485474, 0.015174866, 0.026153564, 0.032318115, 0.034210205, 0.027145386, -0.019515991, -0.018661499, 0.020477295, 0.008598328, -0.06573486, -0.037109375, 0.04043579, 0.030471802, -0.0010843277, 0.009757996, 0.026947021, 0.037017822, -0.018234253, -0.0115356445, 0.099365234, 0.027816772, -0.019927979, 0.0020961761, 0.013198853, -0.019073486, 2.7656555e-05, 0.041259766, 0.029510498, -0.016204834, 0.028137207, 0.039489746, 0.034698486, -0.03918457, -0.029418945, 0.02041626, 0.0073432922, -0.018569946, -0.009849548, 0.002861023, 0.030319214, -0.012886047, 0.014671326, -0.035827637, 0.007247925, -0.027709961, -0.022079468, 0.0012960434, 0.015426636, -0.01725769, 0.01525116, 0.025360107, -0.0077400208, -0.039916992, 0.029037476, -0.011154175, 0.007736206, -0.041748047, 0.05343628, 0.007286072, 0.0435791, 0.034301758, -0.047210693, 0.03552246, -0.015327454, 0.029922485, -0.018859863, 0.013053894, -0.028060913, 0.07757568, -0.020462036, 0.070739746, -0.010223389, 0.03604126, 0.02758789, -0.023284912, 0.012184143, 0.029144287, 0.023880005, -0.019378662, -0.0051116943, 0.0048675537, 0.01864624, -0.04397583, -0.007598877, 0.0713501, 0.0115737915, 0.002922058, 0.011619568, 0.017364502, 0.031921387, -0.0019664764, -0.008575439, 0.003484726, -0.09466553, 0.03475952, 0.026611328, -0.039520264, -0.0104522705, -0.005443573, -0.008392334, 0.012908936, 0.0043792725, -0.002456665, -0.028396606, -0.02027893, -0.0005569458, 0.027786255, 0.03427124, -0.0062332153, -0.018203735, 0.019241333, 0.07244873, -0.0028057098, 0.01234436, -0.0018787384, -0.027496338, 0.0015287399, -0.004032135, -0.013748169, -0.01878357, 0.0018053055, -0.01159668, 0.028213501, 0.004776001, 0.042388916, 0.0024280548, 0.017471313, -0.038085938, 0.026321411, 0.02973938, 0.06213379, 0.006401062, 0.036102295, -0.028121948, -0.00869751, -0.016693115, 0.029190063, 0.016784668, -0.008628845, 0.0039634705, -0.0035381317, 0.019500732, 0.025009155, -0.04547119, -0.003572464, 0.05215454, 0.067871094, -0.04257202, -0.02293396, -0.027175903, 0.05340576, 0.019226074, 0.039978027, 0.056121826, -0.028320312, -0.020217896, -0.035003662, 0.03225708, 0.028656006, 0.062347412, 0.12915039, -0.0137786865, 0.0022201538, -0.057434082, -0.04397583, -0.049865723, -0.013160706, -0.03353882, 0.006427765, -0.014823914, -0.008201599, -0.036346436, -0.037353516, -0.010528564, -0.015930176, -0.027572632, 0.0074272156, 0.004547119, -0.024414062, -0.018859863, -0.020095825, 0.029632568, -0.00067043304, -0.044036865, -0.0043411255, -0.005256653, -0.019195557, 0.022262573, -0.00020956993, -0.013877869, -0.011108398, -0.020324707, -0.015808105, -0.025039673, -0.009498596, 0.05090332, 0.0046195984, -0.017150879, 0.04309082, -0.029067993, 0.002670288, -0.00026249886, -0.032409668, -0.053100586, 0.012481689, -0.014633179, 0.0013475418, -0.034332275, 0.038330078, 0.014892578, -0.046936035, 0.021591187, -0.020385742, -0.0052604675, 0.02796936, 0.0014333725, 0.012077332, -0.0118255615, -0.005569458, 0.008491516, 0.009841919, 0.0031318665, -0.003408432, -0.007144928, 0.040374756, -0.0038928986, 0.005279541, -0.008415222, 0.031707764, 0.0140686035, -0.015029907, -0.02810669, -0.0078125, -0.030853271, -0.03201294, 0.021316528, -0.036193848, -0.0423584, 0.0072784424, 0.014801025, 0.0019607544, -0.012367249, -0.009056091, -0.021438599, -0.02645874, 0.038726807, -0.007549286, 0.0049591064, 0.019012451, 0.017791748, -0.009185791, 0.04006958, 0.003107071, -0.0075302124, -0.010375977, -0.009246826, -0.02130127, -0.0056762695, -0.0076789856, 0.010009766, -0.010536194, 0.041107178, 0.0021133423, 0.029891968, 0.01626587, 0.042236328, -0.02784729, -0.032836914, 0.0317688, 0.045715332, 0.000116825104, 0.028030396, 0.007205963, 0.012512207, -0.035583496, -0.048034668, -0.023529053, -0.04953003, 0.0345459, -0.048339844, -0.060272217, -0.004512787, 0.04425049, 0.0076141357, 0.029510498, 0.007396698, 0.003353119, -0.038726807, 0.07183838, -0.026901245, -0.023529053, -0.038085938, 0.068725586, 0.018096924, -0.013534546, 0.05883789, -0.016113281, 0.017944336, 0.041046143, 0.022918701, 0.036499023, 0.015296936, -0.04916382, 0.0075683594, -0.011390686, 0.009735107, -0.0070152283, 0.003129959, -0.032562256, 0.0003478527, -0.0036640167, -0.006893158, -0.016098022, -0.034332275, 0.037750244, -0.010269165, 0.016494751, -0.02394104, 0.03753662, -0.022644043, -0.0008234978, 0.001001358, -0.048217773, 0.04989624, 0.0078125, 0.0044937134, 0.027038574, 0.04736328, -0.02973938, -0.011726379, 0.01348114, 0.021408081, 0.00844574, -0.03741455, -0.015686035, -0.040893555, 0.001452446, -0.025405884, 0.07348633, 0.038238525, -0.019958496, 0.023071289, -0.016403198, -0.08105469, 0.0071029663, -0.019088745, 5.8174133e-05, -0.005569458, 0.01399231, 0.02255249, 0.011222839, 0.00028824806, 0.0066184998, 0.0017499924, -0.009864807, -0.0115737915, 0.053100586, 0.0065231323, 0.001865387, -0.026428223, 0.03692627, 0.025390625, 0.022613525, 0.018722534, 0.007675171, -0.03439331, 0.041625977, -0.01789856, -0.041046143, 0.0051460266, 0.04144287, 0.048553467, 0.054595947, -0.01108551, -0.033935547, -0.026275635, -0.0118255615, -0.021362305, -0.009841919, -0.00724411, 0.028900146, 0.009887695, -0.023803711, 0.016311646, 0.018798828, -0.03668213, 0.046844482, 0.010696411, -0.014717102, -0.008110046, -0.004589081, -0.0028076172, -0.050811768, -0.017196655, -0.03491211, 0.0074005127, -0.038909912, 0.032440186, -0.034362793, -0.008682251, 0.032928467, -0.04626465, -0.009666443, 0.018951416, 0.031951904, -0.003791809, 0.02015686, -0.05532837, -0.005683899, -0.00054216385, -0.0034332275, 0.008659363, 0.02130127, -0.038879395, -0.0033397675, -0.03866577, -0.0049934387, 0.017944336, 0.001496315, 0.019485474, -0.004348755, 0.00046491623, 0.0007157326, 0.035614014, -0.027694702, 0.03692627, -0.008491516, 0.0524292, -0.016662598, -0.0017795563, -0.021575928, -0.018753052, -0.049346924, -0.06652832, 0.04272461, 0.03186035, 0.0011978149, 0.03463745, 0.024002075, 0.02607727, 0.020446777, 0.0256958, 0.026855469, 0.0074005127, -0.067993164, 0.017944336, -0.0039482117, 0.05496216, -0.041412354, 0.014175415, 0.02444458, -0.026412964, 0.057403564, -0.026779175, 0.023254395, 0.03945923, 0.033569336, -0.030258179, -0.039093018, -0.036468506, 0.017105103, 0.009635925, 0.025497437, 0.04156494, -0.02571106, -0.0010414124, -0.005630493, -0.016448975, -0.026733398, 0.001326561, -0.042022705, 0.0012521744, -0.041259766, -0.12182617, -0.03857422, 0.12548828, -0.005947113, -0.020736694, -0.0033855438, 0.03778076, -0.033813477, 0.038970947, 0.003921509, 0.011810303, 0.031982422, -0.032562256, -0.002653122, -0.025009155, -0.03805542, -0.016998291, 0.018173218, 0.0158844, 0.0011739731, 0.048217773, -0.020401001, 0.044708252, -0.017318726, 0.014457703, -0.041809082, 0.010543823, 0.041931152, 0.076293945, -0.054779053, 0.060272217, -0.046936035, 0.02949524, 0.00554657, 0.041534424, -0.013046265, -0.056152344, 0.010406494, 0.02973938, -0.023727417, -0.022476196, -0.024734497, -0.013168335, 0.060424805, 0.011787415, 0.018997192, -0.043426514, -0.00077724457, -0.010154724, 0.017150879, -0.01171875, -0.022476196, 0.0034255981, -0.0026454926, 0.004837036, -0.0043296814, 0.02619934, -0.021560669, -0.039733887, -0.022415161, -0.06817627, -0.023223877, -0.018585205, -0.015319824, 0.012588501, 0.0064353943, -0.013748169, 0.043304443, 0.002626419, -0.029373169, -0.016784668, -0.026184082, 0.05847168, 0.034179688, 0.03842163, -0.05493164, -0.017486572, 0.016540527, 0.03164673, 0.089904785, 0.013534546, -0.07684326, -0.024108887, 0.07434082, 0.030395508, 0.007091522, 0.07373047, 0.012527466, -0.010856628, -0.01828003, -0.045196533, 0.00065279007, -0.0637207, 0.010726929, 0.023880005, -0.0030708313, -0.012298584, 0.027236938, -0.04928589, 0.023071289, 0.008674622, -0.023529053, -0.015838623, -0.010543823, 0.012168884, 0.014854431, -0.05834961, -0.06088257, -0.012313843, 0.035461426, 0.02027893, 0.019348145, -0.014602661, -0.02104187, -0.0309906, 0.001405716, -0.019973755, -0.00157547, -0.003944397, 0.0009326935, -0.02078247, -0.015731812, -0.044433594, 0.03390503, 0.057159424, 0.018585205, -0.023895264, -0.0057029724, 0.0049552917, 0.013412476, 0.022399902, 0.010154724, 0.0519104, 0.06591797, 0.018341064, 0.012161255, -0.05810547, -0.043304443, -0.031173706, 0.0023860931, -0.003944397, 0.11425781, -0.031036377, 0.019989014, -0.038635254, -0.025939941, 0.035064697, 0.041168213, 0.03161621, -0.069885254, -0.04537964, 0.028945923, -0.023162842, 0.019226074, -0.028442383, 0.015594482, -0.019256592, -0.0046463013, 0.034240723, 0.009124756, 0.05718994, 0.031219482, 0.02154541, 0.009590149, 0.00076818466, 0.04849243, -0.029129028, -0.03375244, -0.023391724, -0.028381348, -0.029708862, -0.0132369995, 0.010353088, 0.020263672, -0.030807495, 0.01007843, -0.03704834, 0.023376465, -0.03665161, 0.03741455, 0.015144348, 0.057281494, 0.03137207, 0.048431396, 0.021194458, 0.008110046, -0.03540039, -0.015312195, 0.022384644, 0.0065956116, 0.008056641, 0.0018348694, -0.009246826, 0.030380249, 0.0003862381, 0.0051841736, 0.04486084, 0.017807007, 0.0026130676, 0.07977295, 0.05419922, 0.062194824, 0.02633667, 0.024841309, -0.041625977, -0.005897522, 0.04031372, -0.055908203, 0.0026226044, -0.05340576, -0.05496216, 0.011474609, -0.006954193, -0.013122559, 0.019714355, -0.07159424, 0.031173706, 0.0034255981, -0.0034103394, 0.0440979, 0.011779785, -0.007827759, -0.03173828, -0.020950317, -0.030166626, -0.035308838, 0.030792236, 0.04525757, -0.028701782, -0.011100769, -0.02331543, -0.0357666, -0.025680542, 0.0011911392, 0.01940918, 0.05706787, 0.028381348, 0.007133484, -0.07733154, -0.007686615, 0.03869629, 0.0066833496, 0.008842468, 0.03439331, -0.014282227, 0.0357666, -0.004737854, -0.039794922, -0.0070381165, 0.02670288, 0.0107421875, 0.016189575, -0.06555176, -0.0138549805, 0.0008363724, -0.016693115, 0.006904602, -0.020263672, -0.030426025, 0.008453369, -0.046173096, -0.01802063, -0.013595581, -0.0044288635, -0.0039978027, -0.0044898987, 0.0007619858, 0.003921509, 0.0053977966, 0.020385742, -0.012329102, -0.023803711, -0.0057525635, 0.038330078, -0.014549255, -0.06298828, -0.047607422, 0.039245605, -0.06781006, -0.035217285, -0.009056091, 0.019927979, -0.003932953, -0.020309448, -0.017044067, 0.018127441, -8.624792e-05, -0.043182373, 0.009590149, 0.035308838, 0.031951904, 0.0011615753, -0.042022705, 0.079956055, 0.026687622, 0.013542175, -0.0074157715, -0.00983429, -0.0022563934, 0.07373047, 0.059387207, 0.03488159, 0.0071372986, -0.06427002, -0.0546875, -0.02482605, 0.11071777, -0.021072388, 0.01626587, -0.049713135, 0.061553955, -0.016860962, 0.051971436, -0.012962341, -0.0011711121, -0.014198303, -0.0061149597, -0.005836487, 0.00022387505, -0.027618408, 0.019836426, 0.009933472, 0.02368164, -0.020309448, -0.0049591064, -0.008628845, -0.03253174, -0.017684937, 0.02468872, -0.0023498535, 0.01448822, 0.061920166, 0.031707764, -0.0026416779, -0.040985107, -0.06335449, -0.036071777, 0.05404663, -0.0044136047, -0.0146102905, -0.0033416748, 0.028671265, -0.012771606, -0.0016565323, -0.0038909912, -0.02407837, -0.009857178, 0.0014467239, -0.008720398, -0.006011963, 0.032073975, -0.033325195, 0.014862061, -0.017227173, -0.018753052, -0.0060424805, 0.022567749, -0.017654419, -0.017562866, -0.07244873, -0.0881958, 0.050476074, 0.02609253, -0.032409668, 0.07458496, 0.009399414, 0.009117126, -0.031051636, -0.03451538, -0.004219055, -0.05718994, 0.020080566, -0.025421143, -0.010948181, 0.06341553, -0.009231567, -0.021697998, -0.009719849, 0.012802124, -0.020370483, 0.0034389496, 0.018859863, -0.025680542, 0.0013141632, 0.068603516, -0.021026611, 0.021881104, -0.0395813, -0.0019073486, 0.0056037903, -0.032348633]
```

### Retrieve the most relevant chunks from the vector database

We use cosine similarity to find the most similar chunks

```python PYTHON
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

similarities = [cosine_similarity(query_embedding, chunk) for chunk in embeddings]
print("similarity scores: ", similarities)

sorted_indices = np.argsort(similarities)[::-1]

top_indices = sorted_indices[:10]
print("Here are the indices of the top 10 chunks after retrieval: ", top_indices)

top_chunks_after_retrieval = [chunks[i] for i in top_indices]
print("Here are the top 10 chunks after retrieval: ")
for t in top_chunks_after_retrieval:
    print("== " + t)
```

```txt title="Output"
similarity scores:  [0.6953257882233425, 0.3713410510180273, 0.46501499776898964, 0.5448546916785195, 0.4014738351361969, 0.3231420292334584, 0.3179003053384008, 0.42799691553367775, 0.18882594531435784, 0.36868801306504106, 0.3404040737300553, 0.3852837621219358, 0.2600249419491577, 0.3723244353775111, 0.3631492691137214, 0.47574774051439606, 0.40415422750911745, 0.4149923346201023, 0.5014741934381444, 0.3549433331883204, 0.32072714802512714, 0.14770872479410424, 0.585277816615252, 0.6999636953772764, 0.7722295084104617, 0.4895347049465806, 0.5170096485954725, 0.7137817366881455, 0.5224900699612323, 0.5914632581598285, 0.2657897083381463, 0.6462342489537262, 0.6317222315431096, 0.5982303530756702, 0.5138265091630297, 0.41385121172723643, 0.4293941094100836, 0.4173182546482015, 0.42621236706314475, 0.4428474375355954, 0.35058541576139896, 0.3578709652019502, 0.3930157841938308, 0.3564608202848675, 0.23016661533167404, 0.4933441863421645, 0.41037089239250985, 0.39993051898770193, 0.3119997063424595, 0.2677143729521374, 0.3700866951454496, 0.46727994925061545, 0.4393343280374425, 0.42111290117172434, 0.4485349189824285, 0.4710573736688592, 0.24169956903740436, 0.3840442910806355, 0.14284631817675886, 0.5381588054138154, 0.431113882725076, 0.5189547209048608, 0.3950667224233914, 0.32429768756510174, 0.4370358125161736, 0.18727062244331039, 0.5206375682478743, 0.5175737635701252, 0.5326043981628349, 0.45586923626994363, 0.21667338125532032, 0.16459878595959285, 0.22236726481673777, 0.5187259906958807, 0.2884444442338396, 0.286407544555338, 0.2313840178160818, 0.2057731158935257, 0.5973876998341746, 0.42904243401792086, 0.4081217538000544, 0.5330523063972133, 0.45080561486977405, 0.414703452285757, 0.2569028899107211, 0.5087916806929323, 0.14159076456040554, 0.46505779053352697, 0.556364222182839, 0.35464351181035236, 0.40174477023626]
Here are the indices of the top 10 chunks after retrieval:  [24 27 23  0 31 32 33 78 29 22]
Here are the top 10 chunks after retrieval:
== stunt coordinator. Dune: Part Two was produced by Villeneuve, Mary Parent, and Cale Boyter, with Tanya Lapointe, Brian Herbert, Byron Merritt, Kim Herbert, Thomas Tull, Jon Spaihts, Richard P. Rubinstein, John Harrison, and Herbert W. Gain serving as executive producers and Kevin J. Anderson as creative consultant. Legendary CEO Joshua Grode confirmed in April 2019 that they plan to make a sequel, adding that "there's a logical place to stop the [first] movie before the book is over".In December 2020,
== that."On October 26, 2021, Legendary officially greenlit Dune: Part Two, with a spokesperson for the company stating, "We would not have gotten to this point without the extraordinary vision of Denis and the amazing work of his talented crew, the writers, our stellar cast, our partners at Warner Bros., and of course the fans! Here's to more Dune." Production work had occurred back-to-back with the first film, as Villeneuve and his wife Lapointe immediately took a flight to Budapest in order to begin
== series. Villeneuve ultimately secured a two-film deal with Warner Bros. Pictures, in the same style as the two-part adaption of Stephen King's It in 2017 and 2019. In January 2019, Joe Walker was confirmed to be serving as the film's editor. Other crew included Brad Riker as supervising art director, Patrice Vermette as production designer, Paul Lambert as visual effects supervisor, Gerd Nefzer as special effects supervisor, and Thomas Struthers as stunt coordinator. Dune: Part Two was produced by
== Dune: Part Two is a 2024 American epic science fiction film directed and produced by Denis Villeneuve, who co-wrote the screenplay with Jon Spaihts. The sequel to Dune (2021) adapts the 1965 novel Dune by Frank Herbert and follows Paul Atreides as he unites with the Fremen people of the desert planet Arrakis to wage war against House Harkonnen. Timothée Chalamet, Rebecca Ferguson, Josh Brolin, Stellan Skarsgård, Dave Bautista, Zendaya, Charlotte Rampling, and Javier Bardem reprise their roles from the first
== Eric Roth was hired to co-write the screenplay in April 2017 for the Dune films, and Jon Spaihts was later confirmed to be co-writing the script alongside Roth and Villeneuve. Game of Thrones language creator David Peterson was confirmed to be developing languages for the film in April 2019. Villeneuve and Peterson had created the Chakobsa language, which was used by actors on set. In November 2019, Spaihts stepped down as showrunner for Dune: Prophecy to focus on Dune: Part Two. In June 2020, Greig Fraser
== on Dune: Part Two. In June 2020, Greig Fraser said, "It's a fully formed story in itself with places to go. It's a fully standalone epic film that people will get a lot out of when they see it". Between the release of Dune and the confirmation of Dune: Part Two, Villeneuve started working the script in a way that production could begin immediately once the film was greenlit. By February 2021, Roth created a full treatment for the sequel, with writing beginning that August. He confirmed that Feyd-Rautha
== that August. He confirmed that Feyd-Rautha would appear in the film, and stated he will be a "very important character". In March 2022, Villeneuve had mostly finished writing the screenplay. Craig Mazin and Roth wrote additional literary material for the film.Villeneuve stated that the film would continue directly from the first, and specifically described it as being the "second part." He described the film as being an "epic war movie", adding that while the first film was more "contemplative", the second
== On the review aggregator website Rotten Tomatoes, 93% of 378 critics' reviews are positive, with an average rating of 8.4/10. The website's consensus reads: "Visually thrilling and narratively epic, Dune: Part Two continues Denis Villeneuve's adaptation of the beloved sci-fi series in spectacular form." Metacritic, which uses a weighted average, assigned the film a score of 79 out of 100, based on 62 critics, indicating "generally favorable" reviews. Audiences surveyed by CinemaScore gave the film an
== theatrical experience is at the very heart of the cinematic language for me." With Dune: Part Two being greenlit, Villeneuve said that his primary concern was to complete the filming as soon as possible, with the earliest he expected to start in the last quarter of 2022. However, he noted that production would be facilitated by the work already established on the first film, which would help expedite production.
== By November 2016, Legendary Pictures had obtained the film and TV rights for the Dune franchise, based on the eponymous 1965 novel by Frank Herbert. Vice chair of worldwide production for Legendary Mary Parent began discussing with Denis Villeneuve about directing a film adaptation, quickly hiring him after realizing his passion for Dune. By February 2018, Villeneuve was confirmed to be hired as director, and intended to adapt the novel as a two-part film series. Villeneuve ultimately secured a two-film
```

## Step 2 - Rerank the chunks retrieved from the vector database

We rerank the 10 chunks retrieved from the vector database. Reranking boosts retrieval accuracy.

Reranking lets us go from 10 chunks retrieved from the vector database, to the 3 most relevant chunks.

```python PYTHON
response = co.rerank(
    query=query,
    documents=top_chunks_after_retrieval,
    top_n=3,
    model="rerank-english-v2.0",
)

top_chunks_after_rerank = [result.document['text'] for result in response]
print("Here are the top 3 chunks after rerank: ")
for t in top_chunks_after_rerank:
    print("== " + t)
```

```txt title="Output"
Here are the top 3 chunks after rerank:
== Dune: Part Two is a 2024 American epic science fiction film directed and produced by Denis Villeneuve, who co-wrote the screenplay with Jon Spaihts. The sequel to Dune (2021) adapts the 1965 novel Dune by Frank Herbert and follows Paul Atreides as he unites with the Fremen people of the desert planet Arrakis to wage war against House Harkonnen. Timothée Chalamet, Rebecca Ferguson, Josh Brolin, Stellan Skarsgård, Dave Bautista, Zendaya, Charlotte Rampling, and Javier Bardem reprise their roles from the first
== stunt coordinator. Dune: Part Two was produced by Villeneuve, Mary Parent, and Cale Boyter, with Tanya Lapointe, Brian Herbert, Byron Merritt, Kim Herbert, Thomas Tull, Jon Spaihts, Richard P. Rubinstein, John Harrison, and Herbert W. Gain serving as executive producers and Kevin J. Anderson as creative consultant. Legendary CEO Joshua Grode confirmed in April 2019 that they plan to make a sequel, adding that "there's a logical place to stop the [first] movie before the book is over".In December 2020,
== series. Villeneuve ultimately secured a two-film deal with Warner Bros. Pictures, in the same style as the two-part adaption of Stephen King's It in 2017 and 2019. In January 2019, Joe Walker was confirmed to be serving as the film's editor. Other crew included Brad Riker as supervising art director, Patrice Vermette as production designer, Paul Lambert as visual effects supervisor, Gerd Nefzer as special effects supervisor, and Thomas Struthers as stunt coordinator. Dune: Part Two was produced by
```

## Step 3 - Generate the model final answer, given the retrieved and reranked chunks

```python PYTHON
preamble = """
## Task &amp; Context
You help people answer their questions and other requests interactively. You will be asked a very wide array of requests on all kinds of topics. You will be equipped with a wide range of search engines or similar tools to help you, which you use to research your answer. You should focus on serving the user's needs as best you can, which will be wide-ranging.

## Style Guide
Unless the user asks for a different style of answer, you should answer in full sentences, using proper grammar and spelling.
"""
```

```python PYTHON
documents = [
    {"title": "chunk 0", "snippet": top_chunks_after_rerank[0]},
    {"title": "chunk 1", "snippet": top_chunks_after_rerank[1]},
    {"title": "chunk 2", "snippet": top_chunks_after_rerank[2]},
  ]

response = co.chat(
  message=query,
  documents=documents,
  preamble=preamble,
  model="command-r",
  temperature=0.3
)

print("Final answer:")
print(response.text)
```

```txt title="Output"
Final answer:
Here are the key crew members involved in 'Dune: Part Two':

- Denis Villeneuve: director and producer
- Jon Spaihts: co-writer of the screenplay
- Mary Parent and Cale Boyter: producers
- Tanya Lapointe, Brian Herbert, Byron Merritt, Kim Herbert, Thomas Tull, Richard P. Rubinstein, John Harrison, Herbert W. Gain and Kevin J. Anderson: executive producers
- Joe Walker: editor
- Brad Riker: supervising art director
- Patrice Vermette: production designer
- Paul Lambert: visual effects supervisor
- Gerd Nefzer: special effects supervisor
- Thomas Struthers: stunt coordinator.

A number of crew members from the first film returned for the sequel, which is set to be released in 2024.
```

Note: this is indeed the answer you'd expect, and here was the passage of text in wikipedia explaining it!

" \[...] Dune: Part Two was originally scheduled to be released on October 20, 2023, but was delayed to November 17, 2023, before moving forward two weeks to November 3, 2023, to adjust to changes in release schedules from other studios. It was later postponed by over four months to March 15, 2024, due to the 2023 Hollywood labor disputes. After the strikes were resolved, the film moved once more up two weeks to March 1, 2024. \[...]"

## Bonus: Citations come for free with Cohere! 🎉

At Cohere, all RAG calls come with... precise citations! 🎉
The model cites which groups of words, in the RAG chunks, were used to generate the final answer.
These citations make it easy to check where the model’s generated response claims are coming from.
They help users gain visibility into the model reasoning, and sanity check the final model generation.
These citations are optional — you can decide to ignore them.

```python PYTHON
print("Citations that support the final answer:")
for cite in response.citations:
  print(cite)
```

```txt title="Output"
Citations that support the final answer:
{'start': 63, 'end': 79, 'text': 'Denis Villeneuve', 'document_ids': ['doc_0']}
{'start': 81, 'end': 102, 'text': 'director and producer', 'document_ids': ['doc_0']}
{'start': 105, 'end': 116, 'text': 'Jon Spaihts', 'document_ids': ['doc_0']}
{'start': 118, 'end': 145, 'text': 'co-writer of the screenplay', 'document_ids': ['doc_0']}
{'start': 148, 'end': 159, 'text': 'Mary Parent', 'document_ids': ['doc_1']}
{'start': 164, 'end': 175, 'text': 'Cale Boyter', 'document_ids': ['doc_1']}
{'start': 177, 'end': 186, 'text': 'producers', 'document_ids': ['doc_1']}
{'start': 190, 'end': 204, 'text': 'Tanya Lapointe', 'document_ids': ['doc_1']}
{'start': 206, 'end': 219, 'text': 'Brian Herbert', 'document_ids': ['doc_1']}
{'start': 221, 'end': 234, 'text': 'Byron Merritt', 'document_ids': ['doc_1']}
{'start': 236, 'end': 247, 'text': 'Kim Herbert', 'document_ids': ['doc_1']}
{'start': 249, 'end': 260, 'text': 'Thomas Tull', 'document_ids': ['doc_1']}
{'start': 262, 'end': 283, 'text': 'Richard P. Rubinstein', 'document_ids': ['doc_1']}
{'start': 285, 'end': 298, 'text': 'John Harrison', 'document_ids': ['doc_1']}
{'start': 300, 'end': 315, 'text': 'Herbert W. Gain', 'document_ids': ['doc_1']}
{'start': 320, 'end': 337, 'text': 'Kevin J. Anderson', 'document_ids': ['doc_1']}
{'start': 339, 'end': 358, 'text': 'executive producers', 'document_ids': ['doc_1']}
{'start': 362, 'end': 372, 'text': 'Joe Walker', 'document_ids': ['doc_2']}
{'start': 374, 'end': 380, 'text': 'editor', 'document_ids': ['doc_2']}
{'start': 383, 'end': 393, 'text': 'Brad Riker', 'document_ids': ['doc_2']}
{'start': 395, 'end': 419, 'text': 'supervising art director', 'document_ids': ['doc_2']}
{'start': 422, 'end': 438, 'text': 'Patrice Vermette', 'document_ids': ['doc_2']}
{'start': 440, 'end': 459, 'text': 'production designer', 'document_ids': ['doc_2']}
{'start': 462, 'end': 474, 'text': 'Paul Lambert', 'document_ids': ['doc_2']}
{'start': 476, 'end': 501, 'text': 'visual effects supervisor', 'document_ids': ['doc_2']}
{'start': 504, 'end': 515, 'text': 'Gerd Nefzer', 'document_ids': ['doc_2']}
{'start': 517, 'end': 543, 'text': 'special effects supervisor', 'document_ids': ['doc_2']}
{'start': 546, 'end': 562, 'text': 'Thomas Struthers', 'document_ids': ['doc_2']}
{'start': 564, 'end': 582, 'text': 'stunt coordinator.', 'document_ids': ['doc_2']}
{'start': 686, 'end': 691, 'text': '2024.', 'document_ids': ['doc_0']}
```

```python PYTHON
def insert_citations_in_order(text, citations):
    """
    A helper function to pretty print citations.
    """
    offset = 0
    document_id_to_number = {}
    citation_number = 0
    modified_citations = []

    # Process citations, assigning numbers based on unique document_ids
    for citation in citations:
        citation_numbers = []
        for document_id in sorted(citation["document_ids"]):
            if document_id not in document_id_to_number:
                citation_number += 1  # Increment for a new document_id
                document_id_to_number[document_id] = citation_number
            citation_numbers.append(document_id_to_number[document_id])

        # Adjust start/end with offset
        start, end = citation['start'] + offset, citation['end'] + offset
        placeholder = ''.join([f'[{number}]' for number in citation_numbers])
        # Bold the cited text and append the placeholder
        modification = f'**{text[start:end]}**{placeholder}'
        # Replace the cited text with its bolded version + placeholder
        text = text[:start] + modification + text[end:]
        # Update the offset for subsequent replacements
        offset += len(modification) - (end - start)

    # Prepare citations for listing at the bottom, ensuring unique document_ids are listed once
    unique_citations = {number: doc_id for doc_id, number in document_id_to_number.items()}
    citation_list = '\n'.join([f'[{doc_id}] source: "{documents[doc_id - 1]["snippet"]}"' for doc_id, number in sorted(unique_citations.items(), key=lambda item: item[1])])
    text_with_citations = f'{text}\n\n{citation_list}'

    return text_with_citations


print(insert_citations_in_order(response.text, response.citations))

```

```markdown title="Output"
Here are the key crew members involved in 'Dune: Part Two':

- **Denis Villeneuve**[1]: **director and producer**[1]
- **Jon Spaihts**[1]: **co-writer of the screenplay**[1]
- **Mary Parent**[2] and **Cale Boyter**[2]: **producers**[2]
- **Tanya Lapointe**[2], **Brian Herbert**[2], **Byron Merritt**[2], **Kim Herbert**[2], **Thomas Tull**[2], **Richard P. Rubinstein**[2], **John Harrison**[2], **Herbert W. Gain**[2] and **Kevin J. Anderson**[2]: **executive producers**[2]
- **Joe Walker**[3]: **editor**[3]
- **Brad Riker**[3]: **supervising art director**[3]
- **Patrice Vermette**[3]: **production designer**[3]
- **Paul Lambert**[3]: **visual effects supervisor**[3]
- **Gerd Nefzer**[3]: **special effects supervisor**[3]
- **Thomas Struthers**[3]: **stunt coordinator.**[3]

A number of crew members from the first film returned for the sequel, which is set to be released in **2024.**[1]

[1] source: "Dune: Part Two is a 2024 American epic science fiction film directed and produced by Denis Villeneuve, who co-wrote the screenplay with Jon Spaihts. The sequel to Dune (2021) adapts the 1965 novel Dune by Frank Herbert and follows Paul Atreides as he unites with the Fremen people of the desert planet Arrakis to wage war against House Harkonnen. Timothée Chalamet, Rebecca Ferguson, Josh Brolin, Stellan Skarsgård, Dave Bautista, Zendaya, Charlotte Rampling, and Javier Bardem reprise their roles from the first"
[2] source: "stunt coordinator. Dune: Part Two was produced by Villeneuve, Mary Parent, and Cale Boyter, with Tanya Lapointe, Brian Herbert, Byron Merritt, Kim Herbert, Thomas Tull, Jon Spaihts, Richard P. Rubinstein, John Harrison, and Herbert W. Gain serving as executive producers and Kevin J. Anderson as creative consultant. Legendary CEO Joshua Grode confirmed in April 2019 that they plan to make a sequel, adding that "there's a logical place to stop the [first] movie before the book is over".In December 2020,"
[3] source: "series. Villeneuve ultimately secured a two-film deal with Warner Bros. Pictures, in the same style as the two-part adaption of Stephen King's It in 2017 and 2019. In January 2019, Joe Walker was confirmed to be serving as the film's editor. Other crew included Brad Riker as supervising art director, Patrice Vermette as production designer, Paul Lambert as visual effects supervisor, Gerd Nefzer as special effects supervisor, and Thomas Struthers as stunt coordinator. Dune: Part Two was produced by"
```


# Basic Semantic Search with Cohere Models

> This page describes how to do basic semantic search with Cohere's models.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Basic_Semantic_Search.ipynb" />

Language models give computers the ability to search by meaning and go beyond searching by matching keywords. This capability is called semantic search.

<img alt="Searching an archive using sentence embeddings" src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/basic-semantic-search-overview.png?3" />

In this notebook, we'll build a simple semantic search engine. The applications of semantic search go beyond building a web search engine. They can empower a private search engine for internal documents or records. It can also be used to power features like StackOverflow's "similar questions" feature.

1. Get the archive of questions
2. [Embed](https://docs.cohere.ai/embed-reference/) the archive
3. Search using an index and nearest neighbor search
4. Visualize the archive based on the embeddings

And if you're running an older version of the SDK, you might need to upgrade it like so:

```python PYTHON
#!pip install --upgrade cohere
```

Get your Cohere API key by [signing up here](https://dashboard.cohere.com/register). Paste it in the cell below.

## 1. Getting Set Up

```python PYTHON
#@title Import libraries (Run this cell to execute required code) {display-mode: "form"}

import cohere
import numpy as np
import re
import pandas as pd
from tqdm import tqdm
from datasets import load_dataset
import umap
import altair as alt
from sklearn.metrics.pairwise import cosine_similarity
from annoy import AnnoyIndex
import warnings
warnings.filterwarnings('ignore')
pd.set_option('display.max_colwidth', None)
```

You'll need your API key for this next cell. [Sign up to Cohere](https://dashboard.cohere.com/) and get one if you haven't yet.

```python PYTHON
model_name = "embed-v4.0"
api_key = ""
input_type_embed = "search_document"

co = cohere.Client(api_key)
```

## 2. Get The Archive of Questions

We'll use the [trec](https://www.tensorflow.org/datasets/catalog/trec) dataset which is made up of questions and their categories.

```python PYTHON
dataset = load_dataset("trec", split="train")

df = pd.DataFrame(dataset)[:1000]

df.head(10)
```

<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          label-coarse
        </th>

        <th>
          label-fine
        </th>

        <th>
          text
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          0
        </td>

        <td>
          0
        </td>

        <td>
          How did serfdom develop in and then leave Russia ?
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          1
        </td>

        <td>
          1
        </td>

        <td>
          What films featured the character Popeye Doyle ?
        </td>
      </tr>

      <tr>
        <th>
          2
        </th>

        <td>
          0
        </td>

        <td>
          0
        </td>

        <td>
          How can I find a list of celebrities ' real names ?
        </td>
      </tr>

      <tr>
        <th>
          3
        </th>

        <td>
          1
        </td>

        <td>
          2
        </td>

        <td>
          What fowl grabs the spotlight after the Chinese Year of the Monkey ?
        </td>
      </tr>

      <tr>
        <th>
          4
        </th>

        <td>
          2
        </td>

        <td>
          3
        </td>

        <td>
          What is the full form of .com ?
        </td>
      </tr>

      <tr>
        <th>
          5
        </th>

        <td>
          3
        </td>

        <td>
          4
        </td>

        <td>
          What contemptible scoundrel stole the cork from my lunch ?
        </td>
      </tr>

      <tr>
        <th>
          6
        </th>

        <td>
          3
        </td>

        <td>
          5
        </td>

        <td>
          What team did baseball 's St. Louis Browns become ?
        </td>
      </tr>

      <tr>
        <th>
          7
        </th>

        <td>
          3
        </td>

        <td>
          6
        </td>

        <td>
          What is the oldest profession ?
        </td>
      </tr>

      <tr>
        <th>
          8
        </th>

        <td>
          0
        </td>

        <td>
          7
        </td>

        <td>
          What are liver enzymes ?
        </td>
      </tr>

      <tr>
        <th>
          9
        </th>

        <td>
          3
        </td>

        <td>
          4
        </td>

        <td>
          Name the scar-faced bounty hunter of The Old West .
        </td>
      </tr>
    </tbody>
  </table>
</div>

## 2. Embed the archive

The next step is to embed the text of the questions.

<img alt="embedding archive texts" src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/semantic-search-embed-text-archive.png" />

To get a thousand embeddings of this length should take about fifteen seconds.

```python PYTHON
embeds = co.embed(texts=list(df['text']),
                  model=model_name,
                  input_type=input_type_embed).embeddings
```

```python PYTHON
embeds = np.array(embeds)
embeds.shape
```

```
(1000, 4096)
```

## 3. Search using an index and nearest neighbor search

<img alt="Building the search index from the embeddings" src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/semantic-search-index.png" />

Let's now use [Annoy](https://github.com/spotify/annoy) to build an index that stores the embeddings in a way that is optimized for fast search. This approach scales well to a large number of texts (other options include [Faiss](https://github.com/facebookresearch/faiss), [ScaNN](https://github.com/google-research/google-research/tree/master/scann), and [PyNNDescent](https://github.com/lmcinnes/pynndescent)).

After building the index, we can use it to retrieve the nearest neighbors either of existing questions (section 3.1), or of new questions that we embed (section 3.2).

```python PYTHON
search_index = AnnoyIndex(embeds.shape[1], 'angular')
for i in range(len(embeds)):
    search_index.add_item(i, embeds[i])

search_index.build(10) # 10 trees
search_index.save('test.ann')
```

```
True
```

### 3.1. Find the neighbors of an example from the dataset

If we're only interested in measuring the distance between the questions in the dataset (no outside queries), a simple way is to calculate the distance between every pair of embeddings we have.

```python PYTHON
example_id = 92

similar_item_ids = search_index.get_nns_by_item(example_id,10,
                                                include_distances=True)
results = pd.DataFrame(data={'texts': df.iloc[similar_item_ids[0]]['text'],
                             'distance': similar_item_ids[1]}).drop(example_id)

print(f"Question:'{df.iloc[example_id]['text']}'\nNearest neighbors:")
results
```

```
Question:'What are bear and bull markets ?'
Nearest neighbors:
```

<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          texts
        </th>

        <th>
          distance
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          614
        </th>

        <td>
          What animals do you find in the stock market ?
        </td>

        <td>
          0.904278
        </td>
      </tr>

      <tr>
        <th>
          137
        </th>

        <td>
          What are equity securities ?
        </td>

        <td>
          0.992819
        </td>
      </tr>

      <tr>
        <th>
          513
        </th>

        <td>
          What do economists do ?
        </td>

        <td>
          1.066583
        </td>
      </tr>

      <tr>
        <th>
          307
        </th>

        <td>
          What does NASDAQ stand for ?
        </td>

        <td>
          1.080738
        </td>
      </tr>

      <tr>
        <th>
          363
        </th>

        <td>
          What does it mean `` Rupee Depreciates '' ?
        </td>

        <td>
          1.086724
        </td>
      </tr>

      <tr>
        <th>
          932
        </th>

        <td>
          Why did the world enter a global depression in 1929 ?
        </td>

        <td>
          1.099370
        </td>
      </tr>

      <tr>
        <th>
          547
        </th>

        <td>
          Where can stocks be traded on-line ?
        </td>

        <td>
          1.105368
        </td>
      </tr>

      <tr>
        <th>
          922
        </th>

        <td>
          What is the difference between a median and a mean ?
        </td>

        <td>
          1.141870
        </td>
      </tr>

      <tr>
        <th>
          601
        </th>

        <td>
          What is `` the bear of beers '' ?
        </td>

        <td>
          1.154140
        </td>
      </tr>
    </tbody>
  </table>
</div>

### 3.2. Find the neighbors of a user query

We're not limited to searching using existing items. If we get a query, we can embed it and find its nearest neighbors from the dataset.

```python PYTHON
query = "What is the tallest mountain in the world?"
input_type_query = "search_query"

query_embed = co.embed(texts=[query],
                  model=model_name,
                  input_type=input_type_query).embeddings

similar_item_ids = search_index.get_nns_by_vector(query_embed[0],10,
                                                include_distances=True)
query_results = pd.DataFrame(data={'texts': df.iloc[similar_item_ids[0]]['text'],
                             'distance': similar_item_ids[1]})


print(f"Query:'{query}'\nNearest neighbors:")
print(query_results) # NOTE: Your results might look slightly different to ours.
```

```
Query:'What is the tallest mountain in the world?'
Nearest neighbors:
```

<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          texts
        </th>

        <th>
          distance
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          236
        </th>

        <td>
          What is the name of the tallest mountain in the world ?
        </td>

        <td>
          0.447309
        </td>
      </tr>

      <tr>
        <th>
          670
        </th>

        <td>
          What is the highest mountain in the world ?
        </td>

        <td>
          0.552254
        </td>
      </tr>

      <tr>
        <th>
          412
        </th>

        <td>
          What was the highest mountain on earth before Mount Everest was
          discovered ?
        </td>

        <td>
          0.801252
        </td>
      </tr>

      <tr>
        <th>
          907
        </th>

        <td>
          What mountain range is traversed by the highest railroad in the world
          ?
        </td>

        <td>
          0.929516
        </td>
      </tr>

      <tr>
        <th>
          435
        </th>

        <td>
          What is the highest peak in Africa ?
        </td>

        <td>
          0.930806
        </td>
      </tr>

      <tr>
        <th>
          109
        </th>

        <td>
          Where is the highest point in Japan ?
        </td>

        <td>
          0.977315
        </td>
      </tr>

      <tr>
        <th>
          901
        </th>

        <td>
          What 's the longest river in the world ?
        </td>

        <td>
          1.064209
        </td>
      </tr>

      <tr>
        <th>
          114
        </th>

        <td>
          What is the largest snake in the world ?
        </td>

        <td>
          1.076390
        </td>
      </tr>

      <tr>
        <th>
          962
        </th>

        <td>
          What 's the second-largest island in the world ?
        </td>

        <td>
          1.088034
        </td>
      </tr>

      <tr>
        <th>
          27
        </th>

        <td>
          What is the highest waterfall in the United States ?
        </td>

        <td>
          1.091145
        </td>
      </tr>
    </tbody>
  </table>
</div>

## 4. Visualizing the archive

Finally, let's plot out all the questions onto a 2D chart so you're able to visualize the semantic similarities of this dataset!

```python PYTHON
#@title Plot the archive {display-mode: "form"}

reducer = umap.UMAP(n_neighbors=20)
umap_embeds = reducer.fit_transform(embeds)
df_explore = pd.DataFrame(data={'text': df['text']})
df_explore['x'] = umap_embeds[:,0]
df_explore['y'] = umap_embeds[:,1]

chart = alt.Chart(df_explore).mark_circle(size=60).encode(
    x=#'x',
    alt.X('x',
        scale=alt.Scale(zero=False)
    ),
    y=
    alt.Y('y',
        scale=alt.Scale(zero=False)
    ),
    tooltip=['text']
).properties(
    width=700,
    height=400
)
chart.interactive()
```

Hover over the points to read the text. Do you see some of the patterns in clustered points? Similar questions, or questions asking about similar topics?

This concludes this introductory guide to semantic search using sentence embeddings. As you continue the path of building a search product additional considerations arise (like dealing with long texts, or finetuning to better improve the embeddings for a specific use case).

We can’t wait to see what you start building! Share your projects or find support on [Discord](https://discord.com/invite/co-mmunity).


# Getting Started with Basic Tool Use

> This page describes how to work with Cohere's basic tool use functionality.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/agents/Vanilla_Tool_Use.ipynb" />

Tool use allows customers to **connect their large language models to external tools, such as search engines, APIs, functions, and databases**.

This allows the customer to unlock a richer set of model behaviors by, for instance, leveraging data stored in tools, taking actions through APIs, interacting with a vector database, or querying a search engine.

Below, we illustrate tool use in four steps:

* Step 1: the user configures the request to the model
* Step 2: the model uses context to **determine which tool(s) to use and how**
* Step 3: the tool calls are executed
* Step 4: the model **generates a final answer with precise citations** based on the tool results

```python PYTHON
import cohere, json
API_KEY = "..." # fill in your Cohere API key here
co = cohere.Client(API_KEY)
```

## Step 0: Create a mock database

Before we can illustrate tool use, we first need to do some setup. Here, we'll define the mock data that our tools will query. This data represents sales reports and a product catalog.

```python PYTHON
sales_database = {
    '2023-09-28': {
        'total_sales_amount': 5000,
        'total_units_sold': 100,
    },
    '2023-09-29': {
        'total_sales_amount': 10000,
        'total_units_sold': 250,
    },
    '2023-09-30': {
        'total_sales_amount': 8000,
        'total_units_sold': 200,
    }
}

product_catalog = {
    'Electronics': [
        {'product_id': 'E1001', 'name': 'Smartphone', 'price': 500, 'stock_level': 20},
        {'product_id': 'E1002', 'name': 'Laptop', 'price': 1000, 'stock_level': 15},
        {'product_id': 'E1003', 'name': 'Tablet', 'price': 300, 'stock_level': 25},
    ],
    'Clothing': [
        {'product_id': 'C1001', 'name': 'T-Shirt', 'price': 20, 'stock_level': 100},
        {'product_id': 'C1002', 'name': 'Jeans', 'price': 50, 'stock_level': 80},
        {'product_id': 'C1003', 'name': 'Jacket', 'price': 100, 'stock_level': 40},
    ]
}
```

Now, we'll define the tools that simulate querying this database.\
For example, you could use the API of an enterprise sales platform.

```python PYTHON
def query_daily_sales_report(day: str) -> dict:
    """
    Function to retrieve the sales report for the given day
    """
    report = sales_database.get(day, {})
    if report:
        return {
            'date': day,
            'summary': f"Total Sales Amount: {report['total_sales_amount']}, Total Units Sold: {report['total_units_sold']}"
        }
    else:
        return {'date': day, 'summary': 'No sales data available for this day.'}


def query_product_catalog(category: str) -> dict:
    """
    Function to retrieve products for the given category
    """
    products = product_catalog.get(category, [])
    return {
        'category': category,
        'products': products
    }


functions_map = {
    "query_daily_sales_report": query_daily_sales_report,
    "query_product_catalog": query_product_catalog
}
```

## Step 1 - User configures the request to the model

The developer provides a few things to the model:

* A system instruction (preamble) containing instructions about the task and the desired style for the output.
* The user request.
* A list of tools to the model.
* (Optionally) a chat history for the model to work with.

You can specify one or many tools to the model. Every tool needs to be described with a JSON schema, indicating the tool name, description, and parameters (code snippets below).

In our example, we provide two tools to the model: `daily_sales_report` and `product_catalog`.

```python PYTHON
tools = [
    {
        "name": "query_daily_sales_report",
        "description": "Connects to a database to retrieve overall sales volumes and sales information for a given day.",
        "parameter_definitions": {
            "day": {
                "description": "Retrieves sales data for this day, formatted as YYYY-MM-DD.",
                "type": "str",
                "required": True
            }
        }
    },
    {
        "name": "query_product_catalog",
        "description": "Connects to a a product catalog with information about all the products being sold, including categories, prices, and stock levels.",
        "parameter_definitions": {
            "category": {
                "description": "Retrieves product information data for all products in this category.",
                "type": "str",
                "required": True
            }
        }
    }
]
```

Now let's define the user request.

In our example we'll use: "Can you provide a sales summary for 29th September 2023, and also give me the details of all products in the 'Electronics' category that were sold that day, including their prices and stock levels?"

Only a language model with Tool Use can answer this request: it requires looking up information in the right external tools (step 2), and then providing a final answer based on the tool results (step 4).

```python PYTHON
preamble = """
## Task &amp; Context
You help people answer their questions and other requests interactively. You will be asked a very wide array of requests on all kinds of topics. You will be equipped with a wide range of search engines or similar tools to help you, which you use to research your answer. You should focus on serving the user's needs as best you can, which will be wide-ranging.

## Style Guide
Unless the user asks for a different style of answer, you should answer in full sentences, using proper grammar and spelling.
"""

message = "Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?"
```

## Step 2 – The model smartly decides which tool(s) to use and how

The model intelligently selects the right tool(s) to call -- and the right parameters for each tool call -- based on the content of the user message.

```python PYTHON
response = co.chat(
    message=message,
    tools=tools,
    preamble=preamble,
    model="command-r"
)


print("The model recommends doing the following tool calls:")
print("\n".join(str(tool_call) for tool_call in response.tool_calls))
```

```
The model recommends doing the following tool calls:
cohere.ToolCall {
	name: query_daily_sales_report
	parameters: {'day': '2023-09-29'}
	generation_id: eaf955e3-623d-4796-bf51-23b07c66ed2c
}
cohere.ToolCall {
	name: query_product_catalog
	parameters: {'category': 'Electronics'}
	generation_id: eaf955e3-623d-4796-bf51-23b07c66ed2c
}
```

## Step 3 – The tool calls are executed

You can now execute the appropriate calls, using the tool calls and tool parameters generated by the model.\
These tool calls return tool results that will be fed to the model in Step 4.

```python PYTHON
tool_results = []
for tool_call in response.tool_calls:
    # here is where you would call the tool recommended by the model, using the parameters recommended by the model
    print(f"= running tool {tool_call.name}, with parameters: {tool_call.parameters}")
    output = functions_map[tool_call.name](**tool_call.parameters)
    # store the output in a list
    outputs = [output]
    print(f"== tool results: {outputs}")
    # store your tool results in this format
    tool_results.append({
        "call": tool_call,
        "outputs": outputs
    })

print("Tool results that will be fed back to the model in step 4:")
print(json.dumps(tool_results, indent=4))
```

```
= running tool query_daily_sales_report, with parameters: {'day': '2023-09-29'}
== tool results: [{'date': '2023-09-29', 'summary': 'Total Sales Amount: 10000, Total Units Sold: 250'}]
= running tool query_product_catalog, with parameters: {'category': 'Electronics'}
== tool results: [{'category': 'Electronics', 'products': [{'product_id': 'E1001', 'name': 'Smartphone', 'price': 500, 'stock_level': 20}, {'product_id': 'E1002', 'name': 'Laptop', 'price': 1000, 'stock_level': 15}, {'product_id': 'E1003', 'name': 'Tablet', 'price': 300, 'stock_level': 25}]}]
Tool results that will be fed back to the model in step 4:
[
    {
        "call": {
            "name": "query_daily_sales_report",
            "parameters": {
                "day": "2023-09-29"
            },
            "generation_id": "eaf955e3-623d-4796-bf51-23b07c66ed2c"
        },
        "outputs": [
            {
                "date": "2023-09-29",
                "summary": "Total Sales Amount: 10000, Total Units Sold: 250"
            }
        ]
    },
    {
        "call": {
            "name": "query_product_catalog",
            "parameters": {
                "category": "Electronics"
            },
            "generation_id": "eaf955e3-623d-4796-bf51-23b07c66ed2c"
        },
        "outputs": [
            {
                "category": "Electronics",
                "products": [
                    {
                        "product_id": "E1001",
                        "name": "Smartphone",
                        "price": 500,
                        "stock_level": 20
                    },
                    {
                        "product_id": "E1002",
                        "name": "Laptop",
                        "price": 1000,
                        "stock_level": 15
                    },
                    {
                        "product_id": "E1003",
                        "name": "Tablet",
                        "price": 300,
                        "stock_level": 25
                    }
                ]
            }
        ]
    }
]
```

## Step 4 - The model generates a final answer based on the tool results

Finally, the developer calls the Cohere model, providing the tools results, in order to generate the model's final answer.

```python PYTHON
response = co.chat(
    message=message,
    tools=tools,
    tool_results=tool_results,
    preamble=preamble,
    model="command-r",
    temperature=0.3
)
```

```python PYTHON
print("Final answer:")
print(response.text)
```

```
Final answer:
On the 29th of September 2023, there were 10,000 sales with 250 units sold.

The Electronics category contains three products. There are details below:

| Product Name | Price | Stock Level |
| ------------ | ----- | ----------- |
| Smartphone | 500 | 20 |
| Laptop | 1000 | 15 |
| Tablet | 300 | 25 |

The total stock level for Electronics items is 50.
```

## Bonus: Citations come for free with Cohere! 🎉

At Cohere, model generations come with... precise citations! 🎉\
The model cites which groups of words, in the tool results, were used to generate the final answer.\
These citations make it easy to check where the model’s generated response claims are coming from.\
They help users gain visibility into the model reasoning, and sanity check the final model generation.\
These citations are optional — you can decide to ignore them.

```python PYTHON
print("Citations that support the final answer:")
for cite in response.citations:
  print(cite)
```

```
Citations that support the final answer:
{'start': 7, 'end': 29, 'text': '29th of September 2023', 'document_ids': ['query_daily_sales_report:0:0']}
{'start': 42, 'end': 75, 'text': '10,000 sales with 250 units sold.', 'document_ids': ['query_daily_sales_report:0:0']}
{'start': 112, 'end': 127, 'text': 'three products.', 'document_ids': ['query_product_catalog:1:0']}
{'start': 234, 'end': 244, 'text': 'Smartphone', 'document_ids': ['query_product_catalog:1:0']}
{'start': 247, 'end': 250, 'text': '500', 'document_ids': ['query_product_catalog:1:0']}
{'start': 253, 'end': 255, 'text': '20', 'document_ids': ['query_product_catalog:1:0']}
{'start': 260, 'end': 266, 'text': 'Laptop', 'document_ids': ['query_product_catalog:1:0']}
{'start': 269, 'end': 273, 'text': '1000', 'document_ids': ['query_product_catalog:1:0']}
{'start': 276, 'end': 278, 'text': '15', 'document_ids': ['query_product_catalog:1:0']}
{'start': 283, 'end': 289, 'text': 'Tablet', 'document_ids': ['query_product_catalog:1:0']}
{'start': 292, 'end': 295, 'text': '300', 'document_ids': ['query_product_catalog:1:0']}
{'start': 298, 'end': 300, 'text': '25', 'document_ids': ['query_product_catalog:1:0']}
```

```python PYTHON
def insert_citations_in_order(text, citations):
    """
    A helper function to pretty print citations.
    """
    offset = 0
    document_id_to_number = {}
    citation_number = 0
    modified_citations = []

    # Process citations, assigning numbers based on unique document_ids
    for citation in citations:
        citation_numbers = []
        for document_id in sorted(citation["document_ids"]):
            if document_id not in document_id_to_number:
                citation_number += 1  # Increment for a new document_id
                document_id_to_number[document_id] = citation_number
            citation_numbers.append(document_id_to_number[document_id])

        # Adjust start/end with offset
        start, end = citation['start'] + offset, citation['end'] + offset
        placeholder = ''.join([f'[{number}]' for number in citation_numbers])
        # Bold the cited text and append the placeholder
        modification = f'**{text[start:end]}**{placeholder}'
        # Replace the cited text with its bolded version + placeholder
        text = text[:start] + modification + text[end:]
        # Update the offset for subsequent replacements
        offset += len(modification) - (end - start)

    # Prepare citations for listing at the bottom, ensuring unique document_ids are listed once
    unique_citations = {number: doc_id for doc_id, number in document_id_to_number.items()}
    citation_list = '\n'.join([f'[{doc_id}] source: {tool_results[doc_id - 1]["outputs"]} \n    based on tool call: {dict(tool_results[doc_id - 1]["call"])}' for doc_id, number in sorted(unique_citations.items(), key=lambda item: item[1])])
    text_with_citations = f'{text}\n\n{citation_list}'

    return text_with_citations


print(insert_citations_in_order(response.text, response.citations))

```

```
On the **29th of September 2023**[1], there were **10,000 sales with 250 units sold.**[1]

The Electronics category contains **three products.**[2] There are details below:

| Product Name | Price | Stock Level |
| ------------ | ----- | ----------- |
| **Smartphone**[2] | **500**[2] | **20**[2] |
| **Laptop**[2] | **1000**[2] | **15**[2] |
| **Tablet**[2] | **300**[2] | **25**[2] |

The total stock level for Electronics items is 50.

[1] source: [{'date': '2023-09-29', 'summary': 'Total Sales Amount: 10000, Total Units Sold: 250'}]
    based on tool call: {'name': 'query_daily_sales_report', 'parameters': {'day': '2023-09-29'}, 'generation_id': 'eaf955e3-623d-4796-bf51-23b07c66ed2c'}
[2] source: [{'category': 'Electronics', 'products': [{'product_id': 'E1001', 'name': 'Smartphone', 'price': 500, 'stock_level': 20}, {'product_id': 'E1002', 'name': 'Laptop', 'price': 1000, 'stock_level': 15}, {'product_id': 'E1003', 'name': 'Tablet', 'price': 300, 'stock_level': 25}]}]
    based on tool call: {'name': 'query_product_catalog', 'parameters': {'category': 'Electronics'}, 'generation_id': 'eaf955e3-623d-4796-bf51-23b07c66ed2c'}
```

Now, you've used Cohere for Tool Use. Tool use opens up a wide range of new use cases. Here are a few examples:

* **Function calling**: It's now possible to ask the model to output a JSON object with specific function parameters.\
  For instance, this allows your chatbot to interact with your CRM to change the status of a deal, or to engage with a Python interpreter to conduct data science analyses.

* **Query transformation**: You can transform a user message into a search query for a vector database or any search engine.\
  For instance, this enables your work assistant to automatically retrieve the appropriate data from your company's documentation by creating the right query for your vector database.

* **Advanced searches**: You can transform a user message into one-or-many queries, to do multiple subtasks based on the content of the message.\
  For instance, this allows your chatbot to search across different databases and platforms to retrieve relevant information or to conduct comparative analysis.


# Calendar Agent with Native Multi Step Tool

> This page describes how to use cohere Chat API with list_calendar_events and create_calendar_event tools to book appointments.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/agents/Tool_Use.ipynb" />

In the example below, we demonstrate how to use the cohere Chat API with the `list_calendar_events` and `create_calendar_event` tools to book appointments. Booking the correct appointment requires the model to first check for an available slot by listing existing events, reasoning about the correct slot to book the new appointment and then finally invoking the right tool to create the calendar event. To learn more about Tool Use, read the official [multi-step tool use guide](https://docs.cohere.com/docs/multi-step-tool-use).

```python PYTHON
# !pip install cohere==5.5.3
```

```python PYTHON
# Instantiate the Cohere client

import cohere
import os

COHERE_API_KEY = os.environ["COHERE_API_KEY"]
co = cohere.Client(api_key=COHERE_API_KEY)
```

```python PYTHON
# Define the tools

import json

def list_calendar_events(date: str):
  events = '[{"start": "14:00", "end": "15:00"}, {"start": "15:00", "end": "16:00"}, {"start": "17:00", "end": "18:00"}]'
  print(f"Listing events: {events}")
  return events

def create_calendar_event(date: str, time: str, duration: int):
  print(f"Creating a {duration} hour long event at {time} on {date}")
  return True

list_calendar_events_tool = {
  "name": "list_calendar_events",
  "description": "returns a list of calendar events for the specified date, including the start time and end time for each event",
  "parameter_definitions": {
    "date": {
      "description": "the date to list events for, formatted as mm/dd/yy",
      "type": "str",
      "required": True
    }
  }
}

create_calendar_event_tool = {
  "name": "create_calendar_event_tool",
  "description": "creates a calendar event of the specified duration at the specified time and date",
  "parameter_definitions": {
    "date": {
      "description": "the date on which the event starts, formatted as mm/dd/yy",
      "type": "str",
      "required": True
    },
    "time": {
      "description": "the time of the event, formatted using 24h military time formatting",
      "type": "str",
      "required": True
    },
    "duration": {
      "description": "the number of hours the event lasts for",
      "type": "float",
      "required": True
    }
  }
}

# helper function for routing to the correct tool
def invoke_tool(tool_call: cohere.ToolCall):
  if tool_call.name == list_calendar_events_tool["name"]:
    date = tool_call.parameters["date"]
    return [{
        "events": list_calendar_events(date)
    }]
  elif tool_call.name == create_calendar_event_tool["name"]:
    date = tool_call.parameters["date"]
    time = tool_call.parameters["time"]
    duration = tool_call.parameters["duration"]

    return [{
        "is_success": create_calendar_event(date, time, duration)
    }]
  else:
    raise f"Unknown tool name '{tool_call.name}'"
```

```python PYTHON
# Check what tools the model wants to use and how to use them
res = co.chat(
    model="command-a-03-2025",
    preamble="Today is Thursday, may 23, 2024",
    message="book an hour long appointment for the first available free slot after 3pm",
    force_single_step=False,
    tools=[list_calendar_events_tool, create_calendar_event_tool])

while res.tool_calls:
  print(res.text) # This will be an observation and a plan with next steps

  # invoke the recommended tools
  tool_results = []
  for call in res.tool_calls:
    tool_results.append({"call": call, "outputs": invoke_tool(call)})

  # send back the tool results
  res = co.chat(
    model="command-a-03-2025",
    chat_history=res.chat_history,
    message="",
    force_single_step=False,
    tools=[list_calendar_events_tool, create_calendar_event_tool],
    tool_results=tool_results,
  )

print(res.text) # print the final answer
```

```txt title="Output"
I will check the user's calendar for today after 3pm and book an hour-long appointment in the first available slot.
Listing events: [{"start": "14:00", "end": "15:00"}, {"start": "15:00", "end": "16:00"}, {"start": "17:00", "end": "18:00"}]
The user has events scheduled from 2pm to 4pm and from 5pm to 6pm. I will book an hour-long appointment from 4pm to 5pm.
Creating a 1 hour long event at 16:00 on 05/23/2024
I've booked an hour-long appointment for you today from 4pm to 5pm.
```


# Effective Chunking Strategies for RAG

> This page describes various chunking strategies you can use to get better RAG performance.

<AuthorsContainer
  authors={[
    {
      name: "Ania Bialas",
      imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/c5dc5a3-Ania.jpg",
    },
  ]}
/>

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Chunking_strategies.ipynb" />

```python PYTHON
%%capture
!pip install cohere
!pip install -qU langchain-text-splitters
!pip install llama-index-embeddings-cohere
!pip install llama-index-postprocessor-cohere-rerank
```

```python PYTHON
import requests
from typing import List

from bs4 import BeautifulSoup

import cohere
from getpass import getpass
from IPython.display import HTML, display

from langchain_text_splitters import CharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

from llama_index.core import Document
from llama_index.embeddings.cohere import CohereEmbedding
from llama_index.postprocessor.cohere_rerank import CohereRerank
from llama_index.core import VectorStoreIndex, ServiceContext
```

```python PYTHON
co_model = 'command-r'
co_api_key = getpass("Enter Cohere API key: ")
co = cohere.Client(api_key=co_api_key)
```

```txt title="Output"
Enter Cohere API key: ··········
```

## Introduction

Chunking is an essential component of any RAG-based system. This cookbook aims to demonstrate how different chunking strategies affect the results of LLM-generated output. There are multiple considerations that need to be taken into account when designing chunking strategy. Therefore, we begin by providing a framework for these strategies and then jump into a practical example. We will focus our example on transcript calls, which create a unique challenge because of their rich content and the change of people speaking throughout the text.

## Chunking strategies framework \[#chunking-strategies-framework]

### Document splitting

By document splitting, we mean deciding on the conditions under which we will break the text. At this stage, we should ask, *"Are there any parts of consecutive text we want to ensure we do not break?"*. If the answer is "no", then, the content-independent splitting strategies are helpful. On the other hand, in scenarios like transcripts or meeting notes, we probably would like to keep the content of one speaker together, which might require us to deploy content-dependent strategies.

#### Content-independent splitting strategies

We split the document based on some content-independent conditions, among the most popular ones are:

* splitting by the number of characters,
* splitting by sentence,
* splitting by a given character, for example, `\n` for paragraphs.

The advantage of this scenario is that we do not need to make any assumptions about the text. However, some considerations remain, like whether we want to preserve some semantic structure, for example, sentences or paragraphs. Sentence splitting is better suited if we are looking for small chunks to ensure accuracy. Conversely, paragraphs preserve more context and might be more useful in open-ended questions.

#### Content-dependent splitting strategies

On the other hand, there are scenarios in which we care about preserving some text structure. Then, we develop custom splitting strategies based on the document's content. A prime example is call transcripts. In such scenarios, we aim to ensure that one person's speech is fully contained within a chunk.

### Creating chunks from the document splits

After the document is split, we need to decide on the desired **size** of our chunks (the split only defines how we break the document, but we can create bigger chunks from multiple splits).

Smaller chunks support more accurate retrieval. However, they might lack context. On the other hand, larger chunks offer more context, but they reduce the effectiveness of the retrieval. It is important to experiment with different settings to find the optimal balance.

### Overlapping chunks

Overlapping chunks is a useful technique to have in the toolbox. Especially when we employ content-independent splitting strategies, it helps us mitigate some of the pitfalls of breaking the document without fully understanding the text. Overlapping guarantees that there is always some buffer between the chunks, and even if an important piece of information might be split in the original splitting strategy, it is more probable that the full information will be captured in the next chunk. The disadvantage of this method is that it creates redundancy.

## Getting started \[#getting-started]

Designing a robust chunking strategy is as much a science as an art. There are no straightforward answers; the most effective strategies often emerge through experimentation. Therefore, let's dive straight into an example to illustrate this concept.

## Utils

```python PYTHON
def set_css():
  display(HTML('''

  '''))
get_ipython().events.register('pre_run_cell', set_css)

set_css()
```

```python PYTHON
def insert_citations(text: str, citations: List[dict]):
    """
    A helper function to pretty print citations.
    """
    offset = 0
    # Process citations in the order they were provided
    for citation in citations:
        # Adjust start/end with offset
        start, end = citation['start'] + offset, citation['end'] + offset
        placeholder = "[" + ", ".join(doc[4:] for doc in citation["document_ids"]) + "]"
        # ^ doc[4:] removes the 'doc_' prefix, and leaves the quoted document
        modification = f'{text[start:end]} {placeholder}'
        # Replace the cited text with its bolded version + placeholder
        text = text[:start] + modification + text[end:]
        # Update the offset for subsequent replacements
        offset += len(modification) - (end - start)

    return text

def build_retriever(documents, top_n=5):
  # Create the embedding model
  embed_model = CohereEmbedding(
      cohere_api_key=co_api_key,
      model_name="embed-v4.0",
      input_type="search_query",
  )

  # Load the data, for this example data needs to be in a test file
  index = VectorStoreIndex.from_documents(
      documents,
      embed_model=embed_model
  )

  # Create a cohere reranker
  cohere_rerank = CohereRerank(api_key=co_api_key)

  # Create the retriever
  retriever = index.as_retriever(node_postprocessors=[cohere_rerank], similarity_top_k=top_n)
  return retriever
```

## Load the data

In this example we will work with an 2023 Tesla earning call transcript.

```python PYTHON
# Get all investement memos (19) in bvp repository
url_path = 'https://www.fool.com/earnings/call-transcripts/2024/01/24/tesla-tsla-q4-2023-earnings-call-transcript/'
response = requests.get(url_path)
soup = BeautifulSoup(response.content, 'html.parser')

target_divs = soup.find("div", {"class": "article-body"}).find_all("p")[2:]
print('Length of the script: ', len(target_divs))

print()
print('Example of processed text:')
text = '\n\n'.join([div.get_text() for div in target_divs])
print(text[:500])
```

```txt title="Output"
Length of the script:  385

Example of processed text:
Martin Viecha

Good afternoon, everyone, and welcome to Tesla's fourth-quarter 2023 Q&amp;A webcast. My name is Martin Viecha, VP of investor relations, and I'm joined today by Elon Musk, Vaibhav Taneja, and a number of other executives. Our Q4 results were announced at about 3 p.m. Central Time in the update that we published at the same link as this webcast.

During this call, we will discuss our business outlook and make forward-looking statements. These comments are based on our predictions and
```

## Example 1: Chunking using content-independent strategies \[#example-1]

Let's begin with a simple content-independent strategy. We aim to answer the question, `Who mentions Jonathan Nolan?`. We chose this question as it is easily verifiable and it requires to identify the speaker. The answer to this question can be found in the downloaded transcript, here is the relevant passage:

```
Elon Musk -- Chief Executive Officer and Product Architect

Yeah. The creators of Westworld, Jonathan Nolan, Lisa Joy Nolan, are friends -- are all friends of mine, actually. And I invited them to come see the lab and, like, well, come see it, hopefully soon. It's pretty well -- especially the sort of subsystem test stands where you've just got like one leg on a test stand just doing repetitive exercises and one arm on a test stand pretty well.
```

```python PYTHON
# Define the question
question = "Who mentions Jonathan Nolan?"
```

In this case, we are more concerned about accuracy than a verbose answer, so we **focus on keeping the chunks small**. To ensure that the desired size is not exceeded, we will randomly split the list of characters, in our case `["\n\n", "\n", " ", ""]`.

We employ the `RecursiveCharacterTextSplitter` from [LangChain](https://python.langchain.com/docs/get_started/introduction) for this task.

```python PYTHON
# Define the chunking function
def get_chunks(text, chunk_size, chunk_overlap):
  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    length_function=len,
    is_separator_regex=False,
  )

  documents = text_splitter.create_documents([text])
  documents = [Document(text=doc.page_content) for doc in documents]

  return documents
```

### Experiment 1 - no overlap

In our first experiment we define the chunk size as 500 and allow **no overlap between consecutive chunks**.

Subsequently, we implement the standard RAG pipeline. We feed the chunks into a retriever, selecting the `top_n` most pertinent to the query chunks, and supply them as context to the generation model. Throughout this pipeline, we leverage [Cohere's endpoints](https://docs.cohere.com/reference/about), specifically, `co.embed`, `co.re.rank`, and finally, `co.chat`.

```python PYTHON
chunk_size = 500
chunk_overlap = 0
documents = get_chunks(text, chunk_size, chunk_overlap)
retriever = build_retriever(documents)

source_nodes = retriever.retrieve(question)
print('Number of docuemnts: ',len(source_nodes))
source_nodes= [{"text": ni.get_content()}for ni in source_nodes]


response = co.chat(
  message=question,
  documents=source_nodes,
  model=co_model
)
response = response
print(response.text)
```

```txt title="Output"
Number of docuemnts:  5
An unknown speaker mentions Jonathan Nolan in a conversation about the creators of Westworld. They mention that Jonathan Nolan and Lisa Joy Nolan are friends of theirs, and that they have invited them to visit the lab.
```

A notable feature of [`co.chat`](https://docs.cohere.com/reference/chat) is its ability to ground the model's answer within the context. This means we can identify which chunks were used to generate the answer. Below, we show the previous output of the model together with the citation reference, where `[num]` represents the index of the chunk.

```python PYTHON
print(insert_citations(response.text, response.citations))
```

```txt title="Output"
An unknown speaker [0] mentions Jonathan Nolan in a conversation about the creators of Westworld. [0] They mention that Jonathan Nolan and Lisa Joy Nolan [0] are friends [0] of theirs, and that they have invited them to visit the lab. [0]
```

Indeed, by printing the cited chunk, we can validate that the text was divided so that the generation model could not provide the correct response. Notably, the speaker's name is not included in the context, which is why the model refes to an `unknown speaker`.

```python PYTHON
print(source_nodes[0])
```

```python title="Output"
{'text': "Yeah. The creators of Westworld, Jonathan Nolan, Lisa Joy Nolan, are friends -- are all friends of mine, actually. And I invited them to come see the lab and, like, well, come see it, hopefully soon. It's pretty well -- especially the sort of subsystem test stands where you've just got like one leg on a test stand just doing repetitive exercises and one arm on a test stand pretty well.\n\nYeah.\n\nUnknown speaker\n\nWe're not entering Westworld anytime soon."}
```

### Experiment 2 - allow overlap

In the previous experiment, we discovered that the chunks were generated in a way that made it impossible to generate the correct answer. The name of the speaker was not included in the relevant chunk.

Therefore, this time to mitigate this issue, we **allow for overlap between consecutive chunks**.

```python PYTHON
chunk_size = 500
chunk_overlap = 100
documents = get_chunks(text,chunk_size, chunk_overlap)
retriever = build_retriever(documents)

source_nodes = retriever.retrieve(question)
print('Number of docuemnts: ',len(source_nodes))
source_nodes= [{"text": ni.get_content()}for ni in source_nodes]


response = co.chat(
  message=question,
  documents=source_nodes,
  model=co_model
)
response = response
print(response.text)
```

```txt title="Output"
Number of docuemnts:  5
Elon Musk mentions Jonathan Nolan. Musk is the CEO and Product Architect of the lab that resembles the set of Westworld, a show created by Jonathan Nolan and Lisa Joy Nolan.
```

Again, we can print the text along with the citations.

```python PYTHON
print(insert_citations(response.text, response.citations))
```

```txt title="Output"
Elon Musk [0] mentions Jonathan Nolan. Musk is the CEO and Product Architect [0] of the lab [0] that resembles the set of Westworld [0], a show created by Jonathan Nolan [0] and Lisa Joy Nolan. [0]
```

And investigate the chunks which were used as context to answer the query.

```python PYTHON
source_nodes[0]
```

```python title="Output"
{'text': "Yeah, not the best reference.\n\nElon Musk -- Chief Executive Officer and Product Architect\n\nYeah. The creators of Westworld, Jonathan Nolan, Lisa Joy Nolan, are friends -- are all friends of mine, actually. And I invited them to come see the lab and, like, well, come see it, hopefully soon. It's pretty well -- especially the sort of subsystem test stands where you've just got like one leg on a test stand just doing repetitive exercises and one arm on a test stand pretty well.\n\nYeah."}
```

As we can see, by allowing overlap we managed to get the correct answer to our question.

## Example 2: Chunking using content-dependent strategies \[#example-2]

In the previous experiment, we provided an example of how using or not using overlapping can affect a model's performance, particularly in documents such as call transcripts where subjects change frequently. Ensuring that each chunk contains all relevant information is crucial. While we managed to retrieve the correct information by introducing overlapping into the chunking strategy, this might still not be the optimal approach for transcripts with longer speaker speeches.

Therefore, in this experiment, we will adopt a content-dependent strategy.

Our proposed approach entails segmenting the text whenever a new speaker begins speaking, which requires preprocessing the text accordingly.

### Preprocess the text

Firstly, let's observe that in the HTML text, each time the speaker changes, their name is enclosed within `<p><strong>Name</strong></p>` tags, denoting the speaker's name in bold letters.

To facilitate our text chunking process, we'll use the above observation and introduce a unique character sequence `###`, which we'll utilize as a marker for splitting the text.

```python PYTHON
print('HTML text')
print(target_divs[:3])
print('-------------------\n')

text_custom = []
for div in target_divs:
  if div.get_text() is None:
    continue
  if str(div).startswith('<p><strong>'):
    text_custom.append(f'### {div.get_text()}')
  else:
    text_custom.append(div.get_text())

text_custom = '\n'.join(text_custom)
print(text_custom[:500])
```

```txt title="Output"
HTML text
[<p><strong>Martin Viecha</strong></p>, <p>Good afternoon, everyone, and welcome to Tesla's fourth-quarter 2023 Q&amp;A webcast. My name is Martin Viecha, VP of investor relations, and I'm joined today by Elon Musk, Vaibhav Taneja, and a number of other executives. Our Q4 results were announced at about 3 p.m. Central Time in the update that we published at the same link as this webcast.</p>, <p>During this call, we will discuss our business outlook and make forward-looking statements. These comments are based on our predictions and expectations as of today. Actual events or results could differ materially due to a number of risks and uncertainties, including those mentioned in our most recent filings with the SEC. [Operator instructions] But before we jump into Q&amp;A, Elon has some opening remarks.</p>]
-------------------

### Martin Viecha
Good afternoon, everyone, and welcome to Tesla's fourth-quarter 2023 Q&amp;A webcast. My name is Martin Viecha, VP of investor relations, and I'm joined today by Elon Musk, Vaibhav Taneja, and a number of other executives. Our Q4 results were announced at about 3 p.m. Central Time in the update that we published at the same link as this webcast.
During this call, we will discuss our business outlook and make forward-looking statements. These comments are based on our predictions an
```

In this approach, we prioritize splitting the text at the appropriate separator, `###.` To ensure this behavior, we'll use `CharacterTextSplitter` from [LangChain](https://python.langchain.com/docs/get_started/introduction), guaranteeing such behavior. From our analysis of the text and the fact that we aim to preserve entire speaker speeches intact, we anticipate that most of them will exceed a length of 500. Hence, we'll increase the chunk size to 1000.

```python PYTHON
separator = "###"
chunk_size = 1000
chunk_overlap = 0

text_splitter = CharacterTextSplitter(
    separator = separator,
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    length_function=len,
    is_separator_regex=False,
)

documents = text_splitter.create_documents([text_custom])
documents = [Document(text=doc.page_content) for doc in documents]

retriever = build_retriever(documents)

source_nodes = retriever.retrieve(question)
print('Number of docuemnts: ',len(source_nodes))
source_nodes= [{"text": ni.get_content()}for ni in source_nodes]

response = co.chat(
  message=question,
  documents=source_nodes,
  model=co_model
)
response = response
print(response.text)
```

```txt title="Output"
WARNING:langchain_text_splitters.base:Created a chunk of size 5946, which is longer than the specified 1000
WARNING:langchain_text_splitters.base:Created a chunk of size 4092, which is longer than the specified 1000
WARNING:langchain_text_splitters.base:Created a chunk of size 1782, which is longer than the specified 1000
WARNING:langchain_text_splitters.base:Created a chunk of size 1392, which is longer than the specified 1000
WARNING:langchain_text_splitters.base:Created a chunk of size 2046, which is longer than the specified 1000
WARNING:langchain_text_splitters.base:Created a chunk of size 1152, which is longer than the specified 1000
WARNING:langchain_text_splitters.base:Created a chunk of size 1304, which is longer than the specified 1000
WARNING:langchain_text_splitters.base:Created a chunk of size 1295, which is longer than the specified 1000
WARNING:langchain_text_splitters.base:Created a chunk of size 2090, which is longer than the specified 1000
WARNING:langchain_text_splitters.base:Created a chunk of size 1251, which is longer than the specified 1000


Number of docuemnts:  5
Elon Musk mentions Jonathan Nolan. Musk is friends with the creators of Westworld, Jonathan Nolan and Lisa Joy Nolan.
```

Below we validate the answer using citations.

```python PYTHON
print(insert_citations(response.text, response.citations))
```

```txt title="Output"
Elon Musk [0] mentions Jonathan Nolan. [0] Musk is friends [0] with the creators of Westworld [0], Jonathan Nolan [0] and Lisa Joy Nolan. [0]
```

```python PYTHON
source_nodes[0]
```

```python title="Output"
{'text': "Elon Musk -- Chief Executive Officer and Product Architect\nYeah. The creators of Westworld, Jonathan Nolan, Lisa Joy Nolan, are friends -- are all friends of mine, actually. And I invited them to come see the lab and, like, well, come see it, hopefully soon. It's pretty well -- especially the sort of subsystem test stands where you've just got like one leg on a test stand just doing repetitive exercises and one arm on a test stand pretty well.\nYeah.\n### Unknown speaker\nWe're not entering Westworld anytime soon.\n### Elon Musk -- Chief Executive Officer and Product Architect\nRight, right. Yeah. I take -- take safety very very seriously.\n### Martin Viecha\nThank you. The next question from Norman is: How many Cybertruck orders are in the queue? And when do you anticipate to be able to fulfill existing orders?"}
```

## Discussion \[#discussion]

This example highlights some of the concerns that arise when implementing chunking strategies. This is a field of ongoing research, and many exciting surveys have been published in domain-specific applications. For example, this [paper](https://arxiv.org/pdf/2402.05131.pdf) examines different chunking strategies in finance.



---

**Navigation:** [← Previous](./14-step-4-conversation-with-memory-using-ai-messages-.md) | [Index](./index.md) | [Next →](./16-creating-a-qa-bot-from-technical-documentation.md)
