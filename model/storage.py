# model/storage.py

import sqlite3
from model.skill import Skill
from model.task import Task
from config.settings import rank, rewards
DB_PATH = "learning.db"

# Lấy tất cả kỹ năng gốc (không có parent)
def get_root_skills():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM skills WHERE parent_id IS NULL")
        rows = cursor.fetchall()
        return [load_skill_with_subskills(row[0]) for row in rows]

# Đệ quy lấy skill và sub-skills
def load_skill_with_subskills(skill_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, level, progress FROM skills WHERE id = ?", (skill_id,))
        row = cursor.fetchone()
        if not row:
            return None

        skill = Skill(name=row[1], level=row[2], progress=row[3], sub_skills=[], tasks=[], parent_skill=None)
        skill.id = row[0]  # Gán thêm ID để dùng sau này

        # Load tasks
        cursor.execute("SELECT description, reward, times_completed FROM tasks WHERE skill_id = ?", (skill_id,))
        task_rows = cursor.fetchall()
        for t in task_rows:
            task = Task(description=t[0], reward=t[1], times_completed=t[2])
            task.register(skill)
            skill.add_task(task)

        # Load subskills
        cursor.execute("SELECT id FROM skills WHERE parent_id = ?", (skill_id,))
        subskill_rows = cursor.fetchall()
        for sub in subskill_rows:
            sub_skill = load_skill_with_subskills(sub[0])
            if sub_skill:
                sub_skill.set_parent(skill)
                skill.add_subskill(sub_skill)

        return skill

# Cập nhật số lần hoàn thành của task

def update_task_completion_by_id(skill_id, task_description):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE tasks
            SET times_completed = times_completed + 1
            WHERE description = ? AND skill_id = ?
        """, (task_description, skill_id))

    conn.commit()

def update_skill_with_reward_by_id(skill_id,current_progress,current_level):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE skills
            SET progress = ?,level = ?
            WHERE id = ?
                       """,(current_progress,current_level,skill_id))