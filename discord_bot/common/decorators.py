import functools
import logging
from time import sleep

from retrying import retry

from discord_bot.common.exceptions import TooManyRequests

logger = logging.getLogger(__name__)


def check_exception(exception):
    if isinstance(exception, TimeoutError):
        return True
    if isinstance(exception, TooManyRequests):
        retry_after = float(exception.response["retry_after"])
        logger.info("Got TooManyRequests on url: %s, will retry in %s secs", exception.url, retry_after)
        sleep(retry_after)
        return True


def handle_discord_exception(method):
    @functools.wraps(method)
    @retry(retry_on_exception=check_exception, stop_max_attempt_number=2)
    def wrapper(*args, **kwargs):
        return method(*args, **kwargs)

    return wrapper


def wrap_all_class_methods(decorator):
    def decorate(cls):
        for attr in cls.__dict__:
            _obj = getattr(cls, attr)
            if callable(_obj):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate
