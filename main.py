from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

form = '''
'''

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def validateUser():
    # save form inputs to variables
    username = request.form['username']
    password = request.form['password']
    verifyPassword = request.form['verifypassword']
    email = request.form['email']
    error = {
        'quantity': 0,
        'passwordMatch': false,
        'passwordEmpty': false,
        'verifyPasswordEmpty': false,
        'usernameInvalid': false,
        'passwordInvalid': false,
        'emailEmpty': false,
        'emailInvalid': false
    }

    # log those variables for debugging
    app.logger.info('%s username',username)
    app.logger.info('%s password',password)
    app.logger.info('%s verifyPassword',verifyPassword)
    app.logger.info('%s email',email)

    # validate that verify password & password are the same
    if password != verifypassword:
        error['passwordMatch'] = true
        error['quantity']+=1

    # make sure password isn't empty
    if len(password) == 0:
        error['passwordEmpty'] = true
        error['quantity']+=1

    # make sure username isn't empty
    if len(username) == 0:
        error['usernameEmpty'] = true
        error['quantity']+=1

    # make sure password isn't empty
    if len(verifyPassword) == 0:
        error['verifyPasswordEmpty'] = true
        error['quantity']+=1

    # make sure username doesn't contain space
    if ' ' in username:
        error['usernameInvalid'] = true
        error['quantity']+=1

    # make sure space isn't in password
    if ' ' in password:
        error['passwordInvalid'] = true
        error['quantity']+=1

    #make sure email isn't empty
    if len(email) == 0:
        error['emailEmpty'] = true
        error['quantity']+=1

    #make sure email contains the '@' character
    if '@' not in email:
        errorEmailInvalid = true
        error+=1

    if error > 0:
        return render_template('welcome.html',username)
    else:
        return render_template('index.html',error)

if __name__ == '__main__':
    app.run(debug=True)
