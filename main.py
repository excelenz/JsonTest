#!/usr/bin/python3
import json
import logging
import re

class ParserJson:
    def __init__(self):
        self.logging()
        self.DEBUG=0

    def logging(self):
        logging.basicConfig(filename='telegram.log',format="%(asctime)s:  %(message)s \n",datefmt='%Y-%m-%d,%H:%M',level=logging.INFO)
        logger = logging.getLogger(__name__)
        logger.info("*************************************************************** \n ")
        logger.info(__name__)

    def main(self):
        if self.input_json():
            data= self.input_json()
        else:
            return "not a valid json"
        if self.validation(data):
            return True
        else:
            return "not a valid data in json"

    def validation(self,json):
        try:
            if json['msg_type'] in (0000,83,84):
                return True
            else:
                return False
        except:
            return False
        try:
            transmitter=json['transmitter']
            if re.match(r"^[a-zA-Z]{3}:\d$", transmitter):
                return True
            else:
                return False
        except:
            return False

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
    print(json_object.main())
