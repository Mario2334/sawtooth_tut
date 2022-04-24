from sawtooth_sdk.processor.core import TransactionProcessor
from sawtooth_sdk.processor.log import init_console_logging


def main():
    init_console_logging(verbose_level=0)
    processor = TransactionProcessor(url = "tcp://localhost:4004")
