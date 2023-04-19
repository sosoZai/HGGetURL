from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
#打开空白浏览器
driver = webdriver.Chrome()
#访问网站
driver.get("http://www.chinaclear.cn/zdjs/flfg/law_index_new.shtml")

# ui = driver.find_elements(By.XPATH,'//div[text()="业务规则"]/following-sibling::div/div[@class="pageTabContent"]')
#
# sj = []
# for ui1 in ui:
#     #print(ui1.text)
#     sj.append(ui1.text)
# del sj[1:]
# # print(sj)
# # f_sj = sj[0].split("\n")
# tp = sj[0].replace("- ", "")
# f_sj = tp.split("\n")
# f_sj.pop()
# print(f_sj)
# # print(tp)

ac = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[6]/div[1]/ul/li[2]')
action = ActionChains(driver)
action.click(ac).perform()
# print(ac)
# time.sleep(30)
ui11 = driver.find_elements(By.XPATH,'/html/body/div[2]/div[3]/div[7]/div[2]')
sj1 = []
for ui11 in ui11:
    #print(ui1.text)
    sj1.append(ui11.text)
del sj1[1:]
# print(sj)
# f_sj = sj[0].split("\n")
tp1 = sj1[0].replace("- ", "")
f_sj1 = tp1.split("\n")
f_sj1.pop()
print(f_sj1)


driver.close()

