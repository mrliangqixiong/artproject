#!/usr/bin/env python  
# encoding: utf-8  

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from art.models import Art, Tag
from django.db.models import Q

'''
函数名： SearchHandler
接口URL：/art/search?key=XXX&page=1
      方法：GET
      输入参数说明：
          key: 搜索的关键词
          page: 获取第几页
     输出：
          渲染搜索列表页面
'''
def SearchHandler(request):
	key = request.GET.get('key', '')
	page = request.GET.get('page', 1)
	total = 0
	if key == "":
		return HttpResponseRedirect('/art/index')
	else:
		page = int(page)
		art_sets = Art.objects.filter(Q(a_title__contains=str(key))
									| Q(a_content__contains=str(key))
									| Q(a_info__contains=str(key))).distinct()
		total = art_sets.count()

		shownum = 10
		import math
		pagenum = int(math.ceil(total / shownum))
		if page < 1:
			return HttpResponseRedirect(request.path + "?page=%d&key=%s" % (1, key))
		if page > pagenum:
			return HttpResponseRedirect(request.path + "?page=%d&key=%s" % (pagenum, key))
		offset = (page - 1) * shownum
		art_list = Art.objects.filter(Q(a_title__contains=str(key))
				   | Q(a_content__contains=str(key))
				   | Q(a_info__contains=str(key))).distinct()

		data = art_list[offset:(shownum + offset)]
		btnnum = 5
		if btnnum > pagenum:
			firstpage = 1
			lastpage = pagenum
		else:
			if page == 1:
				firstpage = 1
				lastpage = btnnum
			else:
				firstpage = page - 2
				lastpage = page + btnnum - 3
				if firstpage < 1:
					firstpage = 1
				if lastpage > pagenum:
					lastpage = pagenum
		prev = page - 1
		next = page + 1
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
			key=key,
			page=page
		)
		return render(request, "home/search.html", context=context)

