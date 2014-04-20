#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wowtest.settings.devel")

    from django.core.management import execute_from_command_line

    import pymysql
    pymysql.install_as_MySQLdb()

    execute_from_command_line(sys.argv)
