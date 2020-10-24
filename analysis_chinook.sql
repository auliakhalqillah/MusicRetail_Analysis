-- Data can be download on https://www.sqlitetutorial.net/sqlite-sample-database/
.mode csv
.header on
.output music_retail.csv

-- Read table of artists, albums, tracks, genres, invoices_items, invoices and customers
-- .width 15, 30 30
select artists.Name as ArtistName, albums.Title, tracks.Composer as ComposerName, genres.Name, tracks.Milliseconds, invoice_items.UnitPrice, invoice_items.Quantity, invoices.InvoiceDate, customers.FirstName, customers.LastName, customers.Country
from albums
inner join artists
on artists.ArtistId = albums.ArtistId
inner join tracks
on albums.AlbumId = tracks.AlbumId
inner join invoice_items
on tracks.TrackId = invoice_items.TrackId
inner join invoices
on invoice_items.InvoiceId = invoices.InvoiceId
inner join customers
on invoices.CustomerId = customers.CustomerId
inner join genres
on tracks.GenreId = genres.GenreId
;
