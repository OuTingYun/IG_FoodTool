# selenium登入
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time,re,os
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import lxml
from bs4 import BeautifulSoup as Soup
import pymysql
import requests

class SP():
    def __init__(self) -> None:
        pass
    def add_store(stores,Account_name,Store):
        Account_name = Account_name[0]
        f = stores.filter(AccountName=Account_name)
        if len(f)==0:
            print("=======新增帳號...=======")
            Store.objects.create(AccountName=Account_name)
    def scrap(n_scroll=["1"],Account_name=["foody_tw"]):
       
        # account_url = 'https://www.instagram.com/foody_tw/'
        # n_scroll = 1
        # Account_name="kangol_eat.foodie"
        if Account_name=="":
            return []

        Account_name = Account_name[0]
        n_scroll = int(n_scroll[0])
        account_url = f'https://www.instagram.com/{Account_name}/'
        print("=======載入網址:",account_url,"...=======")
        print("=======登入中...=======")

        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get('https://www.instagram.com/')

        # ------ 填入帳號與密碼 ------
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.NAME, 'username')))
        # ------ 網頁元素定位 ------
        username_input = browser.find_elements_by_name('username')[0]
        password_input = browser.find_elements_by_name('password')[0]
        # ------ 輸入帳號密碼 ------
        username_input.send_keys("cutinatee")
        password_input.send_keys("Oty@789700")

        # ------ 登入 ------
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH,
        '//*[@id="loginForm"]/div/div[3]/button/div')))
        # ------ 網頁元素定位 ------
        login_click = browser.find_elements_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')[0]
        # ------ 點擊登入鍵 ------
        login_click.click()
        # ------ 不儲存登入資料 ------
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))

        # ------網頁元素定位 ------
        store_click = browser.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')[0]

        # ------ 點擊不儲存鍵 ------
        store_click.click()
        # ------ 不開啟通知 ------
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')))

        # ------ 網頁元素定位 ------                                                                                                    
        notification_click = browser.find_elements_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')[0]
# /html/body/div[5]/div/div/div/div[3]/button[2]
        # ------ 點擊不開啟通知 ----
        notification_click.click()

        browser.get(account_url) # 前往該網址
        post_url = []


        # 往下滑並取得新的貼文連結
        # 下拉30次

        print("=======爬蟲中...=======")
        for i in range(n_scroll):
            scroll = 'window.scrollTo(0, document.body.scrollHeight);'
            browser.execute_script(scroll)
            html = browser.page_source
            soup = Soup(html, 'html.parser')

            # 尋找所有的貼文連結
            for elem in soup.select('article div div div div a'):
                # 如果新獲得的貼文連結不在列表裡，則加入
                if elem['href'] not in post_url:
                    post_url.append(elem['href'])
            time.sleep(5) # 等待網頁加載
        
        # 總共加載的貼文連結數
        print("總共取得 " + str(len(post_url)) + " 篇貼文連結")

        post=['https://www.instagram.com'+item for item in post_url]
        Taiwan = pd.DataFrame()
        for i in range(len(post)):
            if i==5:
                break
            print(f"正在處理第: {i} 篇文章...")
            #前往該網址
            url=post[i]
            browser.implicitly_wait(10)
            browser.get(url)
            #解析網站
            soup = Soup(browser.page_source, 'html.parser')
            content_list=soup.select('div.C4VMK span')

            #找不到資料,下一筆
            if not content_list:
                continue
            #將內文取出
            content=content_list[1].text
            
            #店家的所在地
            patten = r"全台|基隆|台北|新北|桃園|新竹|苗栗|台中|彰化|南投|雲林|嘉義|台南|高雄|屏東|台東|花蓮|宜蘭|澎湖|金門"
            Place_list=re.findall(patten,content)


            if Place_list:

                place=Place_list[0]
                #照片網址
                img_path=soup.find_all('img')[1].get('src')
                
                Taiwan = Taiwan.append({"Place":place,"Content":content,"PictureUrl":img_path,"PostID":url},ignore_index=True)

        Place_info = pd.read_csv(os.getcwd()+"\\Lib\\Place_infomation.csv")
        Taiwan = Taiwan.merge(Place_info,on = "Place",how = "left")
        Taiwan["PostID"] = Taiwan["PostID"].apply(lambda x:x[28:-1])
        Taiwan['AccountName']=Account_name
        browser.close()
        return Taiwan

    def compare(result,Taiwan,AccountName=['foody_tw']):
        Account_name = AccountName[0]
        buf = []
    
        for item in result:
            buf.append([item.PostID,item.Content,item.PictureUrl,item.Place,item.AccountName,item.PlaceID])
        df = pd.DataFrame(buf, columns=["PostID","Content","PictureUrl","Place","AccountName","PlaceID"])  
        df_buf = pd.concat([df,df,Taiwan])
        df_buf = df_buf.drop_duplicates(subset=['PostID'], keep=False)
        print(f"加入 {len(df_buf)} 篇文章...")

        
        

        if(os.path.exists(f'./static/picture/{Account_name}/')):
            print("Yes")
        else:
            os.mkdir(f'./static/picture/{Account_name}/')
        for i in range(len(df_buf)):
            print(f"載入第 {i} 篇文章的圖片...")
            item = df_buf.iloc[i]
            PostID = item['PostID']
            path = item['PictureUrl']
            img_data = requests.get(path).content
            with open(f'./static/picture/{Account_name}/'+PostID+'.jpg', 'wb') as handler:
                    handler.write(img_data)
        print(f"共載入 {len(df_buf)} 張圖片...")

        return df_buf
    def Insert(post,data):
        print(f"插入資料庫...")
        for i in range(len(data)):
            item = data.iloc[i]
            post.objects.create(
                PostID = item['PostID'],
                Content = item['Content'],
                PictureUrl = item['PictureUrl'],
                Place = item['Place'],
                AccountName = item['AccountName'],
                PlaceID = item['PlaceID']
            )
        print(f"完成更新資料庫...")