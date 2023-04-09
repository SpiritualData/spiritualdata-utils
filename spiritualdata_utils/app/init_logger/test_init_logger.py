import os
from loguru import logger
import pytest

from init_logger import init_logger


def test_init_logger():
    # Define test parameters
    log_file = "test.log"
    console_level = "INFO"
    file_level = "DEBUG"

    # Call the init_logger() function
    init_logger(log_file=log_file, console_level=console_level, file_level=file_level)

    # Check that the logger has three sinks
    assert len(logger._core.handlers) == 3

    # Delete the log file after running the test

    os.remove(log_file)
