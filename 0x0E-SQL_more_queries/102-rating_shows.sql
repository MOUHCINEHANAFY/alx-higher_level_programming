-- Ce script répertorie toutes les émissions de "hbtn_0d_tvshows_rate" selon leur évaluation
SELECT sh.title, SUM(sr.rate) AS rating
FROM tv_shows AS sh
INNER JOIN tv_show_ratings AS sr
ON sh.id = sr.show_id
GROUP BY sh.title
ORDER BY rating DESC;
