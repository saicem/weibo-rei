# cemotion 判断情感倾向 0~1

import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
from os import path


def weight_average(df: DataFrame):
    like_num = df["like_num"].values
    senti_index = df["senti_index"].values
    ret = sum((like_num + 1) * senti_index) / sum(like_num + 1)
    return ret


df_comment_senti = pd.read_csv(
    f"{path.dirname(__file__)}/data/comment_senti.csv",
    header=0,
    index_col=0,
    dtype={"senti_index": np.float64},
)

# 仅获取非 nan 数据
df_tmp = df_comment_senti.dropna()


df_target = df_tmp.groupby("weibo_id").apply(weight_average)
df_target.to_csv("weight_senti.csv")
