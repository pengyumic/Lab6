import time
import threading

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class send_email(threading.Thread):
    def __init__(self, search_obj, sender, mail_pass):        
        threading.Thread.__init__(self)
        self.one_search_list = {} #key: pk, value: (list of courses, email)
        self.search = search_obj
        self.sender = sender
        self.mail_pass = mail_pass
        self.title = "course available"
        

    def run(self):
        while True:
            while len(self.one_search_list) == 0:
                time.sleep(5)
            self.loops()
            time.sleep(5)
                
    def loops(self):
        need_delete = []
        content = ""
        for k, v in self.one_search_list.items():
            cs = v[0]
            has_seats = self.search.get_tables(cs)
            if len(has_seats) > 0:                
                need_delete.append(k)
                for i in has_seats:
                    content += cs[i].email_format()+'\n'
                self.send_email(self.title, content, v[1])                
        for k in need_delete:
            self.one_search_list.pop(k, None)
            
        
    def add_one_search(self, pk, courses, email):        
        self.one_search_list[pk] = (courses, email)

    def send_email(self, title, content, receiver):         
        fromaddr = self.sender
        toaddr = receiver
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = title

        body = content
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, self.mail_pass)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
