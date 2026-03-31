import pandas as pd

def select_contacts(n=30):

    df = pd.read_csv("data/hr_contacts.csv")

    # Randomly select n contacts
    selected = df.sample(n)

    return selected


# ---------- TEST BLOCK ----------
if __name__ == "__main__":

    contacts = select_contacts(5)

    print("Selected HR Contacts:")
    print(contacts)