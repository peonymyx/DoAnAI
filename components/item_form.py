# components/item_form.py
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

class ItemForm:
    '''
    Form dùng cho tác vụ thêm mới một item vào knapsack.
    '''
    def __init__(self, parent, add_item_callback):
        '''
        Khởi tạo form thêm item.

        :param parent: Container chứa form.
        :param add_item_callback: Hàm xử lý thêm item.
        '''
        self.parent = parent
        self.add_item_callback = add_item_callback
        self.setup_variables()
         
    def setup_variables(self):
        '''
        Thiết lập các biến kiểu string tương ứng với name, weight và value trong form.
        '''
        self.name_var = tk.StringVar()
        self.weight_var = tk.StringVar()
        self.value_var = tk.StringVar()
        
    def create(self):
        # Frame tạo khung, padding 10px
        frame = ttk.LabelFrame(
            self.parent,
            text="THÊM SẢN PHẨM",
            padding=10,
            bootstyle="secondary"
        )
        frame.pack(fill=tk.X, pady=10)

        # Label và textbox cho trường Name (tên), tương ứng biến name_var
        ttk.Label(frame, text="TÊN SẢN PHẨM:").pack(anchor=tk.W)
        ttk.Entry(
            frame,
            textvariable=self.name_var,
            bootstyle="primary"
        ).pack(fill=tk.X, pady=(0, 10))

        # Frame chứa trường Weight và Value
        input_frame = ttk.Frame(frame)
        input_frame.pack(fill=tk.X)

        # Frame chứa label và textbox cho trường Weight (khối lượng), tương ứng biến weight_var
        weight_frame = ttk.Frame(input_frame)
        weight_frame.pack(side=tk.LEFT, expand=tk.YES, padx=(0, 5))
        
        ttk.Label(weight_frame, text="KHỐI LƯỢNG (kg):").pack(anchor=tk.W)
        ttk.Entry(
            weight_frame,
            textvariable=self.weight_var,
            bootstyle="primary"
        ).pack(fill=tk.X)

        # Frame chứa label và textbox cho trường Value (giá trị), tương ứng biến value_var
        value_frame = ttk.Frame(input_frame)
        value_frame.pack(side=tk.LEFT, expand=tk.YES)
        
        ttk.Label(value_frame, text="GIÁ TRỊ HÀNG HÓA ($):").pack(anchor=tk.W)
        ttk.Entry(
            value_frame,
            textvariable=self.value_var,
            bootstyle="primary"
        ).pack(fill=tk.X)

        # Nút "Thêm", padding 10px về phía trên. Nhấn nút này sẽ gọi hàm on_add_item
        ttk.Button(
            frame,
            text="THÊM HÀNG HÓA",
            command=self.on_add_item,
            bootstyle="success"
        ).pack(fill=tk.X, pady=(10, 0))
        
        return frame
    
    def on_add_item(self):
        '''
        Nhận các giá trị đã nhập trong textbox của form, sau đó xử lý và tổng hợp thành
        dữ liệu của item sẽ thêm vào knapsack.
        '''
        item_data = {
            'name': self.name_var.get().strip(),
            'weight': self.weight_var.get(),
            'value': self.value_var.get()
        }
        if self.add_item_callback(item_data):
            self.clear_form()
            
    def clear_form(self):
        '''
        Cài đặt lại các textbox trong form thành trạng thái mặc định (rỗng).
        '''
        self.name_var.set("")
        self.weight_var.set("")
        self.value_var.set("")