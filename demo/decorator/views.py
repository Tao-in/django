from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
#method_decorator 适用于类视图方法的装饰器


def my_decorator(func):
    def wrapper(request,*args,**kwargs):
        print('zhaungshi')
        print(request.path)
        return func(request,*args,**kwargs)
    return wrapper
#
# @method_decorator(my_decorator,name='get')#为一种指定的函数进行装饰
# @method_decorator(my_decorator,name='dispatch')#dispatch为全部请求方法进行装饰@method_decorator

# '''Mixin扩展类'''
# class FirstMixin(object):
#     @classmethod#重写的意思
#     def as_view(cls,*args,**kwargs):
#         view=super().as_view(*args,**kwargs)
#         view=my_decorator(view)
#         return view
class Dname(View):


    def get(self,request):
        print('leizhong get')
        return HttpResponse('ok')


    def post(self,request):
        print('leizhong get')
        return HttpResponse('ok')
