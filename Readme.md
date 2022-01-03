This program does not require Python to be installed. However, i f you wish to compile your own version and not run the pre-compiled .exe, you will need to install Python and Pyinstaller. p

Please do the following if you wish to compile yourself:

- Install the latest version of Python
- In CMD, run:
	pip install pyinstaller
- Change the current working directory to where you saved the git files
- Run:
	pyinstaller -w -F ImageConverter.py
- This will create a directory called dist. This is where you will find the .exe file.
