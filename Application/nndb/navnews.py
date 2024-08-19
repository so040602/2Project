import json
import urllib.request
import datetime
import time


def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header('X-Naver-Client-Id', 'yM3APVPOEbyT5oMTSIKl')
    req.add_header("X-Naver-Client-Secret", 'YnZrwCxs1S')
    # req.add_header("Content-Type", "application/json")

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print('[%s]Url Request Success' % datetime.datetime.now())
            return response.read().decode('utf-8')

    except Exception as e:
        print(e)
        print('[%s] Error for URL : %s' % (datetime.datetime.now(), url))
        return None
# end try


def getNaverSearch(node, srcText, start, display):
    base = 'https://openapi.naver.com/v1/search'
    node1 = '/%s.json' % node
    parameters = '?query=%s&start=%s&display=%s' % (urllib.parse.quote(srcText), start, display)
    print(urllib.parse.quote(srcText))
    url = base + node1 + parameters
    responseDecode = getRequestUrl(url)
    print(url)
    if responseDecode is None:
        print("Failed to decode the response.")
        return None
    else:
        return json.loads(responseDecode)


def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    if link.startswith('https://n.news.naver.com/'):
        pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
        pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

        jsonResult.append({
            'cnt': cnt,
            'title': title,
            'description': description,
            'org_link': org_link,
            'link': link,
            'pDate': pDate
        })
    return


def main():
    node = 'news'
    srcText = ['정치', 'it', '경제', '스포츠', '연애']
    cnt = 0

    for category in srcText:
        jsonResult = []  # 매 카테고리마다 초기화
        jsonResponse = getNaverSearch(node, category, 1, 100)
        total = jsonResponse.get('total', 0)
        print(f'{category} - 전체 검색 : {total} 건')

        while (jsonResponse is not None) and (jsonResponse['display'] != 0):
            # Debugging information
            print(f"{category} - Start: {jsonResponse['start']}, Display: {jsonResponse['display']}")

            # Check if we've reached the limit
            if jsonResponse['start'] >= 1000:
                break

            for post in jsonResponse['items']:
                cnt += 1
                getPostData(post, jsonResult, cnt)

            start = jsonResponse['start'] + jsonResponse['display']
            jsonResponse = getNaverSearch(node, category, start, 100)

        with open(f'{category}_naver_{node}.json', 'w', encoding='utf-8') as outfile:
            jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(jsonFile)

        print(f"{category} - 가져온 데이터 : {cnt} 건")
        print(f'{category}_naver_{node}.json SAVED')
        # 다음 카테고리를 위한 카운트 초기화
        cnt = 0

# 함수가 스크립트에 호출되도록 보장
if __name__ == "__main__":
    main()
