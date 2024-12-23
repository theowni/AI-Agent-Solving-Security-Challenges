# Level 1 - Unrestricted Menu Item Deletion
## Description
The "Unrestricted Menu Item Deletion" vulnerability allowed any user, regardless of their role, to delete menu items from the restaurant's menu. This was due to a missing authorization check in the `delete_menu_item_service.py` file.

## Business Impact
Allowing unauthorized users to delete menu items can lead to significant disruptions in the restaurant's operations. It could result in loss of critical menu data and potential financial loss if malicious users remove popular or important menu items.

## Steps to fix the vulnerability
1. Open the `delete_menu_item_service.py` file.
2. Identify the authorization dependency that was originally commented out.
3. Uncomment and activate the authorization dependency to ensure that only users with specific roles (such as "EMPLOYEE" or "CHEF") can delete menu items.
4. Verify the fix using the ChallengeStatusReader tool, ensuring that unauthorized users can no longer delete menu items and that progression to the next challenge level is confirmed.
