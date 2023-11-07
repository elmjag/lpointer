#!/usr/bin/env python
import time
from PyTango import ConnectionFailed
from tango import Database, DbDevInfo, DeviceProxy

TANGO_CONNECT_RETRY_TIME = 2.1


def _connect_to_db():
    db = None
    while db is None:
        try:
            db = Database()
        except ConnectionFailed:
            print(
                f"failed to connect to tango host, retrying in {TANGO_CONNECT_RETRY_TIME} seconds"
            )
            time.sleep(TANGO_CONNECT_RETRY_TIME)

    return db


def register_device(dev_name, instance_name):
    db = _connect_to_db()

    db_info = DbDevInfo()
    db_info._class = "SarMoto"
    db_info.server = f"SarMoto/{instance_name}"
    db_info.name = dev_name

    db.add_device(db_info)


register_device("b311a-e/dia/alas-01-azi", "azi")
register_device("b311a-e/dia/alas-01-pol", "pol")
