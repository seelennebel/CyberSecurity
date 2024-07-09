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

## How to test

### SQL-vulnerable website
You can, of course, try to inject SQL into the signup page, but it is on purpose not designed for testing SQL injections!!!

Please, follow these steps to test the SQL-vulnerable website:

- Try to type something like "python" or "c++" on the home page search box and press the "search" button to verify that the website works
- Then, you can try to inject the SQL statement:
```
" OR 1=1;#
```
This statement will show you all users without specifying the language explicitly

- The actual experiment doesn't require this step, but to simulate a real-world attack vector we included it. As you don't know the name of the database, you can simulate brute-forcing the database name by injecting these queries:
```
" OR 1=1; use <brute-force name>;#
```
If a specific database exists, the website will return all users without any problems. Otherwise, the website will make a request but will never get a response. At this point, you should stop loading the page and try a new database name.

- Finally, when we know the database name, we can drop it. The experiment doesn't require you to actually find it and you can use the below command to drop the website's database:
```
" OR 1=1; drop database website;#
```
After that, you can try to type "python" or "c++" into the search bar and see that it doesn't work anymore =) 

### SQL-secure website
You can try to complete all previous steps, but in this case, hopefully, our website is protected enough to prevent SQL injections





