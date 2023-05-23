# FastAPI + Psycopg3 Example

1. Inspect the code.

1. Fill out your database connection details as environment variables in a file called `.env`

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
    This assumes you have a Postgres compatible database with a collection called `my_collection` with integer columns `a` and `b`. In my case, I use Materialize with a processing cluster called `demo_processing`.