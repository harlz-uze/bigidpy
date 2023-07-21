# BigID Python Library Classifier Engine used for actions on Classifers
__author__ = "Brenton Harley"
__version__ = "1.0.0"
__status__ = "Development"

import bigid
from data_types import BigData, Classifier

def get_classifiers(bigid: bigid.BigID) -> list[Classifier]:
    ''' Get classifiers from BigID and return them as a list'''
    data = bigid.make_request(api_path='/api/v1/classifiers', http_method='GET')
    res: list[Classifier] = []
    for i in data.data['data']['classifiers']:
        res.append(Classifier.from_dict(i))
    return res