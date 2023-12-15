from DrissionPage import WebPage

# 教程 https://g1879.gitee.io/drissionpagedocs/get_start/examples/switch_mode/#_3

# 创建页面对象
page = WebPage()
# 访问网址
page.get('https://gitee.com/explore')
# 查找文本框元素并输入关键词
page('#q').input('DrissionPage')
# 点击搜索按钮
page('t:button@tx():搜索').click()
# 等待页面加载
page.wait.load_start()
# 切换到收发数据包模式
page.change_mode()
# 获取所有行元素
items = page('#hits-list').eles('.item')
# 遍历获取到的元素
for item in items:
    # 打印元素文本
    print(item('.title').text)
    print(item('.desc').text)
    print()
