# Email-Tracker

Find if someone opens your email easily! You can also use this to grab other's IP Addresses.Works with both IPv4 and IPv6.

Logs -

- Time
- IP Address
- Addition information on the found IP Address
- Broswer Family
- Broswer Version
- OS Family
- OS Version
- Device Family (Mobile only)
- Device Model (Mobile only)
- Device Brand (Mobile only)

# Usage

Any `.png`, `.jpg`, `.jpeg` in the current dirctory will be returned. If there are many, an image will be selected randomly.

You need to host it somewhere (i recommend using ngrok) to host the `start.py` and some images, then you need to the copy the url of the website and add it as an image to your email. Once he/she opens the email, a request will be sent to the image so we can capture the needed data. If the victim is using Gmail (on the webbrowser), the Operating System (OS) information will not be very accurate!

# Credits

Thank you `ᴏʟɪᴠᴇʀ#8903` for giving me the idea!
