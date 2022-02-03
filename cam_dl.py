from numpy import loadtxt
import wget
import time
import os
from urllib.error import HTTPError

# load urls from file into list urls_list
urls_list = loadtxt('urls.txt', dtype="str")

# ensure dirs for each url exist. if they dont, create them
for element in urls_list:

  if os.path.isdir(f"./{element[1]}"):
    pass
  else:
    os.mkdir(element[1])

def load_urls():
  urls_list = loadtxt('urls.txt', dtype="str")
  print(urls_list[0])

def dtstamp_str():
    return str(time.strftime("%Y%m%d-%H%M%S"))

#note - images are updated in 2s intervals ex. 0,2,4,6 in real time, so get all your downloads in then
def get_img():

  global last_sec_dlded
  last_sec_dlded = int(time.strftime("%S"))

  if int(time.strftime("%S"))%2 == 0:
    time.sleep(1/2)
    print(f"[INFO] Downloads initiated at {dtstamp_str()}")
    t1 = timer()
    for element in urls_list:
      try:
        wget.download(element[0], f"./{element[1]}/{dtstamp_str()}.jpeg", bar=None)
        print(f"[INFO] Got image for {element[0]}, written to ./{element[1]}/{dtstamp_str()}.jpeg")
      except HTTPError:
        print(f"[FATAL] Could not get {element[0]}, the link is most likely dead")

    print(f"[INFO] Download complete, done in {t1.end()}s")

    while int(time.strftime("%S"))%2 == last_sec_dlded%2:
      time.sleep(1/100)


class timer:
  """ 
  Gives elapsed time between two calls
  timer() - starts the timing
  timer.end() - stops the timing and returns time (in seconds) since timer() was called 
  """
  def __init__(self):
    self.start = time.time()
  def end(self):
    end = time.time()
    return float(end - self.start)

    
    


# load_urls()
# print(urls_list[0][1])
#get_img(url0)
while True:
  get_img()