### installation
- copy file called cot-env from fenv folder, paste and renamed to .cot-env to
  root folder
- copy file called cot-envdb from fenv folder, paste and renamed to .cot-envdb
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

### migreate db
```
 - docker-compose exec api python manage.py migrate --noinput 
```

### inside the docker images data base 
```
 - docker-compose exec db psql --username=myuser --dbname=mydatabase 
```

### list volumes docker 
### display a list of volumes
```
 - docker volume ls 
```

### inspect a volume 
```
 - docker volume inspect my-volume-listed 
```

### build a docker using tag 
```
 - docker build -f ./app/Dockerfile -t mytagfordocker:latest ./app
```

### run another images in other port 
### docker is running on port localhost:9002
```
docker run -d \                                     
-p 9002:9001 \
-e "SECRET_KEY=mysecretkey" -e "DEBUG=1" -e "ALLOWED_HOSTS=*" \
api python /usr/src/app/manage.py runserver 0.0.0.0:9001
```

### show docker lgos
```
- docker-compose -f docker-compose.prod.yml logs -f
```

### create module
```
- docker-compose exec api python manage.py startapp myapp
```

### TROUBLESHOOTING
### 1
- if not migrate correnctly, check if folder "migrations" is created in folder
  "core"
- then run makemigrations
- then run migrate
- then create super user
- stop docker, and re-run docker

