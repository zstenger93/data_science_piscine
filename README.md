# data_science_piscine

## Day 0 Data Engineer

Since postgres is not available on our Mac's and we are allergic to VM's we decided to run things on docker

ex 00 and 01 was just about to create the docker-compose file which run 2 service, postgres for database and pgadmin to handle and see the db easier

ex 02 we created our first data table where I quickly realized doing things NOT ON the database make it significantly slower so first I connect to the postgres database and run my sql code directly on the database which made a table creation 7 second instead of 1,5-2 minute

ex 03 is the same as 02 but we need to create all the tables from the provided csv files

ex 04 we create the items table from the corresponding csv file

## Day 1 Data Warehouse

ex 00 create all the tables again from previous day with one extra from this subject.

ex 01 we merge all data from 2022 oct until 2023 feb into a customers table keeping all the duplicates

ex 02 we remove all the duplicate rows from table

ex 03 we merge the items table into the customers table but be careful, the items table has duplicates as well, so you should group those duplicates before adding the values to the customers table with the matching id's

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
