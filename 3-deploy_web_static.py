#!/usr/bin/python3
"""Fabric script to create and distribute an archive to web servers."""

from fabric.api import env, local, put, run
import os
from datetime import datetime

env.hosts = ['18.233.64.198', '100.26.158.144']
env.user = 'ubuntu'
env.key_filename = './school'

def do_pack():
    """Generates a .tgz archive from the contents of the web_static."""
    try:
        if not os.path.exists('versions'):
            os.makedirs('versions')
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = f"versions/web_static_{timestamp}.tgz"
        local(f"tar -cvzf {archive_path} web_static")
        return archive_path
    except Exception:
        return None

def do_deploy(archive_path):
    """Deploys an archive to web servers."""
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        archive_filename = os.path.basename(archive_path)
        folder_name = archive_filename.split('.')[0]
        target_dir = f"/data/web_static/releases/{folder_name}"
        run(f"sudo mkdir -p {target_dir}")
        run(f"sudo tar -xzf /tmp/{archive_filename} -C {target_dir}")
        run(f"sudo rm -rf /tmp/{archive_filename}")
        run(f"sudo rm -f /data/web_static/current")
        run(f"sudo ln -s {target_dir}/web_static/ /data/web_static/current")
        return True
    except Exception:
        return False

def deploy():
    """Creates and distributes an archive to web servers."""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

