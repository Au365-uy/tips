import streamlit as st
import random
import math

# 配置参数
CONFIG = {
    'tip_count': 100,       # 提示数量
    'font_size': 16,        # 字体大小
    'heart_scale': 20,      # 爱心缩放
    'container_width': 800, # 页面宽度
    'container_height': 600 # 页面高度
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

st.set_page_config(page_title="温馨提示", layout="wide")
st.title("💖 爱心温馨提示 💖")

# 父容器，固定宽高，用于绝对定位
st.markdown(
    f"""
    <div style="
        position: relative;
        width:{CONFIG['container_width']}px;
        height:{CONFIG['container_height']}px;
        border:1px solid #ddd;
        margin:auto;
        background-color:#fff;
    ">
    """, unsafe_allow_html=True
)

# 生成心形坐标
def get_heart_coordinates(index, total):
    t = 2 * math.pi * index / total
    x = 16 * math.sin(t)**3
    y = 13*math.cos(t) - 5*math.cos(2*t) - 2*math.cos(3*t) - math.cos(4*t)
    return x, -y  # y 取负让心形正立

total = CONFIG['tip_count']
coords = [get_heart_coordinates(i, total) for i in range(total)]

# 显示提示
for i, (x, y) in enumerate(coords):
    tip = random.choice(TIPS)
    bg = random.choice(BG_COLORS)
    st.markdown(
        f"""
        <div style="
            position:absolute;
            left:{CONFIG['container_width']/2 + x*CONFIG['heart_scale']}px;
            top:{CONFIG['container_height']/2 + y*CONFIG['heart_scale']}px;
            background-color:{bg};
            padding:8px 12px;
            border-radius:12px;
            font-size:{CONFIG['font_size']}px;
            text-align:center;
        ">
            {tip}
        </div>
        """,
        unsafe_allow_html=True
    )

# 关闭父容器 div
st.markdown("</div>", unsafe_allow_html=True)
