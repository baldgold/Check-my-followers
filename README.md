# Unsubscribe search in Instagram
I created this small project for personal usе. You get a list with a user ID that have unsubscribed from you in Instagram. 

## How it works?
1. First of all we parsed profile in Instagram. We created folder with json's files with information about my followers.
   Run the "get_followers.py".

2. Next step. We start to work with json files: 
   First time we need to create "old_followers_id.txt". Why? When we run the "parse_followers.py" we create a file with user ID. This file    is needed for comparison.
   (when the program asks you to enter a value, you must enter: '1'). Then after any time (day, two, week, six months) we run this file      again and create it already "parse_followers.py". To do this, enter "2".

3. Last step: We run "check_unsub.py" and get on the console a list with all user IDs that have unsubscribed from you during the time that    has passed since the creation of "old_followers_id.txt".
 
If you want to use that spaghetti code for your Instagram account, then we need to change in "get_followers.py":
1. url_base            // 8 line
2. command_template    // 10 line
3. variables           // 32 line
4. query_has           // 34 line

You can find that information about your account if:
1. go to your instagram page
2. press f12
3. select "Headers" and copy "QUERY STRING PARAMETERS" (variables, query_has)
4. next select "XHR". press "followers" in your page and copy as cURL newly created request. (url_base, command_template)
 
That's all:)
This project was created specifically for training. 
Thanks for your attention!
