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


bool_true_values = {
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
}


def get_value(section, param, lazy=True):
    try:
        return config.get(section, param)
    except (configparser.NoOptionError, configparser.NoSectionError):
        if lazy:
            return None
        raise BadValueError('Bad value for %r.%r in file %r' % (section, param, config_path))


def get_str(section, param, lazy=True):
    value = get_value(section, param, lazy=lazy)
    if (value is None) and lazy:
        return None
    return str(value)


def get_float(section, param, lazy=True):
    value = get_value(section, param, lazy=lazy)
    if (value is None) and lazy:
        return None
    try:
        return float(value)
    except ValueError:
        if lazy:
            return None
        raise BadValueError('Incorrect value %r for float' % value)


def get_int(section, param, lazy=True):
    value = get_value(section, param, lazy=lazy)
    if (value is None) and lazy:
        return None
    try:
        return int(float(value))
    except ValueError as exc:
        if lazy:
            return None
        raise BadValueError('Incorrect value %r for int' % value)


def get_bool(section, param, lazy=True):
    value = get_value(section, param, lazy=lazy)
    return bool_true_values.get(value, False)