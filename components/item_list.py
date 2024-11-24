# Import thư viện cần thiết
import tkinter as tk  # Thư viện chính để tạo GUI
from tkinter import ttk  # Module ttk cho các widget hiện đại trong Tkinter
import ttkbootstrap as ttk  # Thư viện bootstrap cho Tkinter để cải thiện giao diện

# Định nghĩa lớp ItemsList
class ItemsList:
    def __init__(self, parent, remove_callback):
        """
        Hàm khởi tạo lớp ItemsList
        :param parent: Widget cha chứa bảng danh sách (Treeview)
        :param remove_callback: Hàm callback để thực hiện logic xóa bên ngoài
        """
        self.parent = parent  # Lưu tham chiếu đến widget cha
        self.remove_callback = remove_callback  # Lưu hàm callback để gọi khi xóa mục
        
    def create(self):
        """
        Tạo và cấu hình giao diện chính cho danh sách item
        """
        # Tạo LabelFrame để bao bọc Treeview và nút xóa
        frame = ttk.LabelFrame(
            self.parent,
            text="Added Items",  # Tiêu đề của khung
            padding=10,  # Khoảng cách bên trong
            bootstyle="info"  # Áp dụng style bootstrap
        )
        frame.pack(fill=tk.BOTH, expand=tk.YES, pady=10)  # Thêm khung vào cửa sổ cha
        
        # Định nghĩa các cột cho Treeview
        columns = ("name", "weight", "value", "ratio")
        
        # Tạo Treeview để hiển thị danh sách
        self.tree = ttk.Treeview(
            frame, 
            columns=columns,  # Cột hiển thị
            show="headings",  # Chỉ hiển thị tiêu đề các cột
            selectmode="browse",  # Cho phép chọn một dòng duy nhất
            bootstyle="primary"  # Áp dụng style bootstrap
        )
        
        # Đặt tiêu đề cho từng cột
        self.tree.heading("name", text="Name")  # Cột "Name"
        self.tree.heading("weight", text="Weight (kg)")  # Cột "Weight"
        self.tree.heading("value", text="Value ($)")  # Cột "Value"
        self.tree.heading("ratio", text="Value/Weight")  # Cột "Value/Weight"
        
        # Cấu hình độ rộng và căn giữa nội dung các cột
        for col in columns:
            self.tree.column(col, width=100, anchor=tk.CENTER)
        
        # Đặt Treeview vào khung và cấu hình khoảng cách
        self.tree.pack(fill=tk.BOTH, expand=tk.YES, pady=(0, 10))

        # Tạo nút "Remove Selected" để xóa mục được chọn
        ttk.Button(
            frame,
            text="Remove Selected",  # Văn bản trên nút
            command=self.on_remove_item,  # Gọi hàm xử lý xóa mục
            bootstyle="danger"  # Áp dụng style bootstrap
        ).pack(fill=tk.X)  # Nút chiếm toàn bộ chiều ngang
        
        return frame  # Trả về khung đã tạo
    
    def add_item(self, item_data):
        """
        Thêm một mục mới vào Treeview
        :param item_data: Dictionary chứa dữ liệu mục (name, weight, value)
        """
        # Tính giá trị tỷ lệ "Value/Weight" và thêm dữ liệu vào Treeview
        self.tree.insert(
            "",  # Thêm vào cuối danh sách
            "end",  # Thêm mục ở vị trí cuối
            values=(
                item_data['name'],  # Tên
                f"{float(item_data['weight']):.2f}",  # Trọng lượng (kg), làm tròn 2 chữ số
                f"{float(item_data['value']):.2f}",  # Giá trị ($), làm tròn 2 chữ số
                f"{float(item_data['value'])/float(item_data['weight']):.2f}"  # Tỷ lệ Value/Weight
            )
        )
        
    def on_remove_item(self):
        """
        Hàm xử lý xóa mục được chọn từ Treeview
        """
        selected = self.tree.selection()  # Lấy mục đang được chọn
        if selected and self.remove_callback():  # Nếu có mục được chọn và callback trả về True
            self.tree.delete(selected)  # Xóa mục khỏi Treeview
            
    def get_all_items(self):
        """
        Lấy tất cả các mục trong Treeview
        :return: Danh sách các mục (dạng dictionary)
        """
        items = []  # Danh sách chứa các mục
        for item_id in self.tree.get_children():  # Duyệt qua từng mục trong Treeview
            values = self.tree.item(item_id)["values"]  # Lấy giá trị của mục
            items.append({
                'name': values[0],  # Tên
                'weight': float(values[1]),  # Trọng lượng
                'value': float(values[2])  # Giá trị
            })
        return items  # Trả về danh sách các mục