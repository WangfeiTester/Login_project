import os

BASE_PATH = os.path.dirname(__file__)
options = {
    'port':8080,
}
settings = {
    'static_path':os.path.join(BASE_PATH,"static"),
    'template_path':os.path.join(BASE_PATH,"template"),
    'debug':True,
        #自动重启
    'autoreload':True,
    #取消缓冲编译的模板
    'com_piled_template_cache':True,
    #取消缓存静态文件的hash
    'static_has_cache':False,
    #提供追踪信息
    'server_traceback':True


}