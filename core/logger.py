import logging
import os


def setup_logger():

    # Create logs directory

    if not os.path.exists("logs"):
        os.makedirs("logs")


    logger = logging.getLogger(
        "PortBannerAnalyzer"
    )

    logger.setLevel(logging.INFO)


    # Prevent duplicate handlers

    if not logger.handlers:

        file_handler = logging.FileHandler(
            "logs/scanner.log"
        )

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler.setFormatter(
            formatter
        )

        logger.addHandler(
            file_handler
        )


    return logger



# Global logger object

logger = setup_logger()