from django.http import HttpResponse
'''查询字符串传参'''
def query_str(request):
    print(request.GET.get('a'))
    print(request.GET.get('b'))
    print(request.GET.getlist('a'))


    return HttpResponse('hh')

'''路径传参'''
def weather(request,city,yead):
    print('a=%s'%yead)
    print('b=%s'%city)
    return HttpResponse('hh')
