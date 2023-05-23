from dotenv import dotenv_values
from pathlib import Path

path_to_env = Path(__file__).parent.absolute() / ".env"
# Load values from .env file into config dictionary.
# See example.env for what variables you need to define.
config = dotenv_values(path_to_env)

# Set Materialize cluster name
CLUSTER = config["CLUSTER"] if config["CLUSTER"] else "default"

# Replace the @ symbol of your Materialize user email with %40 for the postgres connection string
config["MZ_USER"] = config["MZ_USER"].replace('@','%40')

# Create Data Source Name (DSN) string, including Materialize cluster the query will run on
MY_DSN_STRING = f'''postgresql://{config["MZ_USER"]}:{config["MZ_PASSWORD"]}@{config["MZ_HOST"]}:{config["MZ_PORT"]}/{config["MZ_DB"]}?options=--cluster%3D{CLUSTER}&sslmode=require'''

if __name__=="__main__":
    print(config)
    print(MY_DSN_STRING)