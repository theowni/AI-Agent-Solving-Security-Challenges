# Level 2 - Unrestricted Profile Update (IDOR)

## Description
The application suffered from an Insecure Direct Object Reference (IDOR) vulnerability in the profile update functionality. This vulnerability allowed any authenticated user to update any other user's profile information by manipulating the request to the `update_profile` endpoint. This security flaw arises when the application does not verify that the user making the request has the authority to update the intended profile.

## Business Impact
The IDOR vulnerability impacted the restaurant's application by exposing user profiles to unauthorized modifications. Malicious actors could leverage this flaw to alter sensitive user information such as names, email addresses, and contact details without consent, leading to potential data breaches, privacy violations, and loss of customer trust in the restaurant's brand.

## Steps to fix the vulnerability
1. Modified the `update_profile` function within `app/apis/auth/services/update_profile_service.py` to include a verification step that compares the current authenticated user with the `username` specified in the API request for updating a profile.
2. Implemented a logic that checks if the `username` in the request matches the current user's username. If they do not match, the application raises a `403 Forbidden` error, ensuring that users can only update their own profiles.