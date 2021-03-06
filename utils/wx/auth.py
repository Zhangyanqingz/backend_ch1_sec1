import json
import requests
from backend_ch1_sec1 import settings
from authorization.models import User


def already_authorize(request):
    # 用户登录验证
    is_authorize = False
    if request.session.get('is_authorize'):
        is_authorize = True
    print(request.session.get('is_authorize'))
    return is_authorize


def get_user(request):
    if not already_authorize(request):
        raise Exception('not authorized request')
    open_id = request.session.get('open_id')
    user = User.objects.filter(open_id=open_id)[0]
    return user


def c2s(appid, code):
    return code2session(appid, code)


def code2session(appid, code):
    api = 'https://api.weixin.qq.com/sns/jscode2session'
    params = 'appid=%s&secret=%s&js_code=%s&grant_type=authorization_code' %\
             (appid, settings.WX_APP_SECRET, code)
    url = api + '?' + params
    response = requests.get(url)
    data = json.loads(response.text)
    print(data)
    return data

