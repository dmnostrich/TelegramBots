# Cyber Security News Bot

## Steps
1. Open Telegram > Search "BotFather"
```
## Command for BotFather
- /start
- /newbot
- NewBotNameHere
- NewUserNameForBot
## Then note the HTTP API Key which you will get as response
```
2. Create a telegram channel and add your bot as admin
3. Copy manual or automated script into any linux from this repository, add your own tokens
4. execute the script and check updates on telegram channel

##### Python Virtual Environment Creation
```
sudo apt install python3-venv
python3 -m venv myenv #Creation
source myenv/bin/activate #Activation
```
##### Requirements
```
pip install python-telegram-bot requests feedparser schedule
```
