-- Create the Database for NewsSite.

-- DROP database in case it already exists.
--DROP DATABASE IF EXISTS NewsSite;

-- Create DB
--CREATE DATABASE IF NOT EXISTS NewsSite;
--USE NewsSite;

--SELECT 'CREATING ATTRIBUTE TABLES' as '';

-- Drop tables if already exist.
DROP TABLE AUTHERS;
DROP TABLE PUB_STATUS;
DROP TABLE CATAGORIES;

-- Create tables for the article atributes auther, published status, catagories.
CREATE TABLE AUTHERS ( 
	auther_id 			int 	unsigned 	not null, 
	auther_name 		varchar(64) 		not null, 
	PRIMARY KEY (auther_id)
);
CREATE TABLE PUB_STATUS ( 
	pub_status_id 		int 	unsigned 	not null, 
	pub_status_name 	varchar(64) 		not null,
	display_flag boolean 					not null,
	PRIMARY KEY (pub_status_id)
);
CREATE TABLE CATAGORIES ( 
	catagory_id 		int unsigned 		not null, 
	catagory_name 		varchar(64) 		not null, 
	PRIMARY KEY (catagory_id)
);

--SELECT 'POPULATING ATTRIBUTE TABLES' as '';

-- Populate Attributes tables.

-- Authers table.
INSERT INTO AUTHERS (auther_name) VALUES
	(1,'Anne'),
	(2,'Bob'),
	('Charlie'),
	('Dian'),
	('Eric');

-- Publishes status table.
INSERT INTO PUB_STATUS (pub_status_name,display_flag) VALUES 
	('Draft',FALSE),
	('Approved',FALSE),
	('Published',TRUE);

-- Catagories.
INSERT INTO CATAGORIES (catagory_name) VALUES
	('Poltics'),
	('Sport'),
	('Art, Music & Entertainment');

--SELECT 'CREATING ARTICLES TABLE' as '';

-- Create articles table
-- Drop tables if already exist.
DROP TABLE IF EXISTS ARTICLES;
CREATE TABLE ARTICLES ( 
	article_id 			int		unsigned 	not null, 
	title 				varchar(64) 		not null,
	summary 			varchar(255)		not null,
	content 			text				not null,
	auther_id 			int 	unsigned	not null,
	pub_status_id 		int 	unsigned	not null,
	pub_date 			timestamp,
	PRIMARY KEY (article_id),
	FOREIGN KEY (auther_id) REFERENCES AUTHERS(auther_id),
	FOREIGN KEY (pub_status_id) REFERENCES PUB_STATUS(pub_status_id)
);

--SELECT 'CREATING CATAGORY ARTICLES CONNECTION TABLE' as '';

-- A News article may be in multiple catagories so a article catagory connection table.
DROP TABLE ARTICLES_CATAGORIES;
CREATE TABLE ARTICLE_CATAGORIES ( 
	article_catagory_id	int 	unsigned	not null,
	article_id 			int 	unsigned	not null,
	catagory_id 		int 	unsigned	not null,
	priority 			smallint unsigned 	not null,
	PRIMARY KEY (article_catagory_id),
	FOREIGN KEY (article_id) REFERENCES ARTICLES(article_id),
	FOREIGN KEY (catagory_id) REFERENCES CATAGORIES(catagory_id)
);

--SELECT 'CREATING PRIMARY ATRICLE LIST VIEW' as '';

-- Create primary article list view for end user
DROP VIEW top_articles;
CREATE VIEW top_articles as
	SELECT ARTICLES.title,ARTICLES.summary,AUTHERS.auther_name
	FROM ARTICLES
	LEFT JOIN AUTHERS ON ARTICLES.auther_id = AUTHERS.auther_id
	LEFT JOIN PUB_STATUS ON ARTICLES.pub_status_id = PUB_STATUS.pub_status_id
	WHERE PUB_STATUS.display_flag = TRUE;































