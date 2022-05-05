# Write your MySQL query statement below
# SELECT COUNT(DISTINCT A.requester_id, A.accepter_id) // COUNT(*)
SELECT ROUND(IFNULL(
        (
        (SELECT COUNT(DISTINCT A.requester_id, A.accepter_id) FROM RequestAccepted A) /
        COUNT(DISTINCT R.sender_id, R.send_to_id)), 0),2) AS "accept_rate"
        FROM FriendRequest R





# SELECT
# ROUND(
#     IFNULL(
#     (SELECT COUNT(*) FROM (SELECT DISTINCT requester_id, accepter_id FROM RequestAccepted) AS A)
#     /
#     (SELECT COUNT(*) FROM (SELECT DISTINCT sender_id, send_to_id FROM FriendRequest) AS B),
#     0)
# , 2) AS accept_rate;