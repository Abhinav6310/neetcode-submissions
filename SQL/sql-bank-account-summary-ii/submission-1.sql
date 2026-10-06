-- Write your query below
select a.name , b.balance from users a inner join (select account, sum(amount) as balance from transactions group by account) b on a.account=b.account where b.balance>10000