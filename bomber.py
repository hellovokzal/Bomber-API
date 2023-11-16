from flask import Flask
from requests import get
from threading import Thread
from time import sleep
import os

def bomb(phone):
             while True:
              if os.path.exists(f"{phone}.txt"):
               os.system(f"rm {phone}.txt")
               break
              else:
               url = get("http://example.com")
               print(f"Sended http://example.com/{phone}")

app = Flask(__name__)

@app.route("/<message>")
def echo(message):
    start = Thread(target=bomb, args=(f"{message}",))
    start.start()
    sleep(60)
    f = open(f"{message}.txt", "w")
    f.close()
    return "Окончена атака!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
