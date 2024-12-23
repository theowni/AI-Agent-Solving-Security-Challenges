# Level 4 - Server-Side Request Forgery (SSRF) Vulnerability

## Description
Server-Side Request Forgery (SSRF) is a web security vulnerability that allows an attacker to induce the server-side application to make HTTP requests to an unintended destination. In this scenario, the `_image_url_to_base64` function in the "app/apis/menu/utils.py" file was vulnerable to SSRF. Attackers could exploit this by providing malicious URLs that the server would fetch, potentially accessing internal services or mounted files.

## Business Impact
The SSRF vulnerability could have significant impact on the restaurant's business, including exposing sensitive internal endpoints, unauthorized access to internal services, and potential information leakage. This could result in data breaches, loss of customer trust, and legal compliance issues, all of which could harm the restaurant's reputation and financial standing.

## Steps to fix the vulnerability
1. **Implement Domain Validation**
   - A whitelist of allowed domains was created, and the `_image_url_to_base64` function was modified to only allow HTTP requests to the domains present in this whitelist. This prevents the server from accessing unintended or malicious external URLs.

2. **Restrict Content Types**
   - Before processing the response from an HTTP request, the `Content-Type` header is checked to ensure it is an image MIME type. This ensures that even if an attacker manages to direct a request to a whitelisted domain, only image data will be processed, reducing the risk of executing malicious content.

These changes successfully mitigate the SSRF vulnerability by ensuring that the application only fetches and processes images from trusted domains, thus securing the application from this class of attack.