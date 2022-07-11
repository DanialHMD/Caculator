# Caculator
In this code I a calculator which does 4 main operations with parentheses with out using eval function directly.

## How does it work?
For this, I defined a function named "Calculator" and added a while loop to keep on the code:
```
   while i < len(string):
```
when we jump into the loop we command him too skip on whitespaces.
```
if string[i] == " ":
      i += 1
      continue
```
the whole loop checks for 4 options:
1. whitespaces
2. openning parenthesis
3. number
4. closing parenthesis
> at the end, on the else condition we do a precedence between the last operation and the string operation.

after Calculator we added to other function to have a better look:
- one is prec(precedence) which checks on the which operation should go first.
- other is operating function which does the calculating.

## What about the UI?
graphical user interface is one of the features I add to my codes. it makes it easier for user to use the code.
as my first official project, I wanted it to look perfect; so I added pyqt5.

by importing pyqt5, I made a class and added all the label and buttons that I needed,
added their position on the window, added their functions and we are good to go!


so that was all I wanted to talk about, when we run the code we'll haev a window like this:
![Calculator](https://user-images.githubusercontent.com/108475573/178185745-f410feed-8e7b-46e2-af41-daa6cd140f1f.png)

