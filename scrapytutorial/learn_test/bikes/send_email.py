# coding: utf-8

# Import smtplib for the actual sending function
import smtplib
import sys
import time

# Import the email modules we'll need
from email.mime.text import MIMEText

smtp_server = 'smtp.yeah.net'
# sender = 'scrapy@soogic.com'
sender_name = 'Soogic Spider'
sender = 'soogicspider@yeah.net'
password = 'btis1team'
subtype = 'plain'


def send_mail(subject, content, destination):
    try:
        msg = MIMEText(content, subtype, 'utf-8')
        msg['Subject'] = subject
        msg['From'] = sender  # some SMTP servers will do this automatically, not all
        msg['To'] = destination

        conn = smtplib.SMTP(smtp_server)
        conn.set_debuglevel(False)
        conn.login(sender, password)
        try:
            conn.sendmail(sender, destination, msg.as_string())
        except Exception, exc:
            sys.exit("mail failed; %s" % str(exc))  # give a error message
        finally:
            conn.quit()

    except Exception, exc:
        sys.exit("mail failed; %s" % str(exc))  # give a error message
