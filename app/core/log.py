import os
import logging
from logging import Logger


LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")


class CustomLogger:
    _logger = None

    def __new__(cls, *args, **kwargs):
        if cls._logger is None:
            cls._logger = super().__new__(cls, *args, **kwargs)
            cls._logger = logging.getLogger("sample")
            cls._logger.setLevel(logging._nameToLevel.get(LOG_LEVEL))

            formatter = logging.Formatter(
                "[%(asctime)s] %(name)s [%(levelname)s] %(filename)s:%(lineno)d '%(funcName)s' - %(message)s"
            )
            streamHandler = logging.StreamHandler()
            streamHandler.setFormatter(formatter)

            cls._logger.addHandler(streamHandler)

        return cls._logger


logger: Logger = CustomLogger()
