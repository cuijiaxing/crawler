import os
import urllib2
from bs4 import BeautifulSoup
import sys


def getHtmlDoc(inputUrl):
    try:
        resultStr = urllib2.urlopen(inputUrl).read()
    except:
        print inputUrl
    return resultStr

def getQuestionDescription(url):
    inputHtmlDoc = getHtmlDoc(url)
    soup = BeautifulSoup(inputHtmlDoc)
    return soup.find_all("div", "question-content")[0].string





if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('UTF8')

    inputDir = "result/"
    outputDir = "output/"
    fileNames = os.listdir(inputDir)
    prefix = "https://oj.leetcode.com/problems/"
    for fileName in fileNames:
        if not ".html" in fileName:
            continue
        url = prefix + fileName[0:fileName.find(".html")] + "/"
        inputFile = open(inputDir + fileName)
        inputDoc = inputFile.read()
        inputFile.close()
        onlineDesc = getQuestionDescription(url)

        soup = BeautifulSoup(inputDoc)
        soup.find_all("div", "post-sum")[0] = onlineDesc
        outputStr = soup.prettify()
        outputStr.replace("post-sum", "question-content")
        outputFile = open(outputDir + fileName, "w")
        outputFile.write(outputStr)
        outputFile.close()
    print "finished crawling"




