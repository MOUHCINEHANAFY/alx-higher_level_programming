--Task 8 comment to be updated
SELECT id, name FROM cities
WHERE state_id = (
	SELECT id FROM states
	WHERE name = 'California'
) ORDER BY cities.id ASC;
