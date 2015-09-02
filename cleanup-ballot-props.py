import pandas as pd

data = []

def cleanup(cell):
    try:
        return int(cell)
    except ValueError:
        return 0

with open('_ballot-props-raw.csv', 'r') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 7):
        data.append(map(cleanup, lines[i:i+7]))

df = pd.DataFrame(data, columns=["Year", "Titled", "Qualified", "Approved",
                                 "Rejected", "Failed", "Withdrawn"])

df["ProportionQualified"] = df["Qualified"].astype(float)/df["Titled"]

print df

df.to_csv("ballot-prop-counts.csv", index=False)
