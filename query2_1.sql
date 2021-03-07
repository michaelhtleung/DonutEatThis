-- SQL Query 2.1:
SELECT DISTINCT c.subklass FROM compounds AS c INNER JOIN compound_synonyms AS cs ON c.id=cs.source_id WHERE cs.synonym LIKE '%dextrose%';
