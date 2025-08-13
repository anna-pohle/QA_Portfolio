
**Design your test cases, based on the features that will be developed for the upcoming release of the social medai website!**

**You only have to *design* them, the execution will happen in a later phase.**

**Add the test design technique, if applicable.**

### **1. Age Restriction for Account Creation**

**Test Design Techniques**: Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Error Guessing

### Test Cases:

1. **Boundary Value Analysis**:
    - **Test Case**: Verify account creation for a user exactly 16 years old.
        - **Input**: Date of Birth = (Today - 16 years)
        - **Expected Outcome**: Account creation successful.
2. **Boundary Value Analysis**:
    - **Test Case**: Verify account creation for a user just below 16 years old.
        - **Input**: Date of Birth = (Today - 16 years + 1 day)
        - **Expected Outcome**: Error message "You must be at least 16 years old to create an account."
3. **Equivalence Partitioning**:
    - **Test Case**: Verify account creation for users below the age of 16.
        - **Input**: Date of Birth = (Today - 15 years)
        - **Expected Outcome**: Error message displayed.
4. **Equivalence Partitioning**:
    - **Test Case**: Verify account creation for users above the age of 16.
        - **Input**: Date of Birth = (Today - 17 years)
        - **Expected Outcome**: Account creation successful.
5. **Error Guessing**:
    - **Test Case**: Verify system behavior when Date of Birth is not entered.
        - **Input**: Date of Birth field left empty.
        - **Expected Outcome**: Error message "Date of Birth is required."
6. **Error Guessing**:
    - **Test Case**: Verify system behavior when an invalid Date of Birth format is entered.
        - **Input**: Date of Birth = "13/25/2008"
        - **Expected Outcome**: Error message "Invalid Date of Birth format. Please use MM/DD/YYYY."

### **2. Paid Subscription to Remove Ads**

**Test Design Techniques**: Use Case Testing, Boundary Value Analysis (BVA), Error Guessing

### Test Cases:

1. **Use Case Testing**:
    - **Test Case**: Verify the option to subscribe to a paid plan is present in account settings.
        - **Input**: Navigate to account settings.
        - **Expected Outcome**: Subscription option is visible.
2. **Boundary Value Analysis**:
    - **Test Case**: Verify successful subscription with valid payment details.
        - **Input**: Valid credit card details.
        - **Expected Outcome**: Subscription successful, ads are disabled.
3. **Error Guessing**:
    - **Test Case**: Verify system behavior when payment fails.
        - **Input**: Invalid credit card details.
        - **Expected Outcome**: Error message "Payment failed. Please try again."
4. **Use Case Testing**:
    - **Test Case**: Verify system behavior on subscription renewal.
        - **Input**: Subscription renewal date reached with valid payment details.
        - **Expected Outcome**: Subscription renewed, ads remain disabled.
5. **Error Guessing**:
    - **Test Case**: Verify system behavior on subscription cancellation.
        - **Input**: Cancel subscription.
        - **Expected Outcome**: Subscription canceled, ads are displayed again.
6. **Use Case Testing:**
    - **Test Case**: Verify that the paid plan option is available during the registration process.
        - **Input**: Fill in all required registration details, navigate to the subscription option.
        - **Expected Outcome:** The option to subscribe to the paid plan should be visible during the registration process. The user should be able to select the paid plan and proceed with payment details. Upon successful payment, the user account should be created, and ads should be disabled.

### **3. Profile Story**

**Test Design Techniques**: Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Error Guessing

### Test Cases:

1. **Boundary Value Analysis**:
    - **Test Case**: Verify the profile story with exactly 100 characters.
        - **Input**: Enter a story with 100 characters.
        - **Expected Outcome**: Story saved successfully and displayed under the account name.
2. **Boundary Value Analysis**:
    - **Test Case**: Verify the profile story with more than 100 characters.
        - **Input**: Enter a story with 101 characters.
        - **Expected Outcome**: Error message "Profile story cannot exceed 100 characters."
3. **Equivalence Partitioning**:
    - **Test Case**: Verify the profile story with less than 100 characters.
        - **Input**: Enter a story with 50 characters.
        - **Expected Outcome**: Story saved successfully and displayed under the account name.
4. **Error Guessing**:
    - **Test Case**: Verify the profile story with no input.
        - **Input**: Leave the story field empty.
        - **Expected Outcome**: Story saved successfully (if empty story is allowed).
5. **Error Guessing**:
    - **Test Case**: Verify the profile story with invalid characters or profanity.
        - **Input**: Enter a story with prohibited words.
        - **Expected Outcome**: Error message "Profile story contains prohibited content."
6. **Use Case Testing**:
    - **Test Case**: Verify that the profile story is aligned and visible below the account name on the profile page.
        - **Input**: Navigate to the user's profile page.
        - **Expected Outcome**: The profile story should be displayed directly below the account name, properly aligned and fully visible.
7. **Use Case Testing**:
    - **Test Case**: Verify that the profile story is visible to registered users.
        - **Input**: A registered user navigates to the profile page of the user with the story.
        - **Expected Outcome**: The registered user should be able to see the profile story below the account name on the profile page.
8. **Use Case Testing**:
    - **Test Case**: Verify that the profile story is not visible to unregistered users.
        - **Input**: An unregistered user navigates to the profile page of the user with the story.
        - **Expected Outcome**: The profile story should not be visible to the unregistered user; it may be hidden or replaced with a message prompting the user to log in to view the content.
9. **Boundary Value Analysis (Input Validation)**:
    - **Test Case**: Verify the system's behavior when the profile story field is left empty.
        - **Input**: Leave the profile story input field empty and attempt to save.
        - **Expected Outcome**: The system should either allow saving an empty story (if allowed) or display an error message indicating that the profile story cannot be empty.
10. **Use Case Testing (Session Expiry)**:
    - **Test Case**: Verify the system's behavior when the user is editing their bio and the session expires.
        - **Input**: Let the session expire while editing the profile story, then log back in.
        - **Expected Outcome**: The system should not save the changes made during the expired session. Upon logging back in, the user should see the profile story in its state before the session expired, and any unsaved changes should be lost.
