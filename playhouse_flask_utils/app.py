from flask import Flask
from playhouse.flask_utils import FlaskDB

# 从当前目录下的config模块导入
from .config import Config

app = Flask(__name__)

db_wrapper = FlaskDB(app, Config.DATABASE_URL)
db = db_wrapper.database




