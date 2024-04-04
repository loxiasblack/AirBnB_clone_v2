#!/usr/bin/python3
"""generate .tgz archive with fabric"""

from fabric.api import task
from fabric.api import local
import os
from datetime import datetime


@task
def do_pack():
    """function that create versions directory
    with .tgz archive"""
    if not os.path.exists('versions'):
        os.makedirs('versions')
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = f"web_static_{timestamp}.tgz"
        archive_path = f"versions/{archive_name}"
        try:
            local(f"tar -czf  {archive_path} web_static")
            return archive_path
        except Exception:
            return None

