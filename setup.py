import re
from setuptools import setup


with open("windbgmon.py", "r", encoding="utf-8") as f:
    version = re.search(r'(?m)^__version__ = "([a-zA-Z0-9.-]+)"', f.read()).group(1)

with open("README.rst", "r", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="windbgmon",
    version=version,
    author="Segev Finer",
    author_email="segev208@gmail.com",
    description="Monitor Windows OutputDebugString messages",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/segevfiner/windbgmon",
    project_urls={
        "Documentation": "https://segevfiner.github.io/windbgmon/",
        "Issue Tracker": "https://github.com/segevfiner/windbgmon/issues",
    },
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Win32 (MS Windows)",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Bug Tracking",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="windbg OutputDebugString OutputDebugStringA OutputDebugStringW",
    zip_safe=False,
    py_modules=["windbgmon"],
    python_requires='>=3.6',
    install_requires=[
        "pywin32",
    ],
    extras_require={
        "dev": [
            "flake8",
            "sphinx==4.*",
            "pytest",
        ],
    },
)
