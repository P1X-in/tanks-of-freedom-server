START TRANSACTION;

INSERT INTO versioning (version_number) VALUES (2);

CREATE INDEX matches_code_index ON matches (join_code);

COMMIT;