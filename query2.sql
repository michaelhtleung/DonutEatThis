-- SQL Query 2:
-- SELECT DISTINCT c.description FROM compounds AS c INNER JOIN compound_synonyms AS cs ON c.id=cs.source_id WHERE cs.synonym LIKE '%dextrose%';
SELECT DISTINCT c.description FROM compounds AS c INNER JOIN compound_synonyms AS cs ON c.id=cs.source_id WHERE cs.synonym LIKE '%dextrose%' AND (
	c.description LIKE '%fat%' OR 
	c.description LIKE '%oil%' OR 
	c.description LIKE '%sugar%' OR 
	c.description LIKE '%salt%' OR 
	c.description LIKE '%carbohydrate%' OR 
	c.description LIKE '%protein%'
);
