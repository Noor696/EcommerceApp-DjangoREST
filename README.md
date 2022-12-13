# SchoolApp-DjangoREST

## LAB-25

## Project: School-DjangoREST-API

**Author: Noor Alkhateeb**

I Use Django REST Framework to create an School API, then "containerize" it with Docker.

**/api/v1/schools/** URL

1. API-list objects

![](./Images/API-list.PNG)

2. API-create objects

![](./Images/API-create.PNG)

3. API-update or delete specific object **/api/v1/schools/_id_**

![](./Images/API-update-delete.PNG)



**Run:**

> python3 manage.py runserver


**update the database:**

python manage.py makemigrations
python manage.py migrate

**docker-compose up**
when run this command:
* my image will be build
* my container will be build
* take all the project and put it inside the container
* then run the server inside the container.



