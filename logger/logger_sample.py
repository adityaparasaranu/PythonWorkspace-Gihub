import logging

logging.basicConfig(format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
                    datefmt= "%d-%m-%Y %H:%M:%S",
                    level= logging.DEBUG,
                    filename="log.txt") # You can add this if you want to show loggers in file. Else remove it.

logger = logging.getLogger("test_logger")

logger.info("This is logger info msg")
logger.warning("This is a warning msg. Be Careful")
logger.debug("This is debug")
logger.critical("This is Critical")
