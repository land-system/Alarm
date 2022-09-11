#Pythonista_Code_Alarm
from pyowm import OWM
import datetime
from sound import *
import schedule
import webbrowser
import socket
import sys
import jpholiday
from speech import say
import time
import random

wifi_text = None

def Time_Now():
	time_now = datetime.datetime.now()
	month_text = time_now.month
	day_text = time_now.day
	hour_text = time_now.hour
	minute_text = time_now.minute
	date_text = f'{str(hour_text).zfill(2)}:{str(minute_text).zfill(2)}'
	speech_word_1 = f'おはようございます、今日は{str(month_text)}月{str(day_text)}日、 現在時刻は' + date_text + 'です。'
	speech_word_2 = f'こんにちは、今日は{str(month_text)}月{str(day_text)}日、 現在時刻は' + date_text + 'です。'
	speech_word_3 = f'こんばんは、今日は{str(month_text)}月{str(day_text)}日、 現在時刻は' + date_text + 'です。'
	if hour_text < 10 :
		say(speech_word_1)
		print(speech_word_1)
	elif hour_text < 17 :
		say(speech_word_2)
		print(speech_word_2)
	elif hour_text >= 18 :
		say(speech_word_3)
		print(speech_word_3)
		
def National():
	time_now = datetime.datetime.now()
	year_text = time_now.year
	month_text = time_now.month
	day_text = time_now.day
	holiday = jpholiday.is_holiday_name(datetime.date(year_text,month_text,day_text))
	date_text = f'今日は、{holiday}の日です。'
	if holiday == None:
		pass
	else:
		say(date_text)
		print(date_text)
		
def Wifi_Chack():
	global wifi_text
	host = '8.8.8.8'
	port = 53
	timeout = 5
	try:
		socket.setdefaulttimeout(timeout)
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((host,port))
		wifi_text = True
	except:
		wifi_text = False
		
def Weather_Now():
	id = 000000#地域のidを入力して下さい。
	api_key = ''#openweatherで収得したAPIkeyを入力して下さい。
	for i in range(2):
		owm = OWM(api_key)
		text = owm.weather_at_id(id)
		text_text = text.get_weather()
		weather = text_text.get_detailed_status()
	date0 = '今日の天気は、'
	date_text_list = ['晴れ','弱い雨','強い雨','激しい雨','非常に激しい雨','猛烈な雨','少数の雲','壊れた雲','散乱した雲','曇りの雲']
	date1 = 'です。'
	date2 = 'かっぱや傘を持っていきましょう、また、怪我をしないように注意してください。'
	date3 = '雨が降るかもしれないので、傘やカッパを持っていきましょう。'
	if weather == 'sunny':
		say(f'{date0}{date_text_list[0]}{date1}')
		print(f'{date0}{date_text_list[0]}{date1}')
	elif weather == 'light rain':
		say(f'{date0}{date_text_list[1]}{date1}')
		say(date2)
		print(f'{date0}{date_text_list[1]}{date1}')
		print(date2)
	elif weather == 'moderate rain':
		say(f'{date0}{date_text_list[2]}{date1}')
		say(date2)
		print(f'{date0}{date_text_list[2]}{date1}')
		print(date2)
	elif weather == 'heavy intensity rain':
		say(f'{date0}{date_text_list[3]}{date1}')
		say(date2)
		print(f'{date0}{date_text_list[3]}{date1}')
		print(date2)
	elif weather == 'very heavy rain':
		say(f'{date0}{date_text_list[4]}{date1}')
		say(date2)
		print(f'{date0}{date_text_list[4]}{date1}')
		print(date2)
	elif weather == 'extreme rain':
		say(f'{date0}{date_text_list[5]}{date1}')
		say(date2)
		print(f'{date0}{date_text_list[5]}{date1}')
		print(date2)
	elif weather == 'few clouds':
		say(f'{date0}{date_text_list[6]}{date1}')
		say(date3)
		print(f'{date0}{date_text_list[6]}{date1}')
		print(date3)
	elif weather == 'broken clouds':
		say(f'{date0}{date_text_list[7]}{date1}')
		say(date3)
		print(f'{date0}{date_text_list[7]}{date1}')
		print(date3)
	elif weather == 'scattered clouds':
		say(f'{date0}{date_text_list[8]}{date1}')
		say(date3)
		print(f'{date0}{date_text_list[8]}{date1}')
		print(date3)
	elif weather == 'overcast clouds':
		say(f'{date0}{date_text_list[9]}{date1}')
		say(date3)
		print(f'{date0}{date_text_list[9]}{date1}')
		print(date3)
	else:
		say('すみません、天気様子のデータがないため音声ではなく、表示します。')
		print(f'Weather : {weather}')
		
def News():
	say('ニュースサイトに飛びます。')
	#好きなニュースサイトのURLを貼り付けて下さい。
	print('ニュースサイトに飛びます。(Yahoo News)')
	webbrowser.open('https://news.yahoo.co.jp')	
def Sound():
	music_list = ['BGM_0','BGM_1','BGM_2','BGM_3']#このテキストと同じパスで音楽名を入れて下さい。(拡張子は入れないで下さい。mp3しか対応してないので注意を)
	music_file = random.choice(music_list) + '.mp3'
	music = play_effect(name=music_file,looping=True)
	input()#Enterで停止
	stop_effect(music)
	print(f'{music_file}を停止しました。')
	
def Main():
	say('時間です。')
	print('時間です。')
	Sound()
	Time_Now()
	National()
	Weather_Now()
	time.sleep(15)
	News()
	word_list = ['体調を気をつけてください','油断は禁物です','どうか、楽しい一日を']
	say(random.choice(word_list))
	sys.exit()	
if __name__ == '__main__':
	try:
		print("目覚ましをセットする時間を指定してください。")
		hour = input("時間　: ")
		minute = input("分 : ")
		target = f"{hour.zfill(2)}:{minute.zfill(2)}"
		say(target+"にアラームをセットしました。")
		print(target+"にアラームをセットしました。")
		schedule.every().day.at(target).do(Main)
		while True:
			schedule.run_pending()
			time.sleep(1)
		sys.exit()
	except ConnectionError:
		time.sleep(10)
		say('インターネットの接続が確認できないため、これより接続テストを行います。')
		print('インターネットの接続が確認できないため、これより接続テストを行います。')
		for i in range(10):
				Wifi_Chack()
				if wifi_text == True:
					say('接続が確認されました。')
					print('接続が確認されました。')
					continue
				elif wifi_text == False:
					say('インターネットの接続を確認してください。')
					print('インターネットの接続を確認してください。')
					sys.exit()
	else:
		say('インターネットの接続が出来ません。')
		print('インターネットの接続が出来ません。')
		sys.exit()
