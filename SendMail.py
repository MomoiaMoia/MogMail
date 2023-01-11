import smtplib
import email.utils
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import sys

from jinja2 import Environment, FileSystemLoader

import configparser


props = configparser.ConfigParser()
props.read("pymail.conf", encoding="utf-8")
message = MIMEMultipart("related")

# 初始化发函信息
message["to"] = email.utils.formataddr((props.get("pymail", "toName"), props.get("pymail", "to")))
message["from"] = email.utils.formataddr((props.get("pymail", "fromName"), props.get("pymail", "from")))
message["subject"] = props.get("pymail", "subject")

msgAlternative = MIMEMultipart("alternative")
message.attach(msgAlternative)

# 处理信函内容
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("MogMail.html")

output = template.render(content=props.get("pymail", "content"), id=props.get("pymail", "id"))
# print(output)

msgAlternative.attach(MIMEText(output, "html"))

fp_1 = open("resources/mail-bg.png", "rb")
fp_2 = open("resources/gray-bg.png", "rb")
fp_3 = open("resources/white-bg1.png", "rb")
fp_4 = open("resources/button-bg1.png", "rb")
fp_5 = open("resources/button-bg2.png", "rb")
fp_list = [fp_1, fp_2, fp_3, fp_4, fp_5]
for i in fp_list:
    fn = "<" + i.__str__().split(" ")[1].split("'")[1].split(".")[0] + ">"
    # print(fn)
    msgImage = MIMEImage(i.read())
    i.close
    msgImage.add_header("Content-ID", fn)
    message.attach(msgImage)

# print(message)

mail = smtplib.SMTP()
mail.connect("smtp.qq.com")
try:
    mail.login(props.get("pymail", "loginmail"), props.get("pymail", "authcode"))
except:
    print(" * 发送失败！请检查授权码是否正确填写。")
    input(" * 按任意键退出...")
    sys.exit()
mail.sendmail(props.get("pymail", "loginmail"), [props.get("pymail", "from"), props.get("pymail", "to")], message.as_string())
print(" * 发送成功！")
input(" * 按任意键退出...")