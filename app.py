from flask import Flask, render_template, Blueprint

app = Flask(__name__, template_folder="templates")


@app.route("/health")
def index():
    return 'index'


@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/demo")
def demo():
    return render_template('demo.html')


# this is the entrance of the app
if __name__ == '__main__':
    app.run(debug=True, port=5005)

"""
for saikrit:
# both username and password:
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


# how to use git to push changes to global:
1. make sure you are in the correct path: 
copy this "cd /Users/deepakjha/Desktop/Roblox/web_design"
and paste in the terminal

2. type "git status" to check any changed files

3. type "git add file_names" to add changes to stage

4. type "git commit -m your_message" to create a reference

5. type "git push" to update remote

"""


# deployment
# https://render.com/docs/deploy-flask

# backend
# https://medium.com/analytics-vidhya/how-to-create-a-contact-page-that-users-can-use-to-contact-you-on-your-website-758187207f65