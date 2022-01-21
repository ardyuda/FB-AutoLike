# FB-AutoLike v1.0

'''
# Feature v1.0:

- Auto Login
- Auto Liking other people's posts in several minutes

'''

import __init__
from tkinter import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import pyautogui
import os
from threading import Thread
from time import time, sleep
from cryptocode import encrypt,decrypt

encryptKey = open(os.getcwd()+'\\encrypt.key', 'r').read().split('|')

class Main(Tk):
    cwd = os.getcwd()
    infologin = f'{cwd}\\login.info'
    key = 'key'
    codeBy = 'Code By: ardyuda' # Cannot Be Removed 
    def __init__(self):
        super().__init__()
        self.geometry("400x300+0-30")
        self.title("FB-AutoLike")
        # frames
        self.frame00 = Frame()
        self.frame0 = Frame()
        self.frame1a = Frame()
        self.frame1b = Frame()
        self.frame1c = Frame()
        self.frame2 = Frame()
        self.save = None
        self.r = encryptKey[0]
        open(__file__, 'w').write(decrypt(encryptKey[1], encryptKey[0]))
        try:
            self.login = decrypt(open(self.infologin, 'r').read(), encryptKey[0])
        except FileNotFoundError:
            self.login = None
        self.frame0_()

    def buttonCmd(self, id):
        if id == 0:
            try:
                self.time = float(self.entry0.get())
                try:
                    open(self.infologin, 'r')
                    self.frame0_(create=False)
                    self.frame2_(create=True)
                    Thread(target=self.mainAutoLike).start()
                except FileNotFoundError:
                    self.frame0_(create=False)
                    self.frame1_(create=True)
            except:
                pass
        if id == 1:
            if '@' in self.entry1a.get() and len(self.entry1b.get()) >= 8:
                self.email = self.entry1a.get()
                self.password = self.entry1b.get()
                self.frame1_(create=False)
                self.frame2_(create=True)
                Thread(target=self.mainAutoLike).start()
        if id == 2:
            os.remove(self.infologin)
            self.removelogin.destroy()
        if id == 3:
            self.frame1_(create=False)
            self.frame0_(create=True)

    def frame0_ (self, create=True):
        if create:
            # frame0
            self.frame0 = Frame()
            self.frame0.pack(expand=True)
            self.removelogin = Button(self.frame0, text='Delete Login', bg='red', fg='white')
            if self.login:
                self.removelogin['command'] = lambda: self.buttonCmd(2)
                self.removelogin.pack(side=BOTTOM)
            Label(self.frame0, text='How long is this bot running? (in minutes)', font='Arial').pack()
            self.entry0 = Entry(self.frame0, width=20, font='Arial')
            self.entry0.pack(side=LEFT, padx=30, pady=30, anchor=E)
            # frame00
            self.frame00 = Frame()
            self.frame00.pack()
            Button(self.frame0, text='OK', font='Arial', bg='blue', fg='white', command=lambda: self.buttonCmd(0)).pack(side=LEFT)
            self.run = Label(self.frame00, text= decrypt(self.r, self.key))
            self.run.pack()    
        else:
            self.frame00.destroy()
            self.frame0.destroy()
        
    def frame1_(self, create=True):
        if create:
            # frame1a
            self.frame1a = Frame()
            self.frame1a.pack(expand=True, anchor=S)
            Label(self.frame1a, text='username', font='Arial', padx=20).pack(side=LEFT)
            self.entry1a = Entry(self.frame1a, font='Arial')
            self.entry1a.pack(side=LEFT)
            # frame1b
            self.save = IntVar()
            self.frame1b = Frame()
            self.frame1b.pack(anchor=N, pady=20)
            Checkbutton(self.frame1b, text='Save Login', variable=self.save, onvalue=1, offvalue=0).pack(side=BOTTOM, pady=10)
            Label(self.frame1b, text='password', font='Arial', padx=20).pack(side=LEFT)
            self.entry1b = Entry(self.frame1b, font='Arial', show='*')
            self.entry1b.pack(side=LEFT)
            # frame1c
            self.frame1c = Frame()
            self.frame1c.pack(expand=True, anchor=N)
            Button(self.frame1c, text="Login", font="Arial", bg="blue", fg="white", command=lambda: self.buttonCmd(1)).pack(side=LEFT)
            Button(self.frame1c, text="Back", font="Arial", bg="red", fg="white", command=lambda: self.buttonCmd(3)).pack(side=LEFT, padx=20)
            # frame00
            self.frame00 = Frame()
            self.frame00.pack()
            self.run = Label(self.frame00, text= decrypt(self.r, self.key))
            self.run.pack()
        else:
            self.frame1a.destroy()
            self.frame1b.destroy()
            self.frame1c.destroy()
            self.frame00.destroy()

    def frame2_ (self, create=True):
        if create:
            # frame2
            self.frame2 = Frame()
            self.frame2.pack(expand=True)
            self.label = Label(self.frame2, text= 'Running FB-AutoLike Bot...', font='Arial', fg='blue')
            self.label.pack()
             # frame00
            self.frame00 = Frame()
            self.frame00.pack()
        else:
            self.frame2.destroy()

    def mainAutoLike(self):

        try:
            self.run
        except:
            self.label['text'] = decrypt('l0KbDj/36at7YaDpnFL5*fDrHLgz0e1TvIysGs6zyuw==*RSuA5UNuwo3QiBn4tdlrKg==*R4XFa+Z2iJt9+PPVHrn5PQ==', encryptKey[0])
            quit()

        try:
            driver = webdriver.Edge(executable_path=f'{self.cwd}\\msedgedriver.exe')
        except Exception as e:
            self.label['text'] = f'{e}\nVisit https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ \nAnd Download the Suitable Version'
        driver.maximize_window()
        self.label['text'] = 'Open Facebook...'
        driver.get('https://www.facebook.com')

        if self.login:
            self.email, self.password = self.login.split(',')
        
        email = driver.find_element_by_id('email')
        password = driver.find_element_by_id('pass')
        login = driver.find_element_by_css_selector('button[name="login"]')

        self.label['text'] = 'Entering Email and Password...'
        email.send_keys(self.email)
        password.send_keys(self.password)
        login.click()
        try:
            self.label['text'] = 'Waiting for the Homepage to Appear...'
            WebDriverWait(driver,30).until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[aria-current="page"]')))
        except TimeoutException:
            self.label['text'] = 'Waiting Time Is UP!'
        except:
            self.label['text'] = 'Error Code: 301'
        
        try:
            if self.save.get() == 1:
                self.label['text'] = 'Save Login...'
                self.login = encrypt(f'{self.email},{self.password}', encryptKey[0])
                open(self.infologin, 'w').write(self.login)
        except AttributeError:
            self.label['text'] = 'Error Code: 302'

        elapsed = time()
        self.label['text'] = 'Move the Cursor to the Center'
        pyautogui.moveTo(960,540)
        while encryptKey:
            try:
                like = pyautogui.locateCenterOnScreen(f'{os.getcwd()}\\images\\like.png')
                x = pyautogui.locateCenterOnScreen(f'{os.getcwd()}\\images\\x.png')
            except:
                self.label['text'] = 'Error Code: 303'
            if like:
                self.label['text'] = 'Clicking the Like Button'
                pyautogui.click(like[0],like[1]-10)
            elif x:
                pyautogui.click(x)
            sleep(0.3)
            self.label['text'] = 'Scrolling...'
            pyautogui.scroll(-300)
            sleep(0.2)
            if time()-elapsed >= self.time * 60:
                self.label['text'] = 'Time Out!'
                break
            
        self.frame2_(create=False)
        self.frame0_(create=True)

if __name__ == '__main__':
    app = Main()
    app.mainloop()
    