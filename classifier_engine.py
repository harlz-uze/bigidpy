# BigID Python Library Classifier Engine used for actions on Classifers
__author__ = "Brenton Harley"
__version__ = "1.0.0"
__status__ = "Development"

import bigid
from data_types import BigData, RegexClassifier, DocClassifier, NerClassifier

def get_classifiers(bigid: bigid.BigID) -> dict[str, list[RegexClassifier, NerClassifier, DocClassifier]]:
    ''' Get classifiers from BigID and return them as a list'''
    data = bigid.make_request(api_path='/api/v1/classifiers', http_method='GET')
    res: dict[str, list[RegexClassifier, DocClassifier, NerClassifier]] = {'RegexClassifiers': [], 'NerClassifiers': [], 'DocClassifiers': [], 'failures': []}
    for i in data.data['data']['classifiers']:
        if 'classification_regex' in i['originalData'][0]:
            # print(i['originalData'][0])
            res['RegexClassifiers'].append(RegexClassifier.from_dict(i['originalData'][0]))
        elif 'type' in i['originalData'][0] and i['originalData'][0]['type'] == 'DOC':
            res['DocClassifiers'].append(DocClassifier.from_dict(i['originalData'][0]))
        elif 'type' in i['originalData'][0] and i['originalData'][0]['type'] == 'NER':
            res['NerClassifiers'].append(NerClassifier.from_dict(i['originalData'][0]))
        else:
            res['failures'].append(i['originalData'][0])
            # raise ClassifierError(message='Unsupported Classifier type. Classifier is not Regex, NER Or DOC')
    if len(res['failures']) > 0:
        print('Failed to parse classifier, supported types are DOC, NER & Regex see result["failures"] for more info')
    return res

def add_classifier(bigid: bigid.BigID, classifier: RegexClassifier) -> None:
    ''' Add a classifier to the BigID instance '''
    data = bigid.make_request(api_path='/api/v1/classifications', http_method='GET')
    pass