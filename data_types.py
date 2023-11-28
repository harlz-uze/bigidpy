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
    # name: Optional[str] = None
    description: Optional[str]=''
    proximity_before: Optional[int] = None
    version: Optional[str] = None
    # updated_at: Optional[str] = None
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
 
@dataclass_json
@dataclass   
class Role:
    name: str
    description: str
    granularPermissions: dict[str]
    scopes: list[str] # ['root']
    # permissions: list[str] #['ops']
    #{'permission.tasks.edit': True, 'permission.applications.read_custom_apps': True, 'permission.dashboard.access': True, 'permission.inventory.access': True, 'permission.inventory.read': True, 'permission.inventory.export_objects': True, 'permission.inventory.export_attributes': True, 'permission.inventory.investigate_attributes': True, 'permission.inventory.export_entities': True, 'permission.inventory.read_entities': True, 'permission.correlation.access': True, 'permission.correlation.read': True, 'permission.correlation.manage': True, 'permission.clusterAnalysis.access': True, 'permission.clusterAnalysis.read': True, 'permission.clusterAnalysis.edit': True, 'permission.clusterAnalysis.export_objects': True, 'permission.classification.access': True, 'permission.classification.read': True, 'permission.catalog.access': True, 'permission.catalog.read': True, 'permission.catalog.export': True, 'permission.catalog.investigate': True, 'permission.catalog.manual_fields.edit': True, 'permission.catalog.manual_fields.read': True, 'permission.catalog.decrypt': True, 'permission.catalog.manage_preview_file': True, 'permission.policies.access': True, 'permission.policies.read': True, 'permission.policies.edit': True, 'permission.policies.delete': True, 'permission.policies.create': True, 'permission.policies.test': True, 'permission.scanResultsDetails.access': True, 'permission.scanResultsDetails.read': True, 'permission.scanResultsDetails.export': True, 'permission.scanResultsDetails.edit': True, 'permission.scanResultsDetails.edit_confidence_threshold': True, 'permission.scanResultsDetails.edit_confidence_level': True, 'permission.reports.access': True, 'permission.reports.read_activity_highlights': True, 'permission.reports.read_scan_result_summary': True, 'permission.reports.export_scan_files': True, 'permission.reports.export_data_custodian': True, 'permission.reports.export_files_attribute_distribution': True, 'permission.reports.export_failed_object': True, 'permission.reports.export_labeling_propagation': True, 'permission.dataSources.access': True, 'permission.dataSources.read': True, 'permission.correlationSets.access': True, 'permission.correlationSets.read': True, 'permission.secondarySources.access': True, 'permission.secondarySources.read': True, 'permission.secondarySources.edit': True, 'permission.secondarySources.delete': True, 'permission.secondarySources.create': True, 'permission.secondarySources.run': True, 'permission.applicationSetup.access': True, 'permission.applicationSetup.read': True, 'permission.applicationSetup.edit': True, 'permission.applicationSetup.create': True, 'permission.applicationSetup.delete': True, 'permission.classifiers.access': True, 'permission.classifiers.read': True, 'permission.classifiers.edit': True, 'permission.classifiers.create': True, 'permission.classifiers.export': True, 'permission.classifiers.import': True, 'permission.classifiers.delete': True, 'permission.credentials.access': True, 'permission.credentials.read': True, 'permission.credentials.edit': True, 'permission.credentials.create': True, 'permission.credentials.test': True, 'permission.credentials.delete': True, 'permission.certificates.access': True, 'permission.certificates.read': True, 'permission.certificates.edit': True, 'permission.certificates.create': True, 'permission.certificates.delete': True, 'permission.tagsSavedQueries.access': True, 'permission.tagsSavedQueries.read': True, 'permission.tagsSavedQueries.edit': True, 'permission.tagsSavedQueries.create': True, 'permission.tagsSavedQueries.delete': True, 'permission.audit.access': True, 'permission.audit.read': True, 'permission.audit.export': True, 'permission.generalSettings.access': True, 'permission.generalSettings.business_glossary.read': True, 'permission.generalSettings.business_glossary.edit': True, 'permission.generalSettings.business_glossary.create': True, 'permission.generalSettings.business_glossary.export': True, 'permission.generalSettings.business_glossary.import': True, 'permission.generalSettings.business_glossary.delete': True, 'permission.generalSettings.email_setup.read': True, 'permission.generalSettings.email_setup.manage': True, 'permission.generalSettings.ignored_lists.read': True, 'permission.generalSettings.ignored_lists.edit': True, 'permission.generalSettings.ignored_lists.create': True, 'permission.generalSettings.ignored_lists.delete': True, 'permission.generalSettings.license.read': True, 'permission.generalSettings.license.edit': True, 'permission.scans.access': True, 'permission.scans.scan_profiles.read': True, 'permission.scans.scan_profiles.edit': True, 'permission.scans.scan_profiles.create': True, 'permission.scans.scan_profiles.delete': True, 'permission.scans.scan_profiles.run': True, 'permission.scans.scan_activity.read': True, 'permission.scans.scan_activity.edit': True, 'permission.advancedTools.access': True, 'permission.advancedTools.edit_clear_entities_cache': True, 'permission.advancedTools.delete_delete_pii_data': True, 'permission.advancedTools.delete_delete_findings': True, 'permission.advancedTools.edit_services_logs': True, 'permission.advancedTools.system_health.read': True, 'permission.advancedTools.system_health.manage': True, 'permission.advancedTools.system_health.run': True, 'permission.advancedTools.services_configuration.edit': True, 'permission.advancedTools.services_configuration.read': True, 'permission.advancedTools.delete_delete_clusters_results': True, 'permission.advancedTools.export_download_docvecs_result': True, 'permission.advancedTools.export_scan_result': True, 'permission.dataRightsFulfillment.access': True, 'permission.dataRightsFulfillment.request.read': True, 'permission.dataRightsFulfillment.request.export': True, 'permission.dataRightsFulfillment.request.submit': True, 'permission.dataRightsFulfillment.request.stop': True, 'permission.dataRightsFulfillment.request.delete': True, 'permission.dataRightsFulfillment.request.manage': True, 'permission.dataRightsFulfillment.deletion_validation.read': True, 'permission.dataRightsFulfillment.deletion_validation.manage': True, 'permission.dataRightsFulfillment.deletion_validation.stop': True, 'permission.dataRightsFulfillment.audit.read': True, 'permission.dataRightsFulfillment.audit.export': True, 'permission.dataRightsFulfillment.profile_settings.read': True, 'permission.dataRightsFulfillment.profile_settings.edit': True, 'permission.dataRightsFulfillment.profile_settings.create': True, 'permission.dataRightsFulfillment.profile_settings.delete': True, 'permission.dataRightsFulfillment.profile_settings.export': True, 'permission.dataRightsFulfillment.profile_settings.import': True, 'permission.dataRightsFulfillment.privacy_portal_settings.manage': True, 'permission.dataRightsFulfillment.personal_information.read': True, 'permission.dataRightsFulfillment.personal_information.edit': True, 'permission.dataRightsFulfillment.personal_information.run': True, 'permission.consentGovernance.access': True, 'permission.consentGovernance.consent_sources.read': True, 'permission.consentGovernance.consent_sources.edit': True, 'permission.consentGovernance.consent_sources.create': True, 'permission.consentGovernance.consent_sources.delete': True, 'permission.consentGovernance.consent_sources.test': True, 'permission.consentGovernance.reports.read': True, 'permission.consentGovernance.reports.export': True, 'permission.consentGovernance.agreements.read': True, 'permission.consentGovernance.agreements.edit': True, 'permission.consentGovernance.agreements.create': True, 'permission.consentGovernance.agreements.delete': True, 'permission.dataProcessingAndSharing.access': True, 'permission.dataProcessingAndSharing.read': True, 'permission.dataProcessingAndSharing.manage': True, 'permission.applications.cyberark.read': True, 'permission.applications.cyberark.edit': True, 'permission.applications.cyberark.test': True, 'permission.applications.cyberark.create': True, 'permission.applications.cyberark.delete': True, 'permission.applications.hashicorp.read': True, 'permission.applications.hashicorp.edit': True, 'permission.applications.hashicorp.test': True, 'permission.applications.hashicorp.create': True, 'permission.applications.hashicorp.delete': True, 'permission.applications.file_labeling.read': True, 'permission.applications.file_labeling.import': True, 'permission.applications.file_labeling.manage': True, 'permission.applications.file_labeling.delete': True, 'permission.applications.risk.read': True, 'permission.applications.risk.manage': True, 'permission.applications.breach_response.read': True, 'permission.applications.breach_response.edit': True, 'permission.applications.breach_response.create': True, 'permission.applications.breach_response.explore': True, 'permission.applications.breach_response.delete': True, 'permission.applications.access_intelligence.read': True, 'permission.applications.manage_custom_apps': True, 'permission.applications.Remediation.data_owner': True, 'permission.applications.Remediation.preview': True, 'permission.helpAbout.access': True, 'permission.tasks.access': True, 'permission.applications.PIA.record_read': True, 'permission.applications.PIA.record_edit': True, 'permission.applications.PIA.record_invite_collaborators': True, 'permission.applications.PIA.record_delete': True, 'permission.applications.PIA.record_manage': True, 'permission.applications.PIA.records_import': True, 'permission.applications.PIA.template_read': True, 'permission.applications.PIA.template_delete': True, 'permission.applications.PIA.collab_read': True, 'permission.applications.PIA.template_export': True, 'permission.applications.PIA.collab_in_review_edit': True, 'permission.applications.PIA.collab_submit': True, 'permission.applications.PIA.collab_apply': True, 'permission.applications.PIA.risk_manager_manage': True, 'permission.applications.PIA.risk_summary_read': True, 'permission.applications.PIA.collab_delete': True, 'permission.applications.PIA.risk_manager_delete': True, 'permission.applications.PIA.risk_manager_read': True, 'permission.applications.PIA.records_export': True, 'permission.applications.PIA.collab_in_collaboration_edit': True, 'permission.applications.RoPA.record_read': True, 'permission.applications.RoPA.record_edit': True, 'permission.applications.RoPA.record_delete': True, 'permission.applications.RoPA.template_delete': True, 'permission.applications.RoPA.records_import': True, 'permission.applications.RoPA.records_export': True, 'permission.applications.RoPA.record_manage': True, 'permission.applications.RoPA.record_invite_collaborators': True, 'permission.applications.RoPA.template_read': True, 'permission.applications.RoPA.template_manage': True, 'permission.applications.RoPA.template_export': True, 'permission.applications.RoPA.collab_read': True, 'permission.applications.RoPA.collab_in_collaboration_edit': True, 'permission.applications.RoPA.collab_apply': True, 'permission.applications.RoPA.collab_submit': True, 'permission.applications.RoPA.collab_delete': True, 'permission.applications.RoPA.collab_in_review_edit': True, 'permission.applications.PIA.template_manage': True}, 'legacyPermission': 'ops', 'upgraded_at': '2023-03-21T16:52:46.625Z', 'description': 'Data Remediation App Data Owner role'}