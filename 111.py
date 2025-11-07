import tkinter as tk
import random
import time
from threading import Thread

# 配置参数
CONFIG = {
    'window_count': 20,    # 弹窗数量
    'window_width': 250,
    'window_height': 60,
    'display_time': 5000,   # 毫秒
    'start_delay': 0.3,     # 每个窗口启动延迟（秒）
    'font_size': 16
}

TIPS = [
    "很开心遇见你", "每天都要元气满满", "记得吃水果",
    "保持好心情", "好好爱自己", "我想你了", "梦想成真",
    "期待下一次见面", "早点睡觉", "顺顺利利", "下一次见面是什么时候",
    "愿所有烦恼都消失", "别熬夜", "今天过得开心嘛",
    "天冷了，多穿衣服"
]

BG_COLORS = [
    "lightpink", "skyblue", "lightgreen", "lavender", "lightyellow",
    "plum", "coral", "bisque", "aquamarine", "mistyrose",
    "honeydew", "lavenderblush", "oldlace"
]

class TipWindow:
    def __init__(self, master):
        self.master = master
        self.master.overrideredirect(True)  # 去掉窗口边框
        self.width = CONFIG['window_width']
        self.height = CONFIG['window_height']
        self.screen_width = master.winfo_screenwidth()
        self.screen_height = master.winfo_screenheight()
        
        # 初始随机位置
        self.x = random.randint(0, self.screen_width - self.width)
        self.y = random.randint(0, self.screen_height - self.height)
        # 初始随机移动速度
        self.dx = random.choice([-5, -4, 4, 5])
        self.dy = random.choice([-5, -4, 4, 5])
        
        # 随机文字和背景
        self.tip = random.choice(TIPS)
        self.bg = random.choice(BG_COLORS)
        
        # 创建标签
        self.label = tk.Label(master, text=self.tip, bg=self.bg,
                              font=("微软雅黑", CONFIG['font_size']),
                              width=30, height=3)
        self.label.pack(fill=tk.BOTH, expand=True)
        
        # 设置初始位置
        master.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        master.attributes('-topmost', True)
        
        # 启动移动动画
        self.move()
        # 设置自动关闭
        master.after(CONFIG['display_time'], master.destroy)
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        
        # 碰到边界反弹
        if self.x <= 0 or self.x >= self.screen_width - self.width:
            self.dx = -self.dx
        if self.y <= 0 or self.y >= self.screen_height - self.height:
            self.dy = -self.dy
        
        self.master.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        self.master.after(50, self.move)  # 每50毫秒更新一次位置

def start_tips():
    for i in range(CONFIG['window_count']):
        root = tk.Tk()
        TipWindow(root)
        Thread(target=root.mainloop).start()
        time.sleep(CONFIG['start_delay'])

if __name__ == "__main__":
    start_tips()
