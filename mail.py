import smtplib
import os
def send_email(word):
    #It sends me an email consisting of the word to be included. 
    sender_email =  os.getenv("email") 
    app_password = os.getenv("key")
    recipient_email = os.getenv("email") 
    
    subject = "Word to be included "    
    email_message = f"Subject: {subject}\n\n{word}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, recipient_email, email_message)
        server.quit()
        print("Message sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
