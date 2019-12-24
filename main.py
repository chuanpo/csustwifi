import requests ,time
import configparser

def login_cs(mac,user,upass):
	try :
		url = 'http://192.168.7.221:801/eportal/?c=ACSetting&a=Login&'+mac
		form = {
				'DDDDD': ",0,{}".format(user),
				'upass': upass,
				'R1': 0,
				'R2': 0,
				'R3': 0,
				'R6': 0,
				'para': 00,
				'0MKKey': '123456',
				}
		html = requests.post(url, data=form,timeout=1.5)
		html = requests.get('https://www.baidu.com', timeout=2)
	except:
		return ''
def mac_cs():	
	try :
		url = 'http://1.1.1.1/?isReback=1'
		html = requests.post(url=url, allow_redirects=False, timeout=2)
		url= html.headers['Location']
		url=url.split('?',1)[1]
		return url
	except:
		return ''


def main():
	conf = configparser.ConfigParser()
	conf.read('user.conf')
	user=conf.get("default", "user") 
	upass=conf.get("default", "upass") 
	for i in range(3):
		print('尝试采集MAC【第{}次】'.format(i+1))
		mac=mac_cs()
		if mac!='':
			print('MAC采集成功\n',mac.replace('&','\n'))
			break
		elif i==2:
			print('''
检查是否连接WIFI或网线
建议设置 WIFI 自动连接
					''')
			return
	
	for  i in range(3):
		if login_cs(mac,user,upass)!='':
			print('连接成功')
			break
		elif i==2:
			print('连接失败检查一下用户名和密码')
			return

	##input('直接关闭窗口就行')
if __name__=='__main__':
	main()