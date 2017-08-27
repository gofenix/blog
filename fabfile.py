from fabric.api import local
from fabric.decorators import task

def hello():
    print("hello world!")


def install():
    local("pip install -r requirements.txt")

@task
def runserver():
    "Run server"
    local("./growth_studio/manage.py runserver 0.0.0.0:8000")

@task
def tag_version(version):
    "Tag new version"
    local("git tag %s" %version)
    local("git push origin %s" %version)

@task
def fetch_version(version):
    "Fetch git version"
    local("wget https://codeload.github.com/zhenfeng-zhu/blog/tar.gz/%s" %version)
