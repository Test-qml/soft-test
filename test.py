from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.common.by import By

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome()

# 设置最大等待时长为 5秒
wd.implicitly_wait(5)

# 让浏览器打开指定网址
wd.get('https://www.bilibili.com/')
time.sleep(5)


#
# # 浏览“国创”专区
# wd.find_element(By.XPATH, '//*[@id="i_cecream"]/div[2]/div[1]/div[3]/div[2]/div[1]/a[3]').click()
# sleep(5)
#
# new_wd = wd.window_handles[-1]
# wd.switch_to.window(new_wd)
#
# # 返回首页
# wd.find_element(By.CLASS_NAME, 'entry-title').click()
# sleep(5)
#
# new_wd = wd.window_handles[-1]
# wd.switch_to.window(new_wd)

# 选择搜索框
element = wd.find_element(By.CLASS_NAME,'nav-search-input')

# 输入搜索内容“软件测试”
element.send_keys('软件测试\n')
wd.find_element(By.CLASS_NAME,'nav-search-btn')

new_wd = wd.window_handles[-1]
wd.switch_to.window(new_wd)

# 点击第一个视频
u1 = wd.find_element(By.CLASS_NAME, 'bili-video-card')
ele = u1.find_element(By.CLASS_NAME, 'bili-video-card__wrap')
text = ele.text
if '软件测试' in text:
    print('test pass!')
ele.click()
time.sleep(5)

new_wd = wd.window_handles[-1]
wd.switch_to.window(new_wd)

# # 关闭弹幕
# wd.find_element(By.CLASS_NAME, 'bui-danmaku-switch-input').click()
#
# sleep(5)

# # 切换下一集
# vl = wd.find_elements(By.CLASS_NAME,'clickitem')[1]
# vl.find_element(By.CLASS_NAME, 'link-content').click()
#
# sleep(5)

# 点击作者主页
wd.find_element(By.CLASS_NAME, 'up-avatar').click()

sleep(5)

new_wd = wd.window_handles[-1]
wd.switch_to.window(new_wd)

# 发送信息
wd.find_element(By.CLASS_NAME, 'h-message').click()
sleep(5)

new_wd = wd.window_handles[-1]
wd.switch_to.window(new_wd)
#
# 登录
# 使用By.CSS_SELECTOR和CSS选择器来定位输入框
input_element = wd.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入账号"]')
# 在输入框中输入文本
input_element.send_keys('17855386323')

input_element = wd.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入密码"]')
input_element.send_keys('**********')

wd.find_element(By.CLASS_NAME,'btn_primary').click()

sleep(10)

# wd.close()

