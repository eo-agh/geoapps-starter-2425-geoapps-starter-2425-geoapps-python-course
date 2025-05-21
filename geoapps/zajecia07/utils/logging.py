import logging
from pathlib import Path 
from datetime import datetime

def get_logger(
    name: str,
    log_level: int | str = logging.INFO,
    log_file: Path | None = None,
) -> logging.Logger:
    """Builds a `Logger` instance with provided name and log levels for stream and file.

    Args:
        name: The name for the logger.
        log_level: The default log level for the logger.
        log_file: Optional path to the log file. If not specified, logs go to ./logs/logs_{timestamp}.log

    Returns:
        The logger.

    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Avoid adding multiple handlers if the logger already has them
    if not logger.handlers:
        # Formatter for both handlers
        formatter = logging.Formatter(
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Stream handler
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)  # Set level for stream
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        
        # File handler
        if log_file is None:
            logs_dir = Path("./logs")
            logs_dir.mkdir(exist_ok=True)
            timestamp = datetime.now()
            log_file = logs_dir/f"logs_{timestamp}.log"
             
        file_handler = logging.FileHandler(log_file, mode="a")
        file_handler.setLevel(logging.ERROR)  # Set level for file
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
