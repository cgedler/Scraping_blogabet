# Created on : Feb 5, 2024, 7:11:04 PM
# Author     : Christopher Gedler


import src.excel.tool
import src.scraper.core
import src.model.pick


if __name__ == '__main__':
    print('------ Start ------')
    mylist = src.excel.tool.ReadExcelFile("/resources/input/links.xlsx", 347)
    listObj = []
    for x in mylist:
        url = x
        if (src.scraper.core.getStatusConnectionCode(url) == 200):
            document = src.scraper.core.getHtmlDocument(url)         
            picks = ""
            profit = ""
            yields = ""
            followers = ""
            span_picks = document.find_all('span', attrs={"id": "header-picks"})
            for data in span_picks:
                picks = data.get_text()

            span_profit = document.find_all('span', attrs={"id": "header-profit"})
            for data in span_profit:
                profit = data.get_text()

            span_yields = document.find_all('span', attrs={"id": "header-yield"})
            for data in span_yields:
                yields = data.get_text()

            span_followers = document.find_all('span', attrs={"id": "header-followers"})
            for data in span_followers:
                followers = data.get_text()
            
            objPick = src.model.pick.Pick(url, picks, profit, yields, followers)
            listObj.append(objPick)      
        else:
            print("Exception, URL return Status Code: " + str(src.scraper.core.getStatusConnectionCode(url)))
    src.excel.tool.writeExcelFile("./resources/output/result.xlsx", listObj)
    print('------ End ------')
   
    

