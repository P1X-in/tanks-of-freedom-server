START TRANSACTION;

CREATE TABLE matches (
    id INT NOT NULL auto_increment,
    creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    join_code VARCHAR(8) NOT NULL,
    map_id INT NOT NULL,
    status TINYINT(2) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE match_players (
    match_id INT NOT NULL,
    player_id INT NOT NULL,
    side TINYINT(2) NOT NULL,
    status TINYINT(2) NOT NULL,
    join_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (match_id, player_id)
);

CREATE TABLE match_states (
    match_id INT NOT NULL,
    json TEXT DEFAULT NULL,
    PRIMARY KEY (match_id)
);

COMMIT;