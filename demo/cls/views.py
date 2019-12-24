from django.http import HttpResponse
from django.views.generic import View
class Name(View):
    def get(self,requset):
        print('f')
        return HttpResponse('get')

    def post(self,requset):
        print('post')
        return HttpResponse('post')
