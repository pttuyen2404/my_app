# main.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from functools import partial
from datetime import datetime

from model.task import Task
from model.character import Character
from model.storage import get_root_skills, update_task_completion_by_id
from view.view import render_skill, render_task, render_character
from config.settings import color_background, text_color, window_width, window_height, size, length, rewards

def on_button_task_click(task: Task, content_frame):

    reward_info,level_up = task.completed()
    update_task_completion_by_id(task.parent.id, task.get_description())

    message = f"Bạn nhận được {reward_info} EXP"
    if level_up:
        gift = rewards[skill.get_level() - 1][0]  # Lấy phần thưởng mẫu theo level
        message += f" và lên cấp! Quà: {gift}"

    messagebox.showinfo("Thông báo", message)

    # Cập nhật lại toàn bộ giao diện
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Tải lại dữ liệu
    skills = get_root_skills()
    AI_skill = skills[0]
    English_skill = skills[1]
    my_progress = AI_skill.get_total_exp() + English_skill.get_total_exp()
    my = Character("Phan Thanh Tuyển", my_progress)
    render_character(content_frame,my)
    render_skill(content_frame, AI_skill, size, length)
    render_skill(content_frame, English_skill, size, length)

    label_task = tk.Label(content_frame, text="Task", font=("Arial", 12, 'bold'),
                          bg=color_background, fg=text_color)
    label_task.pack()

    for skill in [AI_skill] + AI_skill.get_subskills() + [English_skill] + English_skill.get_subskills():
        render_task(content_frame, skill, size, on_button_task_click, content_frame)

def update_frame_size(event, canvas, frame_id):
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    canvas.itemconfig(frame_id, width=event.width)

def on_scroll(event, canvas):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

def main():
    root = tk.Tk()
    root.title("Niết Bàn")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{window_width}x{window_height}+{screen_width - window_width}+0")

    canvas = tk.Canvas(root, bg=color_background)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.config(yscrollcommand=scrollbar.set)

    content_frame = tk.Frame(canvas, bg=color_background)
    frame_id = canvas.create_window((0, 0), window=content_frame, anchor="nw")

    skills = get_root_skills()
    AI_skill = skills[0]
    English_skill = skills[1]

    my_progress = AI_skill.get_total_exp() + English_skill.get_total_exp()
    my = Character("Phan Thanh Tuyển", my_progress)
    render_character(content_frame,my)
    render_skill(content_frame, AI_skill, size, length)
    render_skill(content_frame, English_skill, size, length)

    label_task = tk.Label(content_frame, text="Task", font=("Arial", 12, 'bold'),
                          bg=color_background, fg=text_color)
    label_task.pack()

    for skill in [AI_skill] + AI_skill.get_subskills() + [English_skill] + English_skill.get_subskills():
        render_task(content_frame, skill, size, on_button_task_click, content_frame)

    # Khi canvas thay đổi kích thước cập nhật vùng cuộn
    canvas.bind("<Configure>", lambda event: update_frame_size(event, canvas, frame_id))
    # Bắt sự kiện cuộn chuột
    canvas.bind_all("<MouseWheel>", lambda event: on_scroll(event, canvas))
    root.mainloop()

if __name__ == "__main__":
    main()
