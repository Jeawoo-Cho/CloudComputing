#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request
import mymodule

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('myname.html')

@app.route('/post', methods=['GET', 'POST'])
def post():

    value = request.form['input']
    subN = "%s" %value
    msg = mymodule.subcode(subN)
    
    day = request.form['chk_day']
    
    updown = request.form['chk_info']
    
    time_xml = mymodule.subtime(msg, day, updown)
    
    return render_template('search.html', data=time_xml)



if __name__=="__main__":
    app.run(host='0.0.0.0', port=9000)


# In[3]:





# In[5]:





# In[7]:





# In[ ]:




