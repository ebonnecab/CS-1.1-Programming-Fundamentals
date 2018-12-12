import pytest
from logger import Logger


def test_init_logger():
    logger = Logger("test.txt")
    assert logger.file_name == "test.txt"


def test_add_to_file():
    logger = Logger("test.txt")
    logger.add_to_file("test worked", "w")


def test_write_metadeta():
    logger = Logger('test_meta.txt')
    logger.write_metadata(100, 0.2, "Snapple", 0.3, 0.4)


def test_log_time_step():
    logger = Logger("time_step.txt")
    logger.log_time_step(1)
