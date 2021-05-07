import logging
import threading


class MySingleton(object):
    _instance: object = None
    _lock: threading.Lock = threading.Lock()

    def __new__(cls):
        """new instance"""
        if MySingleton._instance is None:
            with MySingleton._lock:
                if MySingleton._instance is None:
                    MySingleton._instance = super(MySingleton, cls).__new__(cls)
                    MySingleton._instance._initialized = False

        return MySingleton._instance

    def __init__(self):
        if self._initialized is False:
            self._logger = logging.getLogger(self.__class__.__name__)
            self._count = 0
            self._initialized = True
            self._logger.debug(f" new new")

        self._logger.debug(f"my instance: {self._instance}")
        self._count += 1
        self._logger.debug(f" = {self._count}")


def test_function():
    logging.basicConfig(level=logging.DEBUG, handlers=[logging.StreamHandler()])
    a = MySingleton()
    b = MySingleton()
    a = MySingleton()
    a = MySingleton()


test_function()

https://www.udemy.com/course/androidstudiojava/?fbclid=IwAR1kqpMh-fPVKWrujTwSuicWpfQr8pExqUZOzi0pWn8gjEb17Lt11WARcdQ#overview