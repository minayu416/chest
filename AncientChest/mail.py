import os

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

base_dir = os.path.abspath(os.path.dirname(__file__))


class MailSender(object):
    """SMTP Mail Sender

    Implement class method for helping send SMTP mail.

        self.sender (str) = "sender@mail.com" # mail sender
        self.recipients (list) = ["sample@email.com", "sample@email.com"] # permit multiple recipients.
        self.web_server (str) = "1x.xx.xxx.xxx" # SMTP web server ip
        self.msg (object) = MIMEMultipart() # init a multi-content message for permitting compose mail content
                                     and attached files.
        self.subject (str) = "" # mail subject
        self.text (str) = "" # mail content, permit html style.

        self.logger (function) = print # customizing log alarm, if None, just print the log.

    """

    def __init__(self):
        self.sender = ""

        self.recipients = []
        self.web_server = ""
        self.msg = MIMEMultipart()
        self.subject = ""
        self.text = ""

        # can customize logger alarm.
        self.logger = print

    # TODO if necessary, developing CC
    def new_msg(self):
        self.msg['Subject'] = self.subject
        self.msg['From'] = self.sender
        self.msg['To'] = ", ".join(self.recipients)
        return self

    def content(self):
        # TODO html or string txt
        content = MIMEText(self.text, "html", "utf-8")
        self.msg.attach(content)
        return self

    def attach(self, file_path, file_name):
        file = os.path.join(file_path, file_name)
        attach1 = MIMEApplication(open(file, 'rb').read())
        attach1.add_header('Content-Disposition', 'attachment', filename=file_name)
        self.msg.attach(attach1)
        return self

    def send(self):
        self.logger(f"Mail length is {len(self.msg.as_string())}")

        server = smtplib.SMTP(self.web_server)
        server.set_debuglevel(1)
        server.sendmail(self.sender, self.recipients, self.msg.as_string())
        server.quit()
