import streamlit as st
st.title("我的第一个Streamlit应用")
user_name = st.text_input("请输入你的名字")
if user_name:
    st.write(f"欢迎 {user_name}！")
number = st.slider("选择一个数字", 0, 10)
st.write(f"{number}的平方是 {number * number}")
import streamlit as st
color = st.selectbox("选择一种颜色", ["红色", "绿色", "蓝色"])
if color == "红色":
    st.write("你选择了热情的红色。")
elif color == "绿色":
    st.write("你选择了生机勃勃的绿色。")
elif color == "蓝色":
    st.write("你选择了深沉的蓝色。")