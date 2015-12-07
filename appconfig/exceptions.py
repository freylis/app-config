# coding: utf-8

class AppConfigError(Exception):
    pass


class BadValueError(AppConfigError):
    pass


class ParamsError(AppConfigError):
    pass