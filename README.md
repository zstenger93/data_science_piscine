# data_science_piscine

## up alias as:

```
alias up='docker-compose up -d'
```

## run alias as:
```
alias run='docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q) && docker-compose up -d'
```

## connect alias as:
```
alias connect='docker exec -it postgres psql -U zstenger -d piscineds -h localhost -W'
```

## postgres command examples

```
SELECT * FROM data_2022_oct LIMIT 10;
```

```
DROP TABLE "data_2022_oct";
```

```
SELECT COUNT(*) FROM customers;
```


select * from customers as c
INNER JOIN 
(select 
product_id, COALESCE(MAX(category_id), NULL) as category_id,
COALESCE(MAX(category_code), NULL) as category_code,
COALESCE(MAX(brand), NULL) as brand
from items
GROUP by product_id )
as i
ON c.product_id=i.product_id
