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
from components.test_case_view import TestCaseView # Chọn một trong các test case
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
        self.root.geometry("900x750")  # Kích thước cửa sổ
        
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
        
        self.items_list = ItemsList(left_frame, self.remove_item, self.edit_item)  # Danh sách các item
        self.items_list.create()
        
        # Cột bên phải
        right_frame = ttk.Frame(content_frame)
        right_frame.pack(side=LEFT, fill=BOTH, expand=YES, padx=(0, 10))

        self.test_case_view = TestCaseView(right_frame, self.add_items) # Chọn test case
        self.test_case_view.create()

        self.results_view = ResultsView(right_frame, self.solve)  # Hiển thị kết quả
        self.results_view.create()

    def add_item(self, item_data):
        """
        Thêm hoặc cập nhật một item trong danh sách.

        :param item_data: Dữ liệu của item (name, weight, value).
        :return: True nếu thêm/cập nhật thành công, False nếu có lỗi.
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
            
            # Kiểm tra xem có đang ở chế độ chỉnh sửa không
            if self.items_list.editing_mode:
                # Cập nhật item hiện tại
                self.items_list.update_edited_item(item_data)
            else:
                # Thêm item mới vào danh sách
                self.items_list.add_item(item_data)
            
            return True
            
        except ValueError as e:
            # Hiển thị thông báo lỗi
            messagebox.showerror("Error", str(e))
            return False
        
    def add_items(self, case):
        """
        Đọc một file text chứa dữ liệu item trong test case và thêm vào danh sách.

        :param case: Tên file (không gồm phần mở rộng).
        """
        if not case or case == '0':
            return False

        with open(f"cases\\{case}.txt", 'r') as case_file:        
            weights = case_file.readline().split() # Dòng 1: Khối lượng
            values = case_file.readline().split() # Dòng 2: Giá trị
            capacity_case = float(case_file.readline()) # Dòng 3: Dung lượng túi

        for index in range(len(weights)):
            item_data = {
                'name': index,
                'weight': float(weights[index]),
                'value': float(values[index])
            }
            self.items_list.add_item(item_data)

        self.capacity_input.set_capacity(capacity_case)
        return True
    
    def edit_item(self, item_data):
        """
        Điền thông tin item vào form để chỉnh sửa
        
        :param item_data: Dữ liệu item được chọn để chỉnh sửa
        :return: True nếu điền thành công
        """
        # Điền các giá trị của item vào các ô input
        self.item_form.name_var.set(str(item_data['name']))
        self.item_form.weight_var.set(str(item_data['weight']))
        self.item_form.value_var.set(str(item_data['value']))
        return True

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
            
            # Lấy dạng bài toán và phương pháp giải từ giao diện
            is_fractional = self.results_view.get_is_fractional()
            selected_method = self.results_view.get_selected_method()
            
            # Giải bài toán Knapsack theo phương pháp được chọn

            if is_fractional:
                solution = self.solver.solve_greedy_fractional()
            else:
                if selected_method == "Giá trị (Value)":
                    solution = self.solver.solve_greedy_by_value()  # Giải theo giá trị
                elif selected_method == "Trọng lượng (Weight)":
                    solution = self.solver.solve_greedy_by_weight()  # Giải theo trọng lượng
                elif selected_method == "Tỷ lệ Giá trị/Trọng lượng (Ratio)":
                    solution = self.solver.solve_greedy()  # Giải theo tỷ lệ
                else:
                    raise ValueError("Please select a valid solving method")
            
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