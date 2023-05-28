from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):

    # 获取请求中携带的字典
    data = request.GET

    # 解析字典
    signature = data.get('signature')
    timestamp = data.get('timestamp')
    nonce = data.get('nonce')
    echostr = data.get('echostr')

    # 公众号网页后台填写的 token 值
    token = "xxx"

    # 数据加密
    list = [token, timestamp, nonce]
    list.sort()
    sha1 = hashlib.sha1()
    sha1.update(''.join(list).encode('utf-8'))
    hashcode = sha1.hexdigest()

    # 签名验证
    if hashcode == signature:
        return HttpResponse(echostr)
    else:
        return HttpResponse('')
