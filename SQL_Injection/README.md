# SQL injection project
In this project, we simulated two cases: SQLi vulnerable and SQLi secure websites.


## Description
We would like to first explain the installation and launch processes and then provide you with a guide on how to test the websites with SQL injections.

## Installation and requirements
Clone the repository:
```
git clone https://github.com/seelennebel/CyberSecurity.git
```
The project requires Docker installed. Both of the websites, as well as the MySQL database, are containerized and can be launched by following the guide.

As can be seen, the project has three folders: mysql, sql_insecure, and sql_secure. mysql folder contains the Docker file to build MySQL database image with inserted data for the project. In the sql_insecure and sql_secure folders, you can find the source code as well as the Docker files and Docker-Compose files.

First, let's build the MySQL image:
```
cd CyberSecurity/SQL_Injection/mysql
docker build -t mysql-sqli .
```
The docker build command will create an image with the name "mysql-sqli" which will be used to create MySQL containers for both versions of the website.

Next, it is up to you what to launch, you can either launch the SQLi vulnerable or secure version of the website. Please, do not launch websites at the same time!!!

To launch SQL vulnerable website on localhost:8080
```
cd CyberSecurity/SQL_Injection/sql_insecure
docker-compose up
```
We kindly ask you to wait till the MySQL server starts since it can take some time.

To exit and stop the containers from the terminal, you can press Control C. To delete MySQL and SQL-vulnerable website containers and the virtual docker-compose network you can type:
```
docker-compose down
```

To launch SQL secure website on localhost:8080 (we are assuming that you had previously built the MySQL image)

```
cd CyberSecurity/SQL_Injection/sql_secure
docker-compose up
```

To stop and delete the containers you can follow the previous instructions outlined above.





