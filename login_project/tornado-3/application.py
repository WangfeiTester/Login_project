import tornado.web
import config
from views import index

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/',index.IndexHandler),
            (r'/parm',index.ParmHandler,{"name":"wangfei","passwd":"123456"}),
            (r'/json',index.JsonHandler),
            (r'/json1', index.JsonHandler1),
            (r'/status',index.StatusHandler),
            (r'/error',index.ErrorHandler),
            (r'/redict',index.RedirectHandler),
            (r'/data/(?P<p1>\w+)/(?P<p3>\w+)/(?P<p2>\w+)', index.DataHandler),
            (r'/getdata',index.GetdataHandler),
            (r'/getdatas', index.GetdatasHandler),
            (r'/post',index.PostHandler),
            (r'/req',index.ReqtHandler),
            (r'/uploadfile',index.UploadHandler),
            tornado.web.url(r'/weburl',index.WeburlHandler,{"name1":"wangfei","passwd1":"123456"},name="webname"),




        ]
        super(Application,self).__init__(handlers,**config.settings)

