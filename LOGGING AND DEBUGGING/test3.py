import  logging
logging.basicConfig(filename="test3.log", level=logging.INFO ,format='%(levelname)s %(asctime)s %(name)s  %(message)s' )

def devide(a,b) :
   # logging.info("the number entered by user is %s and %s", a, b)
    logging.info(f"the number entered by user is {a} and {b}")
    try :
        logging.info("we are into function")
        div = a /b
        logging.info("we have completed a division operation")
        #logging.info("result of code is %s " , div)
        logging.info(f"result of code is {div} ")
        return div
    except  Exception as e :
        logging.exception(e)
        print(e)


(devide(3,0))