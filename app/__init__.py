from abc import ABC, ABCMeta, abstractmethod
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_apscheduler import APScheduler
from app.commands import define_tasks
import logging
import threading


# Singleton metaclass
class SingletonMeta(ABCMeta):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


# Abstract base class for logger
# Concrete logger class
class BaseLogger(ABC, metaclass=SingletonMeta):
    @abstractmethod
    def debug(self, message):
        pass

    @abstractmethod
    def info(self, message):
        pass

    @abstractmethod
    def warning(self, message):
        pass

    @abstractmethod
    def error(self, message):
        pass

    @abstractmethod
    def critical(self, message):
        pass


class Logger(BaseLogger):
    _logger = None

    def __init__(self):
        self._initiate_logger()

    def _initiate_logger(self):
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.INFO)
        file_handler = RotatingFileHandler(
            "error.log", maxBytes=10000000, backupCount=5
        )

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        self._logger.addHandler(file_handler)
        self._logger.addHandler(console_handler)

    def debug(self, message):
        if self._logger is not None:
            self._logger.debug(message)

    def info(self, message):
        if self._logger is not None:
            self._logger.info(message)

    def warning(self, message):
        if self._logger is not None:
            self._logger.warning(message)

    def error(self, message):
        if self._logger is not None:
            self._logger.error(message)

    def critical(self, message):
        if self._logger is not None:
            self._logger.critical(message)


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    logger = Logger()
    logger.info("Application created.")

    scheduler = APScheduler()
    scheduler.init_app(app)
    define_tasks(scheduler=scheduler, app=app)
    scheduler.start()

    return app
