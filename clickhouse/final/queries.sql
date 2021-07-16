CREATE TABLE events_local ON CLUSTER mycluster
(
    id Int64,
    title String,
    description String,
    content String,
    date Date
)
ENGINE = ReplicatedMergeTree('/clickhouse/{cluster}/tables/events_local ', '{replica}')
PARTITION BY date
ORDER BY id;


CREATE TABLE events_distributed ON CLUSTER 'mycluster'
(
    id Int64,
    title String,
    description String,
    content String,
    date Date
)
ENGINE = Distributed('{cluster}', 'default', 'events_local', rand());


INSERT INTO events_distributed
VALUES (1, 'title1', 'description1', 'content1', now()),
(2, 'title2', 'description2', 'content2', now()),
(3, 'title3', 'description3', 'content3', now()),
(4, 'title4', 'description4', 'content4', now()),
(5, 'title5', 'description5', 'content5', now()),
(6, 'title6', 'description6', 'content6', now()),
(7, 'title7', 'description7', 'content7', now()),
(8, 'title8', 'description8', 'content8', now()),
(9, 'title9', 'description9', 'content9', now());