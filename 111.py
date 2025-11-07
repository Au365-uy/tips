import streamlit as st
import random
import math
import time

# 配置参数
CONFIG = {
    'default_tip_count': 100,  # 默认显示提示数量
    'display_time': 0.5,       # 每个提示显示时间（秒）
    'font_size': 24,           # 字体大小
    'heart_scale': 0.4,        # 爱心大小缩放比例
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
    "#FFC0CB", "#87CEEB", "#90EE90", "#E6E6FA", "#FFFFE0",
    "#DDA0DD", "#FF7F50", "#FFE4C4", "#7FFFD4", "#FFE4E1",
    "#F0FFF0", "#FFF0F5", "#FDF5E6"
]

# Streamlit 页面设置
st.set_page_config(page_title="温馨提示", layout="wide")
st.title("💖 爱心温馨提示 💖")

# 用于生成心形坐标
def get_heart_coordinates(index, total):
    t = 2 * math.pi * index / total
    x = 16 * math.sin(t)**3
    y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2*math.cos(3*t) - math.cos(4*t)
    return x, y

# 显示温馨提示
def display_tips():
    total = CONFIG['default_tip_count']
    coords = [get_heart_coordinates(i, total) for i in range(total)]
    # 归一化和缩放
    max_x = max(abs(x) for x, y in coords)
    max_y = max(abs(y) for x, y in coords)
    for i, (x, y) in enumerate(coords):
        # 随机选择提示和背景
        tip = random.choice(TIPS)
        bg = random.choice(BG_COLORS)
        # 使用 Streamlit 的容器显示
        st.markdown(
            f"<div style='"
            f"display:inline-block;"
            f"margin:5px;"
            f"padding:10px;"
            f"background-color:{bg};"
            f"border-radius:12px;"
            f"font-size:{CONFIG['font_size']}px;"
            f"transform: translate({x*CONFIG['heart_scale']*2}px, {-y*CONFIG['heart_scale']*2}px);"
            f"'>{tip}</div>",
            unsafe_allow_html=True
        )
        time.sleep(CONFIG['display_time'])

display_tips()
