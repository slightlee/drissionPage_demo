# DrissionPage 项目示例

```text
DrissionPage 是一个基于 python 的网页自动化工具。

它既能控制浏览器，也能收发数据包，还能把两者合而为一。

可兼顾浏览器自动化的便利性和 requests 的高效率。

它功能强大，内置无数人性化设计和便捷功能。

它的语法简洁而优雅，代码量少，对新手友好。
```
## 文档地址
> https://g1879.gitee.io/drissionpagedocs/get_start/installation_and_import/

## 安装和导入

### ✅️️安装
请使用 pip 安装 DrissionPage：
```shell
pip install DrissionPage
```

### ✅️️升级
```shell
pip install DrissionPage --upgrade
```

### ✅️️导入

#### 📌 页面类
> 页面类用于控制浏览器，或收发数据包，是最主要的工具。DrissionPage 包含三种主要页面类。根据须要在其中选择使用。

WebPage是功能最全面的页面类，既可控制浏览器，也可收发数据包：
```shell
from DrissionPage import WebPage
```
如果只要控制浏览器，导入ChromiumPage：
```shell
from DrissionPage import ChromiumPage
```
如果只要收发数据包，导入SessionPage：
```shell
from DrissionPage import SessionPage
```

#### 📌 配置工具

> 很多时候我们须要设置启动参数，可导入以下两个类，但不是必须的。

ChromiumOptions类用于设置浏览器启动参数：
```shell
from DrissionPage import ChromiumOptions
```
SessionOptions类用于设置Session对象启动参数：
```shell
from DrissionPage import SessionOptions
```
Settings用于设置全局配置：
```shell
from DrissionPage.common import Settings
```

#### 📌 其它工具
> 有两个我们可能须要用到的工具，需要时可以导入。

动作链，用于模拟一系列键盘和鼠标的操作：
```shell
from DrissionPage.common import ActionChains
```
键盘按键类，用于键入 ctrl、alt 等按键：
```shell
from DrissionPage.common import Keys
```
与 selenium 一致的By类，便于项目迁移：
```shell
from DrissionPage.common import By
```
浏览器数据包监听器，用法详见“进阶使用”章节：
```shell
from DrissionPage.common import Listener, RequestMan
```
easy_set里保存了一些便捷的 ini 文件设置方法，可选择使用：
```shell
from DrissionPage.easy_set import *
```

#### 📌 导入异常
异常放在以下路径：
```shell
from DrissionPage.errors import ElementNotFoundError
```

