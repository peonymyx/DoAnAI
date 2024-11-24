# Import thư viện tkinter và ttkbootstrap để tạo giao diện người dùng
import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as ttk  # Thư viện ttkbootstrap để tạo các widget với giao diện đẹp hơn
from ttkbootstrap.constants import *  # Import các hằng số tiện ích từ ttkbootstrap

# Import các module cần thiết từ dự án
from models.item import Item  # Mô hình đại diện cho các item
from models.knapsack_solver import KnapsackSolver  # Lớp giải bài toán Knapsack
from components.header import Header  # Header của giao diện
from components.capacity_input import CapacityInput  # Input để nhập dung lượng túi
from components.item_form import ItemForm  # Form để nhập thông tin item
from components.item_list import ItemsList  # Danh sách các item đã thêm
from components.result_view import ResultsView  # Hiển thị kết quả giải bài toán

# Lớp chính để tạo giao diện bài toán Knapsack
class KnapsackGUI:
    def __init__(self, root):
        """
        Hàm khởi tạo giao diện người dùng.

        :param root: Widget gốc (Tk) để chứa giao diện.
        """
        self.root = root
        self.root.title("Knapsack Problem Solver")  # Tiêu đề cửa sổ
        self.root.geometry("900x700")  # Kích thước cửa sổ
        
        # Áp dụng giao diện "darkly" từ ttkbootstrap
        self.style = ttk.Style(theme="darkly")
        self.solver = KnapsackSolver()  # Tạo đối tượng giải bài toán Knapsack
        self.setup_gui()  # Thiết lập giao diện

    def setup_gui(self):
        """
        Hàm tạo và thiết lập giao diện chính.
        """
        # Frame chính chứa toàn bộ giao diện
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=BOTH, expand=YES)

        # Header
        self.header = Header(self.main_frame)  # Tạo đối tượng Header
        self.header.create()  # Tạo giao diện cho Header
        
        # Vùng nội dung
        content_frame = ttk.Frame(self.main_frame)
        content_frame.pack(fill=BOTH, expand=YES, pady=10)
        
        # Cột bên trái
        left_frame = ttk.LabelFrame(
            content_frame,
            text="THÊM SẢN PHẨM",
            padding=15,
            bootstyle="primary"
        )
        left_frame.pack(side=LEFT, fill=BOTH, expand=YES, padx=(0, 10))
        
        # Các thành phần của cột bên trái
        self.capacity_input = CapacityInput(left_frame)  # Input nhập dung lượng túi
        self.capacity_input.create()
        
        self.item_form = ItemForm(left_frame, self.add_item)  # Form nhập thông tin item
        self.item_form.create()
        
        self.items_list = ItemsList(left_frame, self.remove_item)  # Danh sách các item
        self.items_list.create()
        
        # Cột bên phải
        self.results_view = ResultsView(content_frame, self.solve)  # Hiển thị kết quả
        self.results_view.create()

    def add_item(self, item_data):
        """
        Thêm một item vào danh sách.

        :param item_data: Dữ liệu của item (name, weight, value).
        :return: True nếu thêm thành công, False nếu có lỗi.
        """
        try:
            name = item_data['name']  # Lấy tên item
            weight = float(item_data['weight'])  # Trọng lượng item
            value = float(item_data['value'])  # Giá trị item
            
            # Kiểm tra các giá trị hợp lệ
            if not name:
                raise ValueError("Please enter an item name")
            if weight <= 0:
                raise ValueError("Weight must be positive")
            if value <= 0:
                raise ValueError("Value must be positive")
            
            # Thêm item vào danh sách
            self.items_list.add_item(item_data)
            return True
            
        except ValueError as e:
            # Hiển thị thông báo lỗi
            messagebox.showerror("Error", str(e))
            return False

    def remove_item(self):
        """
        Xác nhận việc xóa một item.

        :return: True nếu người dùng đồng ý xóa, False nếu không.
        """
        return messagebox.askyesno("Confirm", "Remove selected item?")

    def solve(self):
        """
        Giải bài toán Knapsack bằng thuật toán Greedy.
        """
        try:
            # Lấy dung lượng túi
            capacity = self.capacity_input.get_capacity()
            if capacity <= 0:
                raise ValueError("Capacity must be positive")
                
            # Khởi tạo lại solver và đặt dung lượng túi
            self.solver = KnapsackSolver()
            self.solver.set_capacity(capacity)
            
            # Thêm các item vào solver
            for item_data in self.items_list.get_all_items():
                item = Item(
                    item_data['name'],
                    float(item_data['weight']),
                    float(item_data['value'])
                )
                self.solver.add_item(item)
            
            # Giải bài toán Knapsack bằng thuật toán Greedy
            solution = self.solver.solve_greedy()
            
            # Tạo thông tin tóm tắt kết quả
            summary = {
                'total_value': self.solver.get_total_value(),
                'total_weight': self.solver.get_total_weight(),
                'capacity': capacity,
                'capacity_used': (self.solver.get_total_weight() / capacity) * 100
            }

            # Hiển thị kết quả
            self.results_view.display_results(solution, summary)
        
        except ValueError as e:
            # Hiển thị lỗi liên quan đến giá trị không hợp lệ
            messagebox.showerror("Error", str(e))
        except Exception as e:
            # Hiển thị lỗi bất ngờ
            messagebox.showerror("Unexpected Error", str(e))