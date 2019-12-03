import datetime
import json
from conf import rate_status_init, datetime_format

def isJson(path):
  try:
    json_object = json.loads(path)
  except ValueError as e:
    return False
  return True

def makeJson2dict(path):
    if not isJson(path):
        dictionary = rate_status_init
    else:
        with open(path, 'r') as f:
            dictionary = json.load(f)
    return dictionary

def makeDict2json(dictionary, path):
    if not isinstance(dictionary, dict):
        raise TypeError('Invalid argument! (input is not dict)')
    else:
        with open(path, 'w') as f:
            json.dump(dictionary, f)

def isDatetimeFormat(element):
    try:
        datetime.datetime.strptime(element, datetime_format)
    except TypeError as e:
        return False
    except ValueError as e:
        return False
    return True

def makeDatetime2string(element):
    if not isinstance(element, type(datetime.datetime.now())):
        raise ValueError('Invalid argument! (input is not Datetime)')
    else:
        date_string = element.strftime(datetime_format)
        return date_string

def makeString2datetime(element):
    if not isinstance(element, str):
        raise TypeError('Invalid argument! (input is not str object)')
    else:
        datetime_obj = datetime.datetime.strptime(element, datetime_format)
        return datetime_obj