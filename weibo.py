from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException, WebDriverException
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
zhanghao = input("请输入你的微博账号：")
mima = input("请输入你的密码：")
duixiang = input("请输入需要点赞的微博用户名：")
chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('https://weibo.com/')
# browser.maximize_window()
wait = WebDriverWait(browser,10,0.5)
account = WebDriverWait(browser, 20).until(expected_conditions.visibility_of_element_located((By.NAME, 'username')))\
    .send_keys(zhanghao)
password = browser.find_element_by_name('password').send_keys(mima)
sign_in = browser.find_elements_by_link_text('登录')[1].click()


wait.until(EC.visibility_of_element_located((By.ID,'qrCodeCheck'))).click()


searchInput = WebDriverWait(browser, 10).until(lambda x: x.find_element_by_xpath("//input[@node-type='searchInput']"))
searchInput.send_keys(duixiang)
searchInput = WebDriverWait(browser, 10).until(lambda x: x.find_element_by_xpath("//input[@node-type='searchInput']"))
searchInput.send_keys(Keys.ENTER)

my_class = WebDriverWait(browser, 10).\
    until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, duixiang)))
my_class.click()

handles = browser.window_handles
browser.close()
browser.switch_to.window(handles[1])

#like = WebDriverWait(browser, 10).until(lambda x: x.find_elements_by_xpath("//span[@node-type='like_status']"))
#while True:
    #for i in like:
        #try:
            #if not i.get_attribute('class'):
                #i.click()
        #except WebDriverException:
            #continue
old_like = []
like = []
while True:
    new_like = WebDriverWait(browser, 10).until(lambda x: x.find_elements_by_xpath("//span[@node-type='like_status']"))
    for i in new_like:
        if i not in old_like:
            like.append(i)
    old_like = new_like

    mark = 0
    for i in like:
        try:
            if not i.get_attribute('class'):
                i.click()
            else:
                mark += 1
        except WebDriverException:
            continue
        if mark >= 20:
            break

    browser.execute_script("arguments[0].scrollIntoView();", i)
    if mark >= 20:
        break

input("程序运行完毕")
browser.quit()
