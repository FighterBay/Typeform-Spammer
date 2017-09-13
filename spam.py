import requests
import time
import random
header = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"
}





ctr = 0


while True:

   d_rand = random.randint(0,len(domain) - 1)
   token = requests.get("https://name.typeform.com/app/form/result/token/name/default",headers=header)
   print token
   #time.sleep(random.randint(0,2))
   r = requests.post("https://name.typeform.com/app/form/submit/name",
       data = {"form[language]":"en",
       "form[landed_at]":str(int(time.time())), #Add more fields according to the typeform.
       "form[token]":token},headers=header)
   if (r.status_code == 200):
       ctr = ctr + 1
   print "Total number of forms filled   : ", ctr
