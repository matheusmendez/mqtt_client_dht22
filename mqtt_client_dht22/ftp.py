import ftplib

# send backup to FTP server
session = ftplib.FTP('IP_FTP', 'USER_FTP', 'PASSWORD_FTP')
file = open('database.sql', 'rb')
session.storebinary('STOR database.sql', file)
file.close()
session.quit()
