from dataclasses import dataclass


@dataclass
class BigData:
    ''' Base data class for BigID '''
    status_code: int
    data: dict[str, str]