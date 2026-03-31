import random

templates = {
    "A": "templates/template_ml.txt",
    "B": "templates/template_genai.txt",
    "C": "templates/template_ds.txt"
}

def choose_template():

    key = random.choice(list(templates.keys()))

    return key, templates[key]
