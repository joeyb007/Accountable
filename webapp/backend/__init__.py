import eventlet
# Patches standard libraries prior to imoporting them
eventlet.monkey_patch()
from flask import Flask
# using SocketIO to run the app will enable realtime bidirectional communication between the frontend and backend
from flask_socketio import SocketIO
# CORS will allow frontend and backend communications to all routes
from flask_cors import CORS


app = Flask(__name__)
# NOT SAFE FOR PRODUCTION - CHANGE ALLOWED ORIGINS TO SOLELY FRONTEND DOMAIN IN FIRST PUSH  
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
socket_io = SocketIO(app, cors_allowed_origins="*", async_mode = 'eventlet')

from webapp.backend import routes