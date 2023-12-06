#!/usr/bin/python3
"""
    Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric import task
from datetime import datetime
import os

@task
def do_pack():
    current_time = datatime.utcnow().strftime('%Y%m%d%H%M%S')
    archive_name = f"web_static_{current_time}.tgz"
    version_folder = "versions"
    web_static_folder = "web_static"

    if not os.path.exists(version_folder):
        os.makedirs(version_folder)

    archive_path = f"{version_folder}/{archive_name}"

    command = f"tar -cvzf {archive_path} {web_static_folder}"
    result = os.system(command)

    if result == 0:
        return archive_path
    else:
        return None
