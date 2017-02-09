-- Write a SQL query to find all numbers that appear at least three times consecutively.
--
-- +----+-----+
-- | Id | Num |
-- +----+-----+
-- | 1  |  1  |
-- | 2  |  1  |
-- | 3  |  1  |
-- | 4  |  2  |
-- | 5  |  1  |
-- | 6  |  2  |
-- | 7  |  2  |
-- +----+-----+
-- For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.
--
--
-- # Write your MySQL query statement below
select distinct t.* from (
select a.Num as ConsecutiveNums
from Logs a
join Logs b
on a.Id - 1 = b.Id
and a.Num = b.Num
join Logs c
on b.Id - 1 = c.Id
and b.Num = c.Num) t;
