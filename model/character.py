# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 15:41:21 2024

@author: hoar1
"""

from setting import *
import time
import random

class Character:
    def __init__(self,name,progress):
        self.name = name
        count = 0
        for count in range(len(rank_character)):
            if progress > 0:
               progress -= rank_character[count][1]
            else:
                break
        level = count - 1
        progress += rank_character[level][1]
        self.progress = progress
        self.name_rank = rank_character[level][0]
        self.total_rank = rank_character[level][1]
        if self.progress < self.total_rank/3:
            self.small_rank = "Sơ kỳ"
        elif self.progress > self.total_rank*2/3:
            self.small_rank = "Hậu kỳ"
        else:
            self.small_rank = "Trung kỳ"  
                
    def get_name(self):
        return self.name
    
    def get_name_rank(self):
        return self.name_rank
    
    def get_small_rank(self):
        return self.small_rank
    
    def get_total(self):
        return self.total_rank
    
    def get_progress(self):
        return self.progress
    
    