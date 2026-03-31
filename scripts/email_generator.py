import random

templates = [
    ("A", "templates/template_A.txt"),
    ("B", "templates/template_B.txt")
]

def generate_email(name, company):

    template_id, path = random.choice(templates)

    with open(path, "r") as f:
        content = f.read()

    content = content.replace("{name}", name)
    content = content.replace("{company}", company)

    return content, template_id
