from loguru import logger


init_loggers = {"logger": None}


def init_logger(
    log_file="/logs/spiritual_data_utils.log", console_level="INFO", file_level="DEBUG"
):
    if init_loggers["logger"] != None:
        logger.info("Using cached logger")
        return init_loggers["logger"]

    # # Remove any existing console sinks
    logger.remove()
    # Add a new sink that logs messages to a file
    logger.add(
        log_file,
        level=file_level,
        rotation="500 MB",
        enqueue=True,
        format="<green>{time:DD-MM-YYYY HH:mm:ss}</green>| {file.name} | Function: {function} | Line: {line} | <level>{level}</level> | <cyan>{message}</cyan>\n",
        colorize=True,
    )

    logger.info("Logger initialized")
    init_loggers["logger"] = logger
    logger.info("Logger cached")
    return logger
