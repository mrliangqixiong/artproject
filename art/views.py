from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json
from art.models import Art


def InterfaceHandler(request):
    url = request.path
    page = request.GET.get('page', 1)
    tag = request.GET.get('tag', 1)
    # TODO, query model db data or other logic process here.
    mdict = {"url": url, "page": page, 'tag': tag}
    return HttpResponse(json.dumps(mdict))


def GetArtsHandler(request):
    import json
    arts = Art.objects.all()
    data = []
    for art in arts:
        a_title = art.a_title
        a_info = art.a_info
        a_content = art.a_content
        a_img = str(art.a_img)
        a_addtime = art.a_addtime
        a_addtime = a_addtime.strftime("%Y-%m-%d:%H:%M:%S")
        a_updatetime = art.a_updatetime
        a_updatetime = a_updatetime.strftime("%Y-%m-%d:%H:%M:%S")
        it_dict = dict(
            a_title=a_title,
            a_info=a_info,
            a_content=a_content,
            a_img=a_img,
            a_addtime=a_addtime,
            a_updatetime=a_updatetime
        )
        data.append(it_dict)
    return HttpResponse(json.dumps(data))


def TestPostHandler(request):
    import json
    if request.method == 'POST':
        # print(request.body)
        print(request.POST.get('key1'))
        # received_json_data = json.loads(request.body)
        received_json_data = {'key1': request.POST.get('key1'),
                              'status': 200,
                              'key2': request.POST.get('key2')}
        return HttpResponse(json.dumps(received_json_data))

    elif request.method == "GET":
        return HttpResponse('GET ok.')
    else:
        print('POST has error.')


def render_index(request):
    return render(request, 'statics/index.html')


'''
interface:
   /art/add?x=XXX&y=YYY
method: GET
return: JSON

{
   'code':200,
   'message':'ok',
   'data':[],
}
'''
def add_handler(request):
    x = request.GET.get('x', '1')
    y = request.GET.get('y', '1')
    ###TODO: other works, very slow operations.
    from .tasks import add
    add.delay(int(x), int(y))
    ####TODO
    res = {'code': 200, 'message': 'ok', 'data': [{'x': x, 'y': y}]}
    return HttpResponse(json.dumps(res))
