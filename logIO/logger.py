#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simple wrapper for Python logging module. Adds information about location
emitting the information (file, line, function) and timestamp.
"""
import logging


def get_logger(module_name, use_color=True, log_level=logging.INFO, log_format=None):
    """
    Logger mixin/base class adding verbose logging to subclasses.
    Subclasses get info(), debug(), warning() and error() methods which, alongside
    the information given, also show location of the message (file, line and
    function).

    Example usage:

        from logIO import get_logger

        logger = get_logger(__name__)
        logger.debug('This is a debug message')
        logger.warning('This is a warning message', use_colors=False)
    """
    try:
        import coloredlogs
    except Exception as e:
        print("WARNING: ImportError - Cannot Import 'coloredlogs', Using default logging instead...".format(e))

    log_format = "%(asctime)s %(name)s:L%(lineno)d %(levelname)s: %(message)s" if log_format is None else log_format
    date_format = "%Y-%m-%d %H:%M:%S"

    logging.basicConfig(level=log_level, format=log_format, datefmt=date_format)
    user_logger = logging.getLogger(module_name)

    if coloredlogs is None or not use_color:
        # if colored_logs not found in $PYTHONPATH or user asked specifically
        # for no-color std-out. Use default logger.
        return user_logger

    coloredlogs.install(level=log_level, logger=user_logger, fmt=log_format, datefmt=date_format)
    return user_logger


if __name__ == "__main__":

    test_logger = get_logger(__name__)

    test_logger.debug("this is a debugging message")
    test_logger.info("this is an informational message")
    test_logger.warning("this is a warning message")
    test_logger.error("this is an error message")
    test_logger.critical("this is a critical message")

