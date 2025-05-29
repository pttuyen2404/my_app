# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 19:21:59 2024

@author: hoar1
"""
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import json
import random
from functools import partial
from datetime import datetime
# tạo color của nền
color_background = '#add8e6'
text_color = '#0f084f'

# tạo kích thước của cửa sổ
window_width = 450
window_height = 600
# size chữ phần nhiệm vụ
size = 10
# kích thước của progressbar
length = 300
# Skill
rank = [["Nhập môn",111],["Thuần thục",333],["Tinh thông",999],["Tiểu Thành",3333],["Đại Thành",9999],["Viên mãn",33333],['Ý',99999]]
# Character
rank_character = [["Thông mạch",1000],["Đoàn cốt",3000],["Luyện phủ",9000],["Nguyên Võ",30000],["Thần Lực",1000000]]
name_file = 'data.json'
character_file = 'character.json'
rewards = [["Cá mún","Phồng tôm","1 ván game","Chúc bạn may mắn lần sau","1 tờ vé số",
           "Chúc bạn may mắn lần sau","1 ly nước mía","1 viên kẹo","1 tập film","1 chương truyện",
           "1 hủ artemia 50ml","5 chương truyện","Cá bảy màu","Ngủ 1 giấc 1h30'","3 viên kẹo",
           "1 miếng bánh tráng","1 ly cafe","1 ly cafe","1 artemia ống 5ml","Sơn chấm thấm hồ cá 100ml","1 cây lạp xưởng"
           "1 cây bút","5 viên oxi","5 cây bèo"],
          ["3 ván game","1 đôi dép đi trong nhà","1 ly sinh tố sầu riêng","1 ly sinh tố bơ","Sơn chấm thấm hồ cá 300ml","1 cây lạp xưởng"
           ,"Chúc bạn may mắn lần sau","1 chương truyện","5 chương truyện","10 chương truyện"],
          ["Chúc bạn may mắn lần sau","Sơn chấm thấm hồ cá 500ml"],
          ["Chúc bạn may mắn lần sau"]]
def RewardforWinner():
    ran1 = random.randint(1,100)
    if ran1 <= 75:
        gif = rewards[0][random.randint(0,len(rewards[0]) - 1)]
    else:
        gif = rewards[1][random.randint(0,len(rewards[1]) - 1)]
    return gif

'''

        task1 = Task('1.Học kiến thức cơ bản về AI (> 30 minutes)',10)
        task2 = Task('2.Xử lý dữ liệu và tiền xử lý dữ liệu',20)
        task3 = Task('3.MLOps và triển khai thực tế',20)
        task4 = Task('4.Các thuật toán tối ưu hóa mô hình',15)
        task5 = Task('5.Framework trong khi triển khai mô hình',10)
        task6 = Task('6.Ôn lại những gì đã học (1 bài)',10)
        AI_skill.add_task(task1)
        AI_skill.add_task(task2)
        AI_skill.add_task(task3)
        AI_skill.add_task(task4)
        AI_skill.add_task(task5)
        AI_skill.add_task(task6)

    task1 = Task('1.Học kiến thức nền tảng về toán học và thống kê (> 30 minutes)',10)
    task2 = Task('2.Thuật toán machine learning cơ bản (lý thuyết)',10)
    task3 = Task('3.Thuật toán machine learning cơ bản (code)',10)
    task4 = Task('4. Ôn lại những gì đã học (1 bài)',5)
    AI_skill.get_subskills()[0].add_task(task1)
    AI_skill.get_subskills()[0].add_task(task2)
    AI_skill.get_subskills()[0].add_task(task3)
    AI_skill.get_subskills()[0].add_task(task4)
    
    "      # Task
      # add task
      task1 = Task("Hoàn thành 1 pomodoro 30'",6)
      task2 = Task("Liên tục học 1 điều gì đó trong vòng 24 giờ",15)
      task3 = Task("Phân tích 1 vấn đề nào đó thành từng phần nhỏ",10)
      task4 = Task("Đưa ra giải pháp cho 1 vấn đề",10)
      task5 = Task("Giữ thái độ tích cực trong 6h",10)
      task6 = Task("Đưa ra kế hoạch rõ ràng cho 1 ngày",10)
      task61 = Task("Và hoàn thành nó",30)
      task7 = Task("Đưa ra kế hoạch rõ ràng cho 1 tuần",20)
      task71 = Task("Và hoàn thành nó",60)
      task8 = Task("Đưa ra kế hoạch rõ ràng cho 1 tháng",30)
      task81 = Task("Và hoàn thành nó",90)
      task9 = Task("Dậy sớm trước 6h và Ngủ trước 23h",10)
      task10 = Task("Tập thể dục 15'",5)
      Soft_skills.add_task(task1)
      Soft_skills.add_task(task2)
      Soft_skills.add_task(task3)
      Soft_skills.add_task(task4)
      Soft_skills.add_task(task5)
      Soft_skills.add_task(task6)
      Soft_skills.add_task(task61)
      Soft_skills.add_task(task7)
      Soft_skills.add_task(task71)
      Soft_skills.add_task(task8)
      Soft_skills.add_task(task81)
      Soft_skills.add_task(task9)
      Soft_skills.add_task(task10)
      task1 = Task("Phân tâm trong 1 pomodoro",5)
      task2 = Task("Ngắt quãng việc học 1 kiến thức trong vòng 48h",20)
      task3 = Task("Không có kế hoạch phải làm gì trong 1 ngày",20)
      task4 = Task("Không có kế hoạch phải làm gì trong 1 tuần",40)
      task5 = Task("Không có kế hoạch phải làm gì trong 1 tháng",60)
      task6 = Task("Chơi game hoặc đọc truyện quá 15'",20)
      task61 = Task("Multitasking",20)
      task7 = Task("Dậy muộn sau 8h sáng hoặc ngủ quá khuya sau 24h",20)
      task71 = Task("Bỏ qua mục tiêu đã đề ra trong ngày",30)
      task8 = Task("Dành hơn 1 giờ để lo lắng về một vấn đề không thể kiểm soát",30)
      task81 = Task("Bắt đầu nhiệm vụ muộn hơn 15' so với kế hoạch",10)
      task9 = Task("Không học hoặc nghiên cứu kiến thức mới trong 2 ngày",50)
      task10 = Task("Ngồi im 1 chỗ quá 1h",10)
      Punishment.add_task(task1)
      Punishment.add_task(task2)
      Punishment.add_task(task3)
      Punishment.add_task(task4)
      Punishment.add_task(task5)
      Punishment.add_task(task6)
      Punishment.add_task(task61)
      Punishment.add_task(task7)
      Punishment.add_task(task71)
      Punishment.add_task(task8)
      Punishment.add_task(task81)
      Punishment.add_task(task9)
      Punishment.add_task(task10)
      
    "

    task1 = Task('1.Học kiến thức cơ bản về phân tích dữ liệu (> 30 minutes)',10)
    AI_skill.get_subskills()[2].add_task(task1)

    task1 = Task('1.Học 10-15 từ vựng trong 1 chủ đề',10)
    task2 = Task('2.Ôn 10-15 từ vựng trong 1 chủ đề',5)
    task3 = Task('3.Viết đoạn văn từ 3-4 câu dựa trên chủ đề vừa học',20)
    English_skill.get_subskills()[0].add_task(task1)
    English_skill.get_subskills()[0].add_task(task2)
    English_skill.get_subskills()[0].add_task(task3)
    
    task1 = Task('1.Luyện 5 âm trong tiếng anh',10)
    task2 = Task('2.Đọc 1 bài read aloud > 60%',10)
    task3 = Task('3.Mô tả 1 bức ảnh bằng tiếng anh',15)
    task4 = Task('4.Trả lời 1 câu hỏi bằng tiếng anh',10)
    task5 = Task('5.Trả lời 1 câu hỏi có ngữ liệu bằng tiếng anh',15)
    task6 = Task('6.Trình bày quan điểm cá nhân',30)
    English_skill.get_subskills()[1].add_task(task1)
    English_skill.get_subskills()[1].add_task(task2)
    English_skill.get_subskills()[1].add_task(task3)
    English_skill.get_subskills()[1].add_task(task4)
    English_skill.get_subskills()[1].add_task(task5)
    English_skill.get_subskills()[1].add_task(task6)
    
    task1 = Task('1.Viết câu theo 1 bức tranh cho sẵn',5)
    task2 = Task('2.Viết 1 email',20)
    task3 = Task('3.Viết bài luận trình bày quan điểm',50)

    English_skill.get_subskills()[2].add_task(task1)
    English_skill.get_subskills()[2].add_task(task2)
    English_skill.get_subskills()[2].add_task(task3)
'''