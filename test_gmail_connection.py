import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('jibinjjohny11@gmail.com', 'ovozyjhcksgsixrz')
    print("Connected to Gmail successfully.")
except Exception as e:
    print(f"Failed to connect to Gmail: {e}")
finally:
    server.quit()
