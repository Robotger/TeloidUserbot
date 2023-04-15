from flask import Flask
import threading
import os
import random
app = Flask(__name__)

@app.route("/")
def hello():
 owner_username = os.environ.get("REPL_OWNER")

 if owner_username == "ByMisakiMey":
  print("Öncelikle Botu forklamalısın.")
  print("First of all You should fork the bot")
  return "Öncelikle Botu forklamalısın.\nFirst of all You should fork the bot"
 else:
      return "Powered By Ber4tbey"
 
@app.route("/log")
def log():
 
  dosya = open('logfile.txt', 'r') 
  reddo = dosya.read()
  
  return str(reddo)
 

def run_flask_app():
    app.run("0.0.0.0",port=random.randint(1000,9999))


def start_flask_app():
    # Yeni bir thread oluştur
    t = threading.Thread(target=run_flask_app)
    # Arka planda çalıştır
    t.daemon = True
    # Thread'i başlat
    t.start()

if __name__ == "__main__":
    start_flask_app()
    from userbot import main
    



 

