import sys
import pandas as pd

def main():
    df = pd.read_csv(sys.stdin, names=['unixtime', 'value'])
    start = df['unixtime'].iloc[0]
    df['elapsed'] = df['unixtime'] - start
    df[['elapsed', 'value']].to_csv(sys.stdout, float_format="%.6f", index=False, header=False)

if __name__ == "__main__":
    main()
