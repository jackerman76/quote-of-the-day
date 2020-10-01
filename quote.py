import pandas as pd
import smtplib, ssl
import config


def get_quote_of_day():
    dfs = pd.read_html("https://en.wikiquote.org/wiki/Main_Page")
    df = dfs[2]
    message = df.loc[0].at[0]
    return message


def send_message():
    for recipient in config.recipients:
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = config.sender_email  # Enter your address
        receiver_email = recipient  # Enter receiver address
        password = config.password
        subject = "Quote of the Day"

        #message = get_quote_of_day()
        quote = get_quote_of_day()

        message = 'Subject: {}\n\n{}'.format(subject, quote)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message, subject)


def main():
    send_message()

if __name__ == '__main__':
    main()
