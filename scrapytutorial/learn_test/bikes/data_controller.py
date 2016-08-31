import scrapy_data as sd
import email_controller as sc
import time
import yahoo_search as ys


def send_email():
    subject = "%s" % str(int(round(time.time())))
    content = sd.assemble_content()
    destination = 'soogicspider@yeah.net'
    try:
        sc.send_mail(subject, content, destination)
        print '%s send successfully :)' % subject
        sd.udpate_status(2)
    except Exception, err:
        print err.message


ys.search_and_save()
send_email()