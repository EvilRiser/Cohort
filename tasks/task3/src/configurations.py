import os
from dotenv import load_dotenv, find_dotenv

# load_dotenv(find_dotenv())
env_file = find_dotenv(".env.dev")
load_dotenv(env_file)

user_name = os.getenv("USER_NAME", "my_username")
password = os.getenv("PASSWORD", "my_pwd")
