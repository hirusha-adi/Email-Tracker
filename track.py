import os
import random
from datetime import datetime


def pip_install(module_name):
    os.system(f"{'pip' if os.name == 'nt' else 'pip3'} install {module_name}")

try:
    from flask import Flask, request, send_from_directory
except:
    pip_install("flask")
    from flask import Flask, request, send_from_directory

try:
    from user_agents import parse
except:
    pip_install("user_agents")
    from user_agents import parse

try:
    import requests
except:
    pip_install("requests")
    import requests


app = Flask(__name__)


def log_open_mail():
    ua = parse(request.headers.get("User-Agent"))
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    print(f"EMAIL-OPENED: {ip}")

    try:
        ip_data = requests.get(f"http://ip-api.com/json/{ip.split(',')[0]}").json()
    except requests.RequestException:
        ip_data = {}

    write_file_data = f"""
    \n\n------------------------\n\nEMAIL-OPENED: {datetime.now()}:
    IP - {ip}
    Browser -
        Family: {ua.browser.family}
        Version: {ua.browser.version_string}
    OS -
        Family: {ua.os.family}
        Version: {ua.os.version_string}
    Device -
        Family: {ua.device.family}
        Model: {ua.device.model}
        Brand: {ua.device.brand}"""

    if ip_data:
        write_file_data += f"""
        IP Info -
        Country: {ip_data.get('country', 'N/A')}
        Country Code: {ip_data.get('countryCode', 'N/A')}
        Region: {ip_data.get('region', 'N/A')}
        Region Name: {ip_data.get('regionName', 'N/A')}
        City: {ip_data.get('city', 'N/A')}
        ZIP: {ip_data.get('zip', 'N/A')}
        Latitude: {ip_data.get('lat', 'N/A')}
        Longitude: {ip_data.get('lon', 'N/A')}
        TimeZone: {ip_data.get('timezone', 'N/A')}
        ISP: {ip_data.get('isp', 'N/A')}
        Organization: {ip_data.get('org', 'N/A')}
        """

    print(write_file_data)

    if not ("log.txt" in os.listdir(os.getcwd())):
        with open("log.txt", "w") as fm1:
            fm1.write(f"\nINFO: {datetime.now()} - Log file created!\n")

    with open("log.txt", "a", encoding="utf-8") as logw:
        logw.write(write_file_data)


@ app.route('/')
def index():
    log_open_mail()
    filenames = []
    images = [f for f in os.listdir(os.getcwd()) if f.lower().endswith(('png', 'jpg', 'jpeg'))]
    if not images:
        return "No images found", 404
    return send_from_directory(".", f"{random.choice(filenames)}")


# Im not very confident about this
@ app.after_request
def add_header(response):
    response.cache_control.max_age = 0
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=False)
