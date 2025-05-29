from Skill import *
from setting import *
from character import *

def view(root,skill:Skill,size,length)->None:
    # Hiện tiêu đề
    skill.get_label_level().pack(anchor="w", padx=5, pady=5)
    # Hiện thanh tiến độ của kỹ năng
    skill.get_progressbar().pack()
    # Hiện tiến trình của kỹ năng
    skill.get_label_progress().pack()
    # Hiện các kỹ năng nhỏ
    if skill.get_subskills() != []:
        for i in range(len(skill.get_subskills())):
            view(root,skill.get_subskills()[i],size-1,length-50)

def view_task(root,skill:Skill,size)-> None:
    label_task = tk.Label(root,text = skill.get_name(),
                             font=("Arial",9, 'bold'),
                             bg= color_background,fg=text_color
                             ,anchor='w')
    label_task.pack(fill='x',padx=5, pady=5)
    for i in skill.get_task():        
        label_task = tk.Label(root,text = i.get_description(),
                              font=("Arial",size - 1)
                              #,bd=1, relief="groove"
                              , bg= color_background,fg=text_color)
        label_task.pack(fill='x')
        button_task = tk.Button(root,text='Hoàn thành',relief="raised",
                                 command = partial(on_button_task_click,skill,i,root))
        button_task.pack(pady=5)

def read_data(name_file) -> None:
    with open(name_file,'r',encoding='utf-8') as file:
        data = json.load(file)
    return data

def write_data(name_file,data)->None:
    with open(name_file,'w',encoding='utf-8') as file:
        json.dump(data,file,ensure_ascii=False, indent=4)


# Cập nhật kích thước của Frame để nó luôn bằng với Canvas (cả chiều rộng và chiều cao)
def update_frame_size(event,canvas,frame_id):
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))    
    # Cập nhật kích thước của content_frame sao cho nó bằng với Canvas
    canvas.itemconfig(frame_id, width=event.width)   

# Liên kết sự kiện cuộn của Canvas với Scrollbar
def on_scroll(event,canvas):
    # Cập nhật cuộn khi cuộn chuột
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

# Tạo hàm xử lý sự kiện khi ấn nút
def on_button_task_click(skill:Skill,task:Task,root):
    gif = skill.grow(task.get_reward())
    root.update_idletasks()
    task.completed()
    current_time = datetime.now()
    formatted_time = current_time.strftime("%d/%m/%Y %H:%M:%S")
    history = formatted_time + " " + task.get_description() + " " + gif + "\n"
    with open("achivement.txt","a+",encoding="utf-8") as file1:
        file1.write(history)
    return 
    
def main():
    root = tk.Tk()
    root.title("Niết Bàn")
    
    # lấy kích thước của màn hình
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # kích thước + vị trí của cửa sổ
    root.geometry(f"{window_width}x{window_height}+{screen_width - window_width}+{0}")
   
    # Tạo một Canvas
    canvas = tk.Canvas(root,bg=color_background)
    canvas.pack(side="left", fill="both", expand=True)
    
    # Tạo một Scrollbar dọc
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    
    # Cấu hình Canvas để sử dụng Scrollbar
    canvas.config(yscrollcommand=scrollbar.set)
    
    # Tạo một Frame con sẽ được gắn vào Canvas
    content_frame = tk.Frame(canvas, bg=color_background)
    
    # Đặt content_frame vào Canvas và gắn nó vào vị trí góc trên bên trái của Canvas
    frame_id = canvas.create_window((0, 0), window=content_frame, anchor="nw")

    


    ''' Đọc các dữ liệu'''
    data = read_data(name_file)
    AI_skill = Skill.from_dict(data[0], content_frame)
    English_skill = Skill.from_dict(data[1], content_frame)
    # Tạo nhãn cơ bản
    label1 = tk.Label(content_frame, text="Kỹ kinh ngàn chùy, có thể gần như Nghệ." +
                     "\n Nghệ kinh bách luyện, có thể gần như Đạo"
                     , font=("Georgia",11,'bold italic'), bg= color_background,fg=text_color)
    label1.pack()
    # Tên
    my_progress = AI_skill.get_total_exp() + English_skill.get_total_exp()
    
    my = Character("Phan Thanh Tuyển", my_progress)
    label2 = tk.Label(content_frame, text = my.get_name(),font=("Arial",12, 'bold'),
                          bg= color_background,fg=text_color)
    label2.pack()
    label3 = tk.Label(content_frame, text = f"{my.get_name_rank()}({my.get_small_rank()})",font=("Arial",10, 'bold'),
                      bg= color_background,fg=text_color)
    label3.pack()
   
    progressbar = ttk.Progressbar(content_frame,length=100,mode="determinate",
                               maximum = my.get_total(),
                               value=my.get_progress())
    progressbar.pack()
    label4 = tk.Label(content_frame, text = f"{round(my.get_progress()*100/my.get_total())}%",font=("Arial",9, 'bold'),
                      bg= color_background,fg=text_color)
    label4.pack()
    

    view(content_frame,AI_skill,size,length)
    view(content_frame,English_skill,size,length)
    ###################################################

    # View task
    label_task = tk.Label(content_frame, text="Task",font=("Arial",12, 'bold'),
                      bg= color_background,fg=text_color)
    label_task.pack()
        
    view_task(content_frame, AI_skill, size)
    for skill in AI_skill.get_subskills():
        if skill.get_parent() == AI_skill.get_name():
            skill.set_parent(AI_skill)
        view_task(content_frame,skill,size)

    view_task(content_frame, English_skill, size)        
    for skill in English_skill.get_subskills():
        if skill.get_parent() == English_skill.get_name():
            skill.set_parent(English_skill)
        view_task(content_frame,skill,size)
    

    
    '''CÁC CHỨC NĂNG'''
    
    # Liên kết sự kiện thay đổi kích thước của Canvas với hàm cập nhật kích
    # thước của Frame và scrollregion
    canvas.bind("<Configure>", lambda event: update_frame_size(event,canvas,frame_id))
    
    # Liên kết sự kiện cuộn chuột vào Canvas
    canvas.bind_all("<MouseWheel>", lambda event: on_scroll(event,canvas))
    root.mainloop()
    
    #Ghi các dữ liệu
    '''AI_skill.reset()
    for i in AI_skill.get_subskills():
        i.reset()
    English_skill.reset()
    for i in English_skill.get_subskills():
        i.reset()'''  
    
    AI_skill_dict = AI_skill.to_dict()
    English_skill_dict = English_skill.to_dict()
    write_data(name_file, [AI_skill_dict,English_skill_dict])
    return 

if __name__ == "__main__":
    main()