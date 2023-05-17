from nicegui import app, ui, Client
from pathlib import Path
import http.server
import socketserver
import multiprocessing
import time
import os
import json
import socket

CONFIG = None
CONFIG_FILE = "../config.json"
CF_NICEGUI_PORT = "nicegui_port"
CF_DOMAIN = "domain"

# postgres
CF_PG15_PORT = "pg15port"
CF_PG15_PORT_WEB = "pg15portweb"
CF_PG15_PORT_READWRITE = "pg15portreadwrite"
CF_PG15_PORT_WEB_READWRITE = "pg15portwebreadwrite"
CF_PG15_PORT_READONLY = "pg15portreadonly"
CF_PG15_PORT_WEB_READONLY = "pg15portwebreadonly"

CF_PG14_PORT = "pg14port"
CF_PG14_PORT_WEB = "pg14portweb"
CF_PG14_PORT_READWRITE = "pg14portreadwrite"
CF_PG14_PORT_WEB_READWRITE = "pg14portwebreadwrite"
CF_PG14_PORT_READONLY = "pg14portreadonly"
CF_PG14_PORT_WEB_READONLY = "pg14portwebreadonly"

CF_PG13_PORT = "pg13port"
CF_PG13_PORT_WEB = "pg13portweb"
CF_PG13_PORT_READWRITE = "pg13portreadwrite"
CF_PG13_PORT_WEB_READWRITE = "pg13portwebreadwrite"
CF_PG13_PORT_READONLY = "pg13portreadonly"
CF_PG13_PORT_WEB_READONLY = "pg13portwebreadonly"

CF_PG12_PORT = "pg12port"
CF_PG12_PORT_WEB = "pg12portweb"
CF_PG12_PORT_READWRITE = "pg12portreadwrite"
CF_PG12_PORT_WEB_READWRITE = "pg12portwebreadwrite"
CF_PG12_PORT_READONLY = "pg12portreadonly"
CF_PG12_PORT_WEB_READONLY = "pg12portwebreadonly"

# ubuntu
CF_UBUNTU_2004_PORT_WEB = "ubuntu2004webport"
CF_UBUNTU_2204_PORT_WEB = "ubuntu2204webport"

# arch
CF_ARCH_LATEST_PORT_WEB = "archlatestwebport"

# ch
CF_CH_21_3_20_PORT_WEB = "ch_21_3_20webport"
CF_CH_21_3_20_PORT_TCP = "ch_21_3_20porttcp"
CF_CH_21_3_20_PORT_HTTP = "ch_21_3_20porthttp"

# citus
CF_CITUS_PG15_CN_PORT =	"citus_pg15_cn_port"
CF_CITUS_PG15_CN_PORT_WEB =	"citus_pg15_cn_webport"
CF_CITUS_PG15_DN1_PORT =	"citus_pg15_dn1_port"
CF_CITUS_PG15_DN1_PORT_WEB =	"citus_pg15_dn1_webport"
CF_CITUS_PG15_DN2_PORT =	"citus_pg15_dn2_port"
CF_CITUS_PG15_DN2_PORT_WEB =	"citus_pg15_dn2_webport"

# k8s
CF_K8S_PORT_WEB = "k8sportweb"

# other
INTRODUCE = '''# 半字节

**4比特=半字节**是一个可以在线使用**PostgreSQL Citus Clickhouse K8S Arch Ubuntu**等多种服务在线网站, 仅需点击 **两次鼠标** 即可达到所需服务，并由**青云科技**提供计算服务



## 青云科技

北京青云科技股份有限公司（简称：青云科技），是一家技术领先的企业级云服务商与数字化解决方案提供商。

自 2012 年创立以来，坚持核心代码自研，以顶尖的技术实力见长，构建起端到端的数字化解决方案，持续打造云原生最佳实践，以中国科技服务数字中国。

青云科技最早布局混合云市场，无缝打通公有云和私有云，交付一致功能与体验的混合云，并于 2021 年 3 月登陆上交所科创板，成为“混合云第一股”。



青云科技坚持自主创新、中立可靠、灵活开放的理念，立足企业现实需求，围绕“私有云、公有云、云原生、信创”四大核心业务线，帮助企业构筑坚实的数字基石，实现全场景自由计算，为数字化创新添加“云动力”。

[查看更多青云科技](https://www.qingcloud.com)



## 开发者信息

张连壮 <lianzhuangzhang@yunify.com> 微信: 18910500207

颜博 <jerryyan@yunify.com> 微信：18792653266



## 提示

本网站数据为共享模式，数据将于每周一凌晨5点进行一次清零。

如何你有引入其他服务的需求可以通过邮箱/微信联系我们。



## 目标

打造在线服务全功能平台

提供高效的学习工作测试的平台 '''

