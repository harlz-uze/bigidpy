# BigID Python Library Data types
__author__ = "Brenton Harley"
__version__ = "1.0.0"
__status__ = "Development"

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Optional

@dataclass_json
@dataclass
class User:
    ''' Base user class'''
    name: str
    firstName: str
    lastName: str
    password: str
    roleIds: Optional[list[str]] = None
    refreshTokens: Optional[list[str]] = None
    
@dataclass
class BigData:
    ''' Base data class for BigID '''
    status_code: int
    data: dict[str, str]
    
@dataclass_json
@dataclass
class BigIdPolicy:
    ''' Base policy object 
    Attributes:
        actions: Actions to take, can be an empty array for no actions
        type: privacy, catalogue, governance, other
        complianceRuleCalc: The rule that triggers the policy for example
            {'bigidQuery': 'field="Citizen ID" AND country="Germany" AND risk > 75', 'maxFindings': '1000'}
        description: A description of why the policy rule exists and what it does
        is_enabled: If the policy should be applied or ignored
        name: A name for the policy
        owner: The owner of the policy
        apps: An empty list
        taskSettings: {'includeLinkToInventory': False, 'includeObjectsReport': False}
        category: string of the category for example GDPR
        id: uid of the policy
    '''
    actions: list[str]
    complianceRuleCalc: dict[str, str]
    description: str
    is_enabled: bool
    name: str
    owner: str
    taskSettings: dict[str, str]
    type: str
    category: str
    apps: list[str]
    id: Optional[str] = None
    
@dataclass_json
@dataclass
class RegexClassifier:
    # id: str
    # name: str
    # attributeRiskName: str
    # type: enumerate
    # totalFindings: int
    # originalData: list[dict[str, str]]
    # nerTitle: Optional[str] =None
    # Allowed: Optional[str] =None #doc┃ner┃meta┃data
    _id: str
    classification_name: str
    classification_regex: str
    name: str
    proximity_before: Optional[int] = None
    version: Optional[str] = None
    updated_at: Optional[str] = None
    support_term_value: Optional[str] = None
    enabled: Optional[bool] = None
    proximity_after: Optional[int] = None
    validation: Optional[str] = None
    max_length: Optional[int] = None
    min_length: Optional[int] = None

    # detection_sensitivity: Optional[int] = None
    # description: Optional[str] = None
    # hierachy: Optional[list[str]] = field(default_factory=list)
    # category: Optional[list[str]] = field(default_factory=list)
    # country_code: Optional[list[str]] = field(default_factory=list)
    # classification_regex: Optional[str] = None
    # nerTitle: Optional[str] = None
    # Allowed: Optional[str] = None
    # classifierType: Optional[str] = None

    # isOutOfTheBox: Optional[bool] = None
    # performance: Optional[int] = None

@dataclass_json
@dataclass
class NerClassifier:
    _id: str
    type: str
    updated_at: str
    name: str
    version: Optional[str] = None
    classifierName: Optional[str] = None
    
@dataclass_json
@dataclass
class DocClassifier:
    _id: str
    category_name: list[str]
    defaultWeightRisk: int
    detection_sensitivity: int
    enabled: bool
    modelId: str
    nerEntityName: str
    type: str
    updated_at: str
    name: str
    country_Code: Optional[list[str]] = None
    
    # _id
    # string
    # classification_name
    # string
    # classifierType
    # enum
    # Allowed: columnName┃data
    # type
    # enum
    # Allowed: NER┃DOC
    # enabled
    # boolean
    # classification_regex
    # string
    # min_length
    # string
    # max_length
    # string
    # validation
    # string
    # description
    # string
    # nerEntityName
    # string
    # modelId
    # string
    # classifierName
    # string
    # modelName
    # string
    # modelNameInMl
    # string
    # originalNames *
    # [string]