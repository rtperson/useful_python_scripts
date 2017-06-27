import urllib2
import time
import os
import socket
import ssl
import datetime
import pytz

url = <URL TO CONNECT>

def play_warning_sound(): 
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 2, 500))

def handle_error(e):
    print ("=====  ERROR FOUND! ====")
    tz = pytz.timezone('US/Hawaii')
    date = datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    e.code = getattr(e, 'code', 'no code')
    e.reason = getattr(e, 'reason', 'reason not available')
    print (e.code, e.reason, date)
    play_warning_sound()

while True:

    request = urllib2.Request(url)
    request.add_header('Pragma', 'no-cache')
    request.add_header('User-Agent', 'Mozilla/5.0')
    try:
        code = urllib2.urlopen(request, timeout=1).getcode()
        if code == 200:
            print ("Still Up")
        else: 
            handle_error(Nil)
    except urllib2.HTTPError as e:
        handle_error(e)
    except urllib2.URLError as e:
        handle_error(e)
    except socket.timeout as e:
        handle_error(e)
    except ssl.SSLError as e:
        handle_error(e)
    except Exception as e:
        handle_error(e)

    time.sleep(30)