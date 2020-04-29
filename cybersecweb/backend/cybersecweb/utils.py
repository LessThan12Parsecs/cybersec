import json
import datetime
from os import path
from django.core.serializers.json import DjangoJSONEncoder

def store(data, contentType):
    date = datetime.datetime.now().strftime("%Y%m%dT%H%M%S%f")
    filepath = 'C:\\Users\\Emanuel\\Repos\\cybersec\\cybersecweb\\backend\\cybersecweb\\backups\\'
    filename = str(filepath + contentType + '-' + date + '.json')
    with open(filename, 'w+', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4,cls=DjangoJSONEncoder)