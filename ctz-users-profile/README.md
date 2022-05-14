### installation
- copy file called env from fenv folder, paste and renamed to .env to
  root folder
- copy file called env from fenv folder, paste and renamed to .env
  to root folder
- create folder and file called log folder and inside log folder a
  cotizate_api_application.log file, all inside app folder. 

### build docker
```
 - docker-compose build
```

### up docker
```
 - docker-compose up -d 
```

### makemigrations
```
  docker-compose exec api python3 manage.py makemigrations 
```

### migreate db
```
  docker-compose exec api python3 manage.py migrate --noinput 
```

### create users with commands 
```
  docker-compose exec api python3 manage.py users
```

### test 
```
  docker-compose exec api python3 manage.py test
```

### TROUBLESHOOTING
### 1
- if not migrate correnctly, check if folder "migrations" is created in folder
  "core"
- then run makemigrations
- then run migrate
- then create super user
- stop docker, and re-run docker

### 2
- if not create database use script below
```bash
  docker-compose exec db psql --username=ctzUs3r --dbname=postgres
```
