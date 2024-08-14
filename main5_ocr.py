import pyocr.tesseract
import streamlit as st
from PIL import Image
import pyocr
import platform
import pytesseract

if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
else:
    pytesseract.pytesseract.tesseract_cmd = r"/usr/local/bin/tesseract"

set_language_list = {
    "日本語":"jpn",
    "英語":"eng"
}

st.title("文字認識アプリ")
set_language = st.selectbox("画像から文字認識をする言語を選んでください。", set_language_list.keys())
file_upload = st.file_uploader("ここに文字が書かれた画像ファイルをアップロードしてください。", type=["png","jpg"])

if (file_upload !=None):
    st.image(file_upload)
    engines = pyocr.get_available_tools()
    if not engines:
        st.error("OCRエンジンが見つかりませんでした。Tesseractが正しくインストールされているか確認してください。")
    else:
        engine = engines[0]
        txt = engine.image_to_string(Image.open(file_upload), set_language_list[set_language])
        st.write(txt)
    
    st.write("感情分析の結果")
    from asari.api import Sonar
    sonar = Sonar()
    res = sonar.ping(text=txt)
    st.write(res["classes"])