# u/TheThornBot
þe original þ bot on r/TheLetterThorn
# How-To Guide
1. Go to https://old.reddit.com/prefs/apps
2. Scroll to þe bottom and click "are you a developer? create a new app"
3. Set þe bot type to script and set þe name to whatever you want
4. Create þe app
5. Write down þe client ID (the long string of text underneaþ þe bots name and type), and þe bot secret
6. Download þis bot by using git or by downloading the zip file
7. In þe bot's code's folder, make a file called .env and make þis þe contents:
```
SECRET="your secret here"
ID="your client id here"
USERNAME="your account's username here"
PASSWORD="your account's password here"
```
8. Install Pyþon if not installed, and þen open up "Command Prompt" for Windows or "Terminal" for mac and run
```python
pip3 install poetry==1.5.1
poetry install
poetry run python3 index.py
```
