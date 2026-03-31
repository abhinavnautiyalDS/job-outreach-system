from scripts.contact_selector import select_contacts
from scripts.email_generator import generate_email
from scripts.email_sender import send_email

contacts = select_contacts("data/hr_contacts.csv", n=30)

for index,row in contacts.iterrows():

    body, template_id = generate_email(row["name"], row["company"])

    send_email(
        sender="yourmail@gmail.com",
        password="app_password",
        receiver=row["email"],
        subject="Quick question regarding AI/ML roles",
        body=body
    )
