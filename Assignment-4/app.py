import web
import os
import json

print(os.getcwd())

urls = (
  '/form', 'Index'
)



#render = web.template.render('templates')
#modified the code by adding the path inside the function

render = web.template.render('/Users/vamshidharpratap/Downloads/DynamicWeb/templates/')

credentials_list = [
    ["Peter", "pete@gmail.com"],
    ["Korok", "sengupta@yahoo.com"],
    ["Stefan", "stef@gmail.com"],
    ["Mara", "mara@yahoo.com"],
    ["Jun", "jun@gmail.com"],
    ["Omar", "omar@uni-koblenz.com"],
    ["Claudia", "claudia@gmail.com"],
    ["Nina", "nina@airbnb.com"],
    ["Husam", "sam@gmail.com"],
    ["Rajesh", "raj@gmail.com"],
]

class Index(object):
    def GET(self):
        
        return render.form()

    def POST(self):
        
        #form = web.input(name="Nobody", email="Hello")
        #item = [form.name, form.email]
        #print(type(web.data()))
        form = json.loads(web.data().decode('utf-8'))
        form = json.loads(form)
        #print(type(form))
        #print(form)
        item = [form['name'],form['email']]
        print(item)
        if item in credentials_list:
            # print (item)
            msg = "Error! This contact is already in the list."
            list_size = "%s" % (len(credentials_list))
            return render.index(list_size=list_size, msg=msg)
            # return app.notfound()
        else:
            msg = "Success! You have added a new contact to the list."
            credentials_list.append(item)
            list_size = "%s" % (len(credentials_list))
            return render.index(list_size = list_size, msg=msg)

if __name__ == "__main__":
    
    app = web.application(urls, globals())
    app.run()