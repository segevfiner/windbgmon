"""
Monitor Windows OutputDebugString messages.
"""

import sys
import mmap
import struct
import argparse
import win32event


_DBG_BUFFER_NAME = "DBWIN_BUFFER"
_DBG_BUFFER_SIZE = 4096
_DBG_BUFFER_READY_EVENT_NAME = "DBWIN_BUFFER_READY"
_DBG_DATA_READY_EVENT_NAME = "DBWIN_DATA_READY"
_GLOBAL_PREFIX = "Global\\"


__version__ = "0.1.0"


class DbgMon:
    """
    Monitor Windows OutputDebugString messages.

    Set *global_* to ``True`` to monitor messages in the global scope (Session 0).

    Yields ``(pid: int, msg: str)`` on iteration. Should be :meth:`closed <close>` when finished.
    """

    def __init__(self, global_=False):
        self.closed = False

        if global_:
            prefix = _GLOBAL_PREFIX
        else:
            prefix = ""

        self._buf = mmap.mmap(-1, _DBG_BUFFER_SIZE, tagname=prefix + _DBG_BUFFER_NAME,
                              access=mmap.ACCESS_WRITE)
        self._buffer_ready_event = win32event.CreateEvent(None, False, False,
                                                          prefix + _DBG_BUFFER_READY_EVENT_NAME)
        self._data_ready_event = win32event.CreateEvent(None, False, False,
                                                        prefix + _DBG_DATA_READY_EVENT_NAME)
        self._stop_event = win32event.CreateEvent(None, False, False, None)

    def __iter__(self):
        self._check_closed()

        events = [self._stop_event, self._data_ready_event]
        while True:
            win32event.SetEvent(self._buffer_ready_event)

            result = win32event.WaitForMultipleObjects(events, False, win32event.INFINITE)
            if result == win32event.WAIT_OBJECT_0:
                break
            elif result == win32event.WAIT_OBJECT_0 + 1:
                pid = struct.unpack_from("I", self._buf)[0]
                msg = self._buf[4:].split(b'\0', 1)[0].decode("ansi")

                yield (pid, msg)
            else:
                assert False, f"Unknown return value from WaitForMultipleObjects: {result}"

    def stop(self):
        """
        Stop monitoring.

        Can be called from a different thread to stop a monitoring thread.
        """
        self._check_closed()
        win32event.SetEvent(self._stop_event)

    def _check_closed(self):
        if self.closed:
            raise ValueError("operation on closed DbgMon")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        """Close the DbgMon."""
        self._buf.close()
        self._buffer_ready_event.close()
        self._data_ready_event.close()
        self._stop_event.close()
        self.closed = True


def main():
    parser = argparse.ArgumentParser(description="Monitor Windows OutputDebugString messages.")
    parser.add_argument("--global", dest="global_", action="store_true",
                        help="monitor messages in the global scope (Session 0)")

    args = parser.parse_args()

    with DbgMon(global_=args.global_) as dbgmon:
        for pid, msg in dbgmon:
            print(f"[{pid}] {msg}")


if __name__ == "__main__":
    sys.exit(main())
