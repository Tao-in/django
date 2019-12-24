from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo,HeroInfo
from django.views import View


class Createview(View):
    def get(self,request):
        # HeroInfo.objects.create(
        #     hname='悟空',
        #     hgender=0,
        #     hcomment='七十二变',
        #     hbook_id=6,
        # )
        #删除 HeroInfo.objects.filter(id=24).delete()
        HeroInfo.objects.filter(hname='孙悟空').update(hname='齐天大圣孙悟空')
        return HttpResponse('ok')
