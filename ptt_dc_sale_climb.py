import requests, re
import time
from bs4 import BeautifulSoup

##Line Notify Subfunction
def SendMessageToLineNotify(message, picurl):
    Token = "RN3PRRsPK6XgH34uSdKf9ty4urTZ6munWUYnqK2SC6J"
    url = "https://notify-api.line.me/api/notify"   
    payload = {'message':message,
               'imageThumbnail':picurl,
               'imageFullsize':picurl,
              }

    header = {'Content-Type':'application/x-www-form-urlencoded',
              'Authorization':'Bearer ' + Token
             }

    resp=requests.post(url, headers=header, data=payload)
    #print resp.text
####

def main():
    f = open('/Users/mm/desktop/ptt_dc_sale.txt', 'r+') 
    fl = f.read()
    print fl

    header = {
    '__cfduid': "",
    'cache-control': "no-cache",
    'Postman-Token': "d35ded36-2762-4115-81c7-3af85ababd8f",
    'cookie' : "over18=1; path=/; domain=.www.ptt.cc; Expires=Tue, 19 Jan 2038 03:14:07 GMT;"
    }

    res = requests.get("https://www.ptt.cc/bbs/Gossiping/index4.html", headers= header)
    res.encoding = 'utf-8'
    
    soup = BeautifulSoup(res.text, "html5lib")
    target1 = "RX580"
    target2 = "1070"
    
    print "+++++++++++++"
    for rent in soup.select('.r-ent'):
        #print rent.a
        print "+++++++++++++"
        renta = rent.span
        print renta
        renta_up = str(renta).upper()

        if ( renta_up.find("F3") != -1 ):
            #and ( fl[int(len(fl))-1] != (str(renta)+ "\n"))
            # if ( fl.find(str(renta)) < 0 ) :
                #fileaString.find(idFilter)
                print "------------------------"
                #print str(fl[int(len(fl))-1])
                #print renta
                #print fl.find(str(renta))
                rentan = str(rent.a) + "\n"
                #print rentan
                x= re.split('"', rentan)
                #print x[2]
                print x[1]
                # f.write(rentan)
                # f.close()
                picurl = ''
                time.sleep(1)
                SendMessageToLineNotify( x[2] + "https://www.ptt.cc" + x[1] , picurl)
                print "END"
        else: 
            #print "None"
            end = "end"

main()

