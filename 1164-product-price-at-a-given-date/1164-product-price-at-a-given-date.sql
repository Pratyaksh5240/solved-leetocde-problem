# Write your MySQL query statement below
SELECT 
    p.product_id,
    IFNULL(p.new_price, 10) AS price
FROM (
    SELECT 
        product_id,
        new_price,
        change_date,
        RANK() OVER (
            PARTITION BY product_id
            ORDER BY change_date DESC
        ) AS rnk
    FROM Products
    WHERE change_date <= '2019-08-16'
) p
WHERE p.rnk = 1

UNION

SELECT 
    product_id,
    10 AS price
FROM Products
GROUP BY product_id
HAVING MIN(change_date) > '2019-08-16';