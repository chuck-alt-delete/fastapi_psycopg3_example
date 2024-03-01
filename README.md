# FastAPI + Psycopg3 Example

1. Inspect the code.

1. Fill out your database connection details as environment variables in a file called `.env`. Here is an example:
    ```
    export MZ_HOST=<id>.<region>.aws.materialize.cloud
    export MZ_USER=chuck@materialize.com
    export MZ_PASSWORD=<app password>
    export MZ_PORT=6875
    export MZ_DB=materialize
    export MZ_CLUSTER=chuck
    export MZ_SCHEMA=public
    export MZ_TRANSACTION_ISOLATION=serializable
    ```

1. Install dependencies.
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

3. Run the FastAPI server.
    ```bash
    uvicorn main:app
    ```

4. Access the endpoint.
    ```bash
    curl -L localhost:8000/my_data
    ```
    ```json
    {"data":[{"a":0,"b":0},{"a":0,"b":1},{"a":1,"b":0},{"a":1,"b":1},{"a":2,"b":0}]}
    ```
    This assumes you have a Postgres compatible database with a collection called `my_collection` with integer columns `a` and `b`.