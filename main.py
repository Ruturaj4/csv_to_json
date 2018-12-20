# Author - Ruturaj Kiran Vaidya

import pandas as pd
import sys


def main():
    try:
        fileName = sys.argv[1]
    except IndexError:
        print("Usage: packagename inputfile")
    # read CSV
    r = pd.read_csv(fileName)
    # Print it as a json
    # It is that simple!
    r.to_json(fileName+".json", orient='records')

if __name__=="__main__":
    main()
