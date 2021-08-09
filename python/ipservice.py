#! /usr/bin/python

import os
import time
import urllib2
import smtplib
import subprocess
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
from datetime import datetime


def check_in():

    fqn = os.uname()[1]
    tries = 0
    success = False
    ext_ip = ""
    while (success == False and tries < 5):
        try:
            ext_ip = urllib2.urlopen('http://canihazip.com/s').read()
            success = True
        except:
            tries += 1
            logf.write("tries: %d, sleeping for 20 secs\n" % tries)
            time.sleep(20)
                
    return success, fqn, ext_ip

def sendMail(to, fro, subject, text, files=[],server="localhost"):
    assert type(to)==list
    assert type(files)==list
 
 
    msg = MIMEMultipart()
    msg['From'] = fro
    msg['To'] = COMMASPACE.join(to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
 
    msg.attach( MIMEText(text) )
 
    for file in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(file,"rb").read() )
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"'
                       % os.path.basename(file))
        msg.attach(part)
 
    smtp = smtplib.SMTP(server)
    smtp.sendmail(fro, to, msg.as_string() )
    smtp.close()


logf = open('updateip.log', 'a')
tstamp = datetime.now()
logf.write("updateip.py starting at: %s\n" % tstamp)
success, fqn, ext_ip = check_in()

if (not success):
    logf.write("Couldn't get current ip, will try again in 20 mins...\n")
else:
    logf.write("FQN: %s\n" % fqn)
    logf.write("Ext IP: %s\n" % ext_ip)
    filedata = ""
    if (os.path.exists('ipaddr.txt')):
        f = open('ipaddr.txt', 'r')
        filedata = f.read()
        f.close()
    if (str(filedata) == ext_ip):
        logf.write("IP address matches!\n")
    else:
        logf.write("IPs don't match, updating ipaddr.txt...\n")
        f = open('ipaddr.txt', 'w')
        f.write(ext_ip)
        f.close()
        logf.write("...sending mail...\n")
        #sendMail(['_email'],'_email','Hello from %s!' % fqn,'Server external IP address: %s' % ext_ip,[])
        bashCommand = "echo 'Hello' | mail -s 'IP Changed' _email" 
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output = process.communicate()[0]
	logf.write("...all done!\n")
logf.close()
