# Write your MySQL query statement below
# SELECT DISTINCT
#     requester_id
#     ,accepter_id
# FROM RequestAccepted

SELECT id
    ,count(id2) as num
FROM
(SELECT requester_id AS id
    ,accepter_id AS id2
FROM RequestAccepted
UNION
SELECT accepter_id AS id
    ,requester_id AS id2
FROM RequestAccepted) TMP
GROUP BY id
ORDER BY num DESC
LIMIT 1

