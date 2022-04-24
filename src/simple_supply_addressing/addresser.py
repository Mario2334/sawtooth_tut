import hashlib
import enum

FAMILY_NAME = 'simple_supply'
FAMILY_VERSION = '0.1'
NAMESPACE = hashlib.sha512(FAMILY_NAME.encode('utf-8')).hexdigest()[:6]
AGENT_PREFIX = '00'
RECORD_PREFIX = '01'


@enum.unique
class AddressSpace(enum.IntEnum):
    AGENT = 0
    RECORD = 1

    OTHER_FAMILY = 100


def get_agent_address(public_key: str):
    return NAMESPACE + AGENT_PREFIX + hashlib.sha512(
        public_key.encode("utf-8")).hexdigest()[:62]


def get_record_address(record_id: str):
    return NAMESPACE + RECORD_PREFIX + hashlib.sha512(
        record_id.encode("utf-8")).hexdigest()[:62]


def get_address_type(address: str):
    if address[:len(NAMESPACE)] != NAMESPACE:
        return AddressSpace.OTHER_FAMILY

    infix = address[6:8]
    if infix == '00':
        return AddressSpace.AGENT
    if infix == '01':
        return AddressSpace.RECORD

    return AddressSpace.OTHER_FAMILY
