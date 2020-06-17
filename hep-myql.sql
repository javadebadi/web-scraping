-- HEP database
-- mysql version
-- as of 2020-06-17

CREATE DATABASE IF NOT EXISTS hep DEFAULT CHARSET = utf8;
USE hep;

DROP TABLE IF EXISTS author;
CREATE TABLE author(
  id INT PRIMARY KEY,
  full_name VARCHAR(32),
  BS_id INT,
  MS_id INT,
  PhD_id INT,
  PD1_id INT,
  PD2_id INT,
  PD3_id INT,
  PD4_id INT,
  Senior_id INT,
  BS_start SMALLINT,
  MS_start SMALLINT,
  PhD_start SMALLINT,
  PD1_start SMALLINT,
  PD2_start SMALLINT,
  PD3_start SMALLINT,
  PD4_start SMALLINT,
  Senior_start SMALLINT,
  n_papers_published MEDIUMINT,
  n_papers_citeable MEDIUMINT,
  n_citation_published MEDIUMINT,
  n_citation_citeable MEDIUMINT,
  citation_per_paper_published DOUBLE,
  citation_per_paper_citeable DOUBLE,
  papers_id VARCHAR(10000)
);

SELECT * FROM author;
