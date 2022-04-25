from sawtooth_sdk.processor.core import TransactionProcessor
from sawtooth_sdk.processor.log import init_console_logging

from src.processor.simple_supply_tp.handler import SimpleSupplyHandler


def main():
    processor = None
    try:
        init_console_logging(verbose_level=0)
        processor = TransactionProcessor(url = "tcp://localhost:4004")
        handler = SimpleSupplyHandler()
        processor.add_handler(handler)
        processor.start()
    except KeyboardInterrupt:
        pass
    except Exception as err:  # pylint: disable=broad-except
        print("Error: {}".format(err))
    finally:
        if processor is not None:
            processor.stop()
if __name__ == "__main__":
    main()