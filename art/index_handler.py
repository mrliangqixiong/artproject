#!/usr/bin/env python  
# encoding: utf-8  


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from art.models import Art, Tag
import logging
logger = logging.getLogger('django')

def IndexHandler(request):
    '''
    :param request:  输入
    :return: render the index.html   输出
    '''
    logger.warning("IndexHandler request Handler begin")
    url = request.path
    # page is the selected current page 被选中的当前页
    # page是第几页
    page = request.GET.get('page', 1)
    logger.error("the page is error with : " + str(page))
    # t is the selected tag , t:  标签类别，整数标识  eg: 0--全部   1--爱情小说  2—科幻小说
    t = request.GET.get('t', 0)  # 取出所有数量
    logger.debug("the param page " + str(page) + ", tag:" + str(t))
    # get方法取提字符串
    page = int(page)
    t = int(t)
    total = 0
    if t == 0:  # 等于0 表示全部
        art_set = Art.objects.all()
        total = art_set.count()
    else:  # 不等于0 ,表示联合
        tag_id = int("{0}".format(t))
        art_set = Art.objects.filter(a_tag_id=tag_id)  # 在全部中根据id查找
        total = art_set.count()
    # print('query total:' + str(total) + ', t:' + str(t) + ', page:'+ str(page))
    logger.debug('query total:' + str(total) + ', t:' + str(t) + ', page:' + str(page))
    tags = Tag.objects.all()
    # 初始化一个字典
    context = dict(
        pagenum=1,
        total=0,
        prev=1,
        next=1,
        pagerange=range(1, 2),
        data=[],
        url=request.path,
        tags=tags,
        page=page,
        t=t
    )
    if total > 0:
        shownum = 20  # 一行显示20个
        import math  # 向上取整
        pagenum = math.ceil(total / shownum)  # 共有多少页
        if page < 1:
            url = request.path + "?page=1&t=1"
            return HttpResponseRedirect(url)
        if page > pagenum:
            url = request.path + "?page=%s&t=%s" % (pagenum, t)
            return HttpResponseRedirect(url)
        offset = (page - 1) * shownum  # 偏移量
        if t == 0:  # 提取所有数据
            data = Art.objects.all()[offset:shownum + offset]  # 切片,在取出所有的数据中只显示输入的页面数据,比如取第3页数据
        else:
            data = Art.objects.filter(a_tag_id=t)[offset:shownum + offset]
        btnum = 5
        if btnum > pagenum:
            firstpage = 1
            lastpage = pagenum
        else:
            if page == 1:
                firstpage = 1
                lastpage = btnum
            else:
                firstpage = page - 2
                lastpage = page + btnum - 3
                if firstpage < 1:
                    firstpage = 1
                if lastpage > pagenum:
                    lastpage = pagenum
        prev = page - 1  # 前一页
        next = page + 1  # 下一页
        if prev < 1:
            prev = 1
        if next > pagenum:
            next = pagenum

        context = dict(
            pagenum=pagenum,
            total=total,
            prev=prev,
            next=next,
            pagerange=range(firstpage, lastpage + 1),
            data=data,
            url=request.path,
            tags=tags,
            page=page,
            t=t
        )
    logger.warning("IndexHandler request Handler end")
    return render(request, "home/index.html", context=context)
# pass
