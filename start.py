import os
import platform
import random
from datetime import datetime


def pip_install(module_name):
    if platform.system().lower().startswith('win'):
        os.system(f"pip install {module_name}")
    else:
        os.system(f"pip3 install {module_name}")


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

    ip_data_req = requests.get(f"http://ip-api.com/json/{ip}").json()

    if 300 > ip_data_req.status_code >= 200:
        try:
            ip_data = ip_data_req.json()
        except:
            ip_data = False
    else:
        ip_data = False

    write_file_data = f"""\n\n------------------------\n\nEMAIL-OPENED: {datetime.now()}:
IP - {ip}
Broswer -
    Family: {ua.browser.family}
    Version: {ua.browser.version_string}
OS -
    Family: {ua.os.family}
    Version: {ua.os.version_string}
Device -
    Family: {ua.device.family}
    Model: {ua.device.model}
    Brand: {ua.device.brand}"""

    if ip_data == False:
        pass
    else:
        write_file_data += f"""
IP Info -
    IP: {ip}
    Country: {ip_data["country"]}
    Country Code: {ip_data["countryCode"]}
    Region: {ip_data["region"]}
    Region Name: {ip_data["regionName"]}
    City: {ip_data["city"]}
    ZIP: {ip_data["zip"]}
    Latitude: {ip_data["lat"]}
    Longitude: {ip_data["lon"]}
    TimeZone: {ip_data["timezone"]}
    ISP: {ip_data["isp"]}
    Organization: {ip_data["org"]}
    ASN: {ip_data["ASN"]}
    Organization: {ip_data["org"]}
"""
    if not ("log.txt" in os.listdir(os.getcwd())):
        with open("log.txt", "w") as fm1:
            fm1.write(f"\nINFO: {datetime.now()} - Log file created!\n")

    with open("log.txt", "a", encoding="utf-8") as logw:
        logw.write(write_file_data)


@ app.route('/')
def index():
    log_open_mail()
    filenames = []
    for filename in os.listdir(os.getcwd()):
        if filename.lower().endswith('png') or filename.lower().endswith('jpg') or filename.lower().endswith('jpeg'):
            filenames.append(filename)
    rfilename = random.choice(filenames)
    return send_from_directory(".", f"{rfilename}")


# Im not very confident about this
@ app.after_request
def add_header(response):
    response.cache_control.max_age = 0
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
