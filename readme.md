

# Python Template

<!-- https://shields.io -->
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Emily_Birch-blue)](https://www.linkedin.com/in/emily-w-birch/)
[![License](https://img.shields.io/github/license/EmilyWB/PythonTemplate)](LICENSE)

## Description
Hiya, this is my Python template for small command line Python projects. It does not do anything particularly fancy, it just provides quick placeholder setup code for:
- Multi-file projects
- Logging
- .ini file configuration
- Unit tests
- C extensions
- Python virtual environment

### C Extensions
This template contains example code for using C foreign functions in Python using [CFFI](https://pypi.org/project/cffi/). This is to add extra functionality to a Python script, which would be unweildy to write natively. For example, attempting to perform bit-wise operations, or handling explicit data types. In my own experience of using Python scripts to generate data and perform tests for embedded systems, handling explicitely unsigned data is cumbersome in Python. This also opens the door for sharing code snippets from the embedded side where applicable. 

We are using the API mode for CFFI, intended for use with C source code. As this template is intended for use with local C extensions written just for this script, this is the simplest way to integrate the extensions. 

### Relevant Docs
* Python Standard Library
    * [logging](https://docs.python.org/3/library/logging.html)
    * [unittest](https://docs.python.org/3/library/unittest.html)
    * [configparser](https://docs.python.org/3/library/configparser.html)
    * [virtualenv](https://docs.python.org/3/tutorial/venv.html)
* [CFFI C API Mode](https://cffi.readthedocs.io/en/latest/overview.html#api-mode-calling-c-sources-instead-of-a-compiled-library)


## What's Included
```text
repo/
├── readme.txt
├── requirements.txt
├── venvsetup.bat
├── venvteardown.bat
├── config.ini
├── clearlogs.bat
├── LICENSE
├── app/
│   ├── __main__.py
│   ├── app.py
│   ├── configLog.py
│   └── anothermodule.py
├── cext/
│   ├── __main__.py
│   ├── demo.c
│   └── demo.h
├── tests/
│   ├── __main__.py
│   ├── test_cffi_demo.py
│   └── test_anothermodule.py
└── logs/
    └── .gitkeep
```

### readme.txt
You are here!

### requirements.txt
Pip-readable package dependencies that need to be installed in order to run the project.

### venvsetup.bat
Batch file that will setup up a Python virtual environment in _.venv/_, install the project dependencies from _requirements.txt_, and adds current working directory to ```PYTHONPATH``` variable.

### venvteardown.bat
Batch file that will teardown the Python virtual environment for the opened command line, and delete the _.venv_ folder.

### config.ini
A useful project-level config file, for when you want to change stuff in the app without digging into the source code. Read using the ```configparser``` standard library package.

### app/
As it says on the tin, this directory contains the main application source code. Nothing fancy here.

### cext/
Dedicated directory for the CFFI C extensions. Contains the C source code, and the _\_\_main\_\_.py_ script required to build the C source into a useable Python module.

### tests/
Again nothing fancy, some unit tests using ```unittests```. Validates that the demo C extensions that we compile do actually work.

### logs/
The ```logging``` package will save .log files in here. Using the _.gitkeep_ file to make sure the directory is present in the repository.

### clearlogs.bat
Purges _.log_ files from the _logs/_ directory.

## Prerequisites
In order to setup the Python virtual environment for the project, the ```virtualenv``` package will need to be installed in the global Python environment. The _virtualenv_ executable must be pointed to by the PATH environment variable, allowing us to use it on the command line.

Given that the project management is done using Batch scripts, this runs on Windows.

## Running the Application
From the project directory in the command line:
* Setup the Python virtual environment: ```venvsetup.bat```
* Run the main application : ```python app```
* Build the C extensions : ```python cext```
* Run unit tests : ```python tests```
* Clean the log file directory : ```clearlogs.bat```
* Tear down the Python virtual environment : ```venvteardown.bat```

## Future Changes
* :thumbsup: Add build dependency and virtualenv handling
    * [Best Practices for Python Dependency Management](https://medium.com/knerd/best-practices-for-python-dependency-management-cc8d1913db82)
    * [A non-magical introduction to Pip and Virtualenv for Python beginners ](https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/)
* Automate unit tests with GitHub actions
    * [Build and testing Python](https://docs.github.com/en/free-pro-team@latest/actions/guides/building-and-testing-python)

## Author
**Emily Birch** on [GitHub](https://github.com/EmilyWB) and [LinkedIn](https://www.linkedin.com/in/emily-w-birch/).

## License
This code is licensed under the [MIT License](LICENSE).