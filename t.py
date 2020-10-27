# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import jieba
import json


# 讀取 json 的程式
def jsonTextReader(jsonFilePath):
    with open(jsonFilePath, 'r', encoding='utf-8') as f:
        jsonFile = json.load(f)
        return jsonFile['text']


# 將字串轉為「句子」列表的程式
def text2Sentence(inputSTR):
    # replace '...' and '…' with ''
    unused = ['...', '…']
    for sep in unused:
        inputSTR = inputSTR.replace(sep, '')

    # replace '，', '、', '。', '「', '」' with separator '\n'
    separators = ['，', '、', '。', '「', '」']
    for sep in separators:
        inputSTR = inputSTR.replace(sep, '\n')

    # if ',' is not located in number, replace it with '\n'
    currentIndex = 0
    while True:
        # find next ','
        currentIndex = inputSTR.find(',', currentIndex)

        # ',' not find
        if currentIndex == -1:
            break

        # ',' is located in numbers
        if str.isdigit(inputSTR[currentIndex - 1]) and str.isdigit(inputSTR[currentIndex + 1]):
            currentIndex += 1
            continue

        inputSTR = inputSTR[:currentIndex] + '\n' + inputSTR[currentIndex + 1:]
        currentIndex += 1

    return inputSTR.strip('\n').split('\n')


def cutSentence(strList):
    resultList = []
    for s in strList:
        resultList.append("/".join(jieba.cut(s, cut_all=False)))
    return resultList


if __name__ == "__main__":
    # 設定要讀取的 news.json 路徑
    newsJsonPath = './example/news.json'

    # 將 news.json 利用 [讀取 json] 的程式打開
    text = jsonTextReader(newsJsonPath)

    # 將讀出來的內容字串傳給 [將字串轉為「句子」 列表」]的程式，存為 newsLIST
    newsLIST = text2Sentence(text)

    print("\n".join(cutSentence(newsLIST)))
