If you wish to compile your own version and not run the pre-compiled .exe, please do the following:

- Install the latest version of Python
- In CMD, run:
	pip install pyinstaller
- Change the current working directory to where you saved the git files
- Run:
	pyinstaller -w -F ImageConverter.py
- This will create a directory called dist. This is where you will find the .exe file.