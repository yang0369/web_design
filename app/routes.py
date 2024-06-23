from flask import Flask, render_template, request
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        return 'form posted'

    return render_template('contact.html', form=form)


# this is the entrance of the app
if __name__ == '__main__':
    app.run(debug=True, port=5005)
