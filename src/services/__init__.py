import logging
from functools import wraps
from typing import Tuple, Type, Union


def try_except(
    exceptions: Union[Type[Exception], Tuple[Type[Exception]]],
    message: str = None,
    num_tries: int = 3,
):
    if type(exceptions) is not tuple:
        exceptions = (exceptions,)

    def decorator_exception(func):
        @wraps(func)
        async def wrapper_exception(*args, **kwargs):
            result = None
            for i in range(num_tries):
                try:
                    result = await func(*args, **kwargs)
                    break
                except exceptions as ex:
                    if (i + 1) == num_tries:
                        logger = logging.getLogger(func.__name__)
                        logger.exception(message or str(ex))
                        return None
                    else:
                        pass
            return result

        return wrapper_exception

    return decorator_exception
