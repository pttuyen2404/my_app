# model/skill.py

import random
from model.task import Task
from config.settings import rank, rewards


class Skill:
    def __init__(self, name, level, progress, tasks=None, sub_skills=None, parent_skill=None, skill_id=None):
        self.name = name
        self.level = level
        self.progress = progress
        self.tasks = tasks if tasks is not None else []
        self.sub_skills = sub_skills if sub_skills is not None else []
        self.parent_skill = parent_skill
        self.total = rank[level][1] if parent_skill else rank[level + 1][1]
        self.id = skill_id  # ✅ thêm dòng này

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_progress(self):
        return self.progress

    def get_total(self):
        return self.total

    def get_subskills(self):
        return self.sub_skills

    def get_total_exp(self):
        exp = rank[self.level][1] if self.level > 0 else 0
        return self.progress + exp

    def get_task(self):
        return self.tasks

    def get_parent(self):
        return self.parent_skill

    def add_task(self, task: Task):
        self.tasks.append(task)

    def add_subskill(self, skill):
        self.sub_skills.append(skill)

    def set_parent(self, parent):
        self.parent_skill = parent

    def update_progress(self, amount):
        level_up = False
        current_progress = self.progress + amount
        if current_progress <= self.total:
            self.progress = current_progress
        else:
            self.progress = current_progress - self.total
            self.level += 1
            level_up = True
            self.total = rank[self.level][1] if self.parent_skill else rank[self.level + 1][1]
        return amount,level_up
    def grow(self, reward):
        from model.storage import update_skill_with_reward_by_id
        # tăng tính ngẫu nhiên bằng cách thêm hàm random
        ran = random.randint(1, 105)
        bonus = 0
        
        if ran >= 104:
            bonus = reward * 10
        elif ran > 95 and ran < 104:
            pass  # UI xử lý phần thưởng đặc biệt
        elif ran <= 10 and ran > 1:
            bonus = reward * -2
        elif ran >= 90 and ran <= 95:
            bonus = reward * 2
        elif ran <= 70 and ran > 40:
            bonus = int(reward * -0.5)
        elif ran <= 40 and ran > 10:
            bonus = 0
        elif ran > 70 and ran < 90:
            bonus = int(reward * random.random())

        reward,lv_up = self.update_progress(bonus + reward)
        update_skill_with_reward_by_id(self.id,self.progress,self.level)
        # áp dụng tương tự cho parent_skill 
        if self.parent_skill:
            self.parent_skill.grow(reward) 
            update_skill_with_reward_by_id(self.parent_skill.id,self.parent_skill.progress,self.parent_skill.level)

        return reward,lv_up

    def reset(self):
        self.progress = 0
        self.level = 0
        
    def get_level_name(self):
        from config.settings import rank
        return rank[self.level][0]
