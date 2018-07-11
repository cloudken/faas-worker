
from datetime import datetime
import logging
import sys
import uuid


LOG = logging.getLogger(__name__)


def generate_uuid():
    """Creates a random uuid string.

    :returns: string
    """
    return str(uuid.uuid4())


def import_module(import_str):
    """Import a module.

    .. versionadded:: 0.3
    """
    __import__(import_str)
    return sys.modules[import_str]


def try_import(import_str, default=None):
    """Try to import a module and if it fails return default."""
    try:
        return import_module(import_str)
    except ImportError:
        return default


def get_resource(resource_name, version):
    res = 'cloudframe.resource.' + version + '.' + resource_name
    return import_module(res)


def set_start_time():
    global START_TIME
    START_TIME = datetime.now()


def get_start_time():
    global START_TIME
    return START_TIME
