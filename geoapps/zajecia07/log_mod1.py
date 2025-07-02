from .utils import get_logger

_logger = get_logger("modul1")


def modul1():
    _logger.debug("Debug message from modul1")
    _logger.info("Info message from modul1")
    _logger.warning("Warning message from modul1")
