import json

from django.http import HttpResponse
def get_json(request):
    data = request.body#获取最原始的请求体数据 二进制bytes
    json_str = data.decode()#把原始数据转换字符串
    json_data = json.loads(json_str)#json.loads 接受数据
    print(json_data['a'])
    print(json_data['b'])
    print(request.META['CONTENT_TYPE'])
    print(request.META['CONTENT_LENGTH'])
    '''request.META  是字典类型：content_type得到的是请求体类型
     '''
    print(request.method)#
    print(request.user)
    print(request.path)
    print(request.encoding)

    return HttpResponse('ok')


