from numpy import float64, log2
import numpy
import pandas as pd
import numpy as np
from os import path

df_tweet_senti = pd.read_csv(
    f"{path.dirname(__file__)}/data/tweet_senti.csv",
    header=0,
    index_col=0,
    dtype={
        "senti_index": np.float64,
        "like_num": np.int32,
        "repost_num": np.int32,
        "comment_num": np.int32,
    },
)

matrix = df_tweet_senti.values.T
tmp = 1.0 / (matrix[4] + matrix[2] * matrix[1] + matrix[3] + 1)
rei = -np.log2(np.float64(tmp))
df_tweet_senti["rei"] = rei
df_tweet_senti[["weibo_id", "rei"]].to_csv("rei.csv")
