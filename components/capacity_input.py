# Import thư viện cần thiết
import tkinter as tk  # Thư viện chính để tạo GUI
from tkinter import ttk  # Module ttk cho các widget hiện đại trong Tkinter
import ttkbootstrap as ttk  # Thư viện bootstrap để cải thiện giao diện Tkinter

# Định nghĩa lớp CapacityInput
class CapacityInput:
    def __init__(self, parent):
        """
        Hàm khởi tạo lớp CapacityInput
        :param parent: Widget cha chứa input (ví dụ: một Frame hoặc cửa sổ chính)
        """
        self.parent = parent  # Lưu tham chiếu đến widget cha
        self.capacity_var = tk.StringVar(value="1000")  # Biến để lưu giá trị tải trọng (mặc định là 1000)

    def create(self):
        """
        Tạo và cấu hình giao diện nhập tải trọng xe tải
        :return: Frame chứa thành phần giao diện
        """
        # Tạo một Frame để chứa nhãn và ô nhập liệu
        frame = ttk.Frame(self.parent)
        frame.pack(fill=tk.X, pady=(0, 15))  # Đặt khung vào cửa sổ cha, với khoảng cách bên dưới 15px

        # Tạo nhãn "Tải trọng xe tải (kg):"
        ttk.Label(
            frame,
            text="Tải trọng xe tải (kg):",  # Văn bản hiển thị
            font=("Helvetica", 10, "bold")  # Định dạng font chữ
        ).pack(side=tk.LEFT)  # Đặt nhãn ở phía bên trái của Frame

        # Tạo ô nhập liệu để nhập tải trọng
        capacity_entry = ttk.Entry(
            frame,
            textvariable=self.capacity_var,  # Liên kết với biến capacity_var để lưu giá trị
            width=10,  # Độ rộng của ô nhập liệu
            bootstyle="primary"  # Áp dụng style bootstrap
        )
        capacity_entry.pack(side=tk.LEFT, padx=5)  # Đặt ô nhập bên cạnh nhãn, với khoảng cách ngang là 5px

        return frame  # Trả về Frame đã tạo

    def get_capacity(self):
        """
        Lấy giá trị tải trọng từ ô nhập liệu
        :return: Giá trị tải trọng (float)
        """
        try:
            return float(self.capacity_var.get())  # Trả về giá trị từ biến capacity_var dưới dạng số thực
        except ValueError:
            raise ValueError("Vui lòng nhập tải trọng hợp lệ (số thực).")
