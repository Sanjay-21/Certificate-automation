import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

df=pd.read_csv("NAME.csv")  #file containing participants' details
email = 'example@gmail.com' #sender's mail id
password = input("Enter the password")  
for i in range(9):
    print(df.iloc[i,0].rstrip())
    send_to_email = df.iloc[i,4]    #receiver's mail id
    subject = 'Sending Email with an attachment'
    message = 'Please find the attachment to email, thanks'
    file_location = "./certificates/"+df.iloc[i,0].rstrip()+".jpg"


    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    # Setup the attachment
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # Attach the attachment to the MIMEMultipart object
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()