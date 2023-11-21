import os 
import importlib

def get_routers():
    routers = []
    for filename in os.listdir('src/routes'):
        # exclude __init__.py and __pycache__
        if filename.endswith('.py') and filename != "__init__.py":
            route = filename[:-3]  # url prefix
            module = importlib.import_module(f'.{route}', package='src.routes')  # get module
            routers.append(module.router) # append router

    return routers
