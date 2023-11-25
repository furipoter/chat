from flask import Blueprint
from src.router.chat import router as chat_router
from src.router.video_list import router as video_list_router

api = Blueprint('api', __name__, url_prefix='/api')

api.register_blueprint(chat_router)
api.register_blueprint(video_list_router)
