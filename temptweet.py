from twython import Twython, TwythonError
from twittersecrets import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
import time
import ow

# Requires Authentication as of Twitter API v1.1
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
currentTime = time.localtime(time.time())
currentHour = currentTime[3]

ow.init('4304')

insidesensors = ['/28.BCDD70040000','/28.113ABC040000']
outsidesensors = ['/28.B9D370040000']

insidetemps = []
outsidetemps = []

for t in outsidesensors:
	try:
		temp =  ow.Sensor(t).temperature
		outsidetemps.append(float(temp))
	except Exception, e:
		print e

for u in insidesensors:
	try:
		temp2 = ow.Sensor(u).temperature
		insidetemps.append(float(temp2))
        except Exception, e:
                print e

outsideavg = 'N/A'
insideavg = 'N/A'

if len(outsidetemps) > 0:
	outsideavg = str( float(sum(outsidetemps))/float(len(outsidetemps)) )

if len(insidetemps) > 0:
        insideavg = str( float(sum(insidetemps))/float(len(insidetemps)) )



print 'O-AVG: ' + outsideavg
print 'I-AVG: ' + insideavg

#ampm = 'am'
#if currentHour > 12:
#	currentHour = currentHour - 12
#	ampm = 'pm'
timeString = str(currentHour)
if currentHour < 10:
	timeString = '0' + timeString

tweet = 'It is ' + timeString  + '00 hrs. Outside Temperature: ' + outsideavg + ' Inside Temperature: ' + insideavg 

try:
    	
	twitter.update_status(status=tweet)
	print tweet
except TwythonError as e:
    print e

#end
