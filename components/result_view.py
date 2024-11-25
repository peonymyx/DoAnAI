# Import thư viện tkinter và ttk để tạo giao diện người dùng
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk  # Thư viện ttkbootstrap để tạo các widget với giao diện đẹp hơn

# Định nghĩa lớp ResultsView để hiển thị kết quả giải bài toán knapsack
class ResultsView:
    def __init__(self, parent, solve_callback):
        """
        Hàm khởi tạo lớp ResultsView.

        :param parent: Widget cha để chứa các widget con.
        :param solve_callback: Hàm callback được gọi khi nhấn nút 'Solve Knapsack Problem'.
        """
        self.parent = parent  # Lưu widget cha
        self.solve_callback = solve_callback  # Lưu hàm callback

    def create(self):
        """
        Hàm tạo giao diện hiển thị kết quả và nút giải bài toán.
        """
        # Tạo một LabelFrame với tiêu đề "Results" để chứa toàn bộ nội dung
        frame = ttk.LabelFrame(
            self.parent,
            text="TỐI ƯU HÓA SẢN PHẨM MANG THEO",
            padding=15,
            bootstyle="primary"  # Kiểu giao diện (theme)
        )
        # Đặt frame này về bên trái, chiếm toàn bộ chiều dọc và mở rộng nếu có không gian
        frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

        # Nút "Solve Knapsack Problem" để gọi hàm solve_callback
        ttk.Button(
            frame,
            text="Giải Bài Toán Knapsack",
            command=self.solve_callback,  # Gọi hàm callback khi nhấn nút
            bootstyle="success-outline",  # Kiểu giao diện của nút
            padding=10  # Thêm khoảng cách xung quanh chữ
        ).pack(fill=tk.X, pady=(0, 15))  # Nút chiếm toàn bộ chiều ngang và có khoảng cách dưới

        # LabelFrame con để hiển thị chi tiết lời giải
        results_frame = ttk.LabelFrame(
            frame,
            text="KẾT QUẢ",
            padding=10,
            bootstyle="info"  # Kiểu giao diện
        )
        # Đặt results_frame chiếm toàn bộ không gian còn lại
        results_frame.pack(fill=tk.BOTH, expand=tk.YES)

        # Khởi tạo scrollbar cho widget Text
        scroll = ttk.Scrollbar(results_frame)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Widget Text để hiển thị kết quả chi tiết
        self.result_text = tk.Text(
            results_frame,
            height=20,  # Chiều cao mặc định
            width=40,  # Chiều rộng mặc định
            wrap=tk.WORD,  # Tự động xuống dòng theo từ
            font=("Helvetica", 10),  # Font chữ
            yscrollcommand=scroll.set
        )
        
        # Đặt widget Text chiếm toàn bộ không gian của results_frame và cấu hình scrollbar
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
        scroll.config(command=self.result_text.yview)

        return frame  # Trả về frame đã tạo

    def display_results(self, solution, summary):
        """
        Hiển thị kết quả giải bài toán knapsack.

        :param solution: Danh sách các item được chọn.
        :param summary: Thông tin tổng hợp về lời giải, bao gồm tổng giá trị, trọng lượng, và dung lượng sử dụng.
        """
        # Xóa toàn bộ nội dung hiện tại trong widget Text
        self.result_text.delete(1.0, tk.END)
        
        # Nếu không có lời giải khả thi, hiển thị thông báo và kết thúc
        if not solution:
            self.result_text.insert(tk.END, "Không tìm thấy lời giải khả thi.\n")
            return
            
        # Hiển thị tiêu đề "Selected Items"
        self.result_text.insert(tk.END, "Các Sản Phẩm Được Chọn:\n", "header")
        self.result_text.insert(tk.END, "="*50 + "\n\n")  # Dòng phân cách

        # Lặp qua từng item trong lời giải và hiển thị thông tin chi tiết
        for item in solution:
            self.result_text.insert(
                tk.END, 
                f"• {item.name}\n"
                f"  KHỐI LƯỢNG: {item.weight:.2f} kg\n"
                f"  GIÁ TRỊ: ${item.value:.2f}\n"
                f"  Giá trị/Trọng lượng: ${item.ratio:.2f}/kg\n\n"
            )
        
        # Hiển thị dòng phân cách và tiêu đề "Summary"
        self.result_text.insert(tk.END, "="*50 + "\n")
        self.result_text.insert(tk.END, "Tóm Tắt:\n", "header")
        
        # Hiển thị thông tin tổng hợp lời giải
        self.result_text.insert(
            tk.END,
            f"Tổng Giá Trị: ${summary['total_value']:.2f}\n"
            f"Tổng Trọng Lượng: {summary['total_weight']:.2f} kg / {summary['capacity']:.2f} kg\n" 
            f"Dung Lượng Sử Dụng: {summary['capacity_used']:.1f}%\n"
        )