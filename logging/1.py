import logging

def log():
    logging.basicConfig(
        filename="demo.log",
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d'
    )
    return logging.getLogger()

logger = log()
logger.info("Program execution started")

a=4
b=3
if a>b:
    print("Rakesh")
    logger.info("A is greater than b")

logger.info(" ")

