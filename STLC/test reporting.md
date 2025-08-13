This document contains two example scenarios. Use a template that is alike for your own portfolio, but cover all the necessary scenarios! 

### Scenario 1: Valid Date of Birth

As a user of FindMate, I am able to sign up and log in when I am 16 years old.

| Step# | Action                        | Expected outcome                                                                                   | OK/NOK | URL                      | Link to issue |
|-------|-------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1     | Go to login page FindMate     | Login page appears                                                                                  | OK     | [https://findmate.masterschool.com/](https://findmate.masterschool.com/) |               |
| 2     | Click on Sign up              | You are directed to the sign up page                                                                | OK     | /auth                    |               |
| 3a    | Fill in RandomUsername        |                                                                                                     |        |                          |               |
| 3b    | Fill 18-08-2008 as Date of Birth |                                                                                                     |        |                          |               |
| 3c    | Write 'This is my Bio'        |                                                                                                     |        |                          |               |
| 3d    | Write karin@faculty.masterschool.com as e-mail address |                                                                                                     |        |                          |               |
| 3e    | Password is 'RandomPassword1' |                                                                                                     |        |                          |               |
| 4     | Click sign up                 | You are directed to the login page. The e-mail and password are filled automatically                | OK     |                          |               |
| 5     | Click on log in               | You are successfully logged in                                                                      | OK     |                          |               |

![image](https://github.com/user-attachments/assets/a593d7b6-456f-4094-9c8a-dc88f4b4ef4c)
![image](https://github.com/user-attachments/assets/4c8dafd1-dd9b-4ee7-9779-0525cade6d46)
![image](https://github.com/user-attachments/assets/2972e9bd-76fc-421f-8d4f-2d175d9a2a2d)
![image](https://github.com/user-attachments/assets/f210f720-d67f-41d7-a94e-454b1142d5c0)


### Scenario 2: Invalid Date of Birth

As a user of FindMate, I am not able to sign up when I register with an invalid Date of Birth.

| Step# | Action                               | Expected outcome                                           | OK/NOK | URL                                                | Link to issue               |
|-------|--------------------------------------|------------------------------------------------------------|--------|----------------------------------------------------|-----------------------------|
| 1     | Go to login page FindMate            | Login page appears                                         | OK     | [https://findmate.masterschool.com/](https://findmate.masterschool.com/)     |                             |
| 2     | Click on Sign up                     | You are directed to the sign up page                       | OK     | /auth                                              |                             |
| 3a    | Fill in 'InputValidationTest' as username |                                                            |        |                                                    |                             |
| 3b    | Fill 19-08-1820 as Date of Birth     |                                                            |        |                                                    |                             |
| 3c    | Write 'This is my Bio'               |                                                            |        |                                                    |                             |
| 3d    | Write karin@faculty.masterschool.com as e-mail address |                                                            |        |                                                    |                             |
| 3e    | Password is 'RandomPassword1'        |                                                            |        |                                                    |                             |
| 4     | Click sign up                        | You cannot be 200 years old, so I expect an error message  | NOK    |                                                    | [https://github.com/software-engineering-ms/example-portfolio/issues/2](https://github.com/software-engineering-ms/example-portfolio/issues/2) |

