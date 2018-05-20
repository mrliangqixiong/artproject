#!/usr/bin/env python
#-*- coding:utf-8 -*-
#written by zhouguangyou
#发送邮件(wd_email_check123账号用于内部测试使用，不要用于其他用途)

import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage 
from email.header import Header
import time

sender = 'pythontest666@163.com'
subject = u'api开放平台邮箱验证'
smtpserver = 'smtp.163.com'  #163网易提供给用户的服务器
username = 'liang'
password = 'abc123'

mail_postfix="163.com"

def send_email(receiver, content):
    try:
        #me = username+"<"+username+"@"+mail_postfix+">"
        msg = MIMEText(content, 'html', 'utf-8')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = receiver
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())  
        smtp.quit()
        return True
    except Exception as e:
        print('send_email has error with : ' + str(e))
        return False


def pack_html(receiver, url):
    html_content = u"<html><div>尊敬的用户<font color='#0066FF'>%s</font> 您好！</div><br>" \
                   "<div>感谢您关注我们的平台 ，我们将为您提供最贴心的服务，祝您购物愉快。</div><br>" \
                   "<div>点击以下链接，即可完成邮箱安全验证：</div><br>"  \
                   "<div><a href='%s'>%s</a></div><br>"  \
                   "<div>为保障您的帐号安全，请在24小时内点击该链接; </div><br>" \
                   "<div>若您没有申请过验证邮箱 ，请您忽略此邮件，由此给您带来的不便请谅解。</div>" \
                   "</html>" % (receiver, url, url)
    html_content = html_content
    return html_content


if __name__ == "__main__":
    url = "http://www.baidu.com"
    receiver = 'pythontest666@163.com'
    #content = pack_html(receiver, url)
    content = 'this is email content. at %s.'%int(time.time())
    send_email(receiver,  content)


