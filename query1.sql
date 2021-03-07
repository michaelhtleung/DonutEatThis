-- SQL Query 1:
SELECT DISTINCT c.name FROM compounds AS c INNER JOIN compound_synonyms AS cs ON c.id=cs.source_id WHERE cs.synonym LIKE '%dextrose%';

-- SELECT c.id FROM compounds AS c INNER JOIN compound_synonyms AS cs ON c.id=cs.id;

-- SELECT c.id, c.name FROM compounds AS c INNER JOIN compound_synonyms AS cs ON c.id=cs.id WHERE cs.synonym LIKE '%dextrose%';


-- SELECT DISTINCT c.id, c.name, c.superklass, c.klass, c.subklass FROM compounds AS c INNER JOIN compound_synonyms AS cs ON c.id=cs.source_id WHERE cs.synonym LIKE '%dextrose%';

-- select * from information_schema.columns where table_schema = 'foodb' order by table_name,ordinal_position;

-- select COLUMN_NAME, TABLE_NAME from information_schema.columns where table_schema = 'foodb' order by column_name, table_name;
