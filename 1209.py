from matplotlib import font_manager, rc

# import matplotlib.font_manager as fm
# import matplotlib.rc as rc

import matplotlib.pyplot as plot
import pytagcloud
import webbrowser

import sampleAna as ana


def showGraph() :
    
    wordInfo = ana.funcAna()
    
    font_loc = "/Users/parkchaeyeon/Library/Fonts/윤고딕350.ttf"
    font_name = font_manager.FontProperties(fname=font_loc).get_name()
    rc('font', family=font_name, size=8)
    
    # print("graph 내 호출 한 wordInfo \n", wordInfo)
    
    """
    print("값의 개수 : ", len(wordInfo))
    print("----------------------------------\n")
    print("items : ", wordInfo.items())
    print("----------------------------------\n")
    print("keys : ", wordInfo.get)
    print("----------------------------------\n")
    print("keys : ", wordInfo.keys())
    print("----------------------------------\n")
    print("values : ", wordInfo.values())
    print("----------------------------------\n")
    """
    
    # dict Type
    # key --> keys()
    # value --> values(), wordInfo[key]

    # x축 --> word
    # y축 --> value

    plot.xlabel("명사")
    plot.ylabel("빈도")
    
    # 빈도수
    sorted_values = sorted(wordInfo.values(), reverse=True) # 내림차순 정렬 (sorted 함수 - 기본적으로 오름차순)
    
    # 명사
    sorted_keys = sorted(wordInfo, key=wordInfo.get, reverse=True)
    
    # wordInfo.values()

    # plot.bar() --> 막대 그래프를 그리기 위함

    plot.bar(range(len(wordInfo)), sorted_values, align="center")
    plot.xticks(range(len(wordInfo)), list(sorted_keys), rotation=-90) # rotation : 글씨각도조정
    
    plot.show()


def wordCloud() :
    
    wordInfo = ana.funcAna()
    
    saveLoc = "/Users/parkchaeyeon/Desktop/GitHub/BigData_Analysis_Technology/wordCloud.jpg"
    
    tagList = pytagcloud.make_tags(wordInfo.items(), maxsize=100)
    pytagcloud.create_tag_image(tagList, saveLoc, size=(640,480), fontname='korean', rectangular=False)
    
    webbrowser.open(saveLoc)


if (__name__ == "__main__") :
    wordCloud()
    