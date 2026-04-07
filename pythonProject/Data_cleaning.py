import pandas as pd

df = pd.read_csv('amazon.csv')


df['discounted_price'] = pd.to_numeric(df['discounted_price'], errors='coerce')
df['actual_price'] = pd.to_numeric(df['actual_price'], errors='coerce')
df['discount_percentage'] = pd.to_numeric(df['discount_percentage'].astype(str).str.replace("%",'',regex=False).str.strip(), errors='coerce')
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce')


df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df['rating_count'] = pd.to_numeric(
    df['rating_count'].astype(str).str.replace(',', ''),
    errors='coerce'
)


df['rating_bin'] = pd.cut(
    df['rating'],
    bins=[0, 2, 3, 4, 4.5, 5],
    labels=['poor', 'avg', 'good', 'great', 'excellent']
)


df['rating_count'] = df.groupby('rating_bin')['rating_count'].transform(
    lambda x: x.fillna(x.mean())
)


df['rating_count'] = df['rating_count'].fillna(df['rating_count'].mean())
df['rating']=df['rating'].fillna(df['rating'].median())


print(df[['rating', 'rating_bin', 'rating_count']].head(20))
df.to_csv('amazon.csv',index=False)

print(df)
print(df.isnull().sum())
print(df['discount_percentage'])