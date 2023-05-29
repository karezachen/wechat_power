from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import hashlib

@csrf_exempt
def index(request):

    # 解析参数
    signature = request.GET.get('signature')
    echostr = request.GET.get('echostr')
    timestamp = request.GET.get('timestamp')
    nonce = request.GET.get('nonce')

    # 公众号网页后台填写的 token 值
    token = 'xxx'

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
