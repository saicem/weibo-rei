# Spider

## 替换Cookie

将`weibospider/settings.py`中:

```python
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Cookie':'SCF=AlvwCT3ltiVc36wsKpuvTV8uWF4V1tZ17ms9t-bZCAuiVJKpCsgvvmSdylNE6_4GbqwA_MWvxNgoc0Ks-qbZStc.; OUTFOX_SEARCH_USER_ID_NCOO=1258151803.428431; SUB=_2A25zjTjHDeRhGeBN6VUX9SvEzT-IHXVQjliPrDV6PUJbkdANLUvskW1NRJ24IEPNKfRaplNknl957NryzKEwBmhJ; SUHB=0ftpSdul-YZaMk; _T_WM=76982927613'
}
```

Cookie字段替换成你自己的Cookie

## 运行程序

### 抓取用户信息

```bash
python run_spider.py user
```

### 抓取用户粉丝列表

```bash
python run_spider.py fan
```

### 抓取用户关注列表

```bash
python run_spider.py follow
```

### 抓取微博评论

```bash
python run_spider.py comment
```

### 抓取用户的微博(全量)

在`./weibospider/spiders/tweet.py`中`start_requests`,urls选择`init_url_by_user_id()`

```bash
python run_spider.py tweet
```

### 抓取用户的微博(指定时间段)

在`./weibospider/spiders/tweet.py`中`start_requests`,urls选择`init_url_by_user_id_and_date()`

```bash
python run_spider.py tweet
```

### 抓取包含关键词的微博（已失效）

在`./weibospider/spiders/tweet.py`中`start_requests`,urls选择`init_url_by_keywords_and_date()`

```bash
python run_spider.py tweet
```

### 抓取微博转发

```bash
python run_spider.py repost
```

## 微博数据字段

### 用户数据

|        字段        |               说明               |
| :----------------: | :------------------------------: |
|        _id         | 用户的ID，可以作为用户的唯一标识 |
|     nick_name      |               昵称               |
|       gender       |               性别               |
|      province      |              所在省              |
|        city        |              所在市              |
| brief_introduction |             个人简介             |
|      birthday      |               生日               |
|     tweets_num     |            微博发表数            |
|      fans_num      |              粉丝数              |
|   followers_num    |              关注数              |
|  sex_orientation   |              性取向              |
|     sentiment      |             感情状况             |
|     vip_level      |             会员等级             |
|   authentication   |             认证情况             |
|     education      |             教育经历             |
|        work        |             工作经历             |
|     person_url     |           用户首页链接           |
|       labels       |       用户标签，用逗号分割       |
|     crawl_time     |            抓取时间戳            |

### 微博数据

|       字段        |                     说明                      |
| :---------------: | :-------------------------------------------: |
|        _id        |                    微博id                     |
|      user_id      |               这则微博作者的ID                |
|      content      |                  微博的内容                   |
|    created_at     |                 微博发表时间                  |
|    repost_num     |                    转发数                     |
|    comment_num    |                    评论数                     |
|     like_num      |                    点赞数                     |
|       tool        |                发布微博的工具                 |
|     image_url     | 微博中图片的URL，注意如果是组图会只抓取第一张 |
|     video_url     |                微博中视频的URL                |
| location_map_info |               定位的经纬度信息                |
|   origin_weibo    |     原始微博，只有转发的微博才有这个字段      |
|    crawl_time     |                  抓取时间戳                   |

### 用户关系数据

|    字段     |       说明       |
| :---------: | :--------------: |
|     _id     |    用户关系id    |
|   fan_id    |  关注者的用户ID  |
| follower_id | 被关注者的用户ID |
| crawl_time  |    抓取时间戳    |

### 评论数据

|      字段       |     说明     |
| :-------------: | :----------: |
|       _id       |   评论的id   |
| comment_user_id | 评论的用户ID |
|    weibo_id     |  weibo的ID   |
|     content     |   评论内容   |
|   created_at    | 评论创建时间 |
|   crawl_time    |  抓取时间戳  |

### 转发数据

|    字段    |      说明       |
| :--------: | :-------------: |
|    _id     |      null       |
| crawl_time |   抓取时间戳    |
|  weibo_id  | 被转发weibo的ID |
|  user_id   |  转发用户的ID   |
|  content   | 转发的评论内容  |
| created_at |    转发时间     |
