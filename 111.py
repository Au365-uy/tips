import streamlit as st
import random
import json
from streamlit.components.v1 import html

# ----------------- 配置 -----------------
CONFIG = {
    'tip_count': 20,
    'font_size': 16,
    'container_width': 800,
    'container_height': 600,
    'move_step': 5,
    'update_interval': 20,       # 帧率 50fps
    'delay_between_tips': 800    # 每个提示弹出延迟 800ms
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

# ----------------- 页面 -----------------
st.set_page_config(page_title="❤️❤️❤️", layout="wide")
st.title("❤️❤️❤️")  # 标题三个爱心

# ----------------- 初始化提示 -----------------
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

# ----------------- HTML + JS -----------------
html_code = f"""
<div id="container" style="
    position: relative;
    width:{CONFIG['container_width']}px;
    height:{CONFIG['container_height']}px;
    margin:auto;
    background-color:#fff;
    overflow:hidden;
">
</div>

<script>
var tips = {json.dumps(tips)};
var container = document.getElementById("container");

// 创建每个提示但先隐藏
for(var i=0;i<tips.length;i++){{
    var t = tips[i];
    var div = document.createElement("div");
    div.id = t.id;
    div.innerHTML = t.text;
    div.style.position = "absolute";
    div.style.left = t.x + "px";
    div.style.top = t.y + "px";
    div.style.backgroundColor = t.bg;
    div.style.padding = "8px 12px";
    div.style.borderRadius = "12px";
    div.style.fontSize = "{CONFIG['font_size']}px";
    div.style.whiteSpace = "nowrap";
    div.style.display = "none";  // 初始隐藏
    container.appendChild(div);
}}

// 逐个弹出提示（延迟显示）
for(let i=0;i<tips.length;i++){{
    setTimeout(function(){{
        document.getElementById(tips[i].id).style.display = "block";
    }}, i*{CONFIG['delay_between_tips']});
}}

// 移动和碰撞逻辑
function moveTips() {{
    for(var i=0;i<tips.length;i++){{
        var t = tips[i];
        var elem = document.getElementById(t.id);
        if(elem.style.display === "none") continue; // 未显示的跳过
        t.x += t.dx;
        t.y += t.dy;

        // 边界碰撞反弹
        if(t.x <=0 || t.x >= {CONFIG['container_width']} - 150) t.dx = -t.dx;
        if(t.y <=0 || t.y >= {CONFIG['container_height']} - 50) t.dy = -t.dy;

        elem.style.left = t.x + "px";
        elem.style.top = t.y + "px";
    }}
}}
setInterval(moveTips, {CONFIG['update_interval']});  // 高帧率移动
</script>
"""

html(html_code, height=CONFIG['container_height'] + 20)
