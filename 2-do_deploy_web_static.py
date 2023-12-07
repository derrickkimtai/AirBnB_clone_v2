#!/usr/bin/python3
"""
    fabric script that distributes an archive to web servers using webservers using do_deploy function
"""
from fabric.api import env, run, put
import os

env.hosts = ['52.87.222.116', '54.209.112.128']

def do_deploy(archive_path):
    """
        Distribute an archive to the web server
        Args:
        archive_path (str): The path to the archive to be distributed.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        file_name = archive_path.split('/')[-1]
        folder_name = file_name.split('.')[0]

        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}/'.format(folder_name))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(file_name, folder_name))
        run('rm /tmp/{}'.format(file_name))
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(folder_name, folder_name))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(folder_name))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(folder_name))

        return True
    except Exception as e:
        print(e)
        return False
