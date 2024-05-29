## MIT License
##
## Copyright 2014 Nicco Kunzmann
##
## Permission is hereby granted, free of charge, to any person obtaining a copy of this
## software and associated documentation files (the "Software"), to deal in the Software
## without restriction, including without limitation the rights to use, copy, modify, merge,
## publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons
## to whom the Software is furnished to do so, subject to the following conditions:
##
## The above copyright notice and this permission notice shall be included in all copies
## or substantial portions of the Software.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
## INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
## PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
## FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
## OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
## DEALINGS IN THE SOFTWARE.
"""
This script uses a while loop that lets an LED blink while the GUI is still responsive.
Running this script outputs
LED on shiny!
LED off shiny!
LED on shiny!
LED off shiny!
LED on shiny!
LED off shiny!
while the GUI is responsive.
This was created because of an stackoverflow question:
    http://stackoverflow.com/questions/21411748/python-how-do-i-continuously-repeat-a-sequence-without-a-while-loop-and-still
examples:
    http://stackoverflow.com/questions/21440731/tkinter-getting-key-pressed-event-from-a-function
    https://gist.github.com/niccokunzmann/8673951#file-example-py
    https://gist.github.com/niccokunzmann/8673951#file-start_and_stop-py
"""

try: from tkinter  import *
except ImportError: from tkinter import *

from guiLoop import guiLoop # https://gist.github.com/niccokunzmann/8673951

@guiLoop
def led_blink(argument):
    while 1:
        print("LED on " + argument)
        yield 0.5 # time to wait
        print("LED off " + argument)
        yield 0.5

t = Tk()

# run led_blink in this GUI
led_blink(t, 'shiny!')

### you can run several loops at once:
##led_blink(t, 'red')
##led_blink(t, 'blue')
##led_blink(t, 'green')

# add a responsive button
def button_pressed():
    print('button pressed')
Button(t, command = button_pressed, text = 'press me').pack()

# start the GUI loop
t.mainloop()