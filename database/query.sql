DELETE FROM TBL_PROJECT;

INSERT INTO TBL_PROJECT VALUES (1,'Dota Shuffle',current_timestamp,current_timestamp);
INSERT INTO TBL_PROJECT VALUES (2,'Animationland',current_timestamp,current_timestamp);

SELECT * FROM TBL_PROJECT;

DELETE FROM TBL_METRICS;

INSERT INTO TBL_METRICS VALUES (1,1,'INTERER','Total Views',1785,NULL,NULL,NULL,current_timestamp,current_timestamp);
INSERT INTO TBL_METRICS VALUES (2,1,'INTEGER','Total Shuffle',4785,NULL,NULL,NULL,current_timestamp,current_timestamp);
INSERT INTO TBL_METRICS VALUES (3,1,'INTERER','Amount of MMR Shuffe',2504582,NULL,NULL,NULL,current_timestamp,current_timestamp);
INSERT INTO TBL_METRICS VALUES (4,1,'INTEGER','Total Top Players',78,NULL,NULL,NULL,current_timestamp,current_timestamp);

SELECT * FROM TBL_METRICS;
