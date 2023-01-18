START TRANSACTION;

INSERT INTO versioning (version_number) VALUES (4);

CREATE TABLE maps_v2 (
    id INT NOT NULL auto_increment,
    download_code VARCHAR(24) NOT NULL,
    base_code VARCHAR(16) NOT NULL,
    iteration INT NOT NULL,
    player_id INT NOT NULL,
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

CREATE INDEX maps_code_v2_index ON maps_v2 (download_code);
CREATE INDEX maps_hash_v2_index ON maps_v2 (map_hash);

CREATE TABLE maps_downloads_v2 (
    map_id INT NOT NULL,
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (map_id, creation_time)
);

COMMIT;