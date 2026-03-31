import pandas as pd
from datetime import datetime, timedelta

def check_followups(file):

    df = pd.read_csv(file)

    today = datetime.today()

    for i,row in df.iterrows():

        sent_date = datetime.strptime(row["date"], "%Y-%m-%d")

        if (today - sent_date).days >= 5 and row["status"]=="sent":

            print("Send follow up to:",row["email"])
