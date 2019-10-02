# Object-Oriented Programming in Python Live Training

This is the code for the *Safari Live Training* - **Object-Oriented Programming in Python** presented by Arianne Dee

Before the class, please follow these instructions:
1. [Install Python](#1-install-python-36-or-higher)
2. [Install PyCharm](#2-download-pycharm-community-edition)
3. [Download the code](#3-download-the-course-files)
4. [Check that Python was installed properly](#4-make-sure-that-python-is-properly-installed)

## Set up instructions
### 1. Install Python 3.6 or higher
Go to https://www.python.org/downloads/

Click the yellow button at the top to download the latest version of Python.

#### On Mac or Linux
Follow the prompts and install using the default settings.

#### On Windows
The default settings don't add Python to your PATH 
so your computer doesn't know where to look for it when Python runs 
(for some inexplicable reason).

##### If you're just installing Python now
Follow the instructions here: [Windows Python installer instructions](docs/WININSTALL.md)

##### If you've already installed Python with the default settings
Follow the instructions here: [Add Python to PATH variable in Windows](docs/WINSETPATH.md)

### 2. Download PyCharm (Community Edition)
Download here: https://www.jetbrains.com/pycharm/download/

Install, open, and use the default settings.

### 3. Download the course files
If you're viewing this on GitHub already, stay on this page.
Otherwise, go to the GitHub repository: https://github.com/ariannedee/intro-to-python

#### If you know git:
Clone the repository.

#### If you don't know git:
1. Click the "Clone or download" (green) button at the top-right of the page
2. Click "Download ZIP"
3. Unzip it and move the **python-level-2-master** folder to a convenient location

### 4. Make sure that Python is properly installed
1. Open the *Command Prompt* application in Windows
or *Terminal* on Mac or Linux

1. Type `python --version` and press enter

1. Type `python3 --version` and press enter

1. One or both of those commands should print 
a Python version of 3.6 or higher 
(whichever version you just downloaded)

**Note:** 
You can now type just the `python` or `python3` command
in *Command Prompt* or *Terminal* 
to run the Python interpreter.
You can also run a *.py* file by running 
`python filename.py`

## FAQs
### Can I use Python 2?

Yes, but I highly recommend using Python 3. If you are using Python 2, a few commands will be different and you can't use [f-strings](https://realpython.com/python-f-strings/) to format strings.

### Can I use a different code editor besides PyCharm?

Yes, but it is only recommended if you are already know it and are comfortable navigating to different files and running commands in the command line. If it has syntax highlighting for Python, that is ideal.

### PyCharm can't find Python 3

On a Mac:
- Go to **PyCharm** > **Preferences**

On a PC:
- Go to **File** > **Settings**

Once in Settings:
- Go to **Project: oop-python** > **Project Interpreter**
- Look for your Python version in the Project Interpreter dropdown
- If it's not there, click **gear icon** > **Add...**
- In the new window, select **System Interpreter** on the left, and then look for the Python version in the dropdown
- If it's not there, click the **...** button and navigate to your Python location
- You may have to search the internet for where Python gets installed by default on your operating system
