#!/usr/bin/python3
import json
import logging
import re
import datetime

class ParserJson:
    def __init__(self):
        self.DEBUG=1
        logging.basicConfig(filename='telegram.log',format="%(asctime)s:  %(message)s \n",datefmt='%Y-%m-%d,%H:%M',level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.info(__name__)

    def main(self):
        data= self.input_json()
        if not data:
            return "not a valid json"
        if not self.is_valid_type(data):
            return "not a valid type in json"
        if not self.is_valid_transmitter(data):
            return "not a valid transmitter in json"
        self.is_valid_time(data)
        return data

    def is_valid_type(self,json):
        try:
            if json['msg_type'] in (0000,83,84):
                return True
            else:
                return False
        except:
            return False

    def is_valid_transmitter(self, json):
        try:
            transmitter=json['transmitter']
            pattern='^([a-zA-Z]{3}):(\d)'
            match = re.search(pattern, transmitter)
            if match:
                self.logger.info("match success %s \n" % transmitter)
                print(transmitter)
                return True
            else:
                self.logger.info("not match %s \n" % transmitter)
                print("not match %s" % transmitter)
                return False
        except:
            return False

    def is_valid_time(self,json):
        try:
            msg_time=json['msg_time']
            "2019-03-15T10:26:37.951Z"
            israel_time=datetime.datetime.strptime(msg_time, '%Y-%m-%dT%H:%M:%S.%fZ')
            print(israel_time)
        except:
            return False


    def input_json(self):
        with open('data.txt') as json_file:
            try:
                data = json.load(json_file)
                self.logger.info("Success on open file")
                return data
            except Exception as e:
                self.logger.info("ERROR ON LOAD %s" % e)
                if self.DEBUG:
                    raise
                return False
        return True

if __name__== '__main__':
    json_object=ParserJson()
    print(json_object.main())

