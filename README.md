# architechture


## Getting started

1. Clone repository

    ```git clone https://github.com/DeijoseDevelop/car_architecture_first.git```

2. Open project folder

    ```cd car_architecture_first```

3. Create tables into database

   3.1. ```sudo docker-compose up --build```

   3.2. ```sudo docker exec architechture_web /code/make_migrations.sh```

    **if the file make_migrations.sh gives permission error run this command:**

    ```sudo chmod 777 make_migrations.sh```

4. Create an user

    ```sudo docker exec -t architechture_web python manage.py createsuperuser```


### Excel or CSV headers

1. document_number
2. first_name
3. last_name
4. born_date
5. address
6. email
7. phone
8. gender
9. career


### Important URLs

1. Admin

    http://localhost:8000/admin/

2. Scrapper and Importer

    http://localhost:8000/home/


### Microservice

#### Getting Started

1. Login to the admin.
2. Creates an api key in its respective module.
3. Copy the api key that appears in the message when you create it.
4. Put the api key in all the requests you make in the headers as: x-api-key.

**To use all endpoints except those starting with /users/ you must authenticate in the ednpoint /users/validate/ with your email and password.**

**The token you get back when authenticating must be sent to all other endpoints in the headers like this: Authorization**

#### Base url: http://localhost:8000/api/v1

#### Users Urls

1. Auth: /users/validate/
2. Create user: /users/create/

#### Students Urls

1. Students: /students/list/

#### Teachers Urls

1. Teacher: /teachers/list/

#### Courses Urls

1. Courses: /courses/list/

#### Qualifications Urls

1. Qualifications: /qualifications/list/
