from flask import Flask, request, redirect, render_template

from roberta import autocomplete

app = Flask(__name__)

@app.route('/')
def home():
    # return "First name: <input type=\"text\" name=\"fname\"><br>"
    return  r'<form method="POST"> Text: <input name="text"><br> <input type="submit" name="submit_button" value="Do Something"> </form>'

@app.route('/', methods=['POST'])
def home_post():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Do Something':
            print("Do something!")
            text = request.form['text']
            print(text)
            next_word = autocomplete(text)
            print(next_word)
            return render_template("answer.html", next_word=next_word)
            # return text + ' {}'.format(next_word)
        elif request.form['submit_button'] == 'Do Something Else':
            return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)