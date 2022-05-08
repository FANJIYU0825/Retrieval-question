
import requests as req
from bs4 import BeautifulSoup 
import pandas as pd
import re
def finout(SearchNum):
  # Remainder
  if SearchNum%30 != 0:
    Quotient=SearchNum/30
    result=int(Quotient)+1
    
  if SearchNum%30 == 0:
    Quotient=SearchNum/30
    result=int(Quotient)
  return result
def url_finder(PageNum,SearchNum):
  
  all_ls=[]
  mergeLs = []
  for i in range ((PageNum)):
    HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    url = f'https://ithelp.ithome.com.tw/articles?tab=tech&page{i+1}'
    print(url)
    html = req.get(url,headers=HEADERS)
    soup = BeautifulSoup(html.text,'html.parser')
    Qa_list = soup.find_all(attrs={"class": "qa-list"})
    Qa_list_url = [Qa_list[i].find_all(class_=re.compile("^qa-condition"))[0].get('href')for i in  range(len(Qa_list))]
    all_ls.append(Qa_list_url)
  for i in range(len(all_ls)):
    a=all_ls[i]
    for mc in a :
      mergeLs.append(mc)
  return mergeLs[0:SearchNum]
def Qacrewing(QaListUrl):
  info_it=[]
  for i in range (len(QaListUrl)):
    HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    
    """
    需要去注意錯誤資料避免異常
    """
    htmlin =req.get(QaListUrl[i],headers=HEADERS)
    SoupIn = BeautifulSoup(htmlin.text,'html.parser')
    #作者
    users = SoupIn.find_all(class_=re.compile("^img-circle qa-header__info-avatar"))[0].getText()
    users = re.sub(r"\s+", '', users)
    users

    #TTILE
    title = SoupIn.find_all(class_=re.compile("^qa-header__title"))[0].getText()
    title = re.sub(r"\s+", '', title)
    title

    #瀏覽次數
    info_view=[]
    if SoupIn.find_all(class_=re.compile("^qa-header__info-view"))[0].getText()==1:

      info_view = SoupIn.find_all(class_=re.compile("^qa-header__info-view"))[0].getText()
      info_view = re.sub(r"\s+", '', info_view)
      info_view= re.sub(r"瀏覽+", '', info_view)
      info_view = int(info_view)
    else:
      info_view
    #LIKENUM
    likeGroup__num=[]
    if  SoupIn.find_all(class_=re.compile("^likeGroup__num"))[0].getText()==1:

      likeGroup__num = SoupIn.find_all(class_=re.compile("^likeGroup__num"))[0].getText()
      likeGroup__num = re.sub(r"\s+", '', likeGroup__num)
      likeGroup__num
    else :
      likeGroup__num
    #留言數量
    likeMESSEGE__num = []
    try: 
    
      likeMESSEGE__num = SoupIn.find_all(class_=re.compile("^qa-action__link-num"))[0].getText()
      likeMESSEGE__num = re.sub(r"\s+", '', likeMESSEGE__num)
      likeMESSEGE__num

    except IndexError:
      likeMESSEGE__num
    #發布時間
    info_time =[]
    try: 
    

      info_time = SoupIn.find_all(class_=re.compile("^qa-header__info-time"))[0].getText()
      info_time = re.sub(r"\s+", '', info_time)
      info_time
    except:
      info_time
    # 內文
    cotent = SoupIn.find_all(class_=re.compile("^markdown"))[0].getText()
    cotent = re.sub(r"\s+", '', cotent)
    cotent
    # 所有留言
    response_info= []
    response=SoupIn.find_all(class_=re.compile("^response-markdown"))
    for r in range (len(response)):
        print("response_text",response_text)
        response_text = SoupIn.find_all(class_=re.compile("^response-markdown"))[r].getText()
        response_text = re.sub(r"\s+", '', response_text)
        response_text
        #留言時間
        response_TIME= SoupIn.find_all(class_=re.compile("^ans-header__time"))[r].getText()
        response_TIME = re.sub(r"\s+", '', response_TIME )
        response_TIME
        # 回應者
        response_USER = SoupIn.find_all(class_=re.compile("^response-header__person"))[r].getText()
        response_USER= re.sub(r"\s+", '', response_USER)
        response_USER
        response_info.append({
        "留言時間":response_TIME,
        "回應者":response_USER,
        "回應內容":response_text
        })
      
    info_it.append({
      "作者ID":users,
      "標題":title,
      "發布時間":info_time,
      "like次數":likeGroup__num, 
      "留言次數":likeMESSEGE__num,
      "瀏覽次數":info_view, 
      "內文":cotent,
      "所有留言":response_info})
  return info_it
 
