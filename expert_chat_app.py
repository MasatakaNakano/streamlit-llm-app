# expert_chat_app.py
import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from dotenv import load_dotenv

# .envからOpenAIのAPIキーを読み込む
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Streamlit UI
st.title("💬 Expert Chat App")
st.write("あなたの質問に、専門家がやさしく丁寧に答えます。")

# 専門家の種類を選択
expert = st.radio("相談したい専門家を選んでください", [
    "育児の専門家",
    "キャリアアドバイザー",
    "法律の専門家"
])

# ユーザーからの質問入力
question = st.text_input("あなたの質問を入力してください:")

# 回答ボタン
if st.button("送信"):
    if not api_key:
        st.error("OpenAI APIキーが読み込めませんでした。")
    elif not question:
        st.warning("質問を入力してください。")
    else:
        # モデルの準備
        chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7, api_key=api_key)
        messages = [
            SystemMessage(content=f"あなたは{expert}です。やさしく丁寧に回答してください。"),
            HumanMessage(content=question)
        ]
        response = chat.invoke(messages)
        st.success("【専門家の回答】")
        st.write(response.content)
