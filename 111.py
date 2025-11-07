import random
import time
import tkinter as tk
from threading import Thread
import sys
import math

# 配置参数
CONFIG = {
    'default_window_count': 10,  # 默认窗口数量
    'max_window_count': 100,  # 最大窗口数量
    'window_width': 250,  # 窗口宽度
    'window_height': 60,  # 窗口高度
    'display_time': 30000,  # 窗口显示时间(毫秒)，默认30秒
    'start_delay': 0.05,  # 启动每个窗口的延迟时间(秒)
    'font_size': 16,  # 字体大小
    'font_family': '微软雅黑',  # 字体
    'heart_scale': 0.4,  # 心形曲线缩放比例
}

# 温馨提示列表
TIPS = [
    "很开心遇见你", "每天都要元气满满", "记得吃水果",
    "保持好心情", "好好爱自己", "我想你了", "梦想成真",
    "期待下一次见面", "早点睡觉", "顺顺利利", "下一次见面是什么时候",
    "愿所有烦恼都消失", "别熬夜", "今天过得开心嘛",
    "天冷了，多穿衣服"
]

# 背景颜色列表
BG_COLORS = [
    "lightpink", "skyblue", "lightgreen", "lavender", "lightyellow",
    "plum", "coral", "bisque", "aquamarine", "mistyrose",
    "honeydew", "lavenderblush", "oldlace"
]


def get_heart_coordinates(index, total, screen_width, screen_height, window_width, window_height):
    """使用改进的心形曲线参数方程生成坐标"""
    # 使用更标准的心形曲线参数方程
    # 调整t的范围，增加密度使心形更完整
    t = 2 * math.pi * index / total

    # 更准确的心形曲线方程
    # 使用笛卡尔坐标系转换
    # 这种参数方程会生成更标准的爱心形状
    x = 16 * math.pow(math.sin(t), 3)
    y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)

    # 调整缩放比例和居中
    scale_factor = min(screen_width, screen_height) * CONFIG['heart_scale'] / 16  # 归一化缩放
    center_x = screen_width / 2 - window_width / 2
    center_y = screen_height / 2 - window_height / 2

    # 计算最终坐标，注意y轴需要反转（因为屏幕坐标y轴向下）
    final_x = center_x + x * scale_factor
    final_y = center_y - y * scale_factor  # 负号用于反转y轴

    # 小的随机偏移使排列更自然，但不要太大影响整体形状
    jitter_x = random.uniform(-5, 5)
    jitter_y = random.uniform(-5, 5)
    final_x += jitter_x
    final_y += jitter_y

    # 确保坐标在屏幕范围内
    final_x = max(0, min(final_x, screen_width - window_width))
    final_y = max(0, min(final_y, screen_height - window_height))

    return final_x, final_y


# 用于跟踪当前窗口索引
window_index_counter = 0
window_count_for_heart = 0


def show_warm_tip():
    """显示一个温馨提示窗口"""
    global window_index_counter

    try:
        # 创建窗口
        window = tk.Tk()

        # 获取屏幕尺寸
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        window_width = CONFIG['window_width']
        window_height = CONFIG['window_height']

        # 使用心形曲线生成坐标
        x, y = get_heart_coordinates(
            window_index_counter,
            window_count_for_heart or 50,  # 增加默认点数使心形更完整
            screen_width,
            screen_height,
            window_width,
            window_height
        )

        # 更新索引计数器
        window_index_counter += 1

        # 选择随机提示和背景色
        tip = random.choice(TIPS)
        bg = random.choice(BG_COLORS)
        # 设置窗口属性
        window.title(tip)
        window.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
        window.attributes('-topmost', True)
        # 创建标签
        label = tk.Label(
            window,
            text=tip,
            bg=bg,
            font=(CONFIG['font_family'], CONFIG['font_size']),
            width=30,
            height=3,
            wraplength=window_width - 20
        )
        label.pack(fill=tk.BOTH, expand=True)

        # 添加关闭窗口的回调
        window.after(CONFIG['display_time'], window.destroy)

        # 启动窗口主循环
        window.mainloop()

    except Exception as e:
        print(f"创建窗口时出错: {str(e)}")


def start_tips_directly(window_count=CONFIG['default_window_count']):
    """直接启动指定数量的提示窗口"""
    global window_index_counter, window_count_for_heart

    # 重置计数器
    window_index_counter = 0
    window_count_for_heart = window_count

    # 确保窗口数量不会超过最大限制
    window_count = min(window_count, CONFIG['max_window_count'])

    # 对于心形排列，建议至少使用20-30个窗口才能显示完整形状
    if window_count < 20:
        print(f"温馨提示：为了更好地显示爱心形状，建议使用至少20个窗口")

    threads = []

    for i in range(window_count):
        thread = Thread(target=show_warm_tip, daemon=False)
        threads.append(thread)
        try:
            thread.start()
            time.sleep(CONFIG['start_delay'])
        except Exception as e:
            print(f"启动线程时出错: {str(e)}")
            break


if __name__ == '__main__':
    # 直接启动100个窗口，这应该能形成一个比较完整的爱心形状
    start_tips_directly(100)  # 增加窗口数量以显示更完整的爱心
