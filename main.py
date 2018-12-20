# Author - Ruturaj Kiran Vaidya

# Requirement - pandas
import pandas as pd
import sys


def main():
    try:
        fileName = sys.argv[1]
    except IndexError:
        print("Usage: package inputfile")
        sys.exit()
    # read CSV
    try:
        r = pd.read_csv(fileName)
    except FileNotFoundError:
        print("No such file!")
        sys.exit()
    except:
        print("Check your file!")
        sys.exit()
    # Print it as a json
    # It is that simple!
    r.to_json(fileName+".json", orient='records')

if __name__=="__main__":
    main()
