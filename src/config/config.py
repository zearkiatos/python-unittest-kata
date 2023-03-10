import os
from dotenv import load_dotenv
from src.utils.pathResolver import get_project_root

class Config():

    def __init__(self):
        self.config = {}

    def get_config(self):
        env = os.getenv('ENVIRONMENT') or 'default'
        environments = {"test":".env.test", "default" : ".env"}
        path = environments[env]
        dotenv_path = str(get_project_root())+"/"+path
        load_dotenv(dotenv_path=dotenv_path)

        return {
            'ENVIRONMENT': os.getenv('ENVIRONMENT'),
            'SQLITE_CONNECTION_STRING': os.getenv('SQLITE_CONNECTION_STRING')
        }