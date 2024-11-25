import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

class Header:
    '''
    Khung tiêu đề (header) của giao diện, bao gồm 2 label cho tiêu đề chính và phụ.
    '''
    def __init__(self, parent):
        '''
        Khởi tạo khung tiêu đề (header) của giao diện.

        :param parent: Container chứa khung tiêu đề.
        '''
        self.parent = parent
        
    def create(self):
        # Frame header cách các khung phía dưới 20px
        header_frame = ttk.Frame(self.parent)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Tiêu đề chính nằm trong frame header, cỡ chữ 24 in đậm; cách tiêu đề phụ 10px
        title = ttk.Label(
            header_frame,
            text="Quản lý hàng hóa trong kho vận",
            font=("Helvetica", 24, "bold"),
            bootstyle="inverse-primary"
        )
        title.pack(pady=10)
        
        # Tiêu đề phụ nằm trong frame header, cỡ chữ 12 
        subtitle = ttk.Label(
            header_frame,
            text="Tối ưu hóa không gian xe tải để đạt giá trị vận chuyển tối đa",
            font=("Helvetica", 12),
            bootstyle="inverse-secondary"
        )
        subtitle.pack()
        
        return header_frame
