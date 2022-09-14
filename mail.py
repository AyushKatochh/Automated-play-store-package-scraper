import smtplib, ssl


def mail(name,package,version,date):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = ""  # Enter your address
    receiver_email=""  # Enter receiver address
    password = "" #sender mail password
    message = f"""\
    Subject: Version Changed for app:{name}
    
    The version of package:{package} has been updated to {version} on {date}"""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
