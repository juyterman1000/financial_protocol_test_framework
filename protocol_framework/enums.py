from enum import Enum

class MessageType(Enum):
    HEARTBEAT = "0"
    LOGIN = "A"
    LOGOUT = "5"
    ORDER_NEW = "D"
    ORDER_CANCEL = "F"
    EXECUTION_REPORT = "8"
    MARKET_DATA = "W"
