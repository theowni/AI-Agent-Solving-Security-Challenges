# Level 3 - Privilege Escalation

## Description
The application had a privilege escalation vulnerability in the `update_user_role` function. Users with insufficient privileges were able to change roles and assign themselves or others roles they were not authorized to assign. This vulnerability arose due to missing role validation checks, allowing any user to escalate privileges or assign roles inappropriate for their current access level.

## Business Impact
Such a vulnerability could have severe business repercussions for the restaurant. Unauthorized users might gain elevated access, potentially accessing sensitive information, altering critical data, and impersonating roles like Chefs or Managers. This could disrupt operations and compromise data integrity and confidentiality, leading to reputational damage and loss of customer trust.

## Steps to fix the vulnerability
1. Navigate to the file `update_user_role_service.py` located at `/home/theowni/Damn-Vulnerable-RESTaurant-API-Game/app/apis/users/services`.
2. Add a validation check to restrict role assignment operations only to users with sufficient privileges (Employee or Chef roles).
3. Incorporate the following code to enforce the above restriction:
    ```python
    # Add restriction for assigning the Employee role
    if user.role == models.UserRole.EMPLOYEE.value and current_user.role not in [models.UserRole.EMPLOYEE.value, models.UserRole.CHEF.value]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only Employees or the Chef can assign Employee role!",
        )
    ```
4. This code ensures that only users with the appropriate role can assign Employee roles, effectively preventing unauthorized privilege escalation.