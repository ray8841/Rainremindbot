import requests
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextSendMessage
from flask import Flask, request, abort
import threading
from pyngrok import ngrok

# ...

ngrok_tunnel = ngrok.connect(5000)  # 假設你的 LINE bot 在本地埠號 5000 上運行

# 取得 Ngrok 提供的公開網址
public_url = ngrok_tunnel.public_url


print("Ngrok 隧道 URL:", public_url)
app = Flask(__name__)

line_bot_api = LineBotApi('ySH5ENFcKkblj/3iSsynjtR7bEvAj8nawuEgl8MJ5hkOawVwmCKkFAuZbIVze+yIP9ClBMaPhJhkWwY5ZIv7gr4lQ1JEQuImIjBvxRwTEn37RETFbCXNBAc0reCV19B5mp1MhphTrBXNzRpT7lFfLwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('88c9f25b995efbc269ac2ff812b49d4e')
openweather_api_key = 'e2c446eb5f2982074a548710794f1f9a'

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

def check_rain():
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}'
    cities = [
    ('London', 'gb'),
    ('Tokyo', 'jp'),
    ('Seoul', 'kr'),
    ('New Delhi', 'in'),
    ('Sydney', 'au'),
    ('Cairo', 'eg'),
    ('Rome', 'it'),
    ('Madrid', 'es'),
    ('Toronto', 'ca'),
    ('Bangkok', 'th'),
    ('Rio de Janeiro', 'br'),
    ('Cape Town', 'za'),
    ('Dubai', 'ae'),
    ('Singapore', 'sg'),
    ('Buenos Aires', 'ar'),
    ('Mumbai', 'in'),
    ('Jakarta', 'id'),
    ('Hong Kong', 'hk'),
    ('Zurich', 'ch'),
    ('Athens', 'gr'),
    ('Budapest', 'hu'),
    ('Oslo', 'no'),
    ('Stockholm', 'se'),
    ('Brussels', 'be'),
    ('Copenhagen', 'dk'),
    ('Lisbon', 'pt'),
    ('Dublin', 'ie'),
    ('Wellington', 'nz'),
    ('Brasilia', 'br'),
    ('Santiago', 'cl'),
    ('Bogota', 'co'),
    ('Lima', 'pe'),
    ('Mexico City', 'mx'),
    ('Vancouver', 'ca'),
    ('Sydney', 'au'),
    ('Auckland', 'nz'),
    ('Oslo', 'no'),
    ('Rome', 'it'),
    ('Madrid', 'es'),
    ('Bangkok', 'th'),
    ('Buenos Aires', 'ar'),
    ('Johannesburg', 'za'),
    ('Munich', 'de'),
    ('Milan', 'it'),
    ('Mumbai', 'in'),
    ('Cairo', 'eg'),
    ('Berlin', 'de'),
    ('Toronto', 'ca'),
    ('Prague', 'cz'),
    ('Budapest', 'hu'),
    ('Seoul', 'kr'),
    ('Istanbul', 'tr'),
    ('Brussels', 'be'),
    ('Lisbon', 'pt'),
    ('Dublin', 'ie'),
    ('Athens', 'gr'),
    ('Jakarta', 'id'),
    ('Hong Kong', 'hk'),
    ('Rio de Janeiro', 'br'),
    ('Lima', 'pe'),
    ('Cape Town', 'za'),
    ('Sydney', 'au'),
    ('Barcelona', 'es'),
    ('New York', 'us'),
    ('Tokyo', 'jp'),
    ('Singapore', 'sg'),
    ('Brasilia', 'br'),
    ('Santiago', 'cl'),
    ('Bogota', 'co'),
    ('Vancouver', 'ca'),
    ('San Francisco', 'us'),
    ('Seattle', 'us'),
    ('Chicago', 'us'),
    ('Boston', 'us'),
    ('Karachi', 'pk'),
    ('Macao', 'mo'),
    ('Kolkata', 'in'),
    ('Manila', 'ph'),
    ('Kuala Lumpur', 'my'),
    ('Ho Chi Minh City', 'vn'),
    ('Busan', 'kr'),
    ('Taipei', 'tw'),
    ('Riyadh', 'sa'),
    ('Doha', 'qa'),
    ('Abu Dhabi', 'ae'),
    ('Baghdad', 'iq'),
    ('Tel Aviv', 'il'),
    ('Kabul', 'af'),
    ('Kuwait City', 'kw'),
    ('Muscat', 'om'),
    ('Colombo', 'lk'),
    ('Dhaka', 'bd'),
    ('Islamabad', 'pk'),
    ('Male', 'mv'),
    ('Hanoi', 'vn'),
    ('Phnom Penh', 'kh'),
    ('Naypyidaw', 'mm'),
    ('Ulaanbaatar', 'mn'),
    ('Astana', 'kz'),
    ('Tashkent', 'uz'),
    ('Bishkek', 'kg'),
    ('Dushanbe', 'tj'),
    ('Ashgabat', 'tm'),
    ('Kathmandu', 'np'),
    ('Thimphu', 'bt'),
    ('Dili', 'tl'),
    ('Nicosia', 'cy'),
    ('Los Angeles', 'us'),
    ('Chicago', 'us'),
    ('Houston', 'us'),
    ('Phoenix', 'us'),
    ('Philadelphia', 'us'),
    ('San Antonio', 'us'),
    ('San Diego', 'us'),
    ('Dallas', 'us'),
    ('San Jose', 'us'),
    ('Austin', 'us'),
    ('Jacksonville', 'us'),
    ('San Francisco', 'us'),
    ('Indianapolis', 'us'),
    ('Columbus', 'us'),
    ('Fort Worth', 'us'),
    ('Charlotte', 'us'),
    ('Seattle', 'us'),
    ('Denver', 'us'),
    ('Washington', 'us'),
    ('Boston', 'us'),
    ('El Paso', 'us'),
    ('Detroit', 'us'),
    ('Nashville', 'us'),
    ('Memphis', 'us'),
    ('Portland', 'us'),
    ('Oklahoma City', 'us'),
    ('Las Vegas', 'us'),
    ('Louisville', 'us'),
    ('Baltimore', 'us'),
    ('Milwaukee', 'us'),
    ('Albuquerque', 'us'),
    ('Tucson', 'us'),
    ('Fresno', 'us'),
    ('Sacramento', 'us'),
    ('Mesa', 'us'),
    ('Kansas City', 'us'),
    ('Atlanta', 'us'),
    ('Long Beach', 'us'),
    ('Colorado Springs', 'us'),
    ('Raleigh', 'us'),
    ('Miami', 'us'),
    ('Virginia Beach', 'us'),
    ('Omaha', 'us'),
    ('Oakland', 'us'),
    ('Minneapolis', 'us'),
    ('Tulsa', 'us'),
    ('Arlington', 'us'),
    ('New Orleans', 'us'),
    ('Wichita', 'us'),
    ('Paris', 'fr'),
    ('Madrid', 'es'),
    ('Berlin', 'de'),
    ('Rome', 'it'),
    ('Athens', 'gr'),
    ('Amsterdam', 'nl'),
    ('Vienna', 'at'),
    ('Dublin', 'ie'),
    ('Helsinki', 'fi'),
    ('Lisbon', 'pt'),
    ('Budapest', 'hu'),
    ('Brussels', 'be'),
    ('Oslo', 'no'),
    ('Geneva', 'ch'),
    ('Barcelona', 'es'),
    ('Munich', 'de'),
    ('Lyon', 'fr'),
    ('Hamburg', 'de'),
    ('Milan', 'it'),
    ('Frankfurt', 'de'),
    ('Cologne', 'de'),
    ('Lisbon', 'pt'),
    ('Athens', 'gr'),
    ('Edinburgh', 'gb'),
    ('Nice', 'fr'),
    ('Krakow', 'pl'),
    ('Naples', 'it'),
    ('Turin', 'it'),
    ('Bologna', 'it'),
    ('Florence', 'it'),
    ('Rotterdam', 'nl'),
    ('Antwerp', 'be'),
    ('Seville', 'es'),
    ('Valencia', 'es'),
    ('Malaga', 'es'),
    ('Porto', 'pt'),
    ('Bilbao', 'es'),
    ('Dublin', 'ie'),
    ('Reykjavik', 'is'),
    ('Gothenburg', 'se'),
    ('Oslo', 'no'),
    ('Warsaw', 'pl'),
    ('Bucharest', 'ro')
    # 在这里添加或修改其他城市
]
 # 您可以根據需要添加更多城市
    for city, country_code in cities:
        response = requests.get(url.format(city, country_code, openweather_api_key))
        data = response.json()
        if 'weather' in data:
            weather_condition = data['weather'][0]['main']
            if weather_condition == 'Rain':
                line_bot_api.broadcast(
                    TextSendMessage(text=f"地區 {city} 正在下雨！")
                )
            

def start_checking_rain():
    # 開始自動檢查下雨
    threading.Timer(3000, start_checking_rain).start()
    check_rain()

if __name__ == "__main__":
    # 啟動自動檢查下雨的計時器
    start_checking_rain()
    app.run()
