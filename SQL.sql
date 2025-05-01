SELECT DISTINCT product_name
FROM Products


SELECT product_id, product_name,  price
FROM Products INNER JOIN Nutritional Information 
ON Products.product_id = Nutritional Information.product_id
WHERE fiber > 5


SELECT product_name
FROM Products INNER JOIN Nutritional Information 
ON Products.product_id = Nutritional Information.product_id
ORDER BY protein DESC
LIMIT 1


SELECT category_id ,  SUM (calories)
FROM Products 
WHERE fat > 0
GROUP BY 1

SELECT category_name ,  AVG (price)
FROM Products INNER JOIN Categories
ON Products.category_id = Categories.category_id
GROUP BY 1
