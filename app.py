from ast import keyword
from timeit import default_timer
from flask import Flask, render_template, request, jsonify
import pyodbc
from server import *
import pickle

app = Flask(__name__)
# CORS(app)

class Main():
    cursor = ''
    data = ''
    @app.route('/', methods=['GET', 'POST'])
    def index():
        end_time = 0
        type = ''
        start_time = 0
        cache_end_time = 0
        cache_start_time = 0
        cursor = connect_db()
        redis = connect_redis()
        if request.method == 'POST':
            print(request.form)
            if 'without-cache' in request.form:
                start_time = default_timer()
                index = 0
                for i in range(1000):
                    index += 1
                    cursor.execute("SELECT * FROM ds2")
                    data = cursor.fetchall()
                    if redis.get('ds2-all') is None:
                        redis.set('ds2-all', pickle.dumps(data))
                    if index % 100 == 0:
                        print(index)
                end_time = default_timer()
            elif 'with-cache' in request.form:
                cache_start_time = default_timer()
                index = 0
                for i in range(1000):
                    index += 1
                    if redis.get('ds2-all') is not None:
                        data = redis.get('ds2-all')
                    else:
                        cursor.execute("SELECT * FROM ds2")
                        data = cursor.fetchall()
                        redis.set('ds2-all', pickle.dumps(data))
                    if index % 100 == 0:
                        print(index)
                cache_end_time = default_timer()
                
        return render_template('index.html', cache_time=cache_end_time - cache_start_time, no_cache_time=end_time - start_time)
        


   

if __name__ == "__main__":

  app.logger.debug("Loading ")

  app.run(
    host='0.0.0.0', 
    port=9001)

        
    

