import pandas as pd
wine_reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip")
country_summary = wine_reviews.groupby('country').agg(
    num_reviews=('country', 'size'),
    avg_points=('points', 'mean'))
# df.sort_values(by=['col1'])
country_summary.sort_values(by=['num_reviews'], inplace=True, ascending=False)
country_summary.rename(columns={'num_reviews': 'count', 'avg_points': 'points'}, inplace=True)
country_summary['points'] = country_summary.points.round(1)
country_summary.reset_index(inplace=True)
print(country_summary.to_string(index=False))
country_summary.to_csv('reviews-per-country.csv', index=False)
reviews_per_country = pd.read_csv('reviews-per-country.csv')
country_summary.to_csv('data/reviews-per-country.csv', index=False)





