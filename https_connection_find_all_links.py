from bs4 import BeautifulSoup as b
import urllib2
user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
headers = { 'User-Agent' : user_agent }
req = urllib2.Request('https://www.hrgworldwide.com/locations/hrg-location-a-z/', None, headers)
response = urllib2.urlopen(req)
page = response.read()
response.close()
soup=b(page, 'html.parser')
for nextlink in soup.findAll("div", {"class" : "col-sm-4 col-xs-12 address"}):
    a = nextlink.find('a')
    print a.get('href')
