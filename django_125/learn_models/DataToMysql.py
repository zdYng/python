from learn_models.learn_models.wsgi import *
from learn_models.people.models import Person

def InputData():
    csvf = 'one-minute.json'
    csvf = os.path.abspath(csvf)
    if os.path.isfile(csvf):
        with open(csvf) as f:
            for row in f:
                time,predict = row['time'],row['*.AV']