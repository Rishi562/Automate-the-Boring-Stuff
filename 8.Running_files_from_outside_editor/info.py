#! python3


"""The first line of all your Python programs should be a shebang line, which tells your computer that you want Python to execute this program. The shebang line begins with #!, but the rest depends on your operating system.
shebang begins with #!

On Windows, the shebang line is #! python3.
On OS X, #! /usr/bin/env python3.
On Linux,#! /usr/bin/python3.

You will be able to run Python scripts from editors without the shebang line, but the line is needed to run them from the command line.
"""

n="hello world"
print(n)

# if we run this from run in windows using py.exe C:\Users\rishi\OneDrive\Desktop\Info.py,it closes witnin a second
#so we need to run a batch file(shell scripts) along with our program

#a batch file is a text file with commands saved to a file that ends with .bat

""" Bat file

@py C:\Users\rishi\OneDrive\Desktop\Info.py %* - tells our PC to run the Python Script
@symbol tells windows to  not display the whole line after @,just run it
%* - tells windows to forward command line arguments to python program

@pause - pauses the cmd so it does not disappear in a second

save both files in same folder

now run the batch file in the folder C:\Users\rishi\OneDrive\Desktop\PythonProgram\hello.bat from run

if we want to skip writing the full directory c:\ and all,we can add the path to environment variable
this can be done in advanced settings
now we can just type hello for the batch file and it will run our program /

"""

#COMMAND LINE ARGUMENTS
# these are typed when we run our program
#if we type hello for the bat file follower by arg1 arg2 arg3
#hello arg1 arg2 arg3, these gets passed on to out python program because of %*

