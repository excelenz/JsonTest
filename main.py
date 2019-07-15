#!/usr/bin/python3
import json
import logging
import re
from datetime import datetime,timezone,timedelta

class ParserJson:
    def __init__(self):
        self.DEBUG=1
        logging.basicConfig(filename='telegram.log',format="%(asctime)s:  %(message)s \n",datefmt='%Y-%m-%d,%H:%M',level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.info(__name__)
        self.tz = timedelta(hours=3)
        self.timegap = datetime.now()-timedelta(days=7)

    def main(self,data_list):
        for data1 in data_list:
            print(data1)
            data='{}'.format(data1)
            print(data)
            if not self.is_valid_json(data):
                return "not a valid json"
            if not self.is_valid_type(data):
                return "not a valid type in message"
            if not self.is_valid_transmitter(data):
                return "not a valid transmitter in message"
            if not self.is_valid_time(data):
                return "not a fresh time in message"
            return data

    def is_valid_type(self,json):
        try:
            if json['msg_type'] in (0000,83,84):
                return True
            else:
                return False
        except:
            if self.DEBUG:
                raise
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
            if self.DEBUG:
                raise
            return False

    def is_valid_time(self,json):
        try:
            msg_time_original=json['msg_time']
            msg_time=datetime.strptime(msg_time_original, '%Y-%m-%dT%H:%M:%S.%fZ')
            if self.timegap<(msg_time + self.tz) and (msg_time + self.tz)<=datetime.now():
                self.logger.info("the message is fresh %s" % self.timegap)
                print("the message is fresh %s" % self.timegap)
                return True
            else:
               self.logger.info("time is rotten %s" % msg_time)
               print("time is rotten %s" % msg_time)
               return False
        except:
            if self.DEBUG:
                raise
            return False


    def is_valid_json(self,item):
        try:
            data = json.load(item)
            self.logger.info("Success on open json")
            return data
        except Exception as e:
            self.logger.info("ERROR ON LOAD json %s" % e)
            if self.DEBUG:
                raise
            return False

    def input_from_file(self):
        try:
            with open('data.txt') as file:
                print(list(file))
        except Exception as e:
            self.logger.info("ERROR ON LOAD file %s" % e)
            if self.DEBUG:
                raise
            return False


if __name__== '__main__':
    json_object=ParserJson()
    data_list=[{
    "transmitter": "abc:123456",
    "msg_time": "2019-03-15T10:26:37.951Z",
    "msg_type": 83,
    "message": "Hello World"},{
    "transmitter": "abc:123456",
    "msg_time": "2019-07-13T10:26:37.951Z",
    "msg_type": 83,
    "message": "Hello World"}]
    print(json_object.main(data_list))

