# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 18:23:47 2024

@author: hoar1
"""
import sys
import time
import random
from setting import *

class Task:
    def __init__(self,description,reward,times_completed=0):
        self.description = description # tên nhiệm vụ
        self.reward = reward # phần thưởng khi hoàn thành
        self.times_completed = times_completed # Tính số lần hoàn thành của task

    def get_description(self):
        return self.description
    
    def get_reward(self):
        return self.reward
    
    def completed(self):
        self.times_completed += 1
    
    def to_dict(self):
        return {
            "description":self.description,
            "reward":self.reward,
            "times_completed": self.times_completed
            }
    @classmethod
    def from_dict(cls,data):
        return cls(data['description'],data['reward'],data['times_completed'])
        
class Skill:
    def __init__(self,name,level,progress,root,tasks:Task = None,sub_skills = None,parent_skill = None):
        self.name = name # Thuộc tính tên kỹ năng
        self.level = level # Thuộc tính cấp độ của kỹ năng
        self.label_level = tk.Label(root,text=f'{self.name}({rank[level][0]})',
                                    font=('Arial',size,'bold'),
                                    bg=color_background,fg=text_color)
        self.progress = progress # Tiến trình của kỹ năng
        self.parent_skill = parent_skill
        self.total = rank[level][1] if self.parent_skill != None else rank[level+1][1] # Tổng tiến trình hiện tại của kỹ năng
        
        self.progressbar = ttk.Progressbar(root,length=length,mode="determinate",
                                   maximum = self.total,
                                   value=self.progress)
                                 
        self.sub_skills = sub_skills if sub_skills is not None else []
        self.label_progress = tk.Label(root,text=f'{self.progress}/{self.total}'
                          ,font=("Arial",size, 'bold')
                          , bg= color_background,fg=text_color)
        self.tasks = tasks if tasks is not None else []
        
    def get_name(self):
        return self.name
    
    def get_level(self):
        return self.level
    def get_label_level(self):
        return self.label_level
    def get_progress(self):
        return self.progress
    
    def get_total(self):
        return self.total

    def get_subskills(self):
        return self.sub_skills
    
    def get_progressbar(self):
        return self.progressbar
    
    def get_total_exp(self):
        exp = rank[self.level][1] if self.level > 0 else 0
        return self.progress + exp
    
    def get_label_progress(self):
        return self.label_progress
    
    def get_task(self):
        return self.tasks
    
    def get_parent(self):
        return self.parent_skill
    
    def add_task(self,task:Task):
        self.tasks.append(task)
        
    def add_subskill(self,skill1: "Skill") -> None:
        self.sub_skills.append(skill1)
        
    def set_parent(self,parent):
        self.parent_skill = parent
        
    def grow(self,reward):
        # set bonus
        ran = random.randint(1, 105)
        bonus = 0
        gif = None
        if ran >= 104:
            bonus = reward * 10
        elif ran > 95 and ran < 104:
            gif = RewardforWinner()
            messagebox.showinfo("Chúc mừng bạn đã nhận được phần quà",f'{gif}')
        elif ran <= 10 and ran > 1:
            bonus = reward * -2
        elif ran >= 90 and ran <= 95:
            bonus = reward * 2
        elif ran <= 70 and ran > 40:
            bonus = int(reward * -0.5)
        elif ran <= 40 and ran > 10:
            bonus = int(reward * 0)
        elif ran > 70 and ran < 90:
            bonus = int(reward*random.random())
        # + điểm
        fprogress = self.progress + reward + bonus
        if fprogress <= self.total:
            self.progress = fprogress
            messagebox.showinfo("Đồ ăn thì luyện nhiều",f'{self.name} + {reward + bonus}EXP')
        else:
            self.progress = fprogress - self.total
            self.level += 1
            gift = rewards[self.level - 1][random.randint(0,len(rewards[self.level - 1]) - 1)]
            messagebox.showinfo("Chúc mừng",f"Bạn được thưởng{gift}")
            self.total = rank[self.level][1] if self.parent_skill != None else rank[self.level+1][1]
            self.progressbar['maximum'] = self.total
            self.label_level.config(text=f'{self.name}({rank[self.level][0]})')
            
        self.label_progress.config(text=f'{self.progress}/{self.total}')
        self.progressbar['value'] = self.progress
        if(self.parent_skill != None):
            self.parent_skill.grow(reward)
        if gif is not None:
            return f"Phần thưởng đạt được là: {reward + bonus}exp và {gif}"
        return f"Phần thưởng đạt được là: {reward + bonus}exp"
    def reset(self):
        self.progress = 0
        self.level = 0
    def to_dict(self):
        return{
            "name":self.name,
            "level":self.level,
            "progress":self.progress,
            "total":self.total,
            "subskills":[subskill.to_dict() for subskill in self.sub_skills],
            "parent_skill":self.parent_skill if self.parent_skill == None else 
            self.parent_skill.get_name(),
            "task": [task1.to_dict() for task1 in self.tasks]
            }
    
    @classmethod
    def from_dict(cls,data,root):
        subskills = [Skill.from_dict(subskill,root) for subskill in data['subskills']]
        tasks = [Task.from_dict(task) for task in data['task']]
        return cls(name = data['name'],level = data['level'],progress = data['progress'],root = root ,sub_skills = subskills,parent_skill = data['parent_skill'],tasks = tasks)
        
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        