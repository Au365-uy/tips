import streamlit as st
import random
import json

# 配置参数
CONFIG = {
    'tip_count': 20,          # 同时显示的提示数量
    'font_size': 16,
    'container_width': 800,
    'container_height': 600,
    'move_step': 5,
    'update_interval': 50     # 毫秒
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
st.title("💖 随机弹窗温馨提示 💖")

# 初始化提示信息
tips = []
for i in range(CONFIG['tip_count']):
    tip = {
        'id': f"tip{i}",
        'text': random.choice(TIPS),
        'bg': random.choice(BG_COLORS),
        'x': random.randint(0, CONFIG['container_width'] - 150),
        'y': random.randint(0, CONFIG['container_height'] - 50),
        'dx': random.choice([-CONFIG['move_step'], CONFIG['move_step']]),
        'dy': random.choice([-CONFIG['move_step'], CONFIG['move_step']])
    }
    tips.append(tip)

# 生成 HTML
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
    ">
        {tip['text']}
    </div>
    """

# JavaScript 控制移动和碰撞
html_script = f"""
<script>
var tips = {json.dumps(tips)};
var containerWidth = {CONFIG['container_width']};
var containerHeight = {CONFIG['container_height']};

function moveTips() {{
    for(var i=0;i<tips.length;i++){{
        var t = tips[i];
        var elem = document.getElementById(t.id);
        t.x += t.dx;
        t.y += t.dy;

        // 边界碰撞反弹
        if(t.x <=0 || t.x >= containerWidth - 150) t.dx = -t.dx;
        if(t.y <=0 || t.y >= containerHeight - 50) t.dy = -t.dy;

        elem.style.left = t.x + "px";
        elem.style.top = t.y + "px";
    }}
}}
setInterval(moveTips, {CONFIG['update_interval']});
</script>
"""

# 父容器
st.markdown(f"""
<div style="
    position: relative;
    width:{CONFIG['container_width']}px;
    height:{CONFIG['container_height']}px;
    border:1px solid #ddd;
    margin:auto;
    background-color:#fff;
    overflow:hidden;
">
{html_tips}
</div>
{html_script}
""", unsafe_allow_html=True)
