#!/usr/bin/env python  
# encoding: utf-8  

from __future__ import absolute_import
import time
from celery.utils.log import get_task_logger

from artproject.celery import app
from art.utils.send_mail import send_email, pack_html


@app.task
def add(x, y):
	return x+y


@app.task
def tsend_email():
	url = "http://www.baidu.com"
	receiver = 'pythontest666@163.com'
	content = pack_html(url, receiver)
	send_email(receiver, content)
	print('tsend_email ok.')
	return True




