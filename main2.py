# フロントエンドを扱うstreamlitの機能をインポート
import streamlit as st
# 時間を扱う機能をインポート
import time

st.title("streamlitの基礎")
st.write("Hello World")

# レイアウトとして2列を定義
col1, col2 = st.columns(2)

# 1列目をwithで囲む
with col1:
    st.write("列1がここに表示されます")

# 2列目をwithで囲む
with col2:
    st.write("列2がここに表示されます")

# .sidebarを付けるとサイドバーに出力されます
st.sidebar.write("Hello World")
# テキストを入力できる欄を表示
st.text_input("ここに文字が入力できます")

# スライダーで数値を入力させる（最小値、最大値、デフォルト値の順で設定されます）
slider_number = st.slider("スライダーで数値を決定できます", 0, 100, 10)
"スライダーの数値：", slider_number

# ボタンの設置
st.button("ボタンだよ")

# 文字が出力される場所をあらかじめ確保します。その場所をxとしています。
x = st.empty()
# 進捗0のプログレスバーを出力します。
bar = st.progress(0)
# iに0から99までを代入しながら実行されます。
for i in range(100):
    time.sleep(0.01) # 0.01秒待機します
    x.text(i) # 確保した場所xに代入されたiの値を代入します。
    bar.progress(i) # 進捗iに変更します。

# 選択肢を配列で指定して選択肢を出力します。
st.selectbox("好きなプロレス団体を選んでください。", ["新日本プロレス", "全日本プロレス", "プロレスリング・ノア"])

# ダウンロードする文字を定義し、output_textに代入します。
output_text = "この文字がダウンロードされます。"
# 代入された文字をダウンロードするボタンを設置。オプションは内容をdataに指定、ファイル名をfile_nameに指定、ファイルタイプをmimeに指定
st.download_button(
    label="記事内容 ダウンロード",
    data=output_text,
    file_name="output.txt",
    mime="text/plain"
)

# ファイルアップローダーを設置します。typeでアップロードできるファイルの種類を指定できます。
file_upload = st.file_uploader("ここに画像ファイルをアップロードしてください。", type=["png","jpg"])
# ファイルがアップロードされた時にその画像を表示します。
if (file_upload !=None):
    st.image(file_upload)

# 数列を扱う機能、データフレームを扱う機能をインポート
import numpy as np
import pandas as pd

# 乱数の配列を作るメソッドを作ります。因数をr,cとし、それぞれのデフォルト値を10と5に設定します。
def rand_df(r=10, c=5):
    df = pd.DataFrame(
        np.random.rand(r, c),
        columns=("col %d" % i for i in range(c))
    ) # 乱数10の5個の数列を作ります。カラムの設定は0-4の名前を付けます。
    return df # 作ったデータフレームを返します。
dataframe = rand_df(r=20, c=5) # rに10、cに3を代入したrand_dfメソッドを処理します。
st.write(dataframe)
# 表の描画をします。
st.dataframe(dataframe.head(n=5))
# データフレームのチャートの描画をします。
st.line_chart(dataframe)