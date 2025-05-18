from enum import Enum

class State(str, Enum):
    COLLECT_CITY = "collect_city"
    COLLECT_CONTACT = "collect_contact_information"
    MASTER_INFORM="master_inform"
    END = "end"
 
