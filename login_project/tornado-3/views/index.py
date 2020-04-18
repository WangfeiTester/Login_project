from tornado.web import  RequestHandler
import json
import config
import os

class IndexHandler(RequestHandler):
    def get(self,*arg,**argv):
        print("wangfei")
        self.write("hello home ")
# 参数解析示例
class ParmHandler(RequestHandler):
    def initialize(self,name,passwd):
        self.name = name
        self.passwd=passwd
    def get(self,*arg,**argv):
        self.write(self.name+self.passwd)
        self.write("hell0 parm")
#发送Json数据 字典格式发送给
class JsonHandler(RequestHandler):
    def get(self,*arg,**argv):
        dic = {
            "name":"wangfei",
            "passwd":"123456"
        }
        self.write(dic)
        self.write("hello json")
#Json格式发送数据
class JsonHandler1(RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type","application/json; charset=UTF-8")
        self.set_header("name","name")

    def get(self,*arg,**argv):
        dic = {
            "name":"wangfei",
            "passwd":"123456"
        }
        jsondumps = json.dumps(dic)
        self.set_header("Content-Type","application/json; charset=UTF-8")
        #self.set_header("name", "myname")
        self.write(jsondumps)
        self.write("hello json1")

# 设置响应状态码
class  StatusHandler(RequestHandler):
    def get(self):
        self.set_status(404,"who i am")
        #self.set_status(999) 报错
        #self.set_status(999,"name") 正常  状态码为未知的必须加原因
        self.write("******8")
        self.write("hello status")

#请求错误处理
class ErrorHandler(RequestHandler):
    def write_error(self, status_code):
        print("status_code: %s"%status_code)
        self.set_status(status_code)
        pass
    def get(self,*arg,**argv):
        self.send_error(404)

#重定向
class RedirectHandler(RequestHandler):
    def get(self,*arg,**argv):
        #self.redirect("/")
        #self.write("<a href='/weburl'>去另一个页面</a>")
        url = self.reverse_url("webname")
        print(url)
        self.write("<a href='%s'>去另一个页面</a>"%url)

# 参数解析和 函数执行顺序
class WeburlHandler(RequestHandler):
    def prepare(self):
        print("prepare")
    def initialize(self,name1,passwd1):
        print("initialize")
        self.name = name1
        self.passwd=passwd1
    def get(self,*arg,**argv):
        print("get")
        self.write(self.name)
        self.write(self.passwd)
        self.write("hello weburl")
    def on_finish(self):
        #常用于处理请求结束后进行资源处理和日志
        print("onfinish")

# 参数传递 获取/data/(?P<p1>\w+)/(?P<p3>\w+)/(?P<p2>\w+) 中的数据
class DataHandler(RequestHandler):
    def get(self,p1,p2,p3,*arg,**argv):
        content = p1+'_'+p2+'_'+p3
        self.write(content)

#参数解析 获取get请求中的数据 /data？a=1&b=2&c=3
class GetdataHandler(RequestHandler):
    def get(self,*arg,**argv):
        #http://localhost:8080/getdata?a=1&b=2&c=3
        a = self.get_query_argument('a',default="1",strip=True)
        b = self.get_query_argument('b',default='2',strip=True)
        c = self.get_query_argument('c',default="3",strip=True)
        self.write(a+b+c)

#参数解析 获取get请求中的数据 /data？a=1&a=2&a=3
class GetdatasHandler(RequestHandler):
    def get(self,*arg,**argv):
        #http://localhost:8080/getdata?a=1&a=2&b=3
        a = self.get_query_arguments('a',strip=True)
        print(a)
        a=str(a)
        self.write(a)

# 处理 Post请求
class PostHandler(RequestHandler):
    def get(self):
        self.render("logintest.html")
    def post(self):
        name = self.get_body_argument("username",strip=True)
        passwd = self.get_body_argument("passwd",strip=True)
        hobby = self.get_body_arguments("hobby")
        print(name)
        print(hobby)
        print(passwd)
        self.write("login success")

# 处理 request 对象属性
class ReqtHandler(RequestHandler):
    def get(self):
        print("---------------------方法")
        print(self.request.method)
        print("---------------------请求头")
        print(self.request.headers)
        print("---------------------被请求主机")
        print(self.request.host)
        print("---------------------请求的完整资源地址")
        print(self.request.uri)
        print("---------------------请求http版本")
        print(self.request.version)
        print("---------------------请求参数部分")
        print(self.request.query)
        print("---------------------用户上传文件")
        print(self.request.files)
        print("---------------------请求体数据")
        print(self.request.body)
        print("---------------------path")

        print(self.request.path)
        print("---------------------客户端ip")
        print(self.request.remote_ip)
        print("---------------------request")
        print(self.request)
        self.write("ok")
# post 文件请求
class UploadHandler(RequestHandler):
    def get(self):
        self.render("uploadfile.html")
    def post(self,*arg,**argv):
        #filename
        #body
        #content-type
        files = self.request.files
        print(files)
        filearry = files["file"]
        for fileobj in filearry:
            name=os.path.join(config.BASE_PATH,"upfile"+os.sep+fileobj["filename"])
            with open(name,'wb') as fp:
                fp.write(fileobj["body"])
            print(fileobj["filename"])
            print(fileobj["content_type"])
        filearry = files["img"]
        for fileobj in filearry:
            name = os.path.join(config.BASE_PATH, "upfile" +os.sep+fileobj["filename"])
            with open(name,'wb') as fp:
                fp.write(fileobj["body"])
            print(fileobj["filename"])
            print(fileobj["content_type"])
        self.write("OK")
        pass


