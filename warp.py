import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
script_version = '4.0.0'
referrer = "Client configuration ID"
def progressBar():
	animation = [
	    "[□□□□□□□□□□]", "[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]",
	    "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]",
	    "[■■■■■■■■□□]", "[■■■■■■■■■□]"
	]
	progress_anim = 0
	save_anim = animation[progress_anim % len(animation)]
	percent = 0
	while True:
		for i in range(10):
			percent += 1
			sys.stdout.write(f"\r[+] Đang gửi yêu cầu. " + save_anim +
			                 f" {percent}%")
			sys.stdout.flush()
			time.sleep(0.005)
		progress_anim += 1
		save_anim = animation[progress_anim % len(animation)]
		if percent == 100:
			sys.stdout.write("\r[+] Nhận được phản hồi. [■■■■■■■■■■] 100%")
			break

def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)

def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))
	except Exception as error:
		print(error)
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'

def run():
	try:
		install_id = genString(22)
		body = {
		    "key": "{}=".format(genString(43)),
		    "install_id": install_id,
		    "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
		    "referrer": referrer,
		    "warp_enabled": False,
		    "tos": datetime.datetime.now().isoformat()[:-3] + "+07:00",
		    "type": "Android",
		    "locale": "vi_VN"
		}
		data = json.dumps(body).encode('utf8')
		headers = {
		    'Content-Type': 'application/json; charset=UTF-8',
		    'Host': 'api.cloudflareclient.com',
		    'Connection': 'Keep-Alive',
		    'Accept-Encoding': 'gzip',
		    'User-Agent': 'okhttp/3.12.1'
		}
		req = urllib.request.Request(url, data, headers)
		response = urllib.request.urlopen(req)
		status_code = response.getcode()
		return status_code
	except Exception as error:
		print("")
		print(error)

g = 0
b = 0
while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	print("[*] Lưu ý: Chạy trên Chrome, Edge, Safari")
	print(f"\n[-] ID của bạn: {referrer}")
	print(f"[#] Kết quả: {g} thành công | {b} thất bại")
	print(f"[✔] Đã +{g}GB data WARP+ vào tài khoản của bạn")
	print("")
	sys.stdout.write("\r[+] Đang gửi lệnh. [□□□□□□□□□□] 0%")
	sys.stdout.flush()
	result = run()
	if result == 200:
		g += 1
		progressBar()
		print("")
		for i in range(18, 0, -1):
			sys.stdout.write(f"\r[*] Sau {i} giây, lệnh sẽ được gửi đi...")
			sys.stdout.flush()
			time.sleep(1)
	else:
		b += 1
		print("[✘] Lỗi kết nối tới máy chủ.")
		for i in range(18, 0, -1):
			sys.stdout.write(f"\r[*] Thử lại sau {i}s...")
			sys.stdout.flush()
			time.sleep(1)
