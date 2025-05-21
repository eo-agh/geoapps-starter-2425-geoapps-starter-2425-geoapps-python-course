from .utils import get_logger
from pathlib import Path
 
log_path = Path("./logs/custom_log_file.log")
_logger = get_logger("modul2", log_level="DEBUG", log_file=log_path)

def modul2():
    _logger.debug("Debug message from modul2")
    _logger.error("Error message from modul2")
    _logger.warning("Warning message from modul2") 