# cemotion 判断情感倾向 0~1

from cemotion import Cemotion
import pandas as pd
import numpy as np
from os import path

df_comment = pd.read_csv(
    f"{path.dirname(__file__)}/data/CommentsCleaned.csv",
    header=0,
    dtype={"like_num": np.int32},
)

# 仅获取非 nan 数据
df_tmp = df_comment[["weibo_id", "content", "like_num"]].dropna()
# 筛选删除字符数小于 8 的评论
df_tmp = df_tmp.drop(df_tmp[df_tmp["content"].str.len() < 8].index)
c = Cemotion()
df_tmp["senti_index"] = df_tmp["content"].apply(lambda x: c.predict(x))
# 存储数据
df_tmp[["weibo_id", "like_num", "senti_index"]].to_csv("comment_senti.csv")


# df_target = df_tmp.groupby("weibo_id")["content"].apply(
#     lambda x: average([c.predict(i) for i in x])
# )
# df_target = df_target.rename("content", "senti_index")
# df_target.to_csv("senti.csv")

# from cnsenti import Sentiment, Emotion

# senti = Sentiment()
# emotion = Emotion()
# test_text = (
#     "我有几个微信群里，总有几个傻儿吧唧的人在传一些东西，这些人不是蠢就是坏，或者又蠢又坏。这个时候别添乱了，请相信官方消息，建议抓到一个处理一个，乱弹琴！"
# )
# # 看积极和消极的词汇
# print(senti.sentiment_count(test_text))
# # 还要看修饰词
# print(senti.sentiment_calculate(test_text))
# # 喜怒哀乐
# print(emotion.emotion_count(test_text))
