# PyChina.org

in fact from 2003 there is CZUG.org ~ the 1st(and only one) focus Zope tech community be set up;

so years ago, there is soooooooo many python tech abt. commuity in China

but never group as one unify community brand,
like as: perl-china/ruby-china etc. 

so after PyCon2013China, some `old` Chinese Pythonista together and building:

![](PyChina_logo_131217_zq_h200.png)

## goal

- by Pythonner in China Operations
- as Pythonner in China Deleloping
- for Pythonista in Global support events organizing srvice


## organizer

- lepture
- KJ
- Sting
- Zoom.Quiet

## usage
How to update the site contents

### writing

- fork https://gitcafe.com/CPyUG/PyChina into local
- or becamed https://gitcafe.com/CPyUG member hold the repo. ACL
- cd into content/
- the sub-dir means:
    
    content/
        +- Events       首字母大写的是分类目录 收集对应文章
        +- Volunteer    ...志愿者
        +- _extra       扩展功能文件 e.g robots.txt
        +- _files       站内文件
        +- _images      站内图片
        `- pages        类似 about 的导航栏文档

#### 文章格式
- 标准 Markdown 格式
- 以 .md 为后缀
- 文件名不得使用中文/空格/符号
- 内容模板:

    Title: 中E可以混杂的标题
    Date: 2013-12-09
    Tags: people, shanghai
    Slug: sting-chen
    Author: Zoom.Quiet

- 其中:
    - `Date:` 如果没有将使用文件的系统时间
    - `Tags:` 使用逗号作间隔
    - `Slug:` 是实际输出的页面文件名, 建议全部小写E文, 使用中划线, 不使用特殊符号


### deploy

支持本地调试! 使用 `fabric` 进行管理, 支持的命令:

    Available commands:

        build       编译所有页面
        clean       清除所有页面
        deploy      向主机部署所有页面
        rebuild     重编译所有页面
        reserve     重编译所有页面再启动本地服务
        serve       启动本地服务 localhost:8000


`注意!` 向主机部署,需要有相关权限,并在本地配置好对应 SSH 信息

### design

基于 [pelican-bootstrap3](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3) 深度定制

- 配置: `pelicanconf.py`
- 样式: `_themes/pelican-bootstrap3/`
- 插件: `_plugins/`

## changelog

- 131218 base pelican build and through qiniu.com publish