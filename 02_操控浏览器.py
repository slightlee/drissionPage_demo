from DrissionPage import ChromiumPage

# 教程 https://g1879.gitee.io/drissionpagedocs/get_start/examples/control_browser/
# 模拟登录gitee

# 创建页面对象，并启动或接管浏览器
page = ChromiumPage()
# 跳转到登录页面
page.get('https://gitee.com/login')

# 定位到账号文本框，获取文本框元素
ele = page.ele('#user_login')
# 输入对文本框输入账号
ele.input('lmm_work@163.com')
# 定位到密码文本框并输入密码
page.ele('#user_password').input('limingwei1009')
# 点击登录按钮
page.ele('@value=登 录').click()
