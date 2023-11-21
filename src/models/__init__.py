import os, importlib

# dynamic loading of models
def import_models():
    print('IMPORTING')
    for filename in os.listdir('src/models'):
        # filter files and import modules dynamically
        if filename.endswith('.py') and filename != "__init__.py":
            module = importlib.import_module(f'.{filename[:-3]}', package='src.models')