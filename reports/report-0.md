# Level 1 - Technology Exposure via HTTP Headers

## Description
The application was exposing its underlying technology details through the "X-Powered-By" HTTP header in the response from the `/healthcheck` endpoint. This can give potential attackers insights into the technologies being used, which can be leveraged for further attacks.

## Business Impact
Exposing technology stack information via HTTP headers can aid attackers in crafting targeted attacks against the restaurant's application. Knowing the specific technologies can allow attackers to exploit known vulnerabilities specific to those technologies, leading to unauthorized access, data breaches, or service disruptions.

## Steps to fix the vulnerability
1. Locate the `service.py` file within the `app/apis/healthcheck` directory.
2. Identify the line of code that is setting the "X-Powered-By" HTTP header.
3. Remove or comment out the line setting this header to ensure it is not included in the HTTP response.
4. Test the `/healthcheck` endpoint to verify that the "X-Powered-By" header is no longer present in the response.

These steps mitigate the risk by not disclosing unnecessary technology information, thus reducing the application's attack surface.