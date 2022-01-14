windbgmon
=========
.. image:: https://img.shields.io/pypi/v/windbgmon.svg
   :target: https://pypi.org/project/windbgmon/
   :alt: PyPI

.. image:: https://github.com/segevfiner/windbgmon/actions/workflows/docs.yml/badge.svg
   :target: https://segevfiner.github.io/windbgmon/
   :alt: Docs

Monitor Windows OutputDebugString messages.

Quick Start:

.. code-block:: python

    import windbgmon

    with windbgmon.DbgMon() as dbgmon:
        for pid, msg in dbgmon:
            print(f"[{pid}] {msg}")

Can also be run as a module: ``python -m windbgmon``.
