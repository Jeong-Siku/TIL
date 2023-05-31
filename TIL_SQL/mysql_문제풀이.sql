use sakila;

select * from film;
select * from film_category;
select * from category;
select * from rental;
select * from customer;
select * from inventory;

-- 1. 영화 대여 이력이 가장 많은 3명의 고객에 대해, 고객 이름, 이메일, 대여 횟수를 출력하세요.
SELECT * from rental;
SELECT * from customer;

SELECT concat(customer.first_name,' ' ,customer.last_name) as customer_full_name, 
	   customer.email, 
       COUNT(rental.customer_id) as rental_count
FROM rental # 대여 이력
JOIN customer ON customer.customer_id = rental.customer_id
GROUP BY rental.customer_id
ORDER BY rental_count DESC
LIMIT 3;

-- 2. "Comedy" 장르에 속한 영화의 평점 평균이 4점 이상이고, 2005년 이후에 발행된 영화 중에서, 평점이 가장 높은 5편의 영화 제목과, 평균평점을 출력하세요.
SELECT film.title,category.name, rental_rate, film.release_year
FROM film # 집합관계 1
JOIN film_category ON film.film_id = film_category.film_id # Bridge 역할을 한다. M:N
JOIN category ON film_category.category_id = category.category_id # 집합관계 1
WHERE film.release_year >= 2005 
	  AND film.rental_rate >= 4
      AND category.name = 'Comedy'
ORDER BY film.rental_rate DESC
LIMIT 5;

-- 3. 2006년 이후에 가장 많이 대여된 3개 영화의 제목과 대여 횟수를 출력하세요.
SELECT 
	film.title, 
    COUNT(rental.customer_id) as rent_cnt
FROM rental # 집합관계 1
JOIN inventory on inventory.inventory_id = rental.inventory_id # 집합관계 N:M
JOIN film on film.film_id = inventory.film_id # 집합 관계 1
WHERE DATE_FORMAT(rental.rental_date, '%Y-%m') >= '2006-01'
-- GROUP BY rental.customer_id  # 그룹바이한 주체에 따라 select의 값이 안 나온다. 주의할 것!
GROUP BY film.film_id
ORDER BY rent_cnt DESC
LIMIT 3;

select title, count(rental.rental_id) as cnt #A라는 film_id 집합에 rental_id가 여러개 들어있음 (film_id로 count해도 같은 값이 나옴)
from rental left join inventory using(inventory_id) join film using(film_id)
where substr(rental_date,1,4)>2005
group by film_id
order by cnt desc
limit 3;

-- 4. 2005년 이후에 발행된 영화(film.release_year) 중에서, 대여한 횟수가 가장 많은 영화의 제목과 대여 횟수를 출력하세요. (inventory 활용)
SELECT 
	film.title, film.release_year, 
    COUNT(rental.customer_id) as rent_cnt
FROM rental 
JOIN inventory on inventory.inventory_id = rental.inventory_id
JOIN film on film.film_id = inventory.film_id
WHERE film.release_year >= 2005 # WHERE은 위에 FROM과 JOIN절로 합쳐진 전체 테이블을 대상으로 실행된다.
GROUP BY film.film_id
ORDER BY rent_cnt DESC
LIMIT 1;


-- 5. 영화 대여 횟수가 가장 많은 고객 3명의 이름, 이메일, 대여 횟수를 출력하세요.
-- 6. "Documentary"와 "Music" 장르에 해당되는 영화 중에서, 2005년 이후에 발행된 영화 제목과 발행 연도, 장르명을 출력하세요.
SELECT film.title, film.release_year, category.name
FROM film
JOIN film_category on film_category.film_id = film.film_id
JOIN category on category.category_id = film_category.category_id
WHERE film.release_year >= 2005
	 AND category.name in("Documentary","Music");
	# (category.name == 'Documentary' OR category.name == 'Music')
    
-- 7. "Comedy" 장르에 해당되는 영화 중에서, 대여 횟수가 가장 많은 영화 제목과 대여 횟수를 출력하세요.
SELECT film.title,COUNT(rental.customer_id) as rental_count
FROM film # 주는 대여횟수이기 때문에 rental이 더 적합.
JOIN inventory on inventory.film_id = film.film_id
JOIN rental on rental.inventory_id = inventory.inventory_id
JOIN film_category on film_category.film_id = film.film_id
JOIN category on category.category_id = film_category.category_id
WHERE category.name = 'Comedy'
GROUP BY film.film_id
ORDER BY rental_count DESC
LIMIT 1;