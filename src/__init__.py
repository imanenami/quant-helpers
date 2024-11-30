import sys
import logging


# logging configuration
logger = logging.getLogger("QuantHelpers")
logger.setLevel(logging.INFO)
_formatter = logging.Formatter('[%(asctime)s] %(name)s | %(levelname)s: %(message)s')


if not logger.hasHandlers():
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(_formatter)
    logger.addHandler(stdout_handler)
