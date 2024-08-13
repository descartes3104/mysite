import streamlit as st
import speech_recognition as sr
import sounddevice as sd
import numpy as np
import wavio

# 言語選択と、APIが認識する言語の変換リストを作成
set_language_list = {
    "日本語": "ja",
    "英語": "en-US",
}

# デフォルトの言語を設定
set_language = "日本語"

# 音声を録音する関数
def record_audio(duration, fs, filename):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    wavio.write(filename, audio, fs, sampwidth=2)
    print("Recording complete")

# 音声認識の言語を引数に音声認識をする
def mic_speech_to_text(set_language, filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio, language=set_language_list[set_language])
        except:
            text = "音声認識に失敗しました"
    return text

st.title("文字起こしアプリ")
st.write("音声認識する言語を選んでください。")
set_language = st.selectbox("音声認識する言語を選んでください。", set_language_list.keys())
current_language_state = st.empty()
current_language_state.write("選択中の言語:" + set_language)
file_upload = st.file_uploader("ここに音声認識したファイルをアップロードしてください。", type=["wav"])

if file_upload is not None:
    st.write("音声認識結果:")
    result_text = file_speech_to_text(file_upload, set_language)
    st.write(result_text)
    st.audio(file_upload)

st.write("マイクでの音声認識はこちらのボタンから")

if st.button("音声認識開始"):
    state = st.empty()
    state.write("音声認識中")
    record_audio(5, 44100, "output.wav")  # 5秒間録音
    result_text = mic_speech_to_text(set_language, "output.wav")
    state.write("音声認識結果:")
    st.write(result_text)
