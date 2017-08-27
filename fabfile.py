from fabric.api import local

def hello():
    print("hello world!")


def install():
    local("pip install -r requirements.txt")

def runserver():
    local("./growth_studio/manage.py runserver 0.0.0.0:8000")
