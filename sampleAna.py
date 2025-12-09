import os
import sys
import urllib.request
import urllib.parse
import json
import re
from konlpy.tag import Kkma
from konlpy.utils import pprint
from collections import Counter


def get_reuqest_url(sp, strV) :
    # developer.naver.com의 client ID, secret code를 작성
    client_id = "Qzmrm7JZT3_I2hr25qOg"
    client_secret = "Wz6nfO_Ioe"

    # utf-8 형태로 인코딩
    encStr = urllib.parse.quote(strV)

    openURL = "https://openapi.naver.com/v1/search/news.json"
    mergeURL = openURL + "?query=" + encStr + + "&display=100" + "&start=" + str(sp)

    # URL을 통하여 요청 시작
    request = urllib.request.Request(mergeURL)

    # 요청을 하기 위해서 먼저 header에 값을 추가 (사이트마다 상이)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    # 위에서 작성된 request를 전송한다
    response = urllib.request.urlopen(request)

    # 정상적으로 접속시 : 200
    # 페이지 또는 매개변수 에러시 : 400
    # 시스템 에러 : 500
    resCode = response.getcode()
    print("rescode : ", resCode)

    if (resCode == 200) :
        return response.read().decode('utf-8')
    else :
        print("error code : ", resCode)


def getNaverSearchResults(sp, strV) :
    
    retData = get_reuqest_url(sp, strV)
    
    # URL 연결을 통하여 결과값을 받아오는데
    # 만약 연결이 되지 않았을 경우, 호출한 함수로 결과값이 없음을 알려주고 
    # 정상적으로 연결하여 결과값을 받았을 경우 데이터를 json 데이터로 변환하여 반환함
    if (retData == None) :
        return None
    else :
        return json.loads(retData)


# URL을 통하여 받아온 결과를 정제하기 위한 함수
def getPostData() :
    
    content = getNaverSearchResults()
    
    jsonResult = []
    
    if (content != None) :
        for post in content['items'] :
            title = post['title']
            link = post['link']
            originallink = post['originallink']
            description = post['description']
            pubdate = post['pubDate']
            
            jsonResult.append({'title' : title, 
                            'link' : link, 
                            'originallink' : originallink, 
                            'description' : description,
                            'pubdate' : pubdate})

    return jsonResult


# 정제된 데이터를 File로 저장하기 위함
def writeFile() :
    
    getData = getPostData()
    
    # with open --> 파일을 열어서 처리하기 위한 명령어
    # with open (파일명, '읽기(r)'/'쓰기(w)', 인코딩 타입)
    with open ('sampleJson.json', 'w', encoding='utf-8') as oFile :
        # json.dump --> json 형태의 내용을 쓰겠다
        # getData --> 받아온 데이터
        # indent --> 들여쓰기
        # sort_keys --> 정렬
        # ensure_ascii --> ascii 코드로 변환 여부
        retJon = json.dumps(getData, indent=4, sort_keys=True, ensure_ascii=False)
        oFile.write(retJon)


def getData() : 
    
    strV = input("검색어 입력 : ") # 검색어
    sp = 1 # 시작 위치
    listV = []

    for i in range(1, 11) :
        if (i >= 2) :
            sp = (i-1)*100+1
        resultVal = getNaverSearchResults(sp, strV)
        
        listV.append(resultVal)


def funcAna() :
    
    wordInfo = dict()
    
    baseDir = os.getcwd()
    # print("변경 전 디렉토리 : ", baseDir)
    
    if (baseDir != "/Users/parkchaeyeon/Desktop/GitHub/BigData_Analysis_Technology") :
        os.chdir("/Users/parkchaeyeon/Desktop/GitHub/BigData_Analysis_Technology")
        baseDir = os.getcwd()
    
    # print("변경 후 디렉터리 : ", baseDir)
    
    fileDir = input("파일명 입력 (확장자까지 입력) : ")
    
    fileLoc = baseDir + "/" + fileDir
    
    fileYN = os.path.isfile(fileLoc)
    # print("파일 존재 여부 : ", fileYN)
    
    if (fileYN == True) :
        rFile = open(fileLoc, 'r', encoding="utf-8").read()
        # rFile1 = open(fileLoc, 'r', encoding="utf-8")
        
        # print("rFile : ", rFile)
        # print("rFile1 : ", rFile1)
        
        jsonData = json.loads(rFile)
        # print("jsonData : ", jsonData)
        
        desc = ''
        
        for i in jsonData : 
            if 'title'in i.keys() :
                desc = desc + re.sub(r'[^\w]',  ' ', i['title'])
            
        # print("desc : ", desc)
        
        ma = Kkma()
        nounsD = ma.nouns(desc)
        cnt = Counter(nounsD)
        
        # print(cnt)
        
        for tag, cnt in cnt.most_common(50) :
            if (len(tag) >= 2) :
                wordInfo[tag] = cnt
                
        # print(wordInfo)
        
    return wordInfo




if (__name__ == "__main__") : # 이 파일에서 직접 실행하면 이 밑 코드 실행 (import 됐을 때는 이 밑 실행 X)
    getData()