from bottle import Bottle, run, static_file

app = Bottle()

@app.route('/')
def index():
    return static_file('index.html', root='.')

@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

if __name__ == "__main__":
    run(app, host='localhost', port=8080)
