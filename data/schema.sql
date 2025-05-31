CREATE TABLE IF NOT EXISTS skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    level INTEGER NOT NULL,
    progress INTEGER NOT NULL,
    parent_id INTEGER,
    FOREIGN KEY (parent_id) REFERENCES skills(id),
    FOREIGN KEY (level) REFERENCES ranks(level)
);

CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    skill_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    reward INTEGER NOT NULL,
    times_completed INTEGER NOT NULL,
    FOREIGN KEY (skill_id) REFERENCES skills(id)
);

CREATE TABLE IF NOT EXISTS ranks (
    level INTERGER PRIMARY KEY AUTOINCREMENT,
    total INTERGER NOT NULL,
    rank TEXT NOT NULL
);

INSERT INTO skills(id, name, level, progress, parent_id)
VALUES 
(1,'AI',1,310,NULL),
(2,'Machine Learning',1,228,1),
(3,'Deep Learning',1,86,1),
(4,'Data Analys',0,0,1),
(5,'English',1,243,NULL),
(6, 'Vocabulary', 0, 24, 5),
(7, 'Speaking', 1, 223, 5),
(8, 'Writting', 1, 114, 5);

INSERT INTO tasks(skill_id, description, reward, times_completed) VALUES
(1, '1.Học kiến thức cơ bản về AI (> 30 minutes)', 10, 7),
(1, '2.Xử lý dữ liệu và tiền xử lý dữ liệu', 20, 1),
(1, '3.MLOps và triển khai thực tế', 20, 0),
(1, '4.Các thuật toán tối ưu hóa mô hình', 15, 6),
(1, '5.Framework trong khi triển khai mô hình', 10, 1),
(1, '6. Ôn lại những gì đã học (1 bài)', 10, 1),
(2, '1.Học kiến thức nền tảng về toán học và thống kê (> 30 minutes)', 10, 1),
(2, '2.Thuật toán machine learning cơ bản (lý thuyết)', 20, 8),
(2, '3.Thuật toán machine learning cơ bản (code)', 20, 4),
(2, '4. Ôn lại những gì đã học (1 bài)', 10, 0),
(3, '1.Học kiến thức nền tảng về Deep Learning (> 30 minutes)', 10, 2),
(3, '2.Thuật toán Deep learning (lý thuyết)', 20, 3),
(3, '3.Thuật toán Deep learning (code)', 20, 4),
(3, '4.Explainable AI (XAI) và Interpretability (Diễn Giải Mô Hình)', 10, 0),
(3, '5.Ôn lại những gì đã học (1 bài)', 10, 0),
(4, '1.Học kiến thức cơ bản về phân tích dữ liệu (> 30 minutes)', 10, 0),
(6, '1.Học 10-15 từ vựng trong 1 chủ đề', 10, 2),
(6, '2.Ôn 10-15 từ vựng trong 1 chủ đề', 5, 0),
(6, '3.Viết đoạn văn từ 3-4 câu dựa trên chủ đề vừa học', 20, 0),
(7, '1.Luyện 5 âm trong tiếng anh', 10, 1),
(7, '2.Đọc 1 bài read aloud > 60%', 10, 7),
(7, '3.Mô tả 1 bức ảnh bằng tiếng anh', 15, 10),
(7, '4.Trả lời 1 câu hỏi bằng tiếng anh', 5, 10),
(7, '5.Trả lời 1 câu hỏi có ngữ liệu bằng tiếng anh', 5, 0),
(7, '6.Trình bày quan điểm cá nhân', 30, 0),
(8, '1.Viết câu theo 2 bức tranh cho sẵn', 5, 17),
(8, '2.Viết 1 email', 20, 3),
(8, '3.Viết bài luận trình bày quan điểm', 50, 1);