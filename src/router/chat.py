from flask import Blueprint, request, jsonify

from src.db import db
from src.db.chat import Chat

router = Blueprint('chat', __name__, url_prefix='/chat')


@router.route('create', methods=['POST'])
def create_chat():
    data = request.get_json()
    chat = Chat(
        video_name=data['video_name'],
        content=data['content'],
    )
    db.session.add(chat)
    db.session.commit()
    return jsonify({
        'message': 'success'
    }), 200


@router.route('list', methods=['GET'])
def chats():
    video_name = request.args.get('video_name', "")

    # video_name none 일 경우
    if video_name == "":
        chats = Chat\
            .query \
            .order_by(Chat.created_at.desc()).all()

    else:
        chats = Chat \
            .query \
            .filter_by(video_name=video_name) \
            .order_by(Chat.created_at.desc()).all()

    if chats is None:
        chats = []

    result = []
    for chat in chats:
        result.append({
            'video_name': chat.video_name,
            'content': chat.content,
            'created_at': chat.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })

    return jsonify({
        'chats': result
    }), 200
