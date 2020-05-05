

Request URL: https://weitoutiao.zjurl.cn/api/feed/forum_flow/v1/?query_id=1656810113086509&tab_id=1656810113086525&category=forum_flow_subject&is_preview=1&request_source=1&stream_api_version=82&aid=13&app_extra_params=



query_id=1656810113086509&tab_id=1656810113086525&category=forum_flow_subject&is_preview=1&request_source=1&stream_api_version=82&aid=13&app_extra_params=


query_id=1656810113086509&tab_id=1656810113086525&category=forum_flow_subject&is_preview=1&request_source=1&stream_api_version=82&aid=13&app_extra_params={%22module_id%22:%221656810113087501%22,%22offset%22:%22200%22}


query_id=1656810113086509&tab_id=1656810113086525&category=forum_flow_subject&is_preview=1&request_source=1&stream_api_version=82&aid=13&app_extra_params={%22module_id%22:%221656810113087501%22,%22offset%22:%22240%22}

query_id: 1656810113086509
tab_id: 1656810113086525

category: forum_flow_subject
is_preview: 1
request_source: 1
stream_api_version: 82
aid: 13
app_extra_params: {"module_id":"1656810113087501","offset":"260"}

```json
{
    "message": "success",
    data = [
        { content: "数据在这里是一个长长的字符串" }
    ],
    "has_more": true,
    "offset": 1,
    "tail": "",
    "api_base_info": {
        "info_type": null,
        "raw_data": null,
        "app_extra_params": "{\"module_id\":\"1656810113087501\",\"offset\":\"200\"}"
    },
    "preload_ack_data": null
}
```

取出 content 字符串内容：

```python
content = json.loads(response.text)['data'][0]['content']
```

将 content json 化，其包含的 key：

```json
{
    "abstract" :
    "allow_download" :
    "article_sub_type" :
    "article_type" :
    "article_url" :
    "ban_comment" :
    "ban_immersive" :
    "behot_time" :
    "bury_count" :
    "cell_type" :
    "comment_count" :
    "content_decoration" :
    "cursor" :
    "data_type" :
    "digg_count" :
    "has_m3u8_video" :
    "has_mp4_video" :
    "has_video" :
    "hot" :
    "id" :
    "ignore_web_transform" :
    "interaction_data" :
    "is_subject" :
    "item_version" :
    "level" :
    "log_pb" :
    "raw_data" :
    "read_count" :
    "req_id" :
    "rid" :
    "share_count" :
    "share_info" :
    "show_dislike" :
    "show_portrait" :
    "show_portrait_article" :
    "small_image" :
    "sub_raw_datas" :  这里面是新闻数据，是个字典元素的列表
    "tip" :
    "user_repin" :
    "user_verified" :
    "verified_content" :
    "video_style" :
}
```

取新闻列表：

```python
subRawDatasList = json.loads(content)["sub_raw_datas"]
        for i in subRawDatasList:
            print(i)
```
