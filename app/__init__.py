from flask import Flask

# Tell Flask where to find templates and static files
app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Register routes after app is created
from app.routes import main
app.register_blueprint(main)
