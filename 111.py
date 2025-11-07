import streamlit as st
import random
import time

# 配置参数
CONFIG = {
    'tip_count': 20,          # 同时显示的提示数量
    'font_size': 18,
    'container_width': 800,
    'container_height': 600,
    'move_step': 5,           # 每次移动像素
    'update_interval': 0.1    # 秒
}

TIPS = [
    "很开心遇见你", "每天都要元气满满", "记得吃水果",
    "保持好心情", "好好爱自己", "我想你了", "梦想成真",
    "期待下一次见面", "早点睡觉", "顺顺利利", "下一次见面是什么时候",
    "愿所有烦恼都消失", "别熬夜", "今天过得开心嘛",
    "天冷了，多穿衣服"
]

BG_COLORS = [
    "#FFC0CB", "#87CEEB", "#90EE90", "#E6E6FA", "#FFFFE0",
    "#DDA0DD", "#FF7F50", "#FFE4C4", "#7FFFD4", "#FFE4E1",
    "#F0FFF0", "#FFF0F5", "#FDF5E6"
]

st.set_page_config(page_title="温馨提示", layout="wide")
st.title("💖 动态温馨提示 💖")

# 父容器
st.markdown(
    f"""
    <div id="container" style="
        position: relative;
        width:{CONFIG['container_width']}px;
        height:{CONFIG['container_height']}px;
        border:1px solid #ddd;
        margin:auto;
        background-color:#fff;
        overflow:hidden;
    ">
    </div>
    """, unsafe_allow_html=True
)

# 初始化提示块
tips = []
for i in range(CONFIG['tip_count']):
    tip = {
        'text': random.choice(TIPS),
        'bg': random.choice(BG_COLORS),
        'x': random.randint(0, CONFIG['container_width'] - 100),
        'y': random.randint(0, CONFIG['container_height'] - 40),
        'dx': random.choice([-1,1]) * CONFIG['move_step'],
        'dy': random.choice([-1,1]) * CONFIG['move_step'],
        'id': f"tip{i}"
    }
    tips.append(tip)

# 用HTML + JS渲染动画
html_tips = ""
for tip in tips:
    html_tips += f"""
    <div id="{tip['id']}" style="
        position:absolute;
        left:{tip['x']}px;
        top:{tip['y']}px;
        background-color:{tip['bg']};
        padding:8px 12px;
        border-radius:12px;
        font-size:{CONFIG['font_size']}px;
        text-align:center;
        white-space:nowrap;
        animation: fadeIn 0.5s;
    ">✨ {tip['text']} ✨</div>
    """

html_script = f"""
<script>
var tips = {[
    {'id': t['id'], 'x': t['x'], 'y': t['y'], 'dx': t['dx'], 'dy': t['dy']} for t in tips
]};
var width = {CONFIG['container_width']};
var height = {CONFIG['container_height']};

function moveTips() {{
    for(var i=0;i<tips.length;i++){{
        var t = tips[i];
        var elem = document.getElementById(t.id);
        t.x += t.dx;
        t.y += t.dy;
        if(t.x <=0 || t.x >= width - 120) t.dx = -t.dx;
        if(t.y <=0 || t.y >= height - 40) t.dy = -t.dy;
        elem.style.left = t.x + "px";
        elem.style.top = t.y + "px";
    }}
}}
setInterval(moveTips, {int(CONFIG['update_interval']*1000)});
</script>
<style>
@keyframes fadeIn {{
  from {{opacity:0; transform: scale(0.5);}}
  to {{opacity:1; transform: scale(1);}}
}}
</style>
"""

st.markdown(html_tips + html_script, unsafe_allow_html=True)
