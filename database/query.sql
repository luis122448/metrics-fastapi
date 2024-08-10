CREATE TABLE TBL_PROJECT (
    id         INTEGER  NOT NULL,
    name       VARCHAR,
    created_at DATETIME,
    updated_at DATETIME,
    PRIMARY KEY (
        id
    )
);

CREATE TABLE TBL_METRICS (
    id            INTEGER      NOT NULL,
    project_id    INTEGER      NOT NULL,
    metrics_type  VARCHAR (50) NOT NULL,
    name          VARCHAR (50),
    value_integer INTEGER,
    value_float   FLOAT,
    value_string  VARCHAR (50),
    value_date    DATETIME,
    created_at    DATETIME,
    updated_at    DATETIME,
    CONSTRAINT PK_METRICS PRIMARY KEY (
        id,
        project_id
    )
);

DELETE FROM TBL_PROJECT;

INSERT INTO TBL_PROJECT VALUES (1,'Dota Shuffle',current_timestamp,current_timestamp);
INSERT INTO TBL_PROJECT VALUES (2,'Animationland',current_timestamp,current_timestamp);

SELECT * FROM TBL_PROJECT;

DELETE FROM TBL_METRICS;

INSERT INTO TBL_METRICS VALUES (1,1,'INTERER','Total Views',2450,NULL,NULL,NULL,current_timestamp,current_timestamp);
INSERT INTO TBL_METRICS VALUES (2,1,'INTEGER','Total Shuffle',5785,NULL,NULL,NULL,current_timestamp,current_timestamp);
INSERT INTO TBL_METRICS VALUES (3,1,'INTERER','Amount of MMR Shuffe',3754582,NULL,NULL,NULL,current_timestamp,current_timestamp);
INSERT INTO TBL_METRICS VALUES (4,1,'INTEGER','Total Top Players',105,NULL,NULL,NULL,current_timestamp,current_timestamp);

SELECT * FROM TBL_METRICS;
