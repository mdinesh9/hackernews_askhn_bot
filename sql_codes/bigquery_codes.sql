SELECT * FROM [bigquery-public-data:hacker_news.full] WHERE title like "%Ask HN%" 
  ORDER BY timestamp DESC
  LIMIT 10000;

SELECT * FROM [bigquery-public-data:hacker_news.full] WHERE title like "%Ask HN%" 
  ORDER BY timestamp DESC
  LIMIT 10000 OFFSET 10000;


    .
    .
    .
    .
    .
    .
    .

SELECT * FROM [bigquery-public-data:hacker_news.full] WHERE title like "%Ask HN%" 
  ORDER BY timestamp DESC
  LIMIT 10000 OFFSET 80000;

SELECT * FROM [bigquery-public-data:hacker_news.full] WHERE title like "%Ask HN%" 
  ORDER BY timestamp DESC
  LIMIT 10000 OFFSET 90000;