def get_config():
    global CONFIG
    CONFIG = read_json_file(CONFIG_FILE)

def read_json_file(filepath):
    ret = None
    try:
        if os.path.isfile(filepath):
            f = open(filepath, "r")
            read_buf = f.read()
            f.close()
            ret = json.loads(read_buf)
        return ret
    except Exception as e:
        print("load json failed: %s" % e)
        exit(1)

def get_html(portweb):
    ht=f'<iframe height=600 width=800 src="http://{CONFIG[CF_DOMAIN]}:{portweb}"></iframe>'
    return ht

get_config()

def add_head():
    # baidu
    ui.add_head_html('<meta name="baidu-site-verification" content="codeva-I7AxdLw3ny" />')
    # bing
    ui.add_head_html('<meta name="msvalidate.01" content="5D84CEB38F10AD8E25481AEC17CF252B" />')
    # google
    ui.add_head_html('<meta name="google-site-verification" content="yNlFqQ4ehwapHJNZVMpNJgH3Ab1i5q_-5VlkqPg1KFI" />')


@ui.page('/')
async def homepage():
    add_head()

    with ui.tabs() as tabs:
        ui.tab('Home', icon='home')
        ui.tab('PostgreSQL', icon='img:images/pg_icon.png')
        ui.tab('Citus', icon='img:images/citus_icon.png')
        ui.tab('ClickHouse', icon='img:images/ch_icon.png')
        ui.tab('K8s', icon='img:images/k8s_icon.png')
        ui.tab('ArchLinux', icon='img:images/arch_icon.png')
        ui.tab('Ubuntu', icon='img:images/ubuntu_icon.png')

    with ui.tab_panels(tabs, value='Home'):
        with ui.tab_panel('Home'):
            ui.image('images/bits.png')
            ui.markdown(INTRODUCE)

        with ui.tab_panel('PostgreSQL'):
            pg15='pg15'
            pg14='pg14'
            pg13='pg13'
            pg12='pg12'
            primary='primary'
            standby='standby'
            single='single'

            ui.label('This is the PostgreSQL server')
            ui.label('support PostgreSQL version : 12.12 13.8 14.5 15.0')
            ui.label('support PostgreSQL architecture：%s-单机  %s-高可用写节点 %s-高可用读节点' % (single, primary, standby))
            pgversion = ui.radio([pg12, pg13, pg14, pg15], value=pg15).props('inline')
            pgrole = ui.radio([primary, standby, single], value=single).props('inline')

            @ui.page('/postgres')
            async def postgres_page():
                ui.label('Welcome to PostgreSQL world. This is %s node' % (pgrole.value))
                if pgversion.value == pg15:
                    if pgrole.value == single:
                        pgport = CONFIG[CF_PG15_PORT]
                        pgportweb = CONFIG[CF_PG15_PORT_WEB]
                    if pgrole.value == primary:
                        pgport = CONFIG[CF_PG15_PORT_READWRITE]
                        pgportweb = CONFIG[CF_PG15_PORT_WEB_READWRITE]
                    if pgrole.value == standby:
                        pgport = CONFIG[CF_PG15_PORT_READONLY]
                        pgportweb = CONFIG[CF_PG15_PORT_WEB_READONLY]
                if pgversion.value == pg14:
                    if pgrole.value == single:
                        pgport = CONFIG[CF_PG14_PORT]
                        pgportweb = CONFIG[CF_PG14_PORT_WEB]
                    if pgrole.value == primary:
                        pgport = CONFIG[CF_PG14_PORT_READWRITE]
                        pgportweb = CONFIG[CF_PG14_PORT_WEB_READWRITE]
                    if pgrole.value == standby:
                        pgport = CONFIG[CF_PG14_PORT_READONLY]
                        pgportweb = CONFIG[CF_PG14_PORT_WEB_READONLY]
                if pgversion.value == pg13:
                    if pgrole.value == single:
                        pgport = CONFIG[CF_PG13_PORT]
                        pgportweb = CONFIG[CF_PG13_PORT_WEB]
                    if pgrole.value == primary:
                        pgport = CONFIG[CF_PG13_PORT_READWRITE]
                        pgportweb = CONFIG[CF_PG13_PORT_WEB_READWRITE]
                    if pgrole.value == standby:
                        pgport = CONFIG[CF_PG13_PORT_READONLY]
                        pgportweb = CONFIG[CF_PG13_PORT_WEB_READONLY]
                if pgversion.value == pg12:
                    if pgrole.value == single:
                        pgport = CONFIG[CF_PG12_PORT]
                        pgportweb = CONFIG[CF_PG12_PORT_WEB]
                    if pgrole.value == primary:
                        pgport = CONFIG[CF_PG12_PORT_READWRITE]
                        pgportweb = CONFIG[CF_PG12_PORT_WEB_READWRITE]
                    if pgrole.value == standby:
                        pgport = CONFIG[CF_PG12_PORT_READONLY]
                        pgportweb = CONFIG[CF_PG12_PORT_WEB_READONLY]
                ui.label(f'you can connect PostgreSQL by client:')
                ui.label(f"1, create user on this page: create user lzzhang password 'password' superuser;")
                ui.label(f"2, connect with the user: PGPASSWORD=password psql -U lzzhang -d postgres -h {CONFIG[CF_DOMAIN]} -p {pgport}")
                ui.html(get_html(pgportweb))
                ui.button('返回首页', on_click=lambda: ui.open('/'))

            ui.button('打开', on_click=lambda: ui.open(postgres_page))

        with ui.tab_panel('Ubuntu'):
            ubuntu2004='20.04'
            ubuntu2204='22.04'

            ui.label('This is the Ubuntu server')
            ui.label('support Ubuntu version : 20.04 22.04')
            ubuntuversion = ui.radio([ubuntu2004, ubuntu2204], value=ubuntu2204).props('inline')

            @ui.page('/ubuntu')
            async def ubuntu_page():
                ui.label('Welcome to Ubuntu world. This version is %s ' % (ubuntuversion.value))
                if ubuntuversion.value == ubuntu2004:
                    ubuntuportweb = CONFIG[CF_UBUNTU_2004_PORT_WEB]
                if ubuntuversion.value == ubuntu2204:
                    ubuntuportweb = CONFIG[CF_UBUNTU_2204_PORT_WEB]
                ui.label(f'The ssh mode is not enabled for security reasons.')
                ui.html(get_html(ubuntuportweb))
                ui.button('返回首页', on_click=lambda: ui.open('/'))

            ui.button('打开', on_click=lambda: ui.open(ubuntu_page))

        with ui.tab_panel('ArchLinux'):
            archlatest='latest'

            ui.label('This is the ArchLinux server')
            ui.label('support ArchLinux version: latest')
            archversion = ui.radio([archlatest], value=archlatest).props('inline')

            @ui.page('/arch')
            async def arch_page():
                ui.label('Welcome to ArchLinux world. This version is %s ' % (archversion.value))
                if archversion.value == archlatest:
                    archportweb = CONFIG[CF_ARCH_LATEST_PORT_WEB]
                ui.label(f'The ssh mode is not enabled for security reasons.')
                ui.html(get_html(archportweb))
                ui.button('返回首页', on_click=lambda: ui.open('/'))

            ui.button('打开', on_click=lambda: ui.open(arch_page))


        with ui.tab_panel('ClickHouse'):
            ch21_3_20='21.3.20'

            ui.label('This is the ClickHouse server')
            ui.label('support ClickHouse version: 21.3.20')
            chversion = ui.radio([ch21_3_20], value=ch21_3_20).props('inline')

            @ui.page('/clickhouse')
            async def ch_page():
                ui.label('Welcome to ClickHouse world. This version is %s ' % (chversion.value))
                if chversion.value == ch21_3_20:
                    chportweb = CONFIG[CF_CH_21_3_20_PORT_WEB]
                ui.label(f'you can connect ClickHouse by client:')
                ui.label(f"1, create user on this page: CREATE USER lzzhang IDENTIFIED WITH plaintext_password BY 'password'")
                ui.label(f"2, grant permission on this page: grant create on *.* to lzzhang")
                ui.label(f"3, connect with the user: clickhouse-client -h {CONFIG[CF_DOMAIN]} --port {CONFIG[CF_CH_21_3_20_PORT_TCP]} -u lzzhang --password password  (http port: {CONFIG[CF_CH_21_3_20_PORT_HTTP]})")
                ui.html(get_html(chportweb))
                ui.button('返回首页', on_click=lambda: ui.open('/'))

            ui.button('打开', on_click=lambda: ui.open(ch_page))

        with ui.tab_panel('Citus'):
            citus_pg15 = 'pg15'
            citus_cn = 'cn'
            citus_dn1 = 'dn1'
            citus_dn2 = 'dn2'

            ui.label('This is the Citus server')
            ui.label('support Citus version: pg15-v11.1.3')
            ui.label('support Citus architecture：%s-协调器  %s-数据节点 %s-数据节点' % (citus_cn, citus_dn1, citus_dn2))
            citusversion = ui.radio([citus_pg15], value=citus_pg15).props('inline')
            citusrole = ui.radio([citus_cn, citus_dn1, citus_dn2], value=citus_cn).props('inline')

            @ui.page('/citus')
            async def citus_page():
                ui.label('Welcome to Citus world. This role is %s ' % (citusrole.value))
                if citusversion.value == citus_pg15:
                    if citusrole.value == citus_cn:
                        citus_port = CONFIG[CF_CITUS_PG15_CN_PORT]
                        citus_port_web = CONFIG[CF_CITUS_PG15_CN_PORT_WEB]
                    if citusrole.value == citus_dn1:
                        citus_port = CONFIG[CF_CITUS_PG15_DN1_PORT]
                        citus_port_web = CONFIG[CF_CITUS_PG15_DN1_PORT_WEB]
                    if citusrole.value == citus_dn2:
                        citus_port = CONFIG[CF_CITUS_PG15_DN2_PORT]
                        citus_port_web = CONFIG[CF_CITUS_PG15_DN2_PORT_WEB]
                ui.label(f'you can connect citus by client:')
                ui.label(f"1, create user on this page(must on cn): create user lzzhang password 'password' superuser;")
                ui.label(f"2, connect with the user: PGPASSWORD=password psql -U lzzhang -d postgres -h {CONFIG[CF_DOMAIN]} -p {citus_port}")
                ui.html(get_html(citus_port_web))
                ui.button('返回首页', on_click=lambda: ui.open('/'))

            ui.button('打开', on_click=lambda: ui.open(citus_page))
        with ui.tab_panel('K8s'):
            k8s_1_21 = 'v1.21.0'

            ui.label('This is the k8s server')
            ui.label('support k8s version: v.1.21.0')
            k8sversion = ui.radio([k8s_1_21], value=k8s_1_21).props('inline')

            @ui.page('/k8s')
            async def k8s_page():
                ui.label('Welcome to k8s world. This version is %s ' % (k8sversion.value))
                if k8sversion.value == k8s_1_21:
                    portweb = CONFIG[CF_K8S_PORT_WEB]
                ui.html(get_html(portweb))
                ui.button('返回首页', on_click=lambda: ui.open('/'))

            ui.button('打开', on_click=lambda: ui.open(k8s_page))

# add static files
folder = Path(__file__).resolve().parent / 'images'
app.add_static_files('/images', folder)

# run
ui.run(favicon='images/title.jpg', title='半字节 在线服务', port=int(CONFIG[CF_NICEGUI_PORT]))
