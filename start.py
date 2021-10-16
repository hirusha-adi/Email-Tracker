import os
import platform
from datetime import datetime

try:
    from flask import Flask, request, send_from_directory
except:
    if platform.system().lower().startswith('win'):
        os.system("pip install flask")
    else:
        os.system("pip3 install flask")
    from flask import Flask, request, send_from_directory

try:
    from user_agents import parse
except:
    if platform.system().lower().startswith('win'):
        os.system("pip install flask")
    else:
        os.system("pip3 install flask")
    from user_agents import parse


app = Flask(__name__)


def log_open_mail():
    # User Info
    ua = parse(request.headers.get("User-Agent"))
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    browser = f"{ua.browser.family} {ua.browser.version_string}"
    os = f"{ua.os.family} {ua.os.version_string}"
    print(f"{datetime.now()}: email opened in {browser} on {os} ({ip})")


@app.route('/')
def index():
    log_open_mail()
    return send_from_directory(".", "1.png")


@app.after_request
def add_header(response):
    response.cache_control.max_age = 0
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0")
