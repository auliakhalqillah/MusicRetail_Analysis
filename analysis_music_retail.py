import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import datetime

df = pd.read_csv('music_retail.csv')
print('[1] INFO')
print(df.info())
print('\n', df.head())

print('\n[2] MISSING DATA')
print(df.isnull().sum())
# Composer Name has missing data, InvoiceData's data type is not datetime

# Replace missing data in Composer Name by unknown
df['ComposerName'].fillna('Unknown', inplace=True)
print('\n[3] CURRENT MISSING DATA')
print(df.isnull().sum())

# Change data type of Invoice Date
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%Y-%m-%d')

# Change column name of Genre Column
df.rename(columns={"Name":"Genre", "Country":"CustomerCountry"}, inplace=True)

# First transaction and Last Transaction
print('\n[4] FIRST TRANSACTION AND LAST TRANSACTION')
first_transaction = df['InvoiceDate'].min()
last_transaction = df['InvoiceDate'].max()
print('First Transaction:', first_transaction)
print('Last Transaction:', last_transaction)
# [4] FIRST TRANSACTION AND LAST TRANSACTION
# First Transaction: 2009-01-01 00:00:00
# Last Transaction: 2013-12-22 00:00:00
# Data in last 4 years

# How many purchased of song by artists name?
print('\n[5] NUMBER PURCHASED OF SONG BY NAME ARTISTS')
print(df['ArtistName'].nunique())

# Number of Composer
print('\n[6] NUMBER OF COMPOSER')
print(df['ComposerName'].nunique())

# Number of Genre
print('\n[7] NUMBER OF GENRE')
print(df['Genre'].nunique())

# How many countries did purchase of song?
print('\n[8] NUMBER OF COUNTRY')
print(df['CustomerCountry'].nunique())
# Based on data, We have 165 song was purchased by artists name, by 24 genres and from 24 countries.

# Group by artists name
group_by_artist = df.groupby('ArtistName').agg({
    'Quantity':sum
    }).sort_values(by='Quantity', ascending=False)
print('\n[9] GROUP BY ARTISTS NAME')
print(group_by_artist)

# Select Top 10 high purchased of song
top_10_artists = group_by_artist.head(10)
print('\n[10] TOP 10 ARTISTS IN LAST 4 YEARS')
print(top_10_artists)
# (F1) Iron Maiden is the high purchased of song in last 4 years.
top_10_artists.plot(kind='bar', legend=None)
plt.xlabel('Artists')
plt.ylabel('Quantity')
plt.title('Top 10 Artists in Last 4 Years')
plt.grid()

# Top 10 title
group_by_title = df.groupby('Title').agg({
    'Quantity':sum
    }).sort_values(by='Quantity', ascending=False)
top_10_title = group_by_title.head(10)
artist_name = df[df['Title'].isin(top_10_title.index)]
print('\n[10a] TOP 10 ARTISTS NAME BASED ON HIGH NUMBER OF TITLE SONG IN LAST 4 YEARS')
print(top_10_title)
print('\n')
print(artist_name.reset_index())
top_10_title.plot(kind='bar', legend=None)
plt.xlabel('Title')
plt.ylabel('Quantity')
plt.title('Top 10 Title in Last 4 Years')
plt.grid()

# CHECK
print(df[df['ArtistName'] == 'Iron Maiden'])
print('\n')
print(df[df['Title'] == 'Minha Historia'])
# The number of title is not directly correlate to number of artits name. 


# Group by invoice date
group_by_invoice_date = df.groupby('InvoiceDate').agg({
    'Quantity':sum
})
print('\n[11] QUANTITY BASED ON INVOICE DATE')
# total_song_year = group_by_invoice_date.resample('Y').sum().sort_values(by='Quantity', ascending=False)
total_song_year = group_by_invoice_date.resample('Y').sum()
total_song_year.index = total_song_year.index.year
print(total_song_year)
# In 2010, by 455 songs was purchased. It is the higher number of purchased in last 4 years.
#  (F2) Plot Quantity of Song Purchase in Last 4 Years
total_song_year.plot(marker='.', legend=None)
plt.xlabel('Year')
plt.ylabel('Quantity')
plt.title('Quantity of Song Purchase in Last 4 Years')
plt.xticks(total_song_year.index, rotation=0)
plt.grid()

# Which genre were high purchase?
group_by_genre = df.groupby('Genre').agg({
    'Quantity':sum
}).sort_values(by='Quantity', ascending=False)
top_10_genre_in_4year = group_by_genre.head(10)
print('\n[12] TOP 10 GENRE BASED ON QUANTITY IN LAST 4 YEARS')
print(top_10_genre_in_4year)
# Genre of rock is the highest purchased song in last 4 years.
top_10_genre_in_4year.plot(kind='bar', figsize=(10,5), legend=None)
plt.ylabel('Quantity')
plt.title('Top 10 Genre in Last 4 Years')
plt.tight_layout()
plt.grid()

# Number of genre in month (in last 1 year)
# genre_in_month = df.groupby(['InvoiceDate','Genre'])['Quantity'].sum()
genre_in_year = df[df['InvoiceDate'] >= '2012-12-22'].groupby('Genre').agg({'Quantity':sum})
top_10_genre_in_year = genre_in_year.sort_values(by='Quantity', ascending=False).head(10)
print('\n[13] TOP 10 GENRE IN LAST ONE YEAR')
print(top_10_genre_in_year)
# (F4) Plot Quantity of Song Purchase Based on Genre in Last One Year
top_10_genre_in_year.plot(kind='bar', figsize=(10,5), legend=None)
# plt.legend(genre_in_year.Quantity.columns, bbox_to_anchor =(1.1, 1), loc='best', ncol=1)
plt.ylabel('Quantity')
plt.title('Top 10 Genre in Last One Year')
plt.tight_layout()
plt.grid()

# Which country was high customers?
group_by_country = df.groupby('CustomerCountry').agg({'Quantity':sum}).sort_values(by='Quantity', ascending=False)
print('\n[14] Quantity of Customer Countries')
print(group_by_country)
# (F5) Plot Number of Country
group_by_country.plot(kind='bar', figsize=(10,5), legend=None)
plt.ylabel('Number of Customers')
plt.title('Number of Customers in Last 4 Years')
plt.tight_layout()
plt.grid()
# USA is the higher number of song purchased

# How much revenue is earned?
df['Revenue'] = df['Quantity'] * df['UnitPrice']
group_by_unitprice = df.groupby('InvoiceDate').agg({'Revenue':sum})
revenue_in_year = group_by_unitprice.resample('Y').sum()
print('\n[15] REVENUE')
print(revenue_in_year)

# (F6) Plot revenue in year
revenue_in_year.plot(marker='.',legend=None)
plt.ylabel('Revennue')
plt.xlabel('Year')
plt.grid()
plt.title('Total Revenue For Each Year')
# InvoiceDate         
# 2009-12-31    449.46
# 2010-12-31    481.45
# 2011-12-31    469.58
# 2012-12-31    477.53
# 2013-12-31    450.58
# In 2011 is the highest revenue in last 4 years

# Head data
print('\n[FINAL] CURRENT DATA')
print(df.head())

plt.show()
