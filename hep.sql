-- HEP database
-- mysql version
-- as of 2020-06-17

CREATE DATABASE IF NOT EXISTS hep DEFAULT CHARSET = utf8;
USE hep;

DROP TABLE IF EXISTS author;
CREATE TABLE IF NOT EXISTS author(
  id INT PRIMARY KEY,
  full_name VARCHAR(255),
  BS_id INT,
  MS_id INT,
  PhD_id INT,
  PD1_id INT,
  PD2_id INT,
  PD3_id INT,
  PD4_id INT,
  Senior_id INT,
  BS_start CHAR(4),
  MS_start CHAR(4),
  PhD_start CHAR(4),
  PD1_start CHAR(4),
  PD2_start CHAR(4),
  PD3_start CHAR(4),
  PD4_start CHAR(4),
  Senior_start CHAR(4),
  n_papers_published MEDIUMINT,
  n_papers_citeable MEDIUMINT,
  n_citation_published MEDIUMINT,
  n_citation_citeable MEDIUMINT,
  citation_per_paper_published DOUBLE,
  citation_per_paper_citeable DOUBLE,
  papers_id VARCHAR(10000)
) ENGINE = InnoDB;

SELECT * FROM author;
