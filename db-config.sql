CREATE DATABASE basicdjango;
CREATE USER basicdjangouser WITH PASSWORD 'password';
ALTER ROLE basicdjangouser SET client_encoding TO 'utf8';
ALTER ROLE basicdjangouser SET default_transaction_isolation TO 'read committed';
ALTER ROLE basicdjangouser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE basicdjango TO basicdjangouser;
