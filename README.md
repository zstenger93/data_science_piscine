# data_science_piscine

## connect alias as:
```
alias connect='docker exec -it postgres psql -U zstenger -d piscineds -h localhost -W'
```

## run alias as:
```
alias run='docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q) && docker-compose up -d'
```

# postgres command examples

```
SELECT * FROM data_2022_oct LIMIT 10;
```

```
DROP TABLE "data_2022_oct";
```