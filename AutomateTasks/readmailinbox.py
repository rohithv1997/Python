import imapclient, pyzmail

connection = imapclient.IMAPClient("imap-mail.outlook.com", port=993, ssl=True)
# change password before git commit
connection.login("rohithv97@outlook.com", Password)
mails = connection.select_folder("Inbox", readonly=True)
messageIds = connection.search([b"SINCE", b"04-Jun-2021"])
print(messageIds)
for id in messageIds:
    rawMessage = connection.fetch([id], ["BODY[]", "FLAGS"])
    message = pyzmail.PyzMessage.factory(rawMessage[id][b"BODY[]"])
    print(message)
print(connection.list_folders())
connection.logout()