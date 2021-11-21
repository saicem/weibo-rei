from os import path
import pandas as pd
import re

from pandas.core.frame import DataFrame

# 加载数据
def load_data(filename: str) -> DataFrame:
    df = pd.read_csv(f"{path.dirname(__file__)}/data/{filename}", header=0)
    return df


# 数据清洗
def clean_data(df: DataFrame):
    df = df.dropna()
    for index, row in df.iterrows():
        content = row["content"]
        # 去除标点符号
        content = re.sub(r"[【】，。？,.《》]", " ", content)
        # 去除话题
        content = re.sub(r"#.+?#", " ", content)
        # 去除 html标签
        content = re.sub(r"<.+?/>", " ", content)
        # 去除特定文字
        content = content.replace(r"转发理由:", " ")
        # 去除 链接
        content = re.sub(r"http.+?[\s:：、]", " ", content)
        # 去除 @用户
        content = re.sub(r"(@.{1,12}){1,5}?[\s:：、]", " ", content)
        content = re.sub(r"@.{1,12}?[\s:：、]", " ", content)
        content = re.sub(r"@.{1,12}?$", " ", content)  # 去除多余的空格
        content = content.strip()
        content = re.sub(r"\s+", " ", content)
        # 改变初始值
        df.loc[index, "content"] = content
    return df


# 数据清洗
if __name__ == "__main__":
    df = load_data("Tweets.csv")
    df = clean_data(df)
    df.to_csv("TweetsCleaned.csv")

    df = load_data("Comments.csv")
    df = clean_data(df)
    df.to_csv("CommentsCleaned.csv")
