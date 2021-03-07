mysqldump --databases foodb -u root -p --hex-blob --set-gtid-purged=OFF --single-transaction --default-character-set=utf8mb4 > local_foodb.sql
