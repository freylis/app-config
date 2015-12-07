# coding: utf-8
import os
import sys
import configparser

from .exceptions import BadValueError


config = configparser.ConfigParser()
config_path = os.path.join(
    os.path.dirname(os.path.abspath(sys.argv[0])),
    'appconfig.ini',
)
config.read(config_path)


bool_values = {

    # True values
    True: True,
    1: True,
    '1': True,
    'True': True,
    'true': True,
    'TRUE': True,
    'Да': True,
    'да': True,
    'ДА': True,
    'Yes': True,
    'yes': True,
    'YES': True,

    # False values
    False: False,
    0: False,
    '0': False,
    'False': False,
    'false': False,
    'FALSE': False,
    'нет': False,
    'Нет': False,
    'НЕТ': False,
    'no': False,
    'No': False,
    'NO': False,
}


def _get_value(section, param, lazy=True, default=None):
    try:
        return config.get(section, param)
    except (configparser.NoOptionError, configparser.NoSectionError):
        if lazy:
            return None
        if default is not None:
            return default
        raise BadValueError('Bad value for %r.%r in file %r' % (section, param, config_path))


def get_str(section, param, lazy=True, default=None):
    value = _get_value(section, param, lazy=lazy, default=default)
    if (value is None) and lazy:
        return None
    return str(value)


def get_float(section, param, lazy=True, default=None):
    value = _get_value(section, param, lazy=lazy, default=default)
    if (value is None) and lazy:
        return None
    try:
        return float(value)
    except ValueError:
        if lazy:
            return None
        raise BadValueError('Incorrect value %r for float' % value)


def get_int(section, param, lazy=True, default=None):
    value = _get_value(section, param, lazy=lazy, default=default)
    if (value is None) and lazy:
        return None
    try:
        return int(float(value))
    except ValueError:
        if lazy:
            return None
        raise BadValueError('Incorrect value %r for int' % value)


def get_bool(section, param, lazy=True, default=None):
    value = _get_value(section, param, lazy=lazy, default=default)
    return bool_values.get(value)