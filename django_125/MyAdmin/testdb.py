# -*- coding:utf-8 -*-

from django.http import HttpResponse
from MyAdmin.blog.models import SfhdPredictDataTest

#从数据库获取数据
def testdb(request):
    #初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = SfhdPredictDataTest.objects.all()

    #filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = SfhdPredictDataTest.objects.filter(time=1470758979)

    #获取单个对象
    response3 = SfhdPredictDataTest.objects.get(time=1470758988)

    #限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    SfhdPredictDataTest.objects.order_by('time')[0:2]

    # 数据排序
    SfhdPredictDataTest.objects.order_by("sample_model_predict_1")

    # 上面的方法可以连锁使用
    SfhdPredictDataTest.objects.filter(time=1470758988).order_by("sample_model_predict_1")

    #输出所有数据

    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")
