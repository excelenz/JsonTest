#!/usr/bin/python
import json
import logging

class ParserJson:
    def __init__(self):
        self.logging()
        self.DEBUG=1

    def logging(self):
        logging.basicConfig(filename='telegram.log',format="%(asctime)s:  %(message)s \n",datefmt='%Y-%m-%d,%H:%M',level=logging.INFO)
        logger = logging.getLogger(__name__)
        logger.info("*************************************************************** \n ")
        logger.info(__name__)

    def main(self):
        return self.input_json()

    def input_json(self):
        with open('data.txt') as json_file:
            try:
                data = json.load(json_file)
                logger = logging.getLogger("Success on open file")
                return data
            except Exception as e:
                logger = logging.getLogger("ERROR ON LOAD %s" % e)
                if self.DEBUG:
                    raise
                return False
        return True

if __name__== '__main__':
    json_object=ParserJson()
    json_object.main()

