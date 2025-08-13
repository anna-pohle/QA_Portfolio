## **The software**

Social media platform, with the following existing functionalities:

- Register and login functionality
- Add pictures to your profile
- Find friends
- Add friends to favorites
- Social media platform had ads

## **New features**

### **1. Age Restriction for Account Creation**

**Vague Requirement**:

- Users should only be able to create an account if they meet the minimum age requirement of 16 years.

**Questions**:

1. How should the age verification be implemented? (e.g., date of birth input)
2. What format should the date of birth be in? (e.g., MM/DD/YYYY)
3. What error message should be displayed if the user is under 16?
4. Are there any specific legal disclaimers or privacy notices required for age verification?

**Detailed Requirement**:

- During the registration process, users must provide their date of birth. The system should validate that the user is at least 16 years old on the date of account creation. If the user is under 16, an error message should be displayed, and the account should not be created.

### **2. Paid Subscription to Remove Ads**

**Vague Requirement**:

- There should be an option for users to subscribe to a paid plan that allows them to use the platform without seeing any advertisements.

**Questions**:

1. Where should the option to subscribe to the paid plan be located? (e.g., account settings, homepage)
2. What payment methods will be supported?
3. What should happen if the payment fails?
4. How should the system handle subscription renewals and cancellations?
5. What pricing tiers will be offered for the subscription?

**Detailed Requirement**:

- Users should have an option in their account settings to subscribe to a premium plan. Upon successful subscription and payment, advertisements should not be disabled across all areas of the platform. The system should also manage the subscription status, renewal reminders, and handle scenarios when the subscription expires or is canceled.

### **3. Profile Story**

**Vague Requirement**:

- Users should have the ability to write a brief story about themselves, which will be displayed under their account name on their profile. This story should have a character limit.

**Questions**:

1. Where should the input field for the profile story be located?
2. Should there be any formatting options (e.g., bold, italic)?
3. What should happen if the user exceeds the character limit? (e.g., error message, truncated text)
4. Are there any restrictions on the content of the story (e.g., profanity filter)?

**Detailed Requirement**:

- Users should have an input field in their profile settings where they can enter a personal story or bio. This field should allow a maximum of 100 characters. The story should be displayed below the account name on the user's profile page. The system should provide feedback if the user attempts to enter more than 100 characters, preventing them from saving the excess characters. For the MVP there will be no profanity filter, this will be implemented later.
