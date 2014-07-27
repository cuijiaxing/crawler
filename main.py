import urllib2
import sys
from bs4 import BeautifulSoup

def getHtmlDoc(inputUrl):
    try:
        resultStr = urllib2.urlopen(inputUrl).read()
    except:
        print inputUrl
    return resultStr 


def getQuestionSolution(soup):
    result = soup.find_all("pre", class_="prettyprint nicefont")[0].string
    result = result.replace("<", "&lt;")
    result = result.replace(">", "&gt;")
    return result;

def getQuestionDescription(soup):
    return soup.find_all("div", "post-sum")[0].string

def getQuestionTitle(soup):
    return soup.find_all("h2", class_="post-title")[0].string

def getInfo(inputStr):
    soup = BeautifulSoup(inputStr)
    title = getQuestionTitle(soup)
    desc = getQuestionDescription(soup)
    solution = getQuestionSolution(soup)
    return (title, desc, solution)

def getTemplate(templateFileName):
    inputFile = open(templateFileName)
    templateStr = inputFile.read()
    inputFile.close()
    return templateStr

def replaceTemplate(templateStr, title, description, solution, prev_url, next_url):
    templateStr = templateStr.replace("fuck_title", title)
    templateStr = templateStr.replace("fuck_desc", description)
    templateStr = templateStr.replace("fuck_solution", solution)
    if prev_url is None:
        templateStr = templateStr.replace("fuck_prev", "#")
    else:
        templateStr = templateStr.replace("fuck_prev", prev_url)
    if next_url is None:
        templateStr = templateStr.replace("fuck_next", "#")
    else:
        templateStr = templateStr.replace("fuck_next", next_url)
    return templateStr

def getAndStore(inputUrl, fileName, prev_url, next_url):
    htmlDoc = getHtmlDoc(inputUrl)
    htmlDoc = htmlDoc.replace("NineChapter", "LeetCode")
    htmlDoc = htmlDoc.replace("http://www.ninechapter.com/", "http://www.leetcodeforyou.com/")
    title, desc, solution = getInfo(htmlDoc)
    templateStr = getTemplate("template.html")
    resultStr = replaceTemplate(templateStr, title, desc, solution, prev_url, next_url)
        
    outputFile = open(fileName, "w")
    outputFile.write(resultStr)
    outputFile.close()

def getFileName(url):
    return url[url[0:-2].rfind("/") + 1 : -1] + ".html"

if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('UTF8')
    urlFileName = "problems.txt"
    inputFile = open(urlFileName)
    urlList = [url.strip() for url in inputFile]
    inputFile.close()
    ourUrl = "http://www.leetcodeforyou.com/problems/"
    for i in range(len(urlList)):
        url = urlList[i]
        fileName = getFileName(url)
        filePath = "result/" + fileName
        #fileName = "result/" + url[url[0:-2].rfind("/") + 1 :]
        if i == 0:
            prev_url = None
        if i == len(urlList) - 1:
            next_url = None
        else:
            next_url = ourUrl + getFileName(urlList[i + 1])
        try:
            getAndStore(url, filePath, prev_url, next_url)
        except:
            print "error"
        prev_url = ourUrl + fileName













