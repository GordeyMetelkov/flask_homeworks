from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def registry():
    if request.method == 'POST':
        user_name = request.form.get('name')
        user_email = request.form.get('email')
        response = make_response(redirect(url_for('user_welcome')))
        response.set_cookie('name', user_name)
        response.set_cookie('email', user_email)
        return response
    else:
        return render_template('registry.html')


@app.route('/welcome/', methods=['POST', 'GET'])
def user_welcome():
    if request.method == 'POST':
        response = make_response(redirect(url_for('user_welcome')))
        response.set_cookie('name', 'user_name', max_age=0)
        response.set_cookie('email', 'user_email', max_age=0)
        return response
    return render_template('user_welcome.html')

if __name__ == '__main__':
    app.run()
