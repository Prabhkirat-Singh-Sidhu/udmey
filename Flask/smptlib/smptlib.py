import smtplib

connection = smtplib.SMTP("smtp.gmail.com", 587)

connection.starttls()

connection.login(
    user="you@gmail.com",
    password="wallahabibii"
)

connection.sendmail(
    from_addr="you@gmail.com",
    to_addrs="friend@gmail.com",
    msg="Hello World"
)

connection.quit()  
