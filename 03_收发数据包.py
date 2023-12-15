from DrissionPage import SessionPage

# 教程 https://g1879.gitee.io/drissionpagedocs/get_start/examples/data_packets/

# 创建页面对象
page = SessionPage()

# 爬取3页
for i in range(1, 4):
    # 访问某一页的网页
    page.get(f'https://gitee.com/explore/all?page={i}')
    # 获取所有开源库<a>元素列表
    links = page.eles('.title project-namespace-path')
    # 遍历所有<a>元素
    for link in links:
        # 打印链接信息
        print(link.text, link.link)
