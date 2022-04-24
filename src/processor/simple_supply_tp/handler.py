from sawtooth_sdk.processor.handler import TransactionHandler

from src.protobuf.simple_supply_protobuf.payload_pb2 import SimpleSupplyPayload
from src.simple_supply_addressing import addresser


class SimpleSupplyHandler(TransactionHandler):

    @property
    def family_name(self):
        return addresser.FAMILY_NAME

    @property
    def family_versions(self):
        return [addresser.FAMILY_VERSION]

    @property
    def namespaces(self):
        return [addresser.NAMESPACE]

    def apply(self, transaction, context):
        header = transaction.header
        payload = SimpleSupplyPayload(transaction.payload)
        state = SimpleSupplyState(context)