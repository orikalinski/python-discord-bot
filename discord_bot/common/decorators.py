import functools
import inspect
import logging
from time import sleep

from retrying import retry

from discord_bot.common.exceptions import TooManyRequests

logger = logging.getLogger()


def check_exception(exception):
    if isinstance(exception, TimeoutError):
        return True
    if isinstance(exception, TooManyRequests):
        retry_after = float(exception.response_json.get("retry_after"))
        if retry_after:
            logger.info("Got TooManyRequests on url: %s, will retry in %s secs, global: %s message: %s",
                        exception.url, retry_after, exception.response_json.get("global"),
                        exception.response_json.get("message"))
            sleep(retry_after)
        else:
            logger.error("Got TooManyRequests without retry_after!!!")
        return True
    return False


def handle_discord_exception(method):
    @functools.wraps(method)
    @retry(retry_on_exception=check_exception, stop_max_attempt_number=2)
    def wrapper(*args, **kwargs):
        return method(*args, **kwargs)

    return wrapper


def is_static_method(klass, attr, value=None):
    """Test if a value of a class is static method.
    example::
        class MyClass(object):
            @staticmethod
            def method():
                ...
    :param klass: the class
    :param attr: attribute name
    :param value: attribute value
    """
    if value is None:
        value = getattr(klass, attr)
    assert getattr(klass, attr) == value

    for cls in inspect.getmro(klass):
        if inspect.isroutine(value):
            if attr in cls.__dict__:
                binded_value = cls.__dict__[attr]
                if isinstance(binded_value, staticmethod):
                    return True
    return False


def wrap_all_class_methods(decorator):
    def decorate(cls):
        for attr in cls.__dict__:
            _obj = getattr(cls, attr)
            if callable(_obj) and not is_static_method(cls, attr, value=_obj):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate
