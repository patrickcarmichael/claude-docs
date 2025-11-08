---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Dataset: Top 3,000 Ask HN posts

We will use the top 3,000 posts from the Ask HN section of Hacker News. We provide a CSV containing the posts.
```python PYTHON
df = pd.read_csv('https://storage.googleapis.com/cohere-assets/blog/text-clustering/data/askhn3k_df.csv', index_col=0)

print(f'Loaded a DataFrame with {len(df)} rows')
```
```
Loaded a DataFrame with 3000 rows
```
```python PYTHON
df.head()
```javascript
<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          title
        </th>

        <th>
          url
        </th>

        <th>
          text
        </th>

        <th>
          dead
        </th>

        <th>
          by
        </th>

        <th>
          score
        </th>

        <th>
          time
        </th>

        <th>
          timestamp
        </th>

        <th>
          type
        </th>

        <th>
          id
        </th>

        <th>
          parent
        </th>

        <th>
          descendants
        </th>

        <th>
          ranking
        </th>

        <th>
          deleted
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          I'm a software engineer going blind, how should I prepare?
        </td>

        <td>
          NaN
        </td>

        <td>
          I&#x27;m a 24 y&#x2F;o full stack engineer (I know some of you are rolling your eyes right now, just highlighting that I have experience on frontend apps as well as backend architecture). I&#x27;ve been working professionally for ~7 years building mostly javascript projects but also some PHP. Two years ago I was diagnosed with a condition called &quot;Usher&#x27;s Syndrome&quot; - characterized by hearing loss, balance issues, and progressive vision loss.<p>I know there are blind software engineers out there. My main questions are:<p>- Are there blind frontend engineers?<p>- What kinds of software engineering lend themselves to someone with limited vision? Backend only?<p>- Besides a screen reader, what are some of the best tools for building software with limited vision?<p>- Does your company employ blind engineers? How well does it work? What kind of engineer are they?<p>I&#x27;m really trying to get ahead of this thing and prepare myself as my vision is degrading rather quickly. I&#x27;m not sure what I can do if I can&#x27;t do SE as I don&#x27;t have any formal education in anything. I&#x27;ve worked really hard to get to where I am and don&#x27;t want it to go to waste.<p>Thank you for any input, and stay safe out there!<p>Edit:<p>Thank you all for your links, suggestions, and moral support, I really appreciate it. Since my diagnosis I&#x27;ve slowly developed a crippling anxiety centered around a feeling that I need to figure out the rest of my life before it&#x27;s too late. I know I shouldn&#x27;t think this way but it is hard not to. I&#x27;m very independent and I feel a pressure to &quot;show up.&quot; I will look into these opportunities mentioned and try to get in touch with some more members of the blind engineering community.
        </td>

        <td>
          NaN
        </td>

        <td>
          zachrip
        </td>

        <td>
          3270
        </td>

        <td>
          1587332026
        </td>

        <td>
          2020-04-19 21:33:46+00:00
        </td>

        <td>
          story
        </td>

        <td>
          22918980
        </td>

        <td>
          NaN
        </td>

        <td>
          473.0
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          Am I the longest-serving programmer – 57 years and counting?
        </td>

        <td>
          NaN
        </td>

        <td>
          In May of 1963, I started my first full-time job as a computer programmer for Mitchell Engineering Company, a supplier of steel buildings.  At Mitchell, I developed programs in Fortran II on an IBM 1620 mostly to improve the efficiency of order processing and fulfillment.  Since then, all my jobs for the past 57 years have involved computer programming.  I am now a data scientist developing cloud-based big data fraud detection algorithms using machine learning and other advanced analytical technologies.  Along the way, I earned a Master’s in Operations Research and a Master’s in Management Science, studied artificial intelligence for 3 years in a Ph.D. program for engineering, and just two years ago I received Graduate Certificates in Big Data Analytics from the schools of business and computer science at a local university (FAU).  In addition, I currently hold the designation of Certified Analytics Professional (CAP).  At 74, I still have no plans to retire or to stop programming.
        </td>

        <td>
          NaN
        </td>

        <td>
          genedangelo
        </td>

        <td>
          2634
        </td>

        <td>
          1590890024
        </td>

        <td>
          2020-05-31 01:53:44+00:00
        </td>

        <td>
          story
        </td>

        <td>
          23366546
        </td>

        <td>
          NaN
        </td>

        <td>
          531.0
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>
      </tr>

      <tr>
        <th>
          2
        </th>

        <td>
          Is S3 down?
        </td>

        <td>
          NaN
        </td>

        <td>
          I&#x27;m getting<p>{\n  &quot;errorCode&quot; : &quot;InternalError&quot;\n}<p>When I attempt to use the AWS Console to view s3
        </td>

        <td>
          NaN
        </td>

        <td>
          iamdeedubs
        </td>

        <td>
          2589
        </td>

        <td>
          1488303958
        </td>

        <td>
          2017-02-28 17:45:58+00:00
        </td>

        <td>
          story
        </td>

        <td>
          13755673
        </td>

        <td>
          NaN
        </td>

        <td>
          1055.0
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>
      </tr>

      <tr>
        <th>
          3
        </th>

        <td>
          What tech job would let me get away with the least real work possible?
        </td>

        <td>
          NaN
        </td>

        <td>
          Hey HN,<p>I&#x27;ll probably get a lot of flak for this. Sorry.<p>I&#x27;m an average developer looking for ways to work as little as humanely possible.<p>The pandemic made me realize that I do not care about working anymore. The software I build is useless. Time flies real fast and I have to focus on my passions (which are not monetizable).<p>Unfortunately, I require shelter, calories and hobby materials. Thus the need for some kind of job.<p>Which leads me to ask my fellow tech workers, what kind of job (if any) do you think would fit the following requirements :<p>- No &#x2F; very little involvement in the product itself (I do not care.)<p>- Fully remote (You can&#x27;t do much when stuck in the office. Ideally being done in 2 hours in the morning then chilling would be perfect.)<p>- Low expectactions &#x2F; vague job description.<p>- Salary can be on the lower side.<p>- No career advancement possibilities required. Only tech, I do not want to manage people.<p>- Can be about helping other developers, setting up infrastructure&#x2F;deploy or pure data management since this is fun.<p>I think the only possible jobs would be some kind of backend-only dev or devops&#x2F;sysadmin work. But I&#x27;m not sure these exist anymore, it seems like you always end up having to think about the product itself. Web dev jobs always required some involvement in the frontend.<p>Thanks for any advice (or hate, which I can&#x27;t really blame you for).
        </td>

        <td>
          NaN
        </td>

        <td>
          lmueongoqx
        </td>

        <td>
          2022
        </td>

        <td>
          1617784863
        </td>

        <td>
          2021-04-07 08:41:03+00:00
        </td>

        <td>
          story
        </td>

        <td>
          26721951
        </td>

        <td>
          NaN
        </td>

        <td>
          1091.0
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>
      </tr>

      <tr>
        <th>
          4
        </th>

        <td>
          What books changed the way you think about almost everything?
        </td>

        <td>
          NaN
        </td>

        <td>
          I was reflecting today about how often I think about Freakonomics. I don&#x27;t study it religiously. I read it one time more than 10 years ago. I can only remember maybe a single specific anecdote from the book. And yet the simple idea that basically every action humans take can be traced back to an incentive has fundamentally changed the way I view the world. Can anyone recommend books that have had a similar impact on them?
        </td>

        <td>
          NaN
        </td>

        <td>
          anderspitman
        </td>

        <td>
          2009
        </td>

        <td>
          1549387905
        </td>

        <td>
          2019-02-05 17:31:45+00:00
        </td>

        <td>
          story
        </td>

        <td>
          19087418
        </td>

        <td>
          NaN
        </td>

        <td>
          1165.0
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>
      </tr>
    </tbody>
  </table>
</div>

We calculate the embeddings using Cohere's `embed-v4.0` model. The resulting embeddings matrix has 3,000 rows (one for each post) and 1024 columns (meaning each post title is represented with a 1024-dimensional embedding).
```python PYTHON
batch_size = 90

embeds_list = []
for i in range(0, len(df), batch_size):
    batch = df[i : min(i + batch_size, len(df))]
    texts = list(batch["title"])
    embs_batch = co.embed(
        texts=texts, model="embed-v4.0", input_type="search_document"
    ).embeddings
    embeds_list.extend(embs_batch)

embeds = np.array(embeds_list)
embeds.shape
```
```
(3000, 1024)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
