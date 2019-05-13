#coding=utf-8

from email.header import Header
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import urllib3
import socks
import socket

def send_mail(file_new):
    # proxy_handler = urllib3.ProxyHandler({'http': '121.193.143.249:80'})
    # opener = urllib3.build_opener(proxy_handler)
    # r = opener.open('http://httpbin.org/ip')
    # print(r.read())
    #
    # urllib3.install_opener(opener)
    # r = urllib3.urlopen('http://httpbin.org/ip')
    # print(r.read())

    # socks.set_default_proxy(socks.HTTP, '10.4.200.21', 18765, True, "ngcrm_xubo", "xcv.2134")
    # socket.socket = socks.socksocket

    f = open(file_new,'rb')
    #读取测试报告正文
    print(file_new)
    mail_body = f.read()

    f.close()
    # 发送邮箱服务器
    host = 'smtp.qq.com'  # 设置发件服务器地址
    port = 25  # 设置发件服务器端口号。注意，这里有SSL和非SSL两种形式
    sender = '729149188@qq.com'  # 设置发件邮箱，一定要自己注册的邮箱
    pwd = 'yqwtcwwaqgmkbech'  # 设置发件邮箱的密码，等会登陆会用到，需要在邮箱设置允许端口调用
    #receiver = ['niugf@inspur.com','wang.f@inspur.com','zmsup@foxmail.com','daixy@inspur.com','liu.ke@inspur.com','1311348325@qq.com']  # 设置邮件接收人,，可以是扣扣邮箱
    receiver = ['niugf@inspur.com']

    #通过  模块构造的带附件的邮件如图
    msg = MIMEMultipart()
    #发送正文
    #Header()用于定义邮件标题
    text = MIMEText(mail_body, 'html', 'utf-8')
    text['Subject'] = Header('自动化测试报告', 'utf-8')
    msg.attach(text)
    # 编写html类型的邮件正文，MIMEtext()用于定义邮件正文
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    msg_file = MIMEText(mail_body, 'html', 'utf-8')
    msg_file['Content-Type'] = 'application/octet-stream'
    msg_file["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    msg.attach(msg_file)

    msg['from'] =sender  # 发送邮件的人
    #msg['to'] =','.join(receiver)
    msg['to'] ='niugf@inspur.com'

    smtp = smtplib.SMTP(host, port)
    smtp.login(sender, pwd)  # 登录的用户名和密码
    smtp.sendmail(sender,msg['to'].split(','),msg.as_string())  # 发送邮件
    smtp.quit()
    print('sendmail success')


