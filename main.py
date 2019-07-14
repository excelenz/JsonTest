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

    def main(self):
        data= self.input_json()

        ###
        #
        # Failed messages should be placed in a separate list with the failure reason
        # We will sort only by one condition (it can fail more than one validation)
        #
        ####

        if not data:
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

