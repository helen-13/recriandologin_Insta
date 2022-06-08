from confg import app_config, app_active
from app import  create_app

config= app_config[app_active]
if __name__=='__main__':