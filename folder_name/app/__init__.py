from flask import Flask

app = Flask(__name__)

# The bottom import is a well known workaround that avoids circular imports, a common problem with Flask applications.
from app import routes
