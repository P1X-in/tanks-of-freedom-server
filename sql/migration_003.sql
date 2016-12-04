START TRANSACTION;

INSERT INTO versioning (version_number) VALUES (3);

CREATE TABLE maps_downloads (
    map_id INT NOT NULL,
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (map_id, creation_time)
);

COMMIT;