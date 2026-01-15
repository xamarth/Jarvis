# Jarvis - UserBot

"""
Exceptions which can be raised by py-Jarvis Itself.
"""


class pyCoreError(Exception):
    ...


class DependencyMissingError(ImportError):
    ...


class RunningAsFunctionLibError(pyCoreError):
    ...
