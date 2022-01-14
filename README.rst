windbgmon
=========
Monitor Windows OutputDebugString messages.

Quick Start::

    import windbgmon

    with DbgMon() as dbgmon:
        for pid, msg in dbgmon:
            print(f"[{pid}] {msg}")

Can also be run as a module: `python -m windbgmon`.
