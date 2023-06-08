import logging
logging.basicConfig(filename="test1.log",level=logging.INFO)
logging.info("this is my very first code for logging")
logging.warning("this will try to load a warning message")
logging.error("this is error message from system")
l=[1,2,3,4,5,6,7,8]
for i in l :
    if i == 2 :
        logging.info(i)
        logging.info(l)
        logging.warning("this is a warning for a user that they have found 2 in list")


logging.shutdown()
