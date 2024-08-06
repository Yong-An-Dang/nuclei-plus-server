import json


def test_human_message():
    input_string = """
    # 模板要求

1. “path” 字段必须由模板变量 “BaseURL”拼接路径
2. poc模板除外，禁止回答其他内容

# HTTP流量

```HTTP-FLOW
GET / HTTP/1.1
Host: baidu.com
Accept-Language: zh-CN
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Connection: keep-alive



HTTP/1.1 302 Moved Temporarily
Server: bfe/1.0.8.18
Date: Sat, 13 Jul 2024 03:58:10 GMT
Content-Type: text/html
Content-Length: 161
Connection: Keep-Alive
Location: https://www.baidu.com/
Expires: Sun, 14 Jul 2024 03:58:10 GMT
Cache-Control: max-age=86400
Cache-Control: privae

<html>
<head><title>302 Found</title></head>
<body bgcolor="white">
<center><h1>302 Found</h1></center>
<hr><center>bfe/1.0.8.18</center>
</body>
</html>
```


请根据 “模板要求” 以及 “HTTP流量”，编写一个poc模板。
    """

    human_message = {
        "humanMessage": input_string
    }

    print()
    print(json.dumps(human_message))
    print()
