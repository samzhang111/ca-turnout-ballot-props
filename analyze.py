import pandas as pd
from scipy import stats

df = pd.read_csv('ballot-prop-joined-agg.csv')

#gradient, intercept, r_value, p_value, std_err = stats.linregress(

print stats.linregress(
    df.StatueVotesRequired,
    df.ProportionQualified
)

