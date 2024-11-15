-- Sample queries for practical daily operations and activities 

-- Insert
INSERT INTO user VALUES
	(1000000000,"Chestnut",21),
    (1000000001,"Jackyeijfi", 40);


-- Delete
DELETE FROM user WHERE USER_ID = 1000000000;
DELETE FROM user WHERE USER_NAME = "Jackyeijfi";


-- Update
UPDATE product set PRICE = PRICE + 5 
	WHERE PRODUCT_NAME="Creme de Coco Shampoo";
UPDATE product set PRICE = PRICE - 5 
	WHERE PRODUCT_NAME="Creme de Coco Shampoo";


-- Retrieve
-- #1
-- Get the number of users who have made a purchase in 2022
SELECT COUNT(DISTINCT USER_ID) AS NUM_OF_USERS
FROM `project`.`orders` AS O
WHERE O.TIMESTAMP BETWEEN DATE('2022-01-01') AND DATE('2022-12-31');

-- #2
-- Count the number of orders placed by Jerry
SELECT COUNT(*) AS `NUM_OF_ORDERS`
FROM `project`.`orders` AS O, `project`.`user` AS U
WHERE O.USER_ID = U.USER_ID AND U.USER_NAME = 'Jerry';

-- #3
-- Calculate the total revenue generated by LA MER in March 2023
SELECT SUM(O.ITEM_PRICE*O.ITEM_QUANTITY) AS REVENUE
FROM `project`.`orders` AS O, `project`.`product` AS P
WHERE O.PRODUCT_ID = P.PRODUCT_ID AND 
	  P.BRAND_NAME = 'LA MER' AND
	  O.TIMESTAMP BETWEEN DATE('2023-03-01') AND DATE('2023-03-31');
      
-- #4
-- Calculate the average rating for a specific product (Creme de Coco Shampoo)
SELECT AVG(RATINGS) AS AVG_RATINGS
FROM `project`.`review` AS R, `project`.`product` AS P
WHERE R.PRODUCT_ID = P.PRODUCT_ID AND
      PRODUCT_NAME = 'Creme de Coco Shampoo';

-- #5
-- Find all products with an average rating greater than 4.5
SELECT P.PRODUCT_NAME
FROM `project`.`review` AS R, `project`.`product` AS P
WHERE R.PRODUCT_ID = P.PRODUCT_ID
GROUP BY R.PRODUCT_ID
HAVING AVG(RATINGS) > 4.5;

-- #6
-- Find all brands with at least 40 complaints
SELECT BRAND_NAME
FROM `project`.`complaint`
GROUP BY BRAND_NAME
HAVING COUNT(*) >= 40;

-- #7
-- Get all orders that were placed in April 2023
SELECT ORDER_ID
FROM `project`.`orders` AS O
WHERE O.TIMESTAMP BETWEEN DATE('2023-04-01') AND DATE('2023-04-30');

-- #8
-- Calculate the total revenue generated by a specific product (Creme de Coco Shampoo)
SELECT SUM(O.ITEM_PRICE*O.ITEM_QUANTITY) AS REVENUE
FROM `project`.`orders` AS O, `project`.`product` AS P
WHERE O.PRODUCT_ID = P.PRODUCT_ID AND
      P.PRODUCT_NAME = 'Creme de Coco Shampoo';

-- #9
-- Calculate the average number of products per brand
SELECT COUNT(PRODUCT_NAME)/COUNT(DISTINCT BRAND_NAME) AS AVG_NUM
FROM `project`.`product`;

-- #10
-- Find the most commonly ordered products
SELECT P1.PRODUCT_NAME
FROM `project`.`orders` AS O1, `project`.`product` AS P1 
WHERE O1.PRODUCT_ID = P1.PRODUCT_ID
GROUP BY O1.PRODUCT_ID
HAVING COUNT(*) = (SELECT COUNT(*)
	FROM `project`.`orders` AS O2
	GROUP BY O2.PRODUCT_ID
	ORDER BY COUNT(*) DESC
	LIMIT 1);

-- #11
-- Find all products that have at least 10 reviews with the highest average rating
WITH PROCESSED_REVIEW AS (
      SELECT PRODUCT_ID, AVG(RATINGS) AS AVG_RATING
      FROM `project`.`review`
      GROUP BY PRODUCT_ID
      HAVING COUNT(*) >= 10
)
SELECT PRODUCT_NAME
FROM PROCESSED_REVIEW AS R, `project`.`product` AS P
WHERE R.PRODUCT_ID = P.PRODUCT_ID AND
	  R.AVG_RATING = (SELECT AVG_RATING
		FROM PROCESSED_REVIEW
		ORDER BY AVG_RATING DESC
		LIMIT 1);

-- #12
-- Count the number of brands that have at least one product with a price greater than $1000
SELECT COUNT(DISTINCT BRAND_NAME) AS NUM_OF_BRANDS
FROM `project`.`product`
WHERE PRICE > 1000;

-- #13
-- Get the number of reviews for products of a specific brand (LA MER) 
SELECT COUNT(*) AS NUM_OF_REVIEWS
FROM `project`.`review` AS R, `project`.`product` AS P
WHERE R.PRODUCT_ID = P.PRODUCT_ID
GROUP BY P.BRAND_NAME
HAVING P.BRAND_NAME = 'LA MER';

-- #14
-- Calculate the total spending of Jerry in 2022
SELECT SUM(O.TOTAL_COST) AS SPENDING
FROM `project`.`orders` AS O, `project`.`user` AS U
WHERE O.USER_ID = U.USER_ID AND
	  U.USER_NAME = 'Jerry' AND
      O.TIMESTAMP BETWEEN DATE('2022-01-01') AND DATE('2022-12-31');
      
-- #15
-- Assume the rating of a brand is the average rating of all its products. 
-- Find all brands with a rating less than 2.
SELECT P.BRAND_NAME
FROM `project`.`product` AS P, `project`.`review` AS R
WHERE P.PRODUCT_ID = R.PRODUCT_ID
GROUP BY P.BRAND_NAME
HAVING AVG(R.RATINGS) < 2;
