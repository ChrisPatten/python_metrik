from mds3loader.utils.logger import get_logger


def test_get_logger():
    logger = get_logger("DEBUG")
    assert logger is not None
    logger.debug("message")
