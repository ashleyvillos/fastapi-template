#### How to make alembic work for database migration

1. Create a migration folder
    ```
    alembic init migration
    ```

2. Create a **.env** file and add these variables ***DB_USER***, ***DB_PASS***, ***DB_NAME***. Set the values based on your database configuration.

2. Go to **alembic.ini** and change ***sqlalchemy.url*** to this value:
    ```
    # use this configuration if you don't have a password. NOTE that this is for a mysql configuration
    sqlalchemy.url = mysql://%(DB_USER)s@localhost/%(DB_NAME)s 

    # use this configuration if you have a password. NOTE that this is for a mysql configuration)
    sqlalchemy.url = mysql://%(DB_USER)s:%(DB_PASS)s@localhost/%(DB_NAME)s 
    ```

3. Go to **migrations/env.py** and import these:
    ```
    from dotenv import dotenv_values
    from src.models import import_models
    ```

4. In **migrations/env.py** add these code snippets below the imports
    ```
    # this is for importing the models so that alembic migration can recognize them
    import_models()

    # This is for reading the .env file
    env = dotenv_values(".env")
    ```

5. Find the code snippet with the section: ***config = context.config*** and add these code below it:
    ```
    # here we allow ourselves to pass interpolation vars to alembic.ini
    # from the host env
    section = config.config_ini_section
    config.set_section_option(section, "DB_USER", env['DB_USER'])
    config.set_section_option(section, "DB_NAME", env['DB_NAME'])
    ```

6. Find the code snippet with the section: ***target_metadata***. Replace target_metadata with this code snippet:
    ```
    from src.utils.database import Base
    target_metadata = Base.metadata
    ```

7. Alembic setup finished! Run these in the terminal to see if the migration works
    ```
    alembic revision --autogenerate -m "initial migration"
    alembic upgrade heads
    ```

8. Check database if the changes were applied
