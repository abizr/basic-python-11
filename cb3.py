import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(host, port, user, pwd, recipients, subject, body, html=None, from_=None):
    """ copied and adapted from
        /programming/10147455/how-to-send-an-email-with-gmail-as-provider-using-python#12424439
    returns None if all ok, but if problem then returns exception object
    """

    PORT_LIST = (25, 587, 465)

    FROM = from_ if from_ else user 
    TO = recipients if isinstance(recipients, (list, tuple)) else [recipients]
    SUBJECT = subject
    TEXT = body.encode("utf8") if isinstance(body) else body
    HTML = html.encode("utf8") if isinstance(html) else html

    if not html:
        # Prepare actual message
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    else:
                # /programming/882712/sending-html-email-using-python#882770
        msg = MIMEMultipart('alternative')
        msg['Subject'] = SUBJECT
        msg['From'] = FROM
        msg['To'] = ", ".join(TO)

        # Record the MIME types of both parts - text/plain and text/html.
        # utf-8 -> /programming/5910104/python-how-to-send-utf-8-e-mail#5910530
        part1 = MIMEText(TEXT, 'plain', "utf-8")
        part2 = MIMEText(HTML, 'html', "utf-8")

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)

        message = msg.as_string()


    try:
        if port not in PORT_LIST: 
            raise Exception("Port %s not one of %s" % (port, PORT_LIST))

        if port in (465,):
            server = smtplib.SMTP_SSL(host, port)
        else:
            server = smtplib.SMTP(host, port)

        # optional
        server.ehlo()

        if port in (587,): 
            server.starttls()

        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        # logger.info("SENT_EMAIL to %s: %s" % (recipients, subject))
    except Exception. ex :
        return

    return None