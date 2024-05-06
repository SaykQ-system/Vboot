from userinfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

class vboot:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("http://hermes.fonetyazilim.com/auth")
        time.sleep(2)
        #login user
        username=self.browser.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div/form/div[2]/input")
        password=self.browser.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div/form/div[3]/input")
        username.send_keys(self.username)
        password.send_keys(self.password)
        time.sleep(1)
        self.browser.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div/form/div[4]/button").click()
        time.sleep(2)

        results = []
        #.csv import
        ID = pd.read_csv('D:\\vboot\\vId.csv')
        print("CSV dosyası başarıyla yüklendi.")
        print("CSV dosyasındaki veriler:")
        print(ID)

        id_list = ID['ID'].tolist()
        for id in id_list:
            #search
            girdi_kutusu = self.browser.find_element("xpath","/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[1]/div/input")
            girdi_kutusu.clear()
            girdi_kutusu.send_keys(id)
            time.sleep(2)
            self.browser.find_element("xpath","/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/div/span[1]").click()
            time.sleep(2)
            #text
            hbs = self.browser.find_element(By.CLASS_NAME,'ribbon-label.cursor-pointer')
            bas = self.browser.find_element(By.CLASS_NAME,'fs-2.d-flex.fw-bolder.text-gray-900.mb-0.me-1')
            met = self.browser.find_element(By.CLASS_NAME,'fs-4.fw-normal.text-gray-800.mb-10')
            HBS = hbs.text
            BAS = bas.text
            MET = met.text
            time.sleep(1)
            results.append([HBS, BAS, MET])
            #search close
            self.browser.find_element("xpath","/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/button").click()
            time.sleep(1)
        
        df = pd.DataFrame(results, columns=['HBS_ID', 'Konu', 'Yorum&Açıklama'])
        df.to_csv('output.csv', index=False)
        self.browser.quit()
        print("\033[92mboot ok\033[0m")    
vboot=vboot(username, password)
vboot.signIn()