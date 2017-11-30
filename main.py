from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def index():
    return render_template('main.html')

@app.route("/", methods=['POST'])
def validateUser():
    # save form inputs to variables
    username = request.form['username']
    password = request.form['password']
    verifyPassword = request.form['verifypassword']
    email = request.form['email']
    error = {
        'quantity': 0,
        'passwordMatch': False,
        'passwordEmpty': False,
        'verifyPasswordEmpty': False,
        'usernameInvalid': False,
        'passwordInvalid': False,
        'emailEmpty': False,
        'emailInvalid': False
    }

    # log those variables for debugging
    app.logger.info('%s username',username)
    app.logger.info('%s password',password)
    app.logger.info('%s verifyPassword',verifyPassword)
    app.logger.info('%s email',email)

    # validate that verify password & password are the same
    if password != verifyPassword:
        error['passwordMatch'] = True
        error['quantity']+=1

    # make sure password isn't empty
    if len(password) == 0:
        error['passwordEmpty'] = True
        error['quantity']+=1

    # make sure username isn't empty
    if len(username) == 0:
        error['usernameEmpty'] = True
        error['quantity']+=1

    # make sure password isn't empty
    if len(verifyPassword) == 0:
        error['verifyPasswordEmpty'] = True
        error['quantity']+=1

    # make sure username doesn't contain space
    if ' ' in username:
        error['usernameInvalid'] = True
        error['quantity']+=1

    # make sure space isn't in password
    if ' ' in password:
        error['passwordInvalid'] = True
        error['quantity']+=1

    #make sure email isn't empty
    if len(email) == 0:
        error['emailEmpty'] = True
        error['quantity']+=1

    #make sure email contains the '@' character
    if '@' not in email:
        error['emailInvalid'] = True
        error['quantity']+=1

    if error['quantity'] == 0:
        return render_template('welcome.html',username=username,email=email)
    else:
        return render_template('main.html',error=error,username=username,email=email)

if __name__ == '__main__':
    app.run()
