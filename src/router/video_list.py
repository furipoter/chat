from flask import Blueprint

from app import s3

router = Blueprint('video_list', __name__, url_prefix='/video_list')


@router.route('/', methods=['GET'])
def get_video_list():
    list = s3.list_objects_v2(Bucket='furiosa-video', Prefix='convert/')
    if 'Contents' not in list:
        return {
            'list': [],
            'count': 0
        }
    result = []
    for item in list:
        result.append({
            'name': item['Key'].split('/')[1],
            'created_at': item['LastModified'].strftime('%Y-%m-%d %H:%M:%S')
        })
    return {
        'list': result,
        'count': len(result)
    }


@router.route('/clear_all', methods=['GET'])
def clear_all():
    list = s3.list_objects_v2(Bucket='furiosa-video', Prefix='convert/')['Contents']
    for item in list:
        s3.delete_object(Bucket='furiosa-video', Key=item['Key'])
    return {
        'message': 'All video list cleared'
    }
