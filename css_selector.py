import time

from selenium import webdriver
import time
# 打开浏览器
driver = webdriver.Chrome()
# 输入地址
driver.get("http://www.baidu.com")
time.sleep(5)

# 定位百度搜索框
# 1. 使用绝对路径去进行定位
# driver.find_element_by_css_selector("html>body>div>div>div>div>div>form>span>input").send_keys("小龙女")  # 使用的是绝对路径，各级之间使用>或者空格都行
# driver.find_element_by_css_selector("html body div div div div div form span input").send_keys("小龙女")  # 使用的是空格

# 2.使用id去进行定位 #
# driver.find_element_by_css_selector("#kw").send_keys("杨过") # id是kw， 如果定位到的元素没有ID属性就无法进行使用

# 3.通过class进行定位  class符号就是.
# driver.find_element_by_css_selector(".s_ipt").send_keys("哈哈哈")

# 4.如果没有class和ID的属性进行定位的话，还可以使用其他的属性进行定位 [属性名="属性值"]
# driver.find_element_by_css_selector("[autocomplete='off']").send_keys("杨过") # 如果其他也有相似的一个，就需要进行多个属性进行定位了
driver.find_element_by_css_selector("[autocomplete='off'] [name='wd']").send_keys("哈哈")  # 可以是多个

# 5.通过层级去进行定位
driver.find_element_by_css_selector("form>span>input").send_keys("哈哈")
# 层级加id组合定位
driver.find_element_by_css_selector("form#form>span>input").send_keys("哈哈")  # form层级上有ID是等于form的
driver.find_element_by_css_selector("form.fm>span>input").send_keys("哈哈")  # form层级上有class是等于fm的

# 6. 通过兄弟节点进行定位，如果无法通过上面这些去定位的话，比如绝对路径都是一样的下面有多个input，而且里面的元素都一样，则可以互相利用
# 定位第一个节点： first-child
# 定位2 3 4 。。。节点 nth-child(n) n是元素的序号
# 最后一个节点： last-child
