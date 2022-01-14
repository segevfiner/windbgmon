import os
import threading
import win32api
import windbgmon


def test_dbgmon():
    messages = []

    with windbgmon.DbgMon() as dbgmon:
        def monitor():
                for pid, msg in dbgmon:
                    messages.append((pid, msg))
        thread = threading.Thread(target=monitor)
        thread.start()

        win32api.OutputDebugString("Hello, World!")

        dbgmon.stop()
        thread.join()

        assert (os.getpid(), "Hello, World!") in messages
