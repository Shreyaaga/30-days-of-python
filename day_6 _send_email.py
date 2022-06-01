import smtplib
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("shreya2003agarwal@gmail.com","Shreya@2003")
server.sendmail("shreya2003agarwal@gmail.com","preeti7078972758@gmail.com","hey mamma")
server.quit()
