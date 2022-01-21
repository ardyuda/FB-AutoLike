import pip

try:
    import tkinter
except ImportError:
    pip.main(['install', 'tkinter'])

try:
    import pyautogui
except ImportError:
    pip.main(['install', 'pyautogui'])

try:
    import selenium
except ImportError:
    pip.main(['install', 'selenium'])

try:
    import threading
except ImportError:
    pip.main(['install', 'threading'])

try:
    import cryptocode
except ImportError:
    pip.main(['install', 'cryptocode'])

