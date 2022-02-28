select distinct b.cart_id
from cart_products b
join (select a.cart_id
from cart_products a
where a.name = 'milk') c on c.cart_id = b.cart_id
where b.name = 'yogurt'
order by b.cart_id