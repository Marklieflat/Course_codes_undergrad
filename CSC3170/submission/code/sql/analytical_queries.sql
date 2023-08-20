-- Sample queries of an analytic or data mining nature 

-- #1
-- What is the main age group of Sephora's customers?
-- (Display a table showing the number of users of each age group)
(
	SELECT '< 20' AS AGE_GROUP, COUNT(*) as NUN_OF_USERS
	FROM `project`.`user` AS U
	WHERE U.AGE < 20
)
UNION
(
	SELECT ' 20 - 50' AS AGE_GROUP, COUNT(*) as NUN_OF_USERS
	FROM `project`.`user` AS U
	WHERE U.AGE >= 20 and U.age <= 50
)
UNION
(
	SELECT '> 50' AS AGE_GROUP, COUNT(*) as NUN_OF_USERS
	FROM `project`.`user` AS U
	WHERE U.AGE > 50
);

-- #2
-- What are the differences between ratings for customers of different age groups in 2022? 
-- (Display a table showing average ratings for customers of age below 20, 20-50, above 50)
(
	SELECT '< 20' AS AGE_GROUP, AVG(R.RATINGS) as AVG_RATINGS
	FROM `project`.`review` as R, `project`.`user` AS U
	WHERE R.USER_ID = U.USER_ID AND
          U.AGE < 20
)
UNION
(
	SELECT '20-50' AS AGE_GROUP, AVG(R.RATINGS) as AVG_RATINGS
	FROM `project`.`review` as R, `project`.`user` AS U
	WHERE R.USER_ID = U.USER_ID AND
		  U.AGE >= 20 AND 
          U.AGE <= 50
)
UNION
(
	SELECT '>50' AS AGE_GROUP, AVG(R.RATINGS) as AVG_RATINGS
	FROM `project`.`review` as R, `project`.`user` AS U
	WHERE R.USER_ID = U.USER_ID AND
		  U.AGE >= 50
);
      
-- #3
-- Is there an obvious relationship between ratings and total revenue among different products? 
-- (Display a table showing the ratings and the total revenue of all products)
WITH REVENUE AS(
	SELECT PRODUCT_ID, SUM(ITEM_PRICE*ITEM_QUANTITY) AS TOTAL_REVENUE
	FROM `project`.`orders`
	GROUP BY PRODUCT_ID
), 
RATINGS AS (
	SELECT PRODUCT_ID, AVG(RATINGS) AS AVG_RATINGS
	FROM `project`.`review`
	GROUP BY PRODUCT_ID
)
SELECT REV.PRODUCT_ID, P.PRODUCT_NAME, REV.TOTAL_REVENUE, RAT.AVG_RATINGS
FROM `project`.`product`AS P, REVENUE AS REV, RATINGS AS RAT
WHERE REV.PRODUCT_ID = RAT.PRODUCT_ID AND
	  REV.PRODUCT_ID = P.PRODUCT_ID;

-- #4
-- Is there any relationship between the demands of the products of each category and the seasons? 
-- (Display a table showing the product sales of each category in each quarter of 2022)
WITH ORDER_TIME_IN_QUARTER AS (
      SELECT O.ORDER_ID, P.CATEGORY AS CATEGORY, O.ITEM_QUANTITY AS QUANTITY, 
			 QUARTER(O.TIMESTAMP) AS TIME_IN_QUARTER
      FROM `project`.`orders` AS O, `project`.`product` AS P
      WHERE O.PRODUCT_ID = P.PRODUCT_ID AND
			YEAR(O.TIMESTAMP) = 2022
)
SELECT TIME_IN_QUARTER AS `QUARTER`, CATEGORY, SUM(QUANTITY) AS TOTAL_SALES
FROM ORDER_TIME_IN_QUARTER
GROUP BY 1, 2
ORDER BY 1 ASC, 2 ASC;

-- #5
-- Which brands are more popular in products for each skin type in 2022 respectively? 
-- (Display a table showing the top 3 brands with the highest total sales of products for each skin type in 2022)
WITH BRAND_SKIN_SALES AS (
	SELECT A.SKIN_TYPE, P.BRAND_NAME, SUM(O.ITEM_QUANTITY) AS TOTAL_SALES
	FROM `project`.`product` AS P, `project`.`orders` AS O, `project`.`applicability` AS A
	WHERE P.PRODUCT_ID = O.PRODUCT_ID AND
	      P.PRODUCT_ID = A.PRODUCT_ID AND
          YEAR(O.TIMESTAMP) = 2022
	GROUP BY 1, 2
)
(
  SELECT *
  FROM BRAND_SKIN_SALES
  WHERE SKIN_TYPE = 'dry'
  ORDER BY TOTAL_SALES DESC
  LIMIT 3
)
UNION
(
  SELECT *
  FROM BRAND_SKIN_SALES
  WHERE SKIN_TYPE = 'normal'
  ORDER BY TOTAL_SALES DESC
  LIMIT 3
)
UNION
(
  SELECT *
  FROM BRAND_SKIN_SALES
  WHERE SKIN_TYPE = 'oily'
  ORDER BY TOTAL_SALES DESC
  LIMIT 3
);

-- #6
-- Which brand is more efficient in addressing complaints? 
-- (Display a table showing the average complaints solving time among different brands)
SELECT C.BRAND_NAME, AVG(TIMESTAMPDIFF(DAY, C.COMPLAINT_DATE, C.RESOLUTION_DATE)) AS `AVG_SOLVING_TIME(DAY)`
FROM `project`.`complaint` AS C
WHERE C.STATUS = 1
GROUP BY C.BRAND_NAME
ORDER BY 2 ASC;