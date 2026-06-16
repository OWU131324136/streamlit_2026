import streamlit as st
import random
import time
import os

# 初期設定
if "name" not in st.session_state:
    st.session_state.name = ""

if "page" not in st.session_state:
    st.session_state.page = "home"

if "result" not in st.session_state:
    st.session_state.result = None

# データ
planets = [
{
    "name": "オーロラ",
    "color": "ラベンダー",
    "item": "ガラスのアクセサリー",
    "message": "今日は小さな勇気が未来の光になります。",
    "stars": "★★★★★"
},
{
    "name": "ネビュラ",
    "color": "ミッドナイトブルー",
    "item": "お気に入りのノート",
    "message": "焦らず進めば新しい発見に出会えるでしょう。",
    "stars": "★★★★☆"
},
{
    "name": "ロゼリア",
    "color": "ローズピンク",
    "item": "ハンドクリーム",
    "message": "優しさが誰かの心を照らします。",
    "stars": "★★★★★"
},
{
    "name": "ルナリア",
    "color": "パールホワイト",
    "item": "イヤホン",
    "message": "静かな時間があなたを導いてくれます。",
    "stars": "★★★☆☆"
}
]

# ホーム画面
if st.session_state.page == "home":
    st.title("My Little Star")
    st.write("### ーあなただけの小さな宇宙へようこそー")

    # 名前未登録
    if st.session_state.name == "":
        name = st.text_input("☆あなたの名前を教えてください☆")
        if st.button("宇宙に登録する"):
            if name:
                st.session_state.name = name
                st.rerun()

    # 名前登録済み
    else:
        col1, col2 = st.columns([5,1])

        with col1:
            st.markdown(f"### 🌙 {st.session_state.name}さん")

        with col2:
            if st.button("✏️"):
                st.session_state.name = ""
                st.rerun()

        st.write("")
        st.write("今日はどんな星が")
        st.write("あなたを見守ってくれるでしょうか？")

        st.markdown(
            "<h1 style='text-align:center;'>🔭</h1>",
            unsafe_allow_html=True
        )

        st.write("")

        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            if st.button("銀河へ向かう", use_container_width=True):
                st.session_state.page = "galaxy"
                st.rerun()

# 銀河画面
elif st.session_state.page == "galaxy":
    st.title("🌠 Star Observatory")

    st.markdown(
        "<h3 style='text-align:center;'>夜空に浮かぶ星に</h3>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align:center;'>そっと触れてみよう</h3>",
        unsafe_allow_html=True
    )

    st.write("")

    # 画像の絶対パスを取得（実行ディレクトリに左右されないようにします）
    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, "galaxy.png")

    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)
    else:
        st.error(f"画像ファイルが見つかりません: {image_path}")

    st.write("")

    # ボタンを配置するためのカラムを定義し、その中にボタンを配置
    # 真ん中の列だけ使う
    c1, c2, c3 = st.columns([1, 2, 1])

    with c2:

        # 星ボタン
        if st.button("★", use_container_width=True):
            progress = st.progress(0)
            st.write("星の光を集めています...")

            for i in range(100):
                time.sleep(0.01)
                progress.progress(i + 1)

            st.session_state.result = random.choice(planets)
            st.session_state.page = "result"
            st.rerun()

        st.write("")  # ボタン間の余白

        # 戻るボタン
        if st.button("🏠 戻る", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()

# 結果画面
elif st.session_state.page == "result":

    result = st.session_state.result

    st.title("🪐 本日の星")

    st.markdown(
        f"<h1 style='text-align:center;'>{result['name']}</h1>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.write(f"⭐ 今日の星模様")
    st.write(result["stars"])

    st.write("")

    st.write(f"🎨 ラッキーカラー")
    st.write(result["color"])

    st.write("")

    st.write(f"🍀 ラッキーアイテム")
    st.write(result["item"])

    st.write("")

    st.write("🌙 宇宙からのメッセージ")
    st.info(result["message"])

    st.write("")

    if st.button("🔄 もう一度観測する"):
        st.session_state.page = "galaxy"
        st.rerun()

    if st.button("🏠 ホームへ戻る"):
        st.session_state.page = "home"
        st.rerun()
