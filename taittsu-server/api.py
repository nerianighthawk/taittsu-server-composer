import os
import requests
from dotenv import load_dotenv
from flask import Blueprint, jsonify


api = Blueprint('api', __name__, url_prefix='/api')

# .env ファイルから API キーを取得
load_dotenv()
X_API_KEY = os.getenv('API_KEY')

base_url = 'https://publicapi.taittsuu.com/publicapi/v0.1'
headers = {'content-type': 'application/json', 'X-API-KEY': X_API_KEY}
public_timelines = '/publictimelines'


# パブリックタイムラインの取得
@api.route(public_timelines, methods=['GET'])
def list_user():
    res = requests.get(
            f'{base_url}{public_timelines}',
            headers=headers
        )
    return res.json()


# エラーのハンドリング
@api.errorhandler(400)
@api.errorhandler(404)
def error_handler(error):
    return jsonify({'error': {
        'code': error.description['code'],
        'message': error.description['message']
    }}), error.code
