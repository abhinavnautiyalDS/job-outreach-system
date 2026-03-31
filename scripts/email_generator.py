def generate_email(name, company, template_path):

    with open(template_path, "r") as f:
        template = f.read()

    template = template.replace("{name}", name)
    template = template.replace("{company}", company)

    return template

email = generate_email("Rahul","ABC Tech","templates/template_ml.txt")
print(email)