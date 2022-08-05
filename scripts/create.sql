PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE scooters (id STRING not null, location POINT not null, user string);
COMMIT;

