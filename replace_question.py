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
    return soup.find_all("div", "question-content")[0]





if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('UTF8')

    inputDir = "result/"
    outputDir = "output/"
    fileNames = os.listdir(inputDir)
    prefix = "https://oj.leetcode.com/problems/"
    scriptInputFile = open("script.txt")
    script = scriptInputFile.read()
    scriptInputFile.close()
    for fileName in fileNames:
        if not ".html" in fileName:
            continue
        url = prefix + fileName[0:fileName.find(".html")] + "/"
        print url
        inputFile = open(inputDir + fileName)
        inputDoc = inputFile.read()
        inputFile.close()
        onlineDesc = getQuestionDescription(url)
        inputDoc = inputDoc.replace("question-content", "post-sum")
        soup = BeautifulSoup(inputDoc)
        soup.find_all("div", "post-sum")[0].string = "fuck_desc"
        outputStr = soup.prettify()
        outputStr = outputStr.replace("post-sum", "question-content")
        outputStr = outputStr.replace("fuck_desc", str(onlineDesc))
        outputStr = outputStr.replace('//static.getclicky.com/js', 'http://code.jquery.com/jquery-2.1.1.min.js')
        outputStr = outputStr.replace("try{ clicky.init(100717227); }catch(e){}", script)
        outputFile = open(outputDir + fileName, "w")
        outputFile.write(outputStr)
        outputFile.close()
    print "finished crawling"




