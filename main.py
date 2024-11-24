# Import Tkinter để tạo giao diện người dùng
import tkinter as tk

# Import các class từ file item.py và knapsack_solver.py
from models.item import Item  # Class Item để đại diện cho các item trong bài toán Knapsack
from models.knapsack_solver import KnapsackSolver  # Class KnapsackSolver để giải bài toán Knapsack
from gui import KnapsackGUI  # Class KnapsackGUI để tạo giao diện người dùng cho bài toán Knapsack

# Đoạn mã này chạy ứng dụng GUI khi main.py được thực thi
if __name__ == "__main__":
    # Khởi tạo cửa sổ chính Tkinter
    root = tk.Tk()
    
    # Tạo ứng dụng GUI bằng cách truyền cửa sổ root cho lớp KnapsackGUI
    app = KnapsackGUI(root)
    
    # Chạy vòng lặp sự kiện GUI, giúp giao diện hoạt động
    root.mainloop()