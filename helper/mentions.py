from helper.usefulcomponents import Components
from src.aireplier import ai
from src.forbiddenletter import forbiddenletter

def mentionuser(reddit, key):
    components = Components(reddit)
    new_mentions = components.new_mentions()
    error_reply = "an error occurred. doesn't seem right? report it [here](https://github.com/neeeerrd/h-bot10000)"
    for mention in new_mentions:
        if "u/h-bot10000 !forbiddenLetter" in mention.body:
            forbiddencount = 0
            if "/u/h-bot10000" in mention.body:
                username = mention.body.replace("/u/h-bot10000 !forbiddenLetter ", "")
            elif "u/h-bot10000" in mention.body:
                username = mention.body.replace("u/h-bot10000 !forbiddenLetter ", "")
            if "/u/" in username:
                username = username.replace("/u/", "")
            elif "u/" in username:
                username = username.replace("u/", "")
            try:
                reply = forbiddenletter(reddit, username)
                mention.reply(reply)
            except:
                mention.reply(error_reply)
        elif "u/h-bot10000 !betaAi" in mention.body:
            if "/u/h-bot10000" in mention.body:
                prompt = mention.body.replace("/u/h-bot10000 !betaAi ", "")
            elif "u/h-bot10000" in mention.body:
                prompt = mention.body.replace("/u/h-bot10000 !betaAi ", "")
            try:
                reply = ai(prompt, key, mention.author)
                mention.reply(reply)
            except:
                mention.reply(error_reply)
        else:
            mention.reply("h")
