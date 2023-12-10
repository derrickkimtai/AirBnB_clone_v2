#!/usr/bin/python3
from fabric.api import env, local, put, run
import os 
import time

env.hosts = ['52.87.222.116', '54.209.112.128']

def do_pack():
    """
        store the path of the created archive
    """
    archive_path = "versions/web_static_{}.tgz".format(int(time.time()))
    local("tar -cvzf {} web_static".format(archive_path))
    return archive_path

def do_deploy(archive_path):
    """
        creates and distributes an archive to your web
    """
    if not os.path.exists(archive_path):
        return False
    put(archive_path, "/tmp/")
    run("mkdir -p /data/web_static/releases/")
    run("tar -xzf /tmp/{} -C /data/web_static/releases/".format(os.path.basename(archive_path)))
    run("rm /tmp/{}".format(os.path.basename(archive_path)))
    run("mv /data/web_static/releases/web_static/* /data/web_static/releases/")
    run("rm -rf /data/web_static/releases/web_static")
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/ /data/web_static/current")
    return True

def deploy():
    """
        Call the do_deploy(archive_path) function, using the new path of the new archive
    """
    archive_path = do_pack()
    return do_deploy(archive_path)
