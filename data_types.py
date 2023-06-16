from dataclasses import dataclass
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
    