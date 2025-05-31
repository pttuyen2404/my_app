# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 19:21:59 2024

@author: hoar1
"""
import tkinter as tk
from tkinter import ttk
#from PIL import Image, ImageTk
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

