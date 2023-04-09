import loguru


def init_logger(log_file="/logs/spiritual_data_utils.log", console_level="INFO", file_level="DEBUG"):
    # Create a new logger object
    logger = loguru.logger

    # Add a new sink that logs messages to a file
    logger.add(log_file, level=file_level, rotation="500 MB")

    # Add a new sink that logs messages to the console
    logger.add(
        sink = log_file,
        colorize=True,
        level=console_level,
        format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | <level>{message}</level>",
    )

    logger.info("Logger initialized")
    return logger
