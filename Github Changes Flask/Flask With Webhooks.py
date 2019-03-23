## IT will notice the changes if something happends in my git repo. (pavan228)
# coding: utf-8




from flask import Flask
from flask import json
from flask import request


# In[2]:


app = Flask(__name__)


# In[3]:


@app.route("/")
def my_def():
    return "Hello Its working!"
@app.route("/git-hub",methods=['POST'])
def my_github_change():
	if request.headers['Content-Type']=="application/json":
		global my_info
		
		my_info = json.dumps(request.json)
		#print(my_info)
		with open("payload.txt",'w') as f:
			f.write(my_info)
		print("Payload Saved!")
		print("Created: ",json.dumps(request.json)['build']['created_at'])
		print("URL",json.dumps(request.json)['pusher']['url'])
		return my_info

#with open("payload.txt",'w') as f:
	#f.write(my_info)
	

if __name__=="__main__":
    app.run(debug=True)

