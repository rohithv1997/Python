import smtplib

connection = smtplib.SMTP("smtp-mail.outlook.com", 587)
connection.ehlo()
connection.starttls()
# change password before git commit
connection.login("rohithv97@outlook.com", Password)
for i in range(100):
    output = connection.sendmail(
        "rohithv97@outlook.com",
        "deepikamukundhan1996@gmail.com",
        "Subject: SMTP Python script\n\n Dear Deepika,\nHow much do you like this mail?\n\n-R"
        + str(i),
    )
