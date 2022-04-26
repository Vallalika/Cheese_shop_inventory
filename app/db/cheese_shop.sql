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
    selling_price NUMERIC(6,2),
    inventory_include BOOLEAN
);

CREATE TABLE providers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    country VARCHAR(255),
    address VARCHAR(255)
);

CREATE TABLE cheese_provisions (
    id SERIAL PRIMARY KEY,
    cheese_id INT REFERENCES cheeses(id) ON DELETE CASCADE,
    provider_id INT REFERENCES providers(id) ON DELETE CASCADE
);