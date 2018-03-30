from app import app
from flask import send_file
import os

@app.route("/up")
def hello():
    return "Up!"

@app.route("/")
def main():
    log_route("/")
    index_path = os.path.join(app.static_folder, 'index.html')
    return send_file(index_path)

@app.route("/<path:path>")
def route_frontend(path):
    file_path = os.path.join(app.static_folder, path)
    if os.path.isfile(file_path):
        log_route(path)
        return send_file(file_path)
    else:
        route_error(path)
        index_path = os.path.join(app.static_folder, 'index.html')
        return send_file(index_path)

def log_route(route):
    return app.logger.info('route hit: ' + route)

def route_error(route):
    return app.logger.error('route error: ' + route + ' not found')

app.logger.info('refreshing...')


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)