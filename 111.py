import streamlit as st
import random
import json
from streamlit.components.v1 import html

CONFIG = {
    'tip_count': 20,
    'font_size': 16,
    'move_step': 5,
    'update_interval': 20,       # 50fps
    'delay_between_tips': 800,   # 弹窗间隔
    'tip_width': 150,
    'tip_height': 50
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

st.set_page_config(page_title="❤️❤️❤️", layout="wide")
st.title("❤️❤️❤️")

# ----------------- 初始化提示 -----------------
tips = []
for i in range(CONFIG['tip_count']):
    tip = {
        'id': f"tip{i}",
        'text': random.choice(TIPS),
        'bg': random.choice(BG_COLORS),
        'dx': random.choice([-CONFIG['move_step'], CONFIG['move_step']]),
        'dy': random.choice([-CONFIG['move_step'], CONFIG['move_step']])
    }
    tips.append(tip)

# ----------------- HTML + JS -----------------
html_code = f"""
<div id="container" style="
    position: relative;
    width: 100vw;
    height: 90vh;
    margin:auto;
    background-color:#fff;
    overflow:hidden;
">
</div>

<script>
var tips = {json.dumps(tips)};
var container = document.getElementById("container");
var container_width = container.clientWidth;
var container_height = container.clientHeight;
var tip_width = {CONFIG['tip_width']};
var tip_height = {CONFIG['tip_height']};

// 初始化随机位置
for(var i=0;i<tips.length;i++){{
    var t = tips[i];
    t.x = Math.floor(Math.random()*(container_width - tip_width));
    t.y = Math.floor(Math.random()*(container_height - tip_height));

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
    div.style.display = "none";
    container.appendChild(div);
}}

// 逐个弹出提示
for(let i=0;i<tips.length;i++){{
    setTimeout(function(){{
        document.getElementById(tips[i].id).style.display = "block";
    }}, i*{CONFIG['delay_between_tips']});
}}

// 移动和碰撞逻辑
function moveTips() {{
    container_width = container.clientWidth;
    container_height = container.clientHeight;

    for(var i=0;i<tips.length;i++){{
        var t = tips[i];
        var elem = document.getElementById(t.id);
        if(elem.style.display === "none") continue;
        t.x += t.dx;
        t.y += t.dy;

        if(t.x <=0 || t.x >= container_width - tip_width) t.dx = -t.dx;
        if(t.y <=0 || t.y >= container_height - tip_height) t.dy = -t.dy;

        elem.style.left = t.x + "px";
        elem.style.top = t.y + "px";
    }}
}}
setInterval(moveTips, {CONFIG['update_interval']});
</script>
"""

html(html_code, height="95vh")
