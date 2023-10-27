<h1 align="center"> MARKETING AND SALES MANAGEMENT SYSTEM </h1>

This project is my final year of high school CS project. I created python web application for managing the data of a sales and marketing management company. The Frontend is built using bootstrap and FLASK framework. The backend is handled by python and the database used to host it is MySQL. It has been built with material UI and Fluent design so make it a delight to use. 




## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install flask and mysql connector. Also make Sure [Mysql](https://dev.mysql.com/downloads/mysql/8.0.html) is running on your system. 

```bash
pip install Flask

pip install mysql-connector-python
```
To install the database, first download the userbase.sql from the repo.Then create a database in mysql named userbase and run the following commands on cmd.
```cmd
>cd C:\Program Files\MySQL\MySQL Server 8.0\bin

>mysqlimport -u <username> -p userbase <path to the downloaded userbase.sql file>

``` 

## Usage
Make sure to change the following in the app.py file .
```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = '<username>'
app.config['MYSQL_PASSWORD'] = '<password>'
app.config['MYSQL_DB'] = 'userbase'
```


## SnapShots
![image](https://user-images.githubusercontent.com/76260870/158964203-cd19e259-85d7-4c61-9f31-41077a4309fb.png)

![image](https://user-images.githubusercontent.com/76260870/158964448-f0018fef-dd6f-448b-b8dd-01bf4c18f1fb.png)

![image](https://user-images.githubusercontent.com/76260870/158964144-99ce1840-3ddd-4005-af8a-52b5eb93a1e2.png)


## Licence
[MIT](https://choosealicense.com/licenses/mit/)
