from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = '''
<!DOCTYPE html>
<html>
    <body>
        <h1>%s</h1>
        <form action="" autocomplete"on">
            <fieldset>
                <legend>Sign Up</legend>
                Username:<br>
                <input type="text" name="username">
                <br>
                Password:<br>
                <input type="password" name="password" autocomplete"off">
                <br>
                Verify Password:<br>
                <input type="text" name="verifypassword" autocomplete"off">
                <br>
                Email(optional):<br>
                <input type="text" name="email">
                <br><br>
                <input type="submit">
            </fieldset>
        </form>
    </body>
</html>
'''

@app.route("/", methods=['GET'])
def index():
    return form % ''

@app.route("/", methods=['POST'])
def validateUser():
    # save form inputs to variables
    username = request.form['username']
    password = request.form['password']
    verifyPassword = request.form['verifypassword']
    email = request.form['email']
    failureMessage = ''

    # log those variables for debugging
    app.logger.info('%s username',username)
    app.logger.info('%s password',password)
    app.logger.info('%s verifyPassword',verifyPassword)
    app.logger.info('%s email',email)

    # validate that verify password & password are the same
    if str(password) == str(verifypassword):
        return '<h1>Welcome %s</h1>' % username
    else:
        return form % failureMessage
    #TODO megan do conditional statements here and alter
    # the filureMessage if something is wrong, if the failure
    #message is empty then return success; otherwise, send
    #them back to the page with the failuremessage on the form
    if len(failureMessage):
      return form % failureMessage
    else:
      return '<h1>Welcome %s</h1>' % username

    app.run()

