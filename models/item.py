class Item:  # Lớp đại diện cho một món đồ
    def __init__(self, name, weight, value):
        self.name = name  # Tên món đồ
        self.weight = weight  # Trọng lượng món đồ
        self.value = value  # Giá trị món đồ
        self.ratio = value / weight  # Tỷ lệ giá trị trên trọng lượng

    def __str__(self):  # Phương thức trả về chuỗi mô tả món đồ
        return f"{self.name} (Trọng lượng: {self.weight}, Giá trị: {self.value})"
