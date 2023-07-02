# h-bot10000
a bot to reply to all comments from a user on a specific subreddit
(in my case, its u/h-bot9000 on r/theletterh)
supply your own information in .env (client id, secret, username, password)
# extremely detailed how-to guide
1. go to https://old.reddit.com/prefs/apps
2. scroll to the bottom and click "are you a developer? create a new app"
3. set the bot type to script and set the name to whatever you want
4. create the app
5. write down the client id (the long string of text underneath the bots name and type), and the bot secret
6. download this bot by using git or by downloading the zip file
7. in the bot's code's folder, make a file called .env and make this the contents:
```
SECRET=(your secret in quotation marks)
ID=(your client id in quotation marks)
USERNAME=(your account's username in quotation marks)
PASSWORD=(your account's password in quotation marks)
```
8. install python if not installed, and then open up command prompt for windows or terminal for mac and run
```python
pip3 install -r requirements.txt
python3 index.py
```
9. if it is successful, the terminal should not show anything. dont worry! the bot is already running.
10. if you do not plan on deploying the bot to https://fly.io/, then you can delete the .dockerignore, swapenable.sh and fly.toml files. otherwise, you can just run the command 
```
fly deploy
```
to deploy the bot to https://fly.io/.