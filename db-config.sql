CREATE DATABASE providas;
CREATE USER providasuser WITH PASSWORD 'password';
ALTER ROLE providasuser SET client_encoding TO 'utf8';
ALTER ROLE providasuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE providasuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE basicdjango TO providasuser;