-- Ce script utilise la base de données "hbtn_0d_tvshows" pour lister tous les genres de l'émission "Dexter"
SELECT tv_genres.name
FROM tv_show_genres
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name;
