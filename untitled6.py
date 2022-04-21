# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 23:50:48 2022

@author: asreno
"""
import time
class time:
    def __init__(self,h,m,s):
        self.hour=h
        self.minute=m
        self.second=s
           
    def add_time(self,t1, t2):
        
       
        sum.seconds = self.seconds1+self.second2
        if ( sum.seconds >60):
            self.minutes = self.minutes + 1
        sum.minutes = t1.minutes + t2.minutes   
        if ( sum.minutes >60):
            self.hours = self.hours + 1    
        sum.hours = t1.hours + t2.hour

        return sum
        
    def sub_time(self,t1, t2):
        self.sub_second=0
        self.sub_minutes=0
        self.sub_hours=0
        self.sub_seconds = t1.seconds1-t2.second2
        if (  self.sub_second >60):
            self.minutes = self.minutes + 1
            self.sub_minutes = t1.minutes - t2.minutes   
        if (self.sub_minutes >60):
            self.hours = self.hours + 1    
        self.sub_hours = t1.hours - t2.hour

        return self.sub_second,self.sub_minutes,self.sub_hours 
        
    def make_time(self,seconds):
        
        time.hours = self.seconds // 3600
        self.seconds = self.seconds - time.hours * 3600
        time.minutes = self.seconds // 60
        self.seconds = self.seconds - time.minutes * 60
        time.seconds = self.seconds
        return time
x=time(10,20,3)

print(x.add_time())
y=time(367954)
print(y.make_time())

    