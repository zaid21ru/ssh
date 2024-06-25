import requests,random
from flask import Flask
app = Flask(__name__)	
@app.route('/')
def zaid():
	user= ''.join(random.choice('qwert_yui_opa_sdfghj_.klz_xcvb_nm12_34_567_890') for i in range(5))
	return user
if __name__ == "__main__":
	app.run()
