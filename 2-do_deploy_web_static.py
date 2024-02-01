#!/usr/bin/python3
"""deploy and the archive to the web server"""

from fabric.api import env, run, put
import os

env.hosts = ["18.233.64.198", "100.26.158.144"]
env.user = "ubuntu"
env.key_filename = "./school"


def do_deploy(archive_path):
    """deploy my archive path in the web server"""
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")

        archive_filename = os.path.basename(archive_path)
        folder_name = archive_filename.split('.')[0]
        target_dir = f"/data/web_static/releases/{folder_name}"

        run(f"mkdir -p {target_dir}")
        run(f"tar -xzf /tmp/{archive_filename} -C {target_dir}")
        run(f"rm /tmp/{archive_filename}")

        run(f"rm -f /data/web_static/current")
        run(f"ln -s {target_dir}/ /data/web_static/current")
        return True
    except Exception:
        return False


archiv_path = "./versions/web_static_20240201013448.tgz"
