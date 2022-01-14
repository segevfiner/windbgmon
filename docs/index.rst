Welcome to windbgmon's documentation!
=====================================

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Contents:

Monitor Windows OutputDebugString messages.

Quick Start::

    import windbgmon

    with DbgMon() as dbgmon:
        for pid, msg in dbgmon:
            print(f"[{pid}] {msg}")

Can also be run as a module: `python -m windbgmon`.

API
---
.. automodule:: windbgmon
   :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
