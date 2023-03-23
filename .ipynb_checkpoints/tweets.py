import snscrape.modules.twitter as sntwitter
import pandas as pd

query ="(from:elonmusk) until:2022-07-14 since:2010-06-14"
tweets = []
limit = 6000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    # print(vars(tweet))
    # break

    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.url, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'Url', 'Tweet'])
df.to_csv("C:\\Users\\amit\\Desktop\\twitter_data.csv")
print(df)

