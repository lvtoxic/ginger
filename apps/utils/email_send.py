# coding=utf-8
from random import Random

from users.models import EmailVerifyRecord
from line.settings import EMAIL_FROM
from django.core.mail import send_mail


def random_str(randomlength=8):
    str = ''
    chars = 'zxcvbnmasdfghjklqwertyuiop1234567890'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '注册激活连接'
        email_body = '点击下列激活http://127.0.0.1:8000/activer/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

    elif send_type == 'forget':
        email_title = '密码重置连接'
        email_body = '点击下列重置密码http://127.0.0.1:8000/reset/{0}'.format(code)
