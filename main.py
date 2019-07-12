#!/usr/bin/python
import json

class ParserJson:
    def __init__(self):
        1==1
    def run(self):
        1==1
    def is_json(json):
        try:
            json_object = json.loads(json)
        except Exception as e:
            return False
        return True

if __name__== '__main__':
    json_object=ParserJson()
    json_object.run()
    js={
    "transmitter": "abc:123456",
    "msg_time": "2019-03-15T10:26:37.951Z",
    "msg_type": 83,
    "message": "Hello World"}

