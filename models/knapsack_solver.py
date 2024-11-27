class KnapsackSolver:  # Lớp giải bài toán túi ba lô
    def __init__(self):
        self.items = []  # Danh sách các món đồ
        self.capacity = 0  # Sức chứa tối đa của túi ba lô
        self.solution = []  # Danh sách các món đồ được chọn vào túi
        
    def add_item(self, item):
        self.items.append(item)  # Thêm một món đồ vào danh sách
        
    def set_capacity(self, capacity):
        self.capacity = capacity  # Đặt sức chứa cho túi ba lô
        
    def solve_greedy(self):
        # Sắp xếp các món đồ theo thứ tự giảm dần của tỷ lệ giá trị/trọng lượng
        sorted_items = sorted(self.items, key=lambda x: x.ratio, reverse=True)
        
        current_weight = 0  # Trọng lượng hiện tại trong túi
        self.solution = []  # Khởi tạo danh sách lời giải
        
        for item in sorted_items:
            if current_weight + item.weight <= self.capacity:  # Nếu có thể thêm món đồ vào túi
                self.solution.append(item)  # Thêm món đồ vào danh sách lời giải
                current_weight += item.weight  # Cập nhật trọng lượng hiện tại
                
        return self.solution  # Trả về danh sách các món đồ được chọn
    
    def solve_greedy_by_weight(self):
        # Sắp xếp các món đồ theo thứ tự tăng dần của trọng lượng
        sorted_items = sorted(self.items, key=lambda x: x.weight)
    
        current_weight = 0 
        self.solution = []
    
        for item in sorted_items:
            if current_weight + item.weight <= self.capacity:
                self.solution.append(item)
                current_weight += item.weight  
            
        return self.solution
    
    def solve_greedy_by_value(self):
        # Sắp xếp các món đồ theo thứ tự giảm dần của giá trị
        sorted_items = sorted(self.items, key=lambda x: x.value, reverse=True)
    
        current_weight = 0 
        self.solution = []
    
        for item in sorted_items:
            if current_weight + item.weight <= self.capacity:
                self.solution.append(item)
                current_weight += item.weight  
            
        return self.solution

    def get_total_value(self):
        # Tính tổng giá trị của các món đồ trong lời giải
        return sum(item.value for item in self.solution)
    
    def get_total_weight(self):
        # Tính tổng trọng lượng của các món đồ trong lời giải
        return sum(item.weight for item in self.solution)
