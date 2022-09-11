# monkeytype
Desktop version of the typing website monkeytype.

This is a desktop interface for https://www.monkeytype.com made in Python 3.8 using PyQt5 WebView, BeautifulSoup, and PyPresence.

This is my first time using PyQt5, so this is mostly just a way for me to learn the library and mess around with things.


To run this program, ensure all modules listed in requirements are installed with pip install. These modules are:
 - PyQt5
 - PyQtWebEngine
 - beautifulsoup4
 - pypresence

Some of these modules only work on python versions above 3.8 so please ensure you are running this program from said version of Python.
Run the program by navigating to the directory it is stored in with cmd and using python main.py 



CURRENTLY:
 - Produces PyQt5 WebView with correct icon, window name etc
 - Displays monkeytype.com
 - Connects with Discord RPC and displays metrics like live wpm, final wpm etc to local users profile (may require user to "add game" under discord activity)

TODO:
 - Add more metrics
 - Optimise and improve code

ISSUES:
 - Each time the program loops to fetch live data, micro stutter occurs in webview, quite annoying while typing. 
 
Different Rich Presence States, and how the interface currently looks:
![image](https://user-images.githubusercontent.com/66559391/189547495-f2704a99-e405-4ea9-b9d8-6a1d087a944a.png)


![image](https://user-images.githubusercontent.com/66559391/189547498-970235a1-07a5-4bc7-a168-635a4d0bea2d.png)
