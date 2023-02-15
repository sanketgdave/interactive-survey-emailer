import smtplib
import ssl
from email.message import EmailMessage
import pandas as pd

sender = 'teknas17@gmail.com'
password = 'htbsbecawwjuorag'

#creating a list for receivers
receiver = ['teknasevad@gmail.com']
subject = 'Simple Email in Python'

# Defining a dictionary to store the responses
responses = {}

for email in receiver:
    # Creating a unique URL for each recipient
    yes_url = f"https://.com/yes?email={email}"
    no_url = f"https://.com/no?email={email}"

    # Define the email body with a form
    body = '''
    <h2>Are you interested in receiving text updates?</h2>
    <form method="post" action="https://.com/response">
        <input type="radio" name="response" value="yes" id="yes"><label for="yes">Yes</label>
        <input type="radio" name="response" value="no" id="no"><label for="no">No</label>
        <br><br>
        <input type="submit" value="Submit">
        <input type="hidden" name="email" value="{}">
    </form>
    '''.format(email)

    
    """body = f
    <h2>Are you interested in receiving text updates?</h2>
    <a href="{yes_url}">Yes</a>
    &ensp?;
    <a href="{no_url}">No</a>
    """

    em = EmailMessage()
    em['From'] = sender
    em['To'] = email
    em['Subject'] = subject
    em.set_content(body, subtype='html')

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, email, em.as_string())



# Creating a dataframe to store the responses
df = pd.DataFrame(list(responses.items()), columns=['Email', 'Response'])