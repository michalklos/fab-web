import web
import fabfile
import inspect
import simplejson as json
from fabric.api import env

def GET(obj):
    """Generic GET function that is added to fabfile function classes
       Accepts arguments as query string
    """
    fn=getattr(obj, obj.__class__.__name__)
    query_string_params=web.input() #get query string data
    #set fabric env singleton with variables that match
    for k,v in query_string_params.items():
        if env.has_key(k):
            env[k]=v
            del(query_string_params[k])
    return fn(**query_string_params)

def POST(obj):
    """Generic POST function that is added to fabfile function classes
       Accepts JSON data only
    """
    fn=getattr(obj, obj.__class__.__name__)
    data_params=dict(json.loads(web.data())) #get posted data
    #checks for a env dictionary to set fabric env singleton
    if data_params.has_key('env'):
        for k,v in data_params['env'].items():
            env[k]=v
        del(data_params['env'])
    return fn(**data_params)

def get_fab_url_classes():
    """Takes functions in fabfile, wraps them in same-named class
       Attaches original function to class as staticmethod
       Adds generic GET and POST methods to class
    """
    urls=()
    fab_classes={}
    for name, f in inspect.getmembers(fabfile):
        if inspect.isfunction(f):
            urls += ('/'+name, name)
            fns={}
            fns[name]=staticmethod(f)
            fns['GET']=GET
            fns['POST']=POST
            fab_classes[name]=type(name, (object,), fns)
    return (urls,fab_classes)

if __name__ == "__main__":
    """
    """
    fab_url_classes=get_fab_url_classes()
    app = web.application(*fab_url_classes)
    app.run()
