from flask import Flask, redirect

app = Flask('app')


@app.route('/')
def hello_world():
    return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


app.run(host='0.0.0.0', port=81)
