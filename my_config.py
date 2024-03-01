from dotenv import dotenv_values
from pathlib import Path

path_to_env = Path(__file__).parent.absolute() / ".env"

# Load values from .env file into config dictionary.
config = dotenv_values(path_to_env)

config["options"] = ''
if config["MZ_CLUSTER"]:
    config["options"] += f'--cluster={config["MZ_CLUSTER"]}'
else:
    config["options"] += '--cluster=quickstart'

if config["MZ_TRANSACTION_ISOLATION"]:
    config["options"] += f' -c transaction_isolation={config["MZ_TRANSACTION_ISOLATION"]}'

if config["MZ_SCHEMA"]:
    config["options"] += f' -c search_path={config["MZ_SCHEMA"]}'

if __name__=="__main__":
    print(config)