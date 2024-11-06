# ETextBook

Welcome to your E-Text book application

Group (23) Member Info:

    1. Md Nazmul Haque (mhaque4)
    2. Fardin Saad (fsaad)
    3. Sanjana Cheerla (scheerl)
    4. Rawshan Mowri (rmowri)

Installation Process

1.  install mysql community server: https://dev.mysql.com/downloads/mysql/
2.  install mysql workbench: https://dev.mysql.com/downloads/workbench/
3.  install `pip install python-dotenv`
4.  setup virtual environment for python:

    `For Linux/MAC run`

    ```bash
    bash vir_env.sh
    ```

    `For Windows run`

    ```bash
    vir_env.bat
    ```

5.  Create a `.env` file and put the following info

        DB_HOST=localhost
        DB_USER=root # put your db user name
        DB_PASSWORD=root@123 #put your mysql db password
        DB_NAME=ETextBook

6.  run the code:
    ```python
    python3 app.py
    ```
