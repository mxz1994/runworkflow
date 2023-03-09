from os import environ

import requests






def main():
    cookies = {
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22%2BUjpBNv8q7k7t6wqb31YpT%2F2Pt1%2B8nRG%2FvCExy8elRrQ38KCNhw%2FSANjV1Jk%2Ba%2Fo%22%2C%22first_id%22%3A%22185b12d69dad6e-033c0ca4587e6b8-65630e54-396328-185b12d69dc923%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg1YjEyZDY5ZGFkNmUtMDMzYzBjYTQ1ODdlNmI4LTY1NjMwZTU0LTM5NjMyOC0xODViMTJkNjlkYzkyMyIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IitVanBCTnY4cTdrN3Q2d3FiMzFZcFQvMlB0MSs4blJHL3ZDRXh5OGVsUnJRMzhLQ05ody9TQU5qVjFKaythL28ifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22%2BUjpBNv8q7k7t6wqb31YpT%2F2Pt1%2B8nRG%2FvCExy8elRrQ38KCNhw%2FSANjV1Jk%2Ba%2Fo%22%7D%2C%22%24device_id%22%3A%22185b12d69dad6e-033c0ca4587e6b8-65630e54-396328-185b12d69dc923%22%7D',
        '__token': 'QoFWqdcv8HAvETeFknCCZ0F2TVXiNNCz6LpQLofBCDKzhTiU81L1oYIExsUk9BAggk0QXXx8zLxHfgPXziFiS6pg6wowVKA6wxMdjnZTsFe1gfBr4Kigg7eruW2Hz0VU0zvM7ri6s3OmVt-uM97s7UZAmc5k-KvEOUkDAi6PWOAuZkorX-h9VKPolbRC2Frnby334UrRLyn7-_xZSgKNSSBT4nteKmXL2KoNcqVtZZw=',
        '__tokenat': '1678211432234',
        '_tracker_distinct_id_': '20230308b4e8f57d',
        '_tracker_launch_': '1',
        '_tracker_session_id_': 'ed105288-8394-4f73-88db-01785269e399',
        'canvasId': '%5Bobject%20Object%5D',
        'Hm_lvt_30af5b3628fbccf83c5f1ef797dd16e2': '1674063905,1674124633',
    }

    headers = {
    'Host': 'youhui.95516.com',
    'Accept': 'application/json, text/plain, */*',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiJQM0pFMDBLWkoiLCJ0IjoiNDc4NDk5IiwiaWF0IjoxNjc4MjExNDMyLCJleHAiOjE2NzgzODQyMzJ9.iBrYDqmFPHcCyqfag25HdZTj7W88g4jZJxf1IDLT0YA',
    'X-Tingyun': 'c=B|p35OnrDoP8k;x=31500971d0fa4553',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'x-city': '410300',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'Origin': 'https://youhui.95516.com',
    # 'Content-Length': '2',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148/sa-sdk-ios  (com.unionpay.chsp) (cordova 4.5.4) (updebug 0) (version 930) (UnionPay/1.0 CloudPay) (clientVersion 190) (language zh_CN) (upHtml) (walletMode 00)',
    'Referer': 'https://youhui.95516.com/newsign/public/app/index.html?t=1678211432234',
    'Connection': 'keep-alive',
    # 'Cookie': 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22%2BUjpBNv8q7k7t6wqb31YpT%2F2Pt1%2B8nRG%2FvCExy8elRrQ38KCNhw%2FSANjV1Jk%2Ba%2Fo%22%2C%22first_id%22%3A%22185b12d69dad6e-033c0ca4587e6b8-65630e54-396328-185b12d69dc923%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg1YjEyZDY5ZGFkNmUtMDMzYzBjYTQ1ODdlNmI4LTY1NjMwZTU0LTM5NjMyOC0xODViMTJkNjlkYzkyMyIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IitVanBCTnY4cTdrN3Q2d3FiMzFZcFQvMlB0MSs4blJHL3ZDRXh5OGVsUnJRMzhLQ05ody9TQU5qVjFKaythL28ifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22%2BUjpBNv8q7k7t6wqb31YpT%2F2Pt1%2B8nRG%2FvCExy8elRrQ38KCNhw%2FSANjV1Jk%2Ba%2Fo%22%7D%2C%22%24device_id%22%3A%22185b12d69dad6e-033c0ca4587e6b8-65630e54-396328-185b12d69dc923%22%7D; __token=QoFWqdcv8HAvETeFknCCZ0F2TVXiNNCz6LpQLofBCDKzhTiU81L1oYIExsUk9BAggk0QXXx8zLxHfgPXziFiS6pg6wowVKA6wxMdjnZTsFe1gfBr4Kigg7eruW2Hz0VU0zvM7ri6s3OmVt-uM97s7UZAmc5k-KvEOUkDAi6PWOAuZkorX-h9VKPolbRC2Frnby334UrRLyn7-_xZSgKNSSBT4nteKmXL2KoNcqVtZZw=; __tokenat=1678211432234; _tracker_distinct_id_=20230308b4e8f57d; _tracker_launch_=1; _tracker_session_id_=ed105288-8394-4f73-88db-01785269e399; canvasId=%5Bobject%20Object%5D; Hm_lvt_30af5b3628fbccf83c5f1ef797dd16e2=1674063905,1674124633',
}

    json_data = {}
    response = requests.post('https://youhui.95516.com/newsign/api/daily_sign_in',
    cookies=cookies, headers=headers, json=json_data)

    # proxies = {
    #     'http': 'http://127.0.0.1:7890',
    #     'https': 'http://127.0.0.1:7890',
    # }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = ('chat_id=5455171178&text=' + response.text).encode()

    TELEGRAM_BOT_TOKEN = environ['TELEGRAM_BOT_TOKEN']
    response = requests.post(
        'https://api.telegram.org/bot'+ TELEGRAM_BOT_TOKEN +'/sendMessage',
        headers=headers,
        data=data,
        # proxies=proxies,
    )


if __name__ == '__main__':
    main()