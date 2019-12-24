from django.http import HttpResponse
from django.http import JsonResponse

def index(request):
    print('yes')
    return HttpResponse('hello Django')
def index1(request):
    '''设置cookie'''
    response=HttpResponse()
    response.set_cookie('name','taojin',max_age=3000)


    print(request.COOKIES.get('name'))#获取cookie的内容
    # 通过
    print(request.META['CONTENT_TYPE'])
    return JsonResponse({'name':'taojin','age':18})


    # return response 返回cookie的内容