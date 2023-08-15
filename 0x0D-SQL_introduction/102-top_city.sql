-- select top 3 cities with highest avg temp
-- from july to august
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month in (7, 8)
GROUP BY city
ORDER BY avg_temp DESC limit 3;
