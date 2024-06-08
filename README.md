# Email Open Tracker with Flask

This project sets up a Flask web server that logs when an email containing a specific image is opened. The log captures details such as the IP address, user agent information, and geolocation data based on the IP address.

## Requirements

- Python 3.x
- pip (or pip3 depending on your system)

## Installation

1. Clone the repository or download the project files.

2. Install the required Python packages. You can use the provided `pip_install` function in the code, or manually run:

   ```sh
   pip install flask user_agents requests
   ```

## Running the Server

To run the server, execute the following command in your terminal:

```sh
python app.py
```

By default, the server will run on `http://0.0.0.0:8090`.

## How It Works

1. **Logging Email Opens**:
    - When an image is requested from the server, the `log_open_mail` function is called.
    - The function parses the user agent and IP address from the request headers.
    - Geolocation data is fetched based on the IP address using the `ip-api.com` service.
    - All the information is logged in a file named `log.txt`.

2. **Serving Images**:
    - The server looks for images with extensions `.png`, `.jpg`, and `.jpeg` in the current directory.
    - If images are found, one is randomly selected and served.
    - If no images are found, a 404 error is returned.

## File Structure

- `app.py`: Main application file containing the Flask server and logging functionality.
- `log.txt`: Log file where the details of email opens are recorded (created automatically).

## Endpoint

- `/`: The root endpoint serves a random image from the current directory and logs the email open event.

## Notes

- Ensure you have images in the current directory where the script is running, or the server will return a 404 error.
- The logging function makes a network request to `ip-api.com` for geolocation data, which may have rate limits. Handle exceptions accordingly.
- Modify the port and host as necessary by changing the parameters in `app.run()`.

## Example Log Entry

```
------------------------

EMAIL-OPENED: 2024-06-08 12:34:56:
IP - 192.168.1.1
Browser -
    Family: Chrome
    Version: 91.0.4472.124
OS -
    Family: Windows
    Version: 10
Device -
    Family: Desktop
    Model: N/A
    Brand: N/A
IP Info -
    Country: United States
    Country Code: US
    Region: CA
    Region Name: California
    City: Mountain View
    ZIP: 94043
    Latitude: 37.422
    Longitude: -122.084
    TimeZone: America/Los_Angeles
    ISP: Google LLC
    Organization: Google
```

## Additional Configuration

### Caching

To disable caching, the `add_header` function sets the `Cache-Control` header to `max-age=0`.

## Security Considerations

- Ensure the server is properly secured if deployed to a production environment.
- Consider using environment variables for sensitive configurations.
- Use HTTPS to encrypt data transmitted between the server and clients.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any improvements or bug fixes.


This file was generated with ChatGPT on `6/8/2024`