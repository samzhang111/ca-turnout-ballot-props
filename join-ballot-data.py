import pandas as pd

df_req = pd.read_csv('ballot-prop-requirements.csv')
df_count = pd.read_csv('ballot-prop-counts.csv')

buckets = []

for i, row in df_req.iterrows():
    group = df_count[(df_count['Year'] >= row['StartYear']) &
                     (df_count['Year'] <= row['EndYear'])]

    if group['Titled'].sum() == 0:
        continue

    buckets.append([
        row['StartYear'],
        group['Titled'].mean(),
        group['Qualified'].mean(),
        row['Statute'],
        (group['Qualified']/group['Titled']).mean()
        ])

df = pd.DataFrame(buckets, columns=['StartYear', 'MeanTitled', 'MeanQualified',
                                    'StatuteVotesRequired', 'ProportionQualified'])

df.to_csv('ballot-prop-joined-agg.csv', index=False)
