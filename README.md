# data_science_piscine

## Day 0 Data Engineer

Since postgres is not available on our Mac's and we are allergic to VM's we decided to run things on docker

ex 00 and 01 was just about to create the docker-compose file which run 2 service, postgres for database and pgadmin to handle and see the db easier



# A few alias to make things smooth and faster, or at least faster than python

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
