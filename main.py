#!/usr/bin/python
import json
import logging

class ParserJson:
    def __init__(self):
        logging.basicConfig(filename='telegram.log',format="%(asctime)s:   %(message)s \n",datefmt='%Y-%m-%d,%H:%M',level=logging.INFO)
        logger = logging.getLogger(__name__)
        logger.info("*************************************************************** \n ")
        logger.info(__name__)

    def main(self):
        return self.input_json()

    def is_json(self):
        try:
            json_object = json.loads(json)
        except Exception as e:
            return False
        return True

    def input_json(self):
        with open('data.txt') as json_file:
            try:
                data = json.load(json_file)
            except Exception as e:
                return False

if __name__== '__main__':
    json_object=ParserJson()
    json_object.main()

