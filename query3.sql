-- SQL Query 3:
SELECT DISTINCT he.description FROM compounds AS c 
INNER JOIN compound_synonyms AS cs ON c.id=cs.source_id 
INNER JOIN compounds_health_effects AS che ON c.id=che.compound_id
INNER JOIN health_effects AS he ON he.id=che.health_effect_id
WHERE cs.synonym LIKE '%dextrose%';
