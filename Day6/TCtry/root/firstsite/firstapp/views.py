from django.shortcuts import render,HttpResponse
from firstapp.models import People
from django.template import Context,Template

# Create your views here.
def first_try(request):
    #由于没有数据，所以只好先创建一个数据，再使用数据
    person = People(name='Spock',job='officer')
    html_string = '''
        <html>
            <head>
                <meta charset="utf-8">
                <title>firstapp</title>
            </head>
            <body>
                <h1>
                    Hello, {{ person.name }}
                </h1>
            </body>
        </html>
    '''
    t = Template(html_string)#将其变成模板
    c = Context({'person':person})#获取数据库信息生成上下文
    web_page = t.render(c)#进行渲染
    return HttpResponse(web_page)
