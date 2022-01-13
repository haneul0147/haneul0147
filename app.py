from flask import Flask, request
from flask_restful import Api
from flask_jwt_extended import JWTManager
from config import Config
from flask.json import jsonify
from http import HTTPStatus
from resource.login import UserLoginResource


from resource.logout import UserLogoutResource, jwt_blacklist
from resource.register import UserRegisterResource

app = Flask(__name__)

# 환경변수 셋팅
app.config.from_object(Config)

# JWT 토큰 만들기
jwt = JWTManager(app)

# todo : 로그아웃 개발하고 나서, 코멘트 해제한다.
@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload) :
    jti = jwt_payload['jti']
    return jti in jwt_blacklist

api = Api(app)

# 경로와 리소스를 연결한다.
api.add_resource(UserRegisterResource, '/api/v1/user/register')
api.add_resource(UserLoginResource, '/api/v1/user/login')
api.add_resource(UserLogoutResource, '/api/v1/user/logout')



if __name__ == '__main__' :
    app.run()
