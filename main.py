import random, praw, time
from multiprocessing import Process
from keep_alive import keep_alive
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup 
import os
from PIL import Image
import json   
import urllib
import shutil
import json   
import random

ua = UserAgent()
print(ua.firefox)
header = {'User-Agent':str(ua.firefox)}
print(header)
# If someone cba to hack a cock bot then they deserve the glory of doing so

# Nah they just have no life like us
#fair point
#cool it's "secured"
# lmao, someone just used it
# best chat plaform is repl.it

id_client = os.environ['id']
secret_client = os.environ['secret']
defo_secure_password = os.environ['totally-secure-password']

reddit = praw.Reddit(
    user_agent="dick_swinger",
    client_id=id_client,
    client_secret=secret_client,
    username="CockifyBot",
    password=defo_secure_password,
    validate_on_submit = True
)


print(reddit.user.me())

def lmaoSnooCockBot():
  #cocks = ['dick_bbc.png','hairycock.png']
  for item in reddit.inbox.stream(skip_existing=True):
    if "u/cockifybot" in item.body.lower():
      print(20*"--")
      print(item.body)
      print("by: ", item.author)
      print(20*"--")
      try:
        

        page = requests.get(f'https://www.reddit.com/user/{item.author}', headers=header)
        soup = BeautifulSoup(page.content, 'html.parser')

        aas = soup.find_all("div", class_='_34XIqvI8-YT1wukR_W8vj6')

        print(aas)
        print("----------------------------------------------")
        image_info = []
        for a in aas:
            image_tag = a.findChildren("img")
            image_info.append((image_tag[0]["src"]))
            
        print(image_info)
        f = open('cock.png','wb')
        f.write(urllib.request.urlopen(image_info[0]).read())
        f.close()

        #imagecock = random.choice(cocks)
        background = Image.open("cock.png")
        foreground = Image.open("hairycock.png")

        background.paste(foreground, (0, 0), foreground)
        background.save("merged_images.png", "PNG")
        submission = reddit.subreddit("CockifyBot").submit_image(f'u/{item.author} with a cock', 'merged_images.png')
        item.reply(f'''I've given your snoo a cock. See your snoo with a cock [here]({submission.url})
        
        Your mom would be so proud! ''')
        image_info.clear()

      except Exception as ex:
        try:
          item.reply(f'''I tried to give your snoo a cock but I couldn't. Are you sure that you have created a snoo? Sometimes the bot doesn't work for users who have Reddit premium or who have set their profile to NSFW. I could probably fix this but I really can't be bothered.''')
          print(ex)
        except Exception as ex:
          print(ex)
          print('fml')
          
    #for fuck's sake 
      #quality coding right here :)
      #wtf was it
      # It was a missing semicolon 
    #ffs

    
    
    



#lmaoSnooCockBot()

if __name__ == '__main__':
  process1 = Process(target=lmaoSnooCockBot)
  process2 = Process(target=keep_alive)
  process1.start()
  process2.start()

  process1.join()
  process2.join()
#comment_inspector()
