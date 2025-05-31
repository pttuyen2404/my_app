# view/skill_view.py

import tkinter as tk
from tkinter import ttk
from config.settings import color_background, text_color

# Hiển thị kỹ năng và cây kỹ năng con

def render_skill(root, skill, size, length):
    label_level = tk.Label(root, text=f'{skill.get_name()} ({skill.get_level_name()})',
                           font=('Arial', size, 'bold'), bg=color_background, fg=text_color)
    label_level.pack(anchor="w", padx=5, pady=5)

    progressbar = ttk.Progressbar(root, length=length, mode="determinate",
                                  maximum=skill.get_total(), value=skill.get_progress())
    progressbar.pack()

    label_progress = tk.Label(root, text=f'{skill.get_progress()}/{skill.get_total()}',
                              font=("Arial", size, 'bold'), bg=color_background, fg=text_color)
    label_progress.pack()

    for subskill in skill.get_subskills():
        render_skill(root, subskill, size - 1, length - 50)

# Hiển thị danh sách nhiệm vụ tương ứng

def render_task(root, skill, size, on_button_task_click, content_frame):
    label_task = tk.Label(root, text=skill.get_name(), font=("Arial", 9, 'bold'),
                          bg=color_background, fg=text_color, anchor='w')
    label_task.pack(fill='x', padx=5, pady=5)

    for task in skill.get_task():
        label_task = tk.Label(root, text=task.get_description(), font=("Arial", size - 1),
                              bg=color_background, fg=text_color)
        label_task.pack(fill='x')

        button_task = tk.Button(root, text='Hoàn thành', relief="raised",
                                command=lambda s=skill, t=task: on_button_task_click(s, t, content_frame))
        button_task.pack(pady=5)
