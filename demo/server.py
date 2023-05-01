from flask import Flask, render_template
from script import *
from api_script import *

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/movie.html')
def movie():
    return render_template('movie.html', imdb_head_lines=imdb_head_lines)


@app.route('/game.html')
def game():
    return render_template('game.html', game_head_lines=game_head_lines)


@app.route('/tech.html')
def tech():
    return render_template('tech.html', tech_head_lines=tech_head_lines)


@app.route('/economy.html')
def economy():
    return render_template('economy.html', economy_head_lines=economy_head_lines)


@app.route('/cricket.html')
def cricket():
    return render_template('cricket.html', cricket_head_lines=cricket_head_lines)


@app.route('/bbc.html')
def bbc():
    return render_template('bbc.html', bbc_headline=bbc_headline)


@app.route('/cnn.html')
def cnn():
    return render_template('cnn.html', cnn_headline=cnn_headline)


@app.route('/bloomberg.html')
def bloomberg():
    return render_template('bloomberg.html', bloomberg_headline=bloomberg_headline)


@app.route('/wallstreet.html')
def wallstreet():
    return render_template('wallstreet.html', wallstreet_headline=wallstreet_headline)


@app.route('/reuters.html')
def reuters():
    return render_template('reuters.html', reuters_headline=reuters_headline)


if __name__ == '__main__':
    app.run(debug=True)
