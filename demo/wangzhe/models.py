from django.db import models
'''- 1、创建一个Django项目，设计一个王者荣耀英雄类 Hero 迁移到数据库
  - 字段
    - 英雄名称 Hname
    - 英雄年纪 Hage
    - 英雄技能 Hskill
- 2、使用Django orm添加5条测试数据
- 3、使用Django完成以下API接口
  - 查询所有的英雄对象，并将英雄对象的所有信息使用jinja2模板引擎渲染到index.html'''

# Create your models here.
class Hero(models.Model):
    Hname=models.CharField(max_length=20,verbose_name='名称')
    Hage=models.IntegerField(verbose_name='年龄')
    Hskill=models.CharField(max_length=20,verbose_name='技能')

    class Meta:
        db_table = 'hero'
        verbose_name = '英雄'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Hname