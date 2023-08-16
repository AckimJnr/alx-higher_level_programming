-- select from cities

SELECT id, name FROM cities
WHERE id =(
    SELECT id FROM states
    WHERE name = 'California'
);
