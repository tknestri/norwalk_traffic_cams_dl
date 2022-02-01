from numpy import loadtxt
import wget
import time
import os

last_sec_dlded = 61

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

# test case
url0 = "https://ie.trafficland.com/v2.0/8290/huge?system=weatherbug-cmn&pubtoken=dca193d631f338175f12fbf81a52cbff77dd128633e2cdb45be114e5b3427802&refreshRate=2000&rnd=1643668023215"

def dtstamp_str():
    return str(time.strftime("%Y%m%d-%H%M%S"))

#note - images are updated in 2s intervals ex. 0,2,4,6 in real time, so get all your downloads in then
def get_img():
  global last_sec_dlded
  last_sec_dlded = int(time.strftime("%S"))
  # if last_sec_dlded != int(time.strftime("%S"))-1 & int(time.strftime("%S"))%2 == 0:
  if int(time.strftime("%S"))%2 == 0:
    time.sleep(1)
    print(last_sec_dlded)
    for element in urls_list:
      wget.download(element[0], f"./{element[1]}/{dtstamp_str()}.jpeg")
    last_sec_dlded = int(time.strftime("%S"))
    print(last_sec_dlded)

    while int(time.strftime("%S"))%2 == last_sec_dlded%2:
      time.sleep(1/100)

    


# load_urls()
# print(urls_list[0][1])
#get_img(url0)
while True:
  get_img()