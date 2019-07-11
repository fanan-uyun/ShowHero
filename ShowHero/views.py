from django.http import HttpResponse
from django.template import Template,Context

def say_hobby(request):
    string="""
    <html>
        <head>
            <title>hobby</title>
        </head>
        <body>
            <p>{{name.last_name}}{{name.first_name}}</p>
            <p>{{desc.11}}</p>
            <p>{{desc.upper}}</p>
        </body>
    </html>
    """
    student = {
        "name":{"first_name":"三","last_name":"张"}, #字典类型
        "desc":"this is to mi" #有序类型
    }
    t = Template(string)
    c = Context(student)
    result = t.render(c)
    return HttpResponse(result)

# for循环标签
def app_for(request):
    string="""
    <html>
        <head>
            <title>hobby</title>
            <style>
                #kw {
                    width: 700px;
                    height: 400px;
                    margin: 0 auto;
                    position: relative;
                    background-color: burlywood;
                }
                img {
                    padding-top: 40px;
                    padding-left: 20px;
                    width: 300px;
                    height: 300px;
				}
                ul {
                    display: inline-block;
                    position: absolute;
                    top: 30px;
                    left: 340px;    
                }
                li {
                    list-style: none;
                    padding-top: 20px;
                }
                .hb {
                   position: relative;
                   left: 48px; 
                   top: 1px;
                  
                }
            </style>
        </head>
        <body>
                  
            {% for line in student %}
                <div id="kw">
                    <img src='{{line.picture}}'>
                    <ul>
                        
                         <li>   <p>姓名：{{line.name}}</p> </li>
                         <li>   <p>年龄：{{line.age}}</p>  </li>
                         <li>   <p>爱好：
                                <p class="hb">{% for h,l in line.hobby.items %}
                                    {{h}}:{{l}}&emsp;
                                {% endfor %}</p>
                            </p>
                         </li>
                    </ul>
                    <br>
                    <br>
                </div>
            {% endfor %}
            
        </body>
    </html>
    """
    dicts={
        "student":[
            {
                "name":"张三",
                "age":18,
                "picture":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2793196489,3222710469&fm=26&gp=0.jpg",
                "hobby":{"吃饭":"10%","运动":"30%"}
            },
            {
                "name": "李四",
                "age": 20,
                "picture": "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1674439402,3668570019&fm=11&gp=0.jpg",
                "hobby": {"音乐": "10%", "篮球": "30%"}
            },
            {
                "name": "王五",
                "age": 21,
                "picture": "https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1146140732,1960311087&fm=26&gp=0.jpg",
                "hobby": {"跑步": "1%", "阅读": "20%"}
            },
            {
                "name": "赵柳",
                "age": 30,
                "picture": "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1112765933,1595165806&fm=15&gp=0.jpg",
                "hobby": {"放空": "2%", "爬山": "30%"}
            },
            {
                "name": "牛蛋",
                "age": 30,
                "picture": "https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2447786428,2802135137&fm=26&gp=0.jpg",
                "hobby": {"音乐": "30%", "攀岩": "30%"}
            }
        ]
    }
    t = Template(string)
    c = Context(dicts)
    result = t.render(c)
    return HttpResponse(result)

# forloop事例
def nav(request):
    string = """
        <html>
            <head>
                <title>hobby</title>
                <style>
                    li {
                        list-style: none;
                        float: left;
                    }
                </style>
            </head>
            <body>
                <ul>
                    {% for n in student %}
                        {% if forloop.last %}
                        
                            <li style="margin-left: 30px;padding-right: 15px;">
                                <a href="#">{{n}}</a>                                
                            </li>
                        {% else %}
                            <li style="margin-left: 30px;padding-right: 15px;border-right: 1px black solid;">
                                <a href="#">{{n}}</a>                                
                            </li>
                        {% endif %}
                        
                    {% endfor %}
                </ul>
            </body>
        </html>
        """
    dicts = {
        "student":["菜单","任务","导航"]
    }
    t = Template(string)
    c = Context(dicts)
    result = t.render(c)
    return HttpResponse(result)

# if判断标签
def login(request):
    string = """
        <html>
            <head>
                <title>hobby</title>
            </head>
            <body>
                {% if student %}
                    欢迎你{{student}}
                {% else %}
                    登出
                {% endif %}
            </body>
        </html>
        """
    dicts = {
        "student": ""
    }
    t = Template(string)
    c = Context(dicts)
    result = t.render(c)
    return HttpResponse(result)

# ifequal
def login_s(request):
    string = """
        <html>
            <head>
                <title>hobby</title>
            </head>
            <body>
                {% ifequal student.age 17 %}
                    欢迎你{{student.name}}
                {% else %}
                    不好意思未满足登录请求，抱歉
                {% endifequal %}
            </body>
        </html>
        """
    dicts = {
        "student": {"name":"老边","age":18}
    }
    t = Template(string)
    c = Context(dicts)
    result = t.render(c)
    return HttpResponse(result)

# 过滤器
def filter(request):
    string = """
        <html>
            <head>
                <title>hobby</title>
            </head>
            <body>
                {{student | safe}}
            </body>
        </html>
        """
    dicts = {
        "student": "<script>alert('hello')</script>"
    }
    t = Template(string)
    c = Context(dicts)
    result = t.render(c)
    return HttpResponse(result)

from django.template.loader import get_template
from django.shortcuts import render_to_response

def getTemplate(request):
    name = "张三"
    # t = get_template("index.html")
    # result = t.render(locals())
    # return HttpResponse(result)
    return render_to_response("index.html",locals())

def imgs(request):
    images=[
        'images/1.jpg',
        'images/2.jpg',
        'images/3.jpg',
        'images/4.jpg',
        'images/5.jpg',
    ]
    return render_to_response("index.html",locals())


def hero(request):
    dicts = {
        "info": [
            {
                "name": "虞姬",
                "locat": "射手",
                "picture": "images/yuji.jpg",
                "attr": {"移速":"350","攻速": "15%"}
            },
            {
                "name": "赵信",
                "locat": "打野",
                "picture": "images/hanxin.jpg",
                "attr": {"移速": "350", "攻速": "10%"}
            },
            {
                "name": "艾琳",
                "locat": "射手",
                "picture": "images/ailin.jpg",
                "attr": {"移速": "355", "攻速": "15%"}
            },
            {
                "name": "百里玄策",
                "locat": "打野",
                "picture": "images/xuance.jpg",
                "attr": {"移速": "380", "攻速": "20%"}
            },
            {
                "name": "孙尚香",
                "locat": "射手",
                "picture": "images/daxiaojie.jpg",
                "attr": {"移速": "360", "攻速": "15%"}
            },
            {
                "name": "武则天",
                "locat": "法师",
                "picture": "images/wuzetian.jpg",
                "attr": {"移速": "355", "攻速": "10%"}
            }
        ]
    }
    return render_to_response("hero.html",dicts)
