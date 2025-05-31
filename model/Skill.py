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

    def grow(self, reward):
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

        fprogress = self.progress + reward + bonus
        level_up = False
        if fprogress <= self.total:
            self.progress = fprogress
        else:
            self.progress = fprogress - self.total
            self.level += 1
            level_up = True
            self.total = rank[self.level][1] if self.parent_skill else rank[self.level + 1][1]

        if self.parent_skill:
            self.parent_skill.grow(reward)

        return reward + bonus, level_up

    def reset(self):
        self.progress = 0
        self.level = 0
        
    def get_level_name(self):
        from config.settings import rank
        return rank[self.level][0]

    def to_dict(self):
        return {
            "name": self.name,
            "level": self.level,
            "progress": self.progress,
            "total": self.total,
            "subskills": [subskill.to_dict() for subskill in self.sub_skills],
            "parent_skill": self.parent_skill.get_name() if self.parent_skill else None,
            "task": [task.to_dict() for task in self.tasks]
        }

    @classmethod
    def from_dict(cls, data):
        subskills = [Skill.from_dict(sub) for sub in data['subskills']]
        tasks = [Task.from_dict(task) for task in data['task']]
        return cls(
            name=data['name'],
            level=data['level'],
            progress=data['progress'],
            tasks=tasks,
            sub_skills=subskills,
            parent_skill=None  # sẽ thiết lập sau nếu cần
        )
