import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class Email:
    _mail_host = 'smtp.northking.net'
    _mail_addr = '@northking.net'

    def __init__(self):
        self.username = os.environ['OA_USERNAME']
        self.password = os.environ['MAIL_PASSWORD']
        if not self.username or not self.password:
            raise Exception('未读取到邮箱配置')
        self.sender = self.username + self._mail_addr
        self.receivers = []

    def append_receivers(self, mail):
        self.receivers.append(mail)

    def send(self, subject, content, content_type='plain'):
        '''
        send email

        params:
        content\r\n
        content_type [plain|html]
        '''
        message = MIMEText(content, content_type, 'utf-8')
        message['From'] = Header(self.sender, 'utf-8')
        receivers_str = ','.join(self.receivers)
        message['To'] = Header(receivers_str, 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self._mail_host, 587)
            smtpObj.login(self.username, self.password)
            smtpObj.sendmail(self.sender, receivers_str, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("邮件发送失败")


if __name__ == "__main__":
    email = Email()
    email.append_receivers(email.sender)
    with open('weekly_report/weekly_report.log', 'r', encoding='utf-8') as f:
        email.send('Weekly report schedule', f.read())
