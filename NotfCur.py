#! /usr/bin/python3

import requests, os
from bs4 import BeautifulSoup
from datetime import datetime


def send_notice(title, message):
	os.system('notify-send "{}" "{}"'.format(title, message)) 



def get_html():
	url = 'https://myfin.by/'
	r = requests.get(url)
	return r.text


def get_usd_rate(html, currence = 0):
	soup = BeautifulSoup(html, 'lxml')
	usd = soup.find('div', class_='header__best-content').find_all('div')[currence].text.split()[1]
	buy = usd[:5]
	sell = usd[5:]
	
	return 'Buy: {}\nSell: {}'.format(buy, sell)


def main():
	html = get_html()
	message = get_usd_rate(html)
	title = datetime.today().strftime("%d/%m/%Y") + '\nДоллар стоит'
	send_notice(title, message)




if __name__ == '__main__':
	main()