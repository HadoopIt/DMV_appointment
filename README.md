DMV_appointment
===============

You probably don't want to wait for nearly a month time for the DMV driving test. This program helps to search for the earliest available DMV "behind-the-wheel driving test" in multiple DMV offices.

Say you want to search for all earliest available appointment slots within the next 10 days, set the value of 'test_in_days' to 10 at the begining of program. Enter your personal information then as if you were registering on DMV website. 

To run the program in schedule, create a simple cron job for your need, e.g. the below cron job runs the program every hour.

    1 * * * * /usr/bin/python dmv_behind-the-wheel_test.py

To save the output whenever there is an available slot, set a directory you want to place the output file to 'output_folder' variable at the top of the program. Extend the program yourself to triger an email alert via smpt server if you want!

Enjoy!
