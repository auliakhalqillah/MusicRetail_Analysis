# Music Retail Analysis
## Introduction
A analysis of music retail has been conducted. This data was downloaded on [SQL Tutorial website](https://www.sqlitetutorial.net/sqlite-sample-database/). Before analysis data is applied, the data is collected from few tables of SQL file, there are artists, albums, tracks, genres, invoice_items, invoices and customers. By these tables, the data have 11 columns and 2240 rows, where the columns are 
1. ArtistName
2. Title
3. ComposerName
4. Name (Genre)
5. Milliseconds
6. UnitPrice
7. Quantity
8. InvoiceDate
9. First Name
10. Last Name
11. Country

## Overview
Data cleaning has been applied. By 596 data are missing data in ComposerName column. Then, these missing data was replaced by 'unknown'. In general, by 165 artists, 573 composers, 24 genres, and 24 customer countries are collected in last 4 years, from 2009-01-01 to 2013-12-22.

## Report
### Based on Artist Name
Iron Maiden is the highest number of song purchased in last 4 years. U2, Metallica, Led Zeppelin, and Deep Purple are following behind.
![fig1](https://github.com/auliakhalqillah/MusicRetail_Analysis/blob/main/1_Top_10_Artists_in_Last_4_Years.png)
### Based on Title of Song
The 'Minha Historia' is the highest number of song purchased. This song is presented by Chico Buarque
![fig2](https://github.com/auliakhalqillah/MusicRetail_Analysis/blob/main/2_Top_10_Title_in_Last_4_Years.png)

```
The highest number based on artists name and song title are not directly correlate. It means, the customers purchased the song of Iron Maiden more variety than the song of Chico Buarque
```
### Based on Quantity(Revenue)
In last 4 years, this music retail earns revenue of $2.328,6, where in 2010 is the highest revenue. Unfortunately, the revenue is decreased in last one year (2012-2013).
![fig3](https://github.com/auliakhalqillah/MusicRetail_Analysis/blob/main/3_Quantity_of_Song_Purchase_in_Last_4_Years.png)
![fig4](https://github.com/auliakhalqillah/MusicRetail_Analysis/blob/main/6_Total_Revenue.png)

### Overall
Overall, the most genre that was purchased last 4 years is Rock and the most customer country that was purchased come from USA.
![gig5](https://github.com/auliakhalqillah/MusicRetail_Analysis/blob/main/7_Top_10_Genre_in_Last_4_Years.png)
![fig6](https://github.com/auliakhalqillah/MusicRetail_Analysis/blob/main/5_Number_of_Customers_in_Last_4_Years.png)

Although the revenue decreased, the Rock genre still on the first chart in last one year
![fig7](https://github.com/auliakhalqillah/MusicRetail_Analysis/blob/main/4_Top_10_Genre_in_One_Last_Year.png)

# Note
Run SQL script through terminal
```
sqlite3 chinook.db < analysis_chinook.sql
```

