START TRANSACTION;

CREATE TABLE players (
    id INT NOT NULL auto_increment,
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    auto_pin VARCHAR(8) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE maps (
    id INT NOT NULL auto_increment,
    download_code VARCHAR(16) NOT NULL,
    map_hash VARCHAR(32) NOT NULL,
    player_id INT NOT NULL,
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

CREATE INDEX maps_code_index ON maps (download_code);
CREATE INDEX maps_hash_index ON maps (map_hash);

CREATE TABLE maps_data (
    map_id INT NOT NULL,
    json TEXT NOT NULL,
    PRIMARY KEY (map_id)
);

COMMIT;