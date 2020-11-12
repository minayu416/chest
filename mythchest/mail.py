import os

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

base_dir = os.path.abspath(os.path.dirname(__file__))


class MailSender(object):

    def __init__(self):
        self.sender = ""

        # recipients = ["sample@email.com", "sample@email.com"]
        self.recipients = []
        self.web_server = ""
        self.msg = MIMEMultipart()
        self.subject = ""
        self.text = ""

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
        # TODO logger: f"Message length is {len(self.msg.as_string())}"

        server = smtplib.SMTP(self.web_server)
        server.set_debuglevel(1)
        server.sendmail(self.sender, self.recipients, self.msg.as_string())
        server.quit()
