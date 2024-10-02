# myapp.wsgi
import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/meteireann')

from data import app as application
