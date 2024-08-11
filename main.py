import streamlit as st
import numpy as np
import pandas as pd

# タイトル
st.title("Streamlit Hello World")

# データフレームの作成
df = pd.DataFrame({
    "1列目":[1, 2, 3, 4],
    "2列目":[7, 8, 5, 6]
})

# データフレームの表示
st.write(df)

# データフレームの表示（スタイル付き）
st.dataframe(df.style.highlight_max(axis=0), width= 150, height=200)

# データフレームの表示（表組み）
st.table(df.style.highlight_max(axis=0))

# テキストの表示
st.write("DateFrame")

# データフレームの作成（ランダム）
df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=["a", "b", "c"]
)

st.write(df)

# 折れ線グラフの表示
st.line_chart(df)
# エリアグラフの表示
st.area_chart(df)

# 地図にランダムにスポットを表示
df = pd.DataFrame(
    np.random.rand(100, 2)/[10, 10] + [35.00, 135.33],
    columns = ["lat", "lon"]
)
st.write(df)
st.map(df)

# 画像の表示
from PIL import Image  
st.title("画像表示のテストです")
st.write("Display Image")
# 画像の読み込み
img = Image.open("../pic/img052.png")
# 画像の表示
st.image(img, caption="テストです", use_column_width=True)

st.title("インタラクティブなウィジェットの活用")
st.write("Interactive Widgets")
# テキストを入力させる
text = st.text_input("あなたの趣味を教えてください。")
# 入力させたテキストを表示
"あなたの趣味は", text, "です。"
# スライダーで数値を入力させる
condition = st.slider("あなたの今の調子は？", 0, 100, 50)
# 入力させた数値をテキスト表示
"あなたのコンディション：", condition
