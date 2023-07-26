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
public_timelines_url = '/publictimelines'
users_url = '/users'
taiitsus_url = '/taiitsus'
liking_users_url = '/liking_users'
following_url = '/following'
followers_url = '/followers'
search_uel = '/search'


# パブリックタイムラインの取得
@api.route(public_timelines_url, methods=['GET'])
def public_timelines():
    print(f'{base_url}{public_timelines_url}')
    res = requests.get(
            f'{base_url}{public_timelines_url}',
            headers=headers
        )
    return res.json()


# ユーザーのタイーツ取得
@api.route(f'{users_url}/<user_id>{taiitsus_url}')
def user_taiitsus(user_id):
    res = requests.get(
            f'{base_url}{users_url}/{user_id}{taiitsus_url}',
            headers=headers
        )
    return res.json()


# タイーツ情報取得
@api.route(f'{taiitsus_url}/<taiitsu_id>')
def taiitsu(taiitsu_id):
    res = requests.get(
            f'{base_url}{taiitsus_url}/{taiitsu_id}',
            headers=headers
        )
    return res.json()


# タイーツのいいね一覧取得
@api.route(f'{taiitsus_url}/<taiitsu_id>{liking_users_url}')
def liking_users(taiitsu_id):
    res = requests.get(
            f'{base_url}{taiitsus_url}/{taiitsu_id}{liking_users_url}',
            headers=headers
        )
    return res.json()


# ユーザー情報取得
@api.route(f'{users_url}/<user_id>')
def user(user_id):
    res = requests.get(
            f'{base_url}{users_url}/{user_id}',
            headers=headers
        )
    return res.json()


# ユーザーのフォロー一覧取得
@api.route(f'{users_url}/<user_id>{following_url}')
def user_following(user_id):
    res = requests.get(
            f'{base_url}{users_url}/{user_id}{following_url}',
            headers=headers
        )
    return res.json()


# ユーザーのフォロワー一覧取得
@api.route(f'{users_url}/<user_id>{followers_url}')
def user_followers(user_id):
    res = requests.get(
            f'{base_url}{users_url}/{user_id}{followers_url}',
            headers=headers
        )
    return res.json()


# ユーザー検索
@api.route(f'{search_uel}{users_url}')
def search_users():
    res = requests.get(
            f'{base_url}{search_uel}{users_url}',
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
