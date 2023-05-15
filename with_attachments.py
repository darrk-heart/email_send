
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Setup port number and server name

smtp_port = 587             # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

email_from = "prospaul999@gmail.com"
email_list = ["prospaul999@gmail.com", "emuhiydeen6@gmail.com", "azametthew@gmail.com", "sirgamah1@gmail.com"]


pswd = "jlzghssyjhtfbjmd"

subject = "Sending email with attachments"

def send_emails(email_list):

    for person in email_list:


        body = f"""
         a little python program to send emails with attachments
        
        hope you received it:-)        
        """

        # define parts of the email with a MIMe object

        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))


        #file to attach
        filename = "tadaa.jpg"
        attachment = open(filename, 'rb')

        #encoding as base 64
        attachment_package = MIMEBase('application', 'octet-stream')
        attachment_package.set_payload((attachment). read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('Content-Disposition', "attachment; filename= " +filename)
        msg.attach(attachment_package)

        text = msg.as_string()

        #connection to server
        print("Connecting to server.....")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, pswd)
        print("Successfully connected to server")
        print()


        print(f"Sending email to: {person}...")
        TIE_server.sendmail(email_from, person, text)
        print(f"Email sent to: {person}")
        print()



    TIE_server.quit()

send_emails(email_list)


