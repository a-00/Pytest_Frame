from pydoc import classname
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

@allure.epic("Z05")
@allure.feature("框架")
@allure.story("登录")
#class Test_login():

@allure.title("人员实力查看接口")

def test_login():
    try:
        # 打开网站
        driver = webdriver.Chrome()
        driver.get('http://192.168.100.119:20100/')

        # 创建显示等待对象
        wait_obj = WebDriverWait(driver, 10)
        # 设置等待条件（等搜索结果的div出现）
        wait_obj.until(expected_conditions.presence_of_element_located
                    ((By.CLASS_NAME, 'el-input__inner')))

        # 登录
        driver.find_elements(By.CLASS_NAME, "el-input__inner")[0].send_keys('admin')
        driver.find_elements(By.CLASS_NAME, "el-input__inner")[1].send_keys('Xqwl8888')
        driver.find_element(By.CLASS_NAME, "login_btn").click()
        print('****************登录成功****************')
        time.sleep(5)
        driver.get_screenshot_as_file("./screenshot/successful.png")

    except (ValueError):
        print('****************登录失败****************')
        driver.get_screenshot_as_file("./logs/screenshot/fail.png")

    finally:
        time.sleep(5)
        driver.quit()


def test_icon(self):
    expected = '应用商店'
    # 进入到应用商店页面
    store_btn = self.driver.find_element_by_css_selector('img[src="f81eeb348e7b7944b6dcec9a54d2a785.png"]')
    store_btn = self.driver.find_element(by=By.LINK_TEXT, value='应用商店')
    store_btn = self.driver.find_element('xpath', '/p[@class="app-item"]')
    store_btn = self.driver.find_element_by_css_selector(
        "#main > div > div > section > section > main > div.workbench-pedestal.height-abs > div > div.df-left > div.el-card.box-card-wrap.application-two.is-always-shadow > div > div.application-two__body > div.app-list > ul > li:nth-child(1) > div > div > img")
    self.driver.implicitly_wait(10)
    store_btn.click()
    
    # 打开指定微服务
    # driver.find_elements(By.CLASS_NAME, "el-image__inner")[1].click()
    # print("应用商店")

    # 断言，判断页面中唯一元素是否存在
    try:
        actual =self.driver.find_element('xpath', '//p[@class="titleApp titleBgYellow"]')
        assert actual.text == expected
        print("断言成功",actual.text == expected)
    except Exception as e:
        print("断言失败")
        raise e

    # 进入子应用页面
    icon_Btn = self.driver.find_element_by_css_selector("#shop1820369029862850561 > div > div:nth-child(1) > div.item-pic")
    icon_Btn.click()
    print("组件演示")
    self.driver.quit()