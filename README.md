# MEPhI PUTR

## Requirements
1. Python 3.6 or higher
1. MySQL

## How to start
1. Install dependencies  
    ```bash
    $ pip3 install -r requirements.txt 
    ```
2. Run MySQL server locally
3. Create database **`putr_db`** with
   ```bash
   $ sudo service mysql start
   ```
4. Make django migrations
    ```bash
    $ python3 manage.py makemigrations
    ```
5. Run django migration
    ```bash
    $ python3 manage.py migrate
    ```
6. Run django server
    ```bash
    $ python3 manage.py runserver
    ```
   
## Contributing

## Maintainers
Artem Kutuzov (architect) [@ArtemCoolAc](https://github.com/ArtemCoolAc)  
