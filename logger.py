import logging
from config import ROOT_DIR

def create_logger():
    logger = logging.getLogger("nova_ai")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(ROOT_DIR / "nova.log", encoding="utf-8")
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
        )
        logger.addHandler(file_handler)

    return logger
