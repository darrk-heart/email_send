
import smtplib
import ssl

# Setup port number and server name

smtp_port = 587             # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

email_from = "prospaul999@gmail.com"
email_to = "prospaul999@gmail.com"

pswd = "jlzghssyjhtfbjmd"

# content of message

message = "Dear God please help!!!"

simple_email_context = ssl.create_default_context()


try:
    print("Connecting to server.......")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls(context=simple_email_context)
    TIE_server.login(email_from, pswd)
    print("Connected to server :-)")

    print()
    print(f"Sending email to - {email_to}")
    TIE_server.sendmail(email_from, email_to, message)
    print(f"Email successfully sent to - {email_to}")

except Exception as e:
    print(e)

finally:
    TIE_server.quit()