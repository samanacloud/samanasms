# Samana SMS forwarder for Slack
This tool will accept Webhook requests from Vonage(Nexmo) for SMS messages sent to phone numbers.
The tool requires two configuration files.
* `vars.env` where Nexmo and Slack keys must be configured. A template (vars.env.template) has been provided as a starting point
* `numbermaps.json` where the mapping of phone numbers and slack ids are defined. This file is a JSON file with a single object; each key in the object is the phone number and the value is the user id in Slack

# Install
To install this application, a docker-compose.yaml file has been provided. To start the application, just create the configuration files described in the previous section and run:
```
docker compose up
```
The application will be exposed on using `http` protocol on port 5000.

# Firewall
It is important to restrict access to the API from the Internet. Because of this, it is very important to setup a firewall in front of the API to restrict access only from Nexmo IP addresses. The list of addresses can be found here:

[Nexmo API IP addresses](https://api.support.vonage.com/hc/en-us/articles/16567926552860-Which-IP-addresses-should-I-allow-for-the-Vonage-messaging-related-API-services)

