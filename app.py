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
for saikrit
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
"""


# deployment
# https://render.com/docs/deploy-flask

# backend
# https://medium.com/analytics-vidhya/how-to-create-a-contact-page-that-users-can-use-to-contact-you-on-your-website-758187207f65