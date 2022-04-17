from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'Keep it to yourselves, no one else should know'


@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template("index.html")


@app.route("/count", methods=["POST"])
def count():
    print("Got Post Info")
    print(request.form)
    if request.form["counter"] == "add":
        session['count'] += 1
        return redirect('/')

    elif request.form["counter"] == "reset":
        return redirect('destroy_session')


@app.route('/destroy_session')
def destroy():
    session.clear()
    session['count'] = 0
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
