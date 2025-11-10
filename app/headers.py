from fake_useragent import UserAgent

ua = UserAgent()
HEADERS = {
            "User-Agent": ua.random,
            "referer":"https://www.pixiv.net",
            "Accept":"image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
            "Cache-Control":"no-cache",
            "Connection":"keep-alive",
            "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "pragma":"no-cache",
            "priority":"u=1, i",
            "sec-ch-ua":'sec-ch-ua"Microsoft Edge";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
            "sec-ch-ua-mobile":"?0",
            "sec-ch-ua-platform":"windows",
            "sec-fetch-mode":"no-cors",
            "sec-fetch-site":"cross-site",
            "sec-fetch-storage-access":"active"
            }
