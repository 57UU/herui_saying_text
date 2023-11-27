import requests
import time
from threading import Thread
import random

class HR:
    def __init__(self,interval:int=10):
        self.interval=interval#每隔interval分钟就更新一次
        self.list=[]
        self.thread=Thread(target=self._task)
        self.thread.start()
    def pickOneSaying(self)->str:
        if(len(self.list)==0):
            return "Loading"
        return self.list[random.randint(0,len(self.list)-1)]
    #--------private-----------
    def _task(self):
        while True:
            self._fetch()
            time.sleep(self.interval*60)
            
    def _fetch(self):
        try:
            txt=requests.get("https://57uu.github.io/herui_saying_text/").text
            self.list=[i for i in txt.split("\n") if i!=""]
        except Exception as e:
            print("An error occured while fetching data :",e)
        
