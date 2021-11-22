# 计算原数据的分布

# 绘制每天发微博数量的柱状图
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.core.series import Series
from matplotlib.axes import Axes
from os.path import dirname

df_tweet = pd.read_csv(
    f"{dirname(__file__)}/../data/Tweets.csv",
    header=0,
    parse_dates=[3],
    dtype={"comment_num": np.int32},
)
df_tweet["created_at"] = df_tweet["created_at"].map(lambda x: datetime.date(x))
df_tweet_cnt = df_tweet["created_at"].value_counts().sort_index()
df_comment_cnt: Series = (
    df_tweet[["comment_num", "created_at"]]
    .groupby("created_at")["comment_num"]
    .apply(lambda x: sum(x))
)


# 绘制发布微博数量的柱状图
plt.subplot(2, 1, 1)
plt.bar(df_tweet_cnt.index, df_tweet_cnt.values)
plt.xlabel("date")
plt.ylabel("tweet count")
# axes[0].tick_params(axis='x', labelrotation=20)
# plt.xticks(rotation=20)


# 绘制评论数量的柱状图
plt.subplot(2, 1, 2)
plt.bar(df_comment_cnt.index, df_comment_cnt.values, color="g")
plt.twinx()
plt.plot(df_tweet_cnt.index, df_tweet_cnt.values, "b")
plt.xlabel("date")
plt.ylabel("comment count")


plt.show()
