import streamlit as st

st.sidebar.write("サイドバー")
st.write("メイン画面")
st.header("自己紹介")
st.write("名前：マスダ")

with st.expander("詳細"):
    st.write("生年月日：")

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.header("Cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")
with col2: 
    st.header("Dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")
with col3:
    st.header("Owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
with col4:
    st.header("Owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")



houhou = st.sidebar.selectbox(
    "連絡方法を選択してください",
    ("メール","携帯電話","LINE")
)

st.sidebar.write("連絡方法は"+houhou+"です")