import pandas as pd
import json

def generate_stats(log_file):

    df = pd.read_csv(log_file)

    stats = {
        "emails_sent": len(df),
        "template_A": len(df[df["template"]=="A"]),
        "template_B": len(df[df["template"]=="B"])
    }

    with open("dashboard/stats.json","w") as f:
        json.dump(stats,f)
