-- Ce script répertorie toutes les émissions sans le genre "Comédie" dans la base de données "hbtn_0d_tvshows"
SELECT sh.title
FROM tv_shows AS sh
WHERE sh.title NOT IN
(
	    SELECT sh.title
	    FROM tv_shows AS sh
	    INNER JOIN tv_show_genres AS sg
	    ON sh.id = sg.show_id
	    INNER JOIN tv_genres AS ge
	    ON ge.id = sg.genre_id
	    WHERE ge.name = 'Comedy'
)
ORDER BY sh.title;
