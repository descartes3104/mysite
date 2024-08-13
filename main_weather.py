import streamlit as st
import requests
from datetime import datetime
import pandas as pd

city_code_list = {
	"札幌":"016010",
	"仙台":"040010",
	"東京":"130010",
	"名古屋":"230010",
	"大阪":"270000",
	"広島":"340010",
	"福岡":"400010",
	"那覇":"471010"
}

city_code_index = "東京都"

st.title("お天気予測アプリです")
st.write("お天気を調べたい地域を選んでください。")
city_code_index = st.selectbox("地域を選んでください。", city_code_list.keys())
city_code = city_code_list[city_code_index]

current_city_code = st.empty()
current_city_code.write("選択中の地域：" + city_code_index)
url = "https://weather.tsukumijima.net/api/forecast/city/" + city_code

response = requests.get(url)

weather_json = response.json()
now_hour = datetime.now().hour

# 今日の0-6時の降水確率を取得し、weather_nowに代入
if 0 <= now_hour and now_hour <6:
    weather_now = weather_json["forecasts"][0]["chanceOfRain"]["T00_06"]
# 今日の6-12時の降水確率を取得し、weather_nowに代入
elif 6 <= now_hour and now_hour <12:
    weather_now = weather_json["forecasts"][0]["chanceOfRain"]["T06_12"]
# 今日の12-18時の降水確率を取得し、weather_nowに代入
elif 12 <= now_hour and now_hour <18:
    weather_now = weather_json["forecasts"][0]["chanceOfRain"]["T12_18"]
# 今日の18-24時の降水確率を取得し、weather_nowに代入
else:
    weather_now = weather_json["forecasts"][0]["chanceOfRain"]["T18_24"]

# 現在時刻の降水確率をweather_now_textに代入
weather_now_text = "現在の降水確率：" + weather_now
st.write(weather_now_text)

# 今日、明日、明後日の３日間の降水確率を返す
# 今日、明日、明後日の降水確率をそれぞれ異なるDataFrameに代入
df1 = pd.DataFrame(weather_json["forecasts"][0]["chanceOfRain"], index=["今日"]) # index名を今日という文字列に設定
df2 = pd.DataFrame(weather_json["forecasts"][1]["chanceOfRain"], index=["明日"]) # index名を明日という文字列に設定
df3 = pd.DataFrame(weather_json["forecasts"][2]["chanceOfRain"], index=["明後日"]) # index名を明後日という文字列に設定

# 今日、明日、明後日の降水確率を結合して一覧にしてdfに代入
df = pd.concat([df1, df2, df3])

st.dataframe(df)