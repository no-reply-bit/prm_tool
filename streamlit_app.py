import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os

# DB接続設定
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./local.db")
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

# ログイン設定
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔒 PRMログイン")
    username = st.text_input("ユーザー名")
    password = st.text_input("パスワード", type="password")
    if st.button("ログイン"):
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            st.session_state.logged_in = True
            st.success("ログイン成功！")
        else:
            st.error("ユーザー名またはパスワードが間違っています")
    st.stop()

st.title("👥 Personal Relationship Manager")
st.write("連絡先と接触履歴のダッシュボード")

try:
    persons = pd.read_sql("SELECT * FROM persons", con=engine)
    touches = pd.read_sql("SELECT * FROM touches", con=engine)
except Exception as e:
    st.error(f"DB読み込みエラー: {e}")
    st.stop()

st.subheader("📇 連絡先")
st.dataframe(persons if not persons.empty else pd.DataFrame({"info": ["データなし"]}))

st.subheader("📝 接触履歴")
if not touches.empty and "person_id" in touches.columns and "id" in persons.columns:
    merged = touches.merge(persons[["id", "name"]], left_on="person_id", right_on="id", how="left")
    st.dataframe(merged.drop(columns=["id_x", "id_y"], errors="ignore"))
else:
    st.write("接触履歴なし")
