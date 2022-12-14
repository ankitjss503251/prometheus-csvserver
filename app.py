import time

import redis
from flask import Flask, render_template, request
import logging
#from werkzeug.utils 
#import inputFile
#from flask import Flask, render_template, request

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)


@app.route('/raw')
def hellos():
    count = get_hit_count()
    return 'name {} times.\n'.format(count)

@app.route('/metrics')
def main():
  # showing different logging levels
    app.logger.debug("debug log info")
    app.logger.info("Info log information")
    app.logger.warning("Warning log info")
    app.logger.error("Error log info")
    app.logger.critical("Critical log info")
    return "testing logging levels."
    return app.logger.debug
    
if __name__ == '__main__':
    app.run(debug=True)

#@app.route('/upload')
#def upload_file():
#   return render_template('inputFile')

#@app.route('/uploader', methods = ['GET', 'POST'])
#def upload_file():
#   if request.method == 'POST':
#      f = request.files['file']
#      f.save(secure_filename(f.filename))
#      return 'file uploaded successfully'
		
#if __name__ == '__main__':
#   app.run(debug = True)

#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



