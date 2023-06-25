#controlling the mouse

# we can use PyAutoGUI

#Controlling Mouse Movement
'''
import pyautogui
wh = pyautogui.size() # Obtain the screen resolution.
wh
Size(width=1920, height=1080)
wh[0]
wh.width

'''


# Moving the Mouse

''' 
import pyautogui
for i in range(10): # Move mouse in a square.
pyautogui.moveTo(100, 100, duration=0.25)
pyautogui.moveTo(200, 100, duration=0.25)
pyautogui.moveTo(200, 200, duration=0.25)
pyautogui.moveTo(100, 200, duration=0.25)

'''

#Getting the Mouse Position
'''
pyautogui.position() # Get current mouse position.
pyautogui.position() # Get current mouse position again.
p = pyautogui.position() # And again.
Point(x=1536, y=637)
p[0] # The x-coordinate is at index 0.
p.x # The x-coordinate is also in the x attribute.

'''


#Planning Your Mouse Movements

'''
One of the difficulties of writing a program that will automate clicking the screen is finding the x- and y-coordinates
of the things you’d like to click. The pyautogui.mouseInfo() function can help you with this.
The pyautogui.mouseInfo() function is meant to be called from the interactive shell, rather than as part of your program. 
It launches a small application named MouseInfo that’s included with PyAutoGUI. The window for the application looks like Figure 20-3.
Enter the following into the interactive shell:

import pyautogui
pyautogui.mouseInfo()

This makes the MouseInfo window appear. This window gives you information 
about the mouse’s cursor current position, as well the color of the pixel 
underneath the mouse cursor, as a three-integer RGB tuple and as a hex value.
The color itself appears in the color box in the window.

To help you record this coordinate or pixel information, you can click one of the eight Copy or Log buttons.
The Copy All, Copy XY, Copy RGB, and Copy RGB Hex buttons will copy their respective information to the clipboard. 
The Log All, Log XY, Log RGB, and Log RGB Hex buttons will write their respective information to the large text field in the window.
You can save the text in this log text field by clicking the Save Log button.
'''