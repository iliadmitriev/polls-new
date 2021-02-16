"""

This file is only use for Mac OS High Sierra and higher.
In order for django tests to work parallel

it changes process start method from spawn to fork

related bugs
https://code.djangoproject.com/ticket/31169
https://code.djangoproject.com/ticket/31116

read more about solution
https://adamj.eu/tech/2020/07/21/how-to-use-djangos-parallel-testing-on-macos-with-python-3.8-plus/

read more about multiproseccing
https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods

How to use

python3 manage.py test --parallel --settings=mysite.settings-test-macos

"""
import multiprocessing as mp
mp.set_start_method('fork', force=True)

from .settings import *

