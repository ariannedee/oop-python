# Object-Oriented Programming in Python Live Training

This is the code for the *O'Reilly Live Training* - **Object-Oriented Programming in Python** presented by Arianne Dee

Before the class, please follow these instructions:
1. [Install Python](#1-install-python-38-or-higher)
1. [Check that Python was installed properly](#2-make-sure-that-python-is-properly-installed)
1. [Install PyCharm](#3-download-pycharm-community-edition)
1. [Download the code](#4-download-the-course-files)
5. [Download the resources](#5-at-the-beginning-of-class-download-the-resources)

## Set up instructions
### 1. Install Python 3.8 or higher
Go to https://www.python.org/downloads/

Click the yellow button at the top to download the latest version of Python.

Follow the prompts and install using the default settings.

### 2. Make sure that Python is properly installed
1. Open the *PowerShell* application in Windows
or *Terminal* on Mac or Linux

1. Type `python --version` and press enter 
2. Type `python3 --version` and press enter
3. Type `py --version` and press enter

At least one of those commands should print 
a Python version of 3.8 or higher 
(whichever version you just downloaded).

**Note:** 
You can now type just the `python`, `python3` or `py` command
in *PowerShell* or *Terminal* to run the Python console.
You can also run a *.py* file by running 
`<python cmd> filename.py`

### 3. Download PyCharm
Download here: https://www.jetbrains.com/pycharm/download/

Install, open, and use the default settings.

*Note*: It comes with a 30-day free trial of professional features. 
These are not needed for the course and the free features (or the Community edition) will suffice.

### 4. Download the course files
If you're viewing this on GitHub already, stay on this page.
Otherwise, go to the GitHub repository: https://github.com/ariannedee/oop-python

#### If you know git:
Clone the repository.

#### If you don't know git:
1. Click the "Clone or download" (green) button at the top-right of the page
2. Click "Download ZIP"
3. Unzip it and move the **oop-python-main** folder to a convenient location

### 5. At the beginning of class, download the resources
When you have signed in to the class,
the **Resources** widget will have PDFs for the slides and
for a resource package that has PyCharm shortcuts, links, and a Python 2 to 3 comparison

## FAQs
### Can I use Python 2?

No, nobody should be using Python 2 anymore.

### Can I use a different code editor besides PyCharm?

Jupyter notebooks are not ideal since we'll be working from multiple folders throughout the class.

Other IDEs like VS Code, Atom, and Spyder are fine, but they are only recommended if you are already know it 
and are comfortable navigating to different files and running commands in the command line. 

### PyCharm can't find Python 3

1. On the bottom right of PyCharm, click on the Python Interpreter and select one from the list
1. If it's not there, click **Add New Interpreter** > **Add Local Interpreter...**
1. Try to select an existing Python system interpreter and then look for the Python version in the dropdown (exact instructions differ depending on PyCharm version)
1. If it's not there, click the **...** or **folder icon** button and navigate to your Python location
   - To find where Python is located, [look in these directories](docs/PATH_LOCATIONS.md)
   - You may have to search the internet for where Python gets installed by default on your operating system
