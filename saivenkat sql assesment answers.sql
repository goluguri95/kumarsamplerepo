
--1
select count(*) as count from customers
--2
select distinct city as city from customers
--3
select count(distinct state) as count from customers
--4
select customer_id,lower(first_name),upper(last_name) from customers where customer_id>80 and customer_id<150
--5
select last_name,len(last_name) as length from customers where len(last_name)>9
--6
select state,count(state) as count from customers group by state
select city,count(city) as count from customers group by city
--7
select sector_id,max(monthly_payment) as maximumpayment from packages group by sector_id
--8
select first_name,last_name,monthly_discount,case  
                                                  when monthly_discount>=0 and monthly_discount<=10 then 'A'
												  when monthly_discount>=11 and monthly_discount<=20 then 'B'
												  when monthly_discount>=21 and monthly_discount<=30 then 'C'
												  ELSE 'D'
												  END as grade
                                                  from customers
--9
SELECT first_name ,birth_date,datediff(year,birth_date,current_timestamp)as age from customers   where datediff(year,birth_date,current_timestamp)>50
--10
select * from customers where datediff(day,join_date,'2007-01-01')>0
--11
select customer_id,first_name,state,city,pack_id from customers where pack_id<>3 and pack_id<>10 and pack_id<>27
--12
select first_name,join_date,monthly_discount,pack_id from customers where last_name not like '%a' order by pack_id asc
--13
select * from customers where city='New York' AND monthly_discount>=30 and monthly_discount<=40
select * from customers where datediff(day,join_date,'2007-01-01')>0 and pack_id<>8 and pack_id<>19 and pack_id<>30
--14
select first_name,last_name,customers.pack_id,speed from customers,packages where customers.pack_id=packages.pack_id
--15
select first_name,last_name,customers.pack_id,speed from customers,packages where customers.pack_id=packages.pack_id and (customers.pack_id=22 or customers.pack_id=27) order by last_name
--16
select last_name,first_name,monthly_discount from customers where monthly_discount<(select monthly_discount from customers where customer_id=103)
--17
select first_name,last_name,join_date from customers where join_date>(select join_date from customers where customer_id=540)
--18
select first_name,monthly_discount,customers.pack_id,main_phone_num,secondary_phone_num from customers,packages,sectors where customers.pack_id=packages.pack_id and packages.sector_id=sectors.sector_id and sectors.sector_name='business'
--19
select pack_id,speed,strt_date from packages where datediff(year,strt_date,current_timestamp)=(select datediff(year,strt_date,current_timestamp) from packages where pack_id=7)