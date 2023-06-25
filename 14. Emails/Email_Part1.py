#it uses SMTP protocol

import smtplib

conn = smtplib.SMTP('smtp.gmail.com' , 587) #define the email server with port number

type (conn)  #now we have connection object

conn.ehlo() #call this to start the connection #ptint to see

conn.starttls() #starts TLS
conn.login('username', 'password')

conn.sendmail('from','to','subject \n\n emailsub')

conn.quit() #disconnect from smtp server

#use app specific password provided by google



