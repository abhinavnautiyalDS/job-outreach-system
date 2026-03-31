import pandas as pd

def select_contacts(file_path, n=30):

    df = pd.read_csv(file_path)

    selected = df.sample(n=n)

    return selected
