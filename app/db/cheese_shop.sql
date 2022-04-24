DROP TABLE IF EXISTS cheese_provisions;
DROP TABLE IF EXISTS cheeses;
DROP TABLE IF EXISTS providers;

CREATE TABLE cheeses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    origin VARCHAR(255),
    type VARCHAR(255),
    description VARCHAR(255),
    stock INT,
    buying_cost NUMERIC(6,2),
    -- decimal type, 6 digits in total, 2 after the .
    selling_price NUMERIC(6,2)
);

CREATE TABLE providers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    country varchar(255),
    address varchar(255)
);

CREATE TABLE cheese_provisions (
    id SERIAL PRIMARY KEY,
    cheese_id SERIAL REFERENCES cheeses(id),
    provider_id SERIAL REFERENCES providers(id)
);