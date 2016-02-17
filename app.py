from flask import Flask, redirect, g, render_template, url_for
import redis
import os

app = Flask(__name__)

DEBUG = True
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.getenv['REDIS_PORT', '6379'])

app.config.from_object(__name__)


def connect_db():
	return redis.Redis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])


@app.before_request
def before_request():
	g.db = connect_db()


@app.route('/')
def index():
	count = g.db.get('counter')
	return render_template('index.html', count=int(count))


@app.route('/count', methods=['POST'])
def count_with_redis():
	g.db.incr(name='counter')
	return redirect(url_for('index'))


if __name__ == '__main__':
	app.run()
