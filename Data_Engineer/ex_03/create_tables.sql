CREATE TABLE data_2022_dec (
    event_time TIMESTAMP,
    event_type VARCHAR(255),
    product_id INT,
    price FLOAT,
    user_id BIGINT,
    user_session UUID
);

COPY data_2022_dec FROM '/tmp/data_2022_dec.csv' CSV HEADER;

CREATE TABLE data_2022_nov (
    event_time TIMESTAMP,
    event_type VARCHAR(255),
    product_id INT,
    price FLOAT,
    user_id BIGINT,
    user_session UUID
);

COPY data_2022_nov FROM '/tmp/data_2022_nov.csv' CSV HEADER;

CREATE TABLE data_2022_oct (
    event_time TIMESTAMP,
    event_type VARCHAR(255),
    product_id INT,
    price FLOAT,
    user_id BIGINT,
    user_session UUID
);

COPY data_2022_oct FROM '/tmp/data_2022_oct.csv' CSV HEADER;

CREATE TABLE data_2023_feb (
    event_time TIMESTAMP,
    event_type VARCHAR(255),
    product_id INT,
    price FLOAT,
    user_id BIGINT,
    user_session UUID
);

COPY data_2023_feb FROM '/tmp/data_2023_feb.csv' CSV HEADER;

CREATE TABLE data_2023_jan (
    event_time TIMESTAMP,
    event_type VARCHAR(255),
    product_id INT,
    price FLOAT,
    user_id BIGINT,
    user_session UUID
);

COPY data_2023_jan FROM '/tmp/data_2023_jan.csv' CSV HEADER;
