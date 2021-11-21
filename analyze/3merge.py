import pandas as pd
from os import path

df_senti = pd.read_csv(f"{path.dirname(__file__)}/data/weight_senti.csv", header=0)
df_tweet = pd.read_csv(
    f"{path.dirname(__file__)}/data/TweetsCleaned.csv", header=0, index_col=0
)
df_tweet = df_tweet.rename(columns={"_id": "weibo_id"})
df = pd.merge(df_senti, df_tweet, how="inner", on="weibo_id").rename(
    columns={"0": "senti_index"}
)
df[["weibo_id", "senti_index", "comment_num", "like_num", "repost_num"]].to_csv(
    "tweet_senti.csv"
)
