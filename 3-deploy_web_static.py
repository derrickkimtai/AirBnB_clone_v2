#!/usr/bin/python3
from fabric.api import env, local, put, run
import os 
import time

env.hosts = ['52.87.222.116', '54.209.112.128']

def do_pack():
    # Define the path of the archive
    archive_path = "versions/web_static_{}.tgz".format(int(time.time()))
    # Use tar to create the archive
    local("tar -cvzf {} web_static".format(archive_path))
    # Return the path of the archive
    return archive_path

def do_deploy(archive_path):
    # Check if the archive exists
    if not os.path.exists(archive_path):
        return False
    # Upload the archive to the servers
    put(archive_path, "/tmp/")
    # Extract the archive on the servers
    run("mkdir -p /data/web_static/releases/")
    run("tar -xzf /tmp/{} -C /data/web_static/releases/".format(os.path.basename(archive_path)))
    # Remove the archive from the servers
    run("rm /tmp/{}".format(os.path.basename(archive_path)))
    # Move the files to the current directory
    run("mv /data/web_static/releases/web_static/* /data/web_static/releases/")
    # Remove the old directory
    run("rm -rf /data/web_static/releases/web_static")
    # Remove the current directory
    run("rm -rf /data/web_static/current")
    # Create a symbolic link to the new directory
    run("ln -s /data/web_static/releases/ /data/web_static/current")
    return True

def deploy():
    # Call do_pack and store the path of the archive
    archive_path = do_pack()
    # Call do_deploy with the path of the archive
    return do_deploy(archive_path)
