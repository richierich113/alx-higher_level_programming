-- a sript that Lists all genres from the database hbtn_0d_tvshows along with the number of
-- shows linked to each.
-- Does not display genres without linked shows.
-- Records are ordered by descending number of shows linked.
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows FROM tv_show_genres
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre
ORDER BY number_of_shows DESC;
