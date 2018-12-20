# Author - Ruturaj Kiran Vaidya

# Requirement - pandas
import pandas as pd
import sys


def convert(csv):
    try: 
        r = pd.read_csv(csv)
        r.to_json(csv+".json", orient='records')
        # Print it as a json
        # It is that simple!
    except FileNotFoundError:
        print("No such file!")
    except:
        print("Usage: csv_to_json.convert(filename)")
