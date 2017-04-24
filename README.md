# Plot Generation Engine

An application that implements a modified version of pyhop to allow for user friendly editing of a series of tasks and states.

## Getting Started

UI: Simply use your preferred python3 interpreter to run pyGame/main.py.
Parser: An example of how the parser operates is given with parser_testing.py

### Prerequisites

UI: Requires PyQt5 and Python 3.5 or later. To install PyQt5 on a Windows, OS X, and/or 64-bit Linux machine, in the command line enter 'pip3 install PyQt5' without the quotes.
Parser: Requires Python3 and the library jsonpickle. To install jsonpickle, use the command "pip install -U jsonpickle"

## Built With

* [PyQt5](https://www.riverbankcomputing.com/software/pyqt/download5) - The GUI tools
* [Pyhop](https://bitbucket.org/dananau/pyhop) - The code that handles the tasks and states, modified to allow for prerequisites to tasks and live editing of the code.

## Versioning

We used github for all version control.

## Authors

* [Spencer Bryant](https://github.com/sevistatic)
* **hapner**
* **bnol**
* **ryannichols**
* **murdrad**

## To-Do

List of all intended features left to implement:

* Complete integration between UI and Parser
* Implementation of editing files via the parser
* Drag and drop in the UI between tasks and current plan
* Opening a file
* Saving a file

## Acknowledgments

* Dana S. Nau - Copyright owner of Pyhop
