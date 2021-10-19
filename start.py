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

    ip_data_req = requests.get(f"http://ip-api.com/json/{ip.split(',')[0]}")

    if 300 > ip_data_req.status_code >= 200:
        try:
            ip_data = ip_data_req.json()
        except:
            ip_data = False
    else:
        ip_data = False

    write_file_data = f"""\n\n------------------------\n\nEMAIL-OPENED: {datetime.now()}:
IP - {ip.split(',')[0]}
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
        write_file_data += f"\nIP Info -"
        try:
            write_file_data += f"""    IP: {ip.split(',')[0]}"""
        except:
            # write_file_data += f"""    DAMN! Somthing is really wrong!"""
            pass

        try:
            write_file_data += f"""    Country: {ip_data["country"]}"""
        except:
            # write_file_data += f"""    Country: Error"""
            pass

        try:
            write_file_data += f"""    Country Code: {ip_data["countryCode"]}"""
        except:
            # write_file_data += f"""    Country Code: Error"""
            pass

        try:
            # write_file_data +=
            write_file_data += f"""    Region: {ip_data["region"]}"""
        except:
            # write_file_data += f"""    Region: Error"""
            pass

        try:
            write_file_data += f"""    Region Name: {ip_data["regionName"]}"""
        except:
            # write_file_data += f"""    Region Name: Error"""
            pass

        try:
            write_file_data += f"""    City: {ip_data["city"]}"""
        except:
            # write_file_data += f"""    City: Error"""
            pass

        try:
            write_file_data += f"""    ZIP: {ip_data["zip"]}"""
        except:
            # write_file_data += f"""    ZIP: Error"""
            pass

        try:
            write_file_data += f"""    Latitude: {ip_data["lat"]}"""
        except:
            # write_file_data += f"""    Latitude: Error"""
            pass

        try:
            write_file_data += f"""    Longitude: {ip_data["lon"]}"""
        except:
            # write_file_data += f"""    Longitude: Error"""
            pass

        try:
            write_file_data += f"""    TimeZone: {ip_data["timezone"]}"""
        except:
            # write_file_data += f"""    TimeZone: Error"""
            pass

        try:
            write_file_data += f"""    ISP: {ip_data["isp"]}"""
        except:
            # write_file_data += f"""    ISP: Error"""
            pass

        try:
            write_file_data += f"""    Organization: {ip_data["org"]}"""
        except:
            # write_file_data += f"""    Organization: Error"""
            pass

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
    app.run(host="0.0.0.0", port=8090, debug=False)
