# BigID Python Library Base BigID class
__author__ = "Brenton Harley"
__version__ = "1.0.0"
__status__ = "Development"

import bigid
from data_types import BigData, CatalogPii, CatalogRisk
from exceptions import CatalogException


def get_supported_filters(method: str) -> dict:
    """Return supported filters for a given method"""
    methods: tuple(dict[str, list]) = {
        "get_pii_findings": ["count"],
        "supported_filters": True,
    }
    if method in methods:
        return methods
    return {f"{method}": "No filter support for method", "supported_filters": None}


def get_findings(bigid: bigid.BigID) -> BigData:
    """Get findings from the catalog"""
    data = bigid.make_request(
        api_path="/api/v1/data-catalog/object-summary", http_method="get"
    )
    return data


def get_pii_findings(
    bigid: bigid.BigID, data_source_name: str = None
) -> list[CatalogPii]:
    """get pii findings for all sources"""
    list_of_sources = list[CatalogPii]
    if data_source_name:
        data = bigid.make_request(
            api_path=f"/api/v1/data-catalog/object-summary/{data_source_name}",
            http_method="GET",
        )
    else:
        data = bigid.make_request(
            api_path="/api/v1/data-catalog/object-summary", http_method="GET"
        )
        for each_data_source in data.data["data"]:
            list_of_sources = CatalogPii(
                source_name=each_data_source["source"],
                total_objects=each_data_source["totalObjects"],
                total_with_pii=each_data_source["totalObjectsWithPii"],
                total_with_pii_open_access=each_data_source[
                    "totalObjectsWithPiiAndOpenAccess"
                ],
                scan_id=each_data_source["scanId"],
            )
    return list_of_sources


# def get_catalog_csv(bigid: bigid.BigID, )
def get_source_risk(bigid: bigid.BigID, data_source_name: str) -> CatalogRisk:
    """get the risk profile of a given data sourece"""
    data = bigid.make_request(
        api_path=f"/api/v1/data-catalog/risk/ds/summary", http_method="GET"
    )
    return data


def get_classification_findings(bigid: bigid.BigID, data_source: str = None):
    """Get classification findings for a given ds if provided"""
    if data_source:
        data = bigid.make_request(
            api_path=f"/api/v1/stream-collections/classification_findings?filter={data_source}",
            http_method="GET",
        )
        return data

    data = bigid.make_request(
        api_path="/api/v1/stream-collections/classification_findings", http_method="GET"
    )
    return data
