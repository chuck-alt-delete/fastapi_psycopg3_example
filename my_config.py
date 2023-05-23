from dotenv import dotenv_values
from pathlib import Path

path_to_env = Path(__file__).parent.absolute() / ".env"
# Load values from .env file into config dictionary.
# See example.env for what variables you need to define.
config = dotenv_values(path_to_env)

# Set Materialize cluster name
CLUSTER = "demo_processing"

# Create Data Source Name (DSN) string
MY_DSN_STRING = f'user={config["MZ_USER"]} password={config["MZ_PASSWORD"]} host={config["MZ_HOST"]} port={config["MZ_PORT"]} dbname={config["MZ_DB"]} sslmode=require'

if __name__=="__main__":
    print(config)
    print(MY_DSN_STRING)