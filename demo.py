from highrise import BaseBot, User, SessionMetadata
from highrise.models import SessionMetadata, User, Item, Position
import random


# Initialize the array of OffenseProof
OffenseProof = [['!!!!!', 1], ['@@@@', 1], ['$$$$$', 1], ['####', 1]]

class Bot(BaseBot):

    async def on_start(self, session_metadata: SessionMetadata) -> None:
        await self.highrise.walk_to(Position(15,6.75,4,"FrontRight"))

        pass

    username_to_id = {}
    async def on_user_join(self, user: User) -> None:
        self.username_to_id[user.username] = user.id
        await self.highrise.chat(f"welcome to HOME, @{user.username}!")
        
    async def on_chat(self, user: User, message: str) -> None:  
        """if message.startswith("/cloud1"):
            await self.highrise.teleport(user.id, Position(12,20,1.5,"FrontRight"))
        if message.startswith("/cloud2"):
            await self.highrise.teleport(user.id, Position(13,20,2,"FrontLeft"))
        if message.startswith("/rain1"):
            await self.highrise.teleport(user.id, Position(12,15.5,2,"FrontRight"))
        if message.startswith("/rain2"):
            await self.highrise.teleport(user.id, Position(13,15.5,3,"FrontLeft"))
        if message.startswith("/back"):
            await self.highrise.teleport(user.id, Position(18,7,5,"FrontLeft"))"""
        """Teleportation only for MODs"""  
        if message.startswith("/tele"):
            if user.username == "_PewDz" or user.username == "__JENNY" or user.username == "xSAY":
                parts = message.split()
                if len(parts) > 3:
                    await self.highrise.chat("Invalid teleport command format.")
                    return
                elif len(parts) == 3:
                    username = parts[1][1:]
                    if username not in self.username_to_id:
                        await self.highrise.chat("User not found.")
                        return
                    try:
                        coords = parts[2].split(',')
                        x, y, z = map(float, coords)
                    except ValueError:
                        await self.highrise.chat("Invalid coordinates format.")
                        return
                    user_id = self.username_to_id[username]
                elif len(parts) == 2:
                    try:
                        coords = parts[1].split(',')
                        x, y, z = map(float, coords)
                    except ValueError:
                        await self.highrise.chat("Invalid coordinates format.")
                        return
                    user_id = user.id
                await self.highrise.teleport(user_id, Position(x,y,z))
                await self.highrise.chat(f"{user.username} has been teleported to ({x}, {y}, {z})")
            else:
                await self.highrise.chat(f"  Only Moderators are allowed to use the Teleport feature")

                
        message = message.lower()

        if message.startswith("/wallet"):
            msg = await self.highrise.get_wallet()
            msg = str(msg)
            start_index = msg.find("amount=") + len("amount=")
            end_index = msg.find(")", start_index)
            amount = int(msg[start_index:end_index])
            print(f"I've {amount} Gold Coins")
            await self.highrise.chat(f"@{user.username}! I've {amount} Gold Coins")
        
        greetings = [  "!hey",  "!hi",  "!hello",  "!hey there",  "!hiya",  "!yo",  "!sup",  "!heyo",  "!wassup",  "!hihi",  "!hola",  "!hey hey",  "!hey friend",  "!what's up",  "!hey dude",  "!hi there",  "!howdy",  "!hey ho",  "!hey you",  "!hi hi hi",  "!what's good",  "!hi friend",  "!how's it going",  "!hi everyone",  "!hey hey hey"]

        questions = [  "!how are you",  "!what's up",  "!what are you doing",  "!wyd",  "!hru",  "!how r u",  "!wassup",  "!what u up 2",  "!sup",  "!what's good",  "!how's it going",  "!what's new",  "!how are ya",  "!what's happening",  "!what's the word",  "!how've you been",  "!what's going o",  "!how's life",  "!what's the scoop",  "!what's crackin'",  "!how ya doin'",  "!what's poppin'",  "!what's cookin'",  "!how's everything",  "!what's shaking",  "!what's the deal",  "!how's your day",  "!what's the haps",  "!what's the story",  "!how's tricks",  "!what's happening",  "!what's the buzz",  "!what's new",  "!what's the 411",  "!what's the lowdown",  "!how's the world treating you"]


        goodbyes = [ "!cya", "!tyt", "!brb", "!goodbye", "!see you later", "!tc", "!bye", "!later", "!see ya", "!take care", "!peace", "!gotta run", "!catch ya later", "!ciao", "!adios", "!ttyl", "!l8r", "!g2g", "!farewell", "!hasta", "!cheers", "!sayonara", "!until next time", "!goodnight", "!buh-bye", "!adieu", "!toodles", "!so long", "!bye-bye", "!au revoir", "!take it easy", "!later alligator", "!keep in touch", "!have a good one", "!peace out", "!later skater"]

        if any(word in message for word in greetings):
            response = random.choice([  "Hey there!",  "Hi, how are you?",  "Hello! How's your day going?",  "Hey, what's up?",  "Hiya!",  "Hello, it's nice to hear from you!",  "Hey, long time no talk!",  "Hi! What's new?",  "Hello, how can I help you?",  "Hey, how's everything?",  "Hi, what's on your mind?",  "Hello, good to see you!",  "Hey, nice to meet you!",  "Hi, how's your week been?",  "Hello, what brings you here?",  "Hey, how can I assist you today?",  "Hi, I hope you're doing well!",  "Hello, it's a pleasure to hear from you!",  "Hey, how's life treating you?",  "Hi, what's happening?",  "Hello, what's the latest?",  "Hey, how have you been?",  "Hi, good to see you!",  "Hello, thanks for reaching out!",  "Hey, what's cooking?",  "Hi, how can I be of assistance?"])

            reply = f" {response}"
            
            await self.highrise.chat(reply)


        if any(word in message for word in questions):
            response = random.choice([  "I'm good, thanks! How about you?",  "Not much, just hanging out. How about you?",  "I'm doing well, thanks. What's new with you?",  "Just staying busy. What about you?",  "I'm doing pretty well. How about yourself?",  "Not much, just trying to keep busy. What's going on with you?",  "I'm doing great, thanks! How about you?",  "Just taking it easy. What's up with you?",  "I'm doing okay, thanks. How about yourself?",  "Not much, just chilling. What about you?",  "I'm doing pretty well, thanks for asking. How about you?",  "Just enjoying some downtime. What's new with you?",  "I'm good, thanks! What about you?",  "Just working on some stuff. How about you?",  "I'm doing well, thanks for asking. What's up with you?",  "Just taking care of some errands. How about you?",  "I'm doing pretty well. How about yourself?",  "Just trying to relax a bit. What's going on with you?",  "I'm good, thanks. What's new?",  "Just hanging out at home. How about you?",  "I'm doing okay, thanks for asking. What about you?",  "Just catching up on some work. What's up with you?",  "I'm doing pretty well, thanks. What's going on with you?",  "Just running some errands. How about you?",  "I'm good, thanks! How about yourself?"])
            
            reply = f" {response}"

            await self.highrise.chat(reply)
        
        
        if any(word in message for word in goodbyes):
            response = random.choice([  "Goodbye! Have a great day!",  "See you later! Take care!",  "Take care and talk to you soon!",  "Bye for now! See you soon!",  "Catch you later!",  "Later! Have a good one!",  "Goodbye! Don't be a stranger!",  "See you soon! Keep in touch!",  "Have a good one!",  "Farewell for now!",  "Goodbye! Stay safe!",  "Take care of yourself!",  "Adios amigo!",  "Until next time!",  "See you later, alligator!",  "Have a great day!",  "Hasta la vista!",  "See you soon! Bye!",  "Take care and have a good one!",  "Bye for now! See you later!",  "Talk to you soon!",  "Goodbye! See you around!",  "Have a great rest of your day!",  "It was great seeing you! Goodbye!",  "Take care of yourself and see you soon!"])
            
            reply = f" {response}"
            
            await self.highrise.chat(reply)
        
        if message.startswith("/macarena"):
            await self.highrise.send_emote("dance-macarena", user.id)
        if message.startswith("/smoothwalk"):
            await self.highrise.send_emote("dance-smoothwalk", user.id)
        if message.startswith("/angry"):
            await self.highrise.send_emote("emoji-angry", user.id)
        if message.startswith("/clap"):
            await self.highrise.send_emote("emoji-clapping", user.id)
        if message.startswith("/thumbs up"):
            await self.highrise.send_emote("emoji-thumbsup", user.id)
        if message.startswith("/exasperate"):
            await self.highrise.send_emote("emote-exasperatedb", user.id)
        if message.startswith("/frustrated"):
            await self.highrise.send_emote("emote-frustrated", user.id)
        if message.startswith("/ghost float"):
            await self.highrise.send_emote("emote-ghost-idle", user.id)
        if message.startswith("/happy"):
            await self.highrise.send_emote("emote-happy", user.id)
        if message.startswith("/love flutter"):
            await self.highrise.send_emote("emote-hearteyes", user.id)
        if message.startswith("/heart hands"):
            await self.highrise.send_emote("emote-heartfingers", user.id)
        if message.startswith("/partner heart arms"):
            await self.highrise.send_emote("emote-heartshape", user.id)
        if message.startswith("/wave"):
            await self.highrise.send_emote("emote-hello", user.id)
        if message.startswith("/partner hug"):
            await self.highrise.send_emote("emote-hug", user.id)
        if message.startswith("/hug yourself"):
            await self.highrise.send_emote("emote-hugyourself", user.id)
        if message.startswith("/kiss"):
            await self.highrise.send_emote("emote-kiss", user.id)
        if message.startswith("/panic"):
            await self.highrise.send_emote("emote-panic", user.id)
        if message.startswith("/do the worm"):
            await self.highrise.send_emote("emote-snake", user.id)
        if message.startswith("/teleport"):
            await self.highrise.send_emote("emote-teleporting", user.id)
        if message.startswith("/think"):
            await self.highrise.send_emote("emote-think", user.id)
        if message.startswith("/tired"):
            await self.highrise.send_emote("emote-tired", user.id)
        if message.startswith("/yes"):
            await self.highrise.send_emote("emote-yes", user.id)
        if message.startswith("/irritated"):
            await self.highrise.send_emote("idle-angry", user.id)
        if message.startswith("/feel the beat"):
            await self.highrise.send_emote("idle-dance-headbobbing", user.id)
        if message.startswith("/aerobics"):
            await self.highrise.send_emote("idle-loop-aerobics", user.id)
        if message.startswith("/annoyed"):
            await self.highrise.send_emote("idle-loop-annoyed", user.id)
        if message.startswith("/shy"):
            await self.highrise.send_emote("idle-loop-shy", user.id)
        if message.startswith("/sit on floor"):
            await self.highrise.send_emote("idle-loop-sitfloor", user.id)
        if message.startswith("/sleepy1"):
            await self.highrise.send_emote("idle-loop-tired", user.id)
        if message.startswith("/attentive"):
            await self.highrise.send_emote("idle_layingdown", user.id)
        if message.startswith("/rest"):
            await self.highrise.send_emote("sit-idle-cute", user.id)
        if message.startswith("/stunned"):
            await self.highrise.send_emote("emoji-dizzy", user.id)
        if message.startswith("/home run"):
            await self.highrise.send_emote("emote-baseball", user.id)
        if message.startswith("/sleepy2"):
            await self.highrise.send_emote("idle-sleep", user.id)
        if message.startswith("/no"):
            await self.highrise.send_emote("emote-no", user.id)
        if message.startswith("/i believe i can fly"):
            await self.highrise.send_emote("emote-wings", user.id)
        if message.startswith("/graceful"):
            await self.highrise.send_emote("emote-graceful", user.id)
        if message.startswith("/dab"):
            await self.highrise.send_emote("emote-dab", user.id)
        if message.startswith("/tapdance"):
            await self.highrise.send_emote("emote-tapdance", user.id)
        if message.startswith("/savage dance"):
            await self.highrise.send_emote("dance-tiktok8", user.id)
        if message.startswith("/relaxed"):
            await self.highrise.send_emote("idle_layingdown2", user.id)
        if message.startswith("/dummy"):
            await self.highrise.send_emote("dance-blackpin", user.id)
        if message.startswith("/dummy"):
            await self.highrise.send_emote("dance-duckwal", user.id)
        if message.startswith("/frolic"):
            await self.highrise.send_emote("emote-frollicking", user.id)
        if message.startswith("/robotic"):
            await self.highrise.send_emote("dance-robotic", user.id)
        if message.startswith("/russian dance"):
            await self.highrise.send_emote("dance-russian", user.id)
        if message.startswith("/orange juice dance"):
            await self.highrise.send_emote("dance-orangejustice", user.id)
        if message.startswith("/shuffle dance"):
            await self.highrise.send_emote("dance-tiktok10", user.id)
        if message.startswith("/renegade"):
            await self.highrise.send_emote("idle-dance-tiktok7", user.id)
        if message.startswith("/proposing"):
            await self.highrise.send_emote("emote-proposing", user.id)
        if message.startswith("/model"):
            await self.highrise.send_emote("emote-model", user.id)
        if message.startswith("/cozy nap"):
            await self.highrise.send_emote("idle-floorsleeping", user.id)
        if message.startswith("/laugh"):
            await self.highrise.send_emote("emote-laughing", user.id)
        if message.startswith("/peace"):
            await self.highrise.send_emote("emote-peace", user.id)
        if message.startswith("/theatrical"):
            await self.highrise.send_emote("emote-theatrical", user.id)
        if message.startswith("/lying"):
            await self.highrise.send_emote("emoji-lying", user.id)
        if message.startswith("/sob"):
            await self.highrise.send_emote("emoji-crying", user.id)
        if message.startswith("/ring on it"):
            await self.highrise.send_emote("dance-singleladies", user.id)
        if message.startswith("/boggie swing"):
            await self.highrise.send_emote("idle-dance-swinging", user.id)
        if message.startswith("/grave dance"):
            await self.highrise.send_emote("dance-weird", user.id)
        if message.startswith("/emote cute"):
            await self.highrise.send_emote("emote-cute", user.id)
        if message.startswith("/hero pose"):
            await self.highrise.send_emote("idle-hero", user.id)
        if message.startswith("/wiggle dance"):
            await self.highrise.send_emote("dance-sexy", user.id)
        if message.startswith("/relaxing"):
            await self.highrise.send_emote("idle-floorsleeping2", user.id)
        if message.startswith("/moonwalk"):
            await self.highrise.send_emote("emote-gordonshuffle", user.id)
        if message.startswith("/zombie dance"):
            await self.highrise.send_emote("dance-zombie", user.id)
        if message.startswith("/hands in the air"):
            await self.highrise.send_emote("dance-handsup", user.id)
        if message.startswith("/jump"):
            await self.highrise.send_emote("emote-jumpb", user.id)
        if message.startswith("/thumb suck"):
            await self.highrise.send_emote("emote-suckthumb", user.id)
        if message.startswith("/froggie hop"):
            await self.highrise.send_emote("emote-frog", user.id)
        if message.startswith("/sing along"):
            await self.highrise.send_emote("idle_singing", user.id)
        if message.startswith("/penny dance"):
            await self.highrise.send_emote("dance-pennywise", user.id)
        if message.startswith("/sword fight"):
            await self.highrise.send_emote("emote-swordfight", user.id)
        if message.startswith("/snow angel"):
            await self.highrise.send_emote("emote-snowangel", user.id)
        if message.startswith("/floating"):
            await self.highrise.send_emote("emote-float", user.id)
        if message == "/telekinesis":
            await self.highrise.send_emote("emote-telekinesis", user.id)
        if message.startswith("/wave"):
            await self.highrise.send_emote("emote-wave", user.id)
        if message.startswith("/exasperated"):
            await self.highrise.send_emote("emote-exasperatedb", user.id)
        if message.startswith("/peekaboo"):
            await self.highrise.send_emote("emote-peekaboo", user.id)
        if message.startswith("/ninja run"):
            await self.highrise.send_emote("emote-ninjarun", user.id)
        if message.startswith("/hero entrance"):
            await self.highrise.send_emote("emote-hero", user.id)
        if message.startswith("/rock out"):
            await self.highrise.send_emote("dance-metal", user.id)
        if message.startswith("/gangnam style"):
            await self.highrise.send_emote("emote-gangnam", user.id)
        if message.startswith("/judo chop"):
            await self.highrise.send_emote("emote-judochop", user.id)
        if message.startswith("/eyeroll"):
            await self.highrise.send_emote("emoji-eyeroll", user.id)
        if message.startswith("/super run"):
            await self.highrise.send_emote("emote-superrun", user.id)
        if message.startswith("/exasperated"):
            await self.highrise.send_emote("emote-exasperated", user.id)
        if message.startswith("/happy"):
            await self.highrise.send_emote("emoji-celebrate", user.id)
        if message.startswith("/super punch"):
            await self.highrise.send_emote("emote-superpunch", user.id)
        if message.startswith("/posh"):
            await self.highrise.send_emote("idle-posh", user.id)
        if message.startswith("/charging"):
            await self.highrise.send_emote("emote-charging", user.id)
        if message.startswith("/sad"):
            await self.highrise.send_emote("emote-sad", user.id)
        if message.startswith("/super kick"):
            await self.highrise.send_emote("emote-kicking", user.id)
        if message.startswith("/point"):
            await self.highrise.send_emote("emoji-there", user.id)
        if message.startswith("/snowball fight"):
            await self.highrise.send_emote("emote-snowball", user.id)
        if message.startswith("/aerobics"):
            await self.highrise.send_emote("dance-aerobics", user.id)
        if message.startswith("/lookup"):
            await self.highrise.send_emote("idle-lookup", user.id)
        if message.startswith("/clumsy"):
            await self.highrise.send_emote("emote-fail2", user.id)
        if message.startswith("/splits drop"):
            await self.highrise.send_emote("emote-splitsdrop", user.id)
        if message.startswith("/harlem shake"):
            await self.highrise.send_emote("emote-harlemshake", user.id)
        if message.startswith("/levitate"):
            await self.highrise.send_emote("emoji-halo", user.id)
        if message.startswith("/faint"):
            await self.highrise.send_emote("emote-fainting", user.id)
        if message.startswith("/happy"):
            await self.highrise.send_emote("idle-loop-happy", user.id)
        if message.startswith("/robot"):
            await self.highrise.send_emote("emote-robot", user.id)
        if message.startswith("/imaginary jetpack"):
            await self.highrise.send_emote("emote-jetpack", user.id)
        if message.startswith("/bunny hop"):
            await self.highrise.send_emote("emote-bunnyhop", user.id)
        if message.startswith("/give up"):
            await self.highrise.send_emote("emoji-give-up", user.id)
        
        parts = message.split()
        BadWords = [ "mc", "fu", "fck", "fcku", "porn", "fucking", "motherfucker", "behen ke take", "bc", "tmkc", "tmc", "bkl", "bsdk", "mf" , "chadarmod", "madharchod", "bhosadiwale", "bhosadike", "behenchod", "behen ke Lund", "laude", "gandu", "teri maki chut", "jhat" "lund", "gand", "mother fucker ", "bloody fool", "bitch", "randi", "fuddi", "lauda", "betichod", "jhatu", "mutthi", "cum", "bloody basterd", "basterd", "dick", "pussy", "penis", "vegina", "boobs", "nipple", "nipples", "anal", "anus", "fuck", "chal na re laude", "ladchatt", "chutiya", "bur ke bal" "macchar ki jhat", "chutiye", "sex", "maa chudao", "lavde", "nunu", "🖕", "xnxx", "xvideos", "naughty america", "savita bhabhi", "chod", "chudwa", "chudva", "chuda"]
        # Get the user input
        usernme = user.username

        # Check if the user is in the array of OffenseProof
        user_exists = False
        
        if any(word in parts for word in BadWords):
            for i in range(len(OffenseProof)):
                if OffenseProof[i][0] == usernme:
                    user_exists = True
                    if OffenseProof[i][1] <= 4:
                        OffenseProof[i][1] += 1
                        await self.highrise.send_whisper(user.id, f"Dear {user.username}, \n\nYou are being warned {OffenseProof[i][1]} time. \nOffensive language & Hate speech is not allowed in this room. Please refrain from using those bad words. \nContinuing to use offensive language may lead to consequences. \n\nSincerely,\nCare Taker\n(ANSH HOME)")
                        print(f"{user.username} Warning: {OffenseProof[i][1]} time")
                        break
                    else:
                        OffenseProof[i][1] += 1
                        print(f"Kicked {usernme}")
                        await self.highrise.teleport(user.id, Position(1,0,0, "FrontLeft" ))
                        await self.highrise.send_whisper(user.id, f"I've already said it earlier\nDo not use any offensive language, you may lead to consequences. \nYou've been Kicked with the 5 warnings. \nIf you used it one more in the room you will be kicked again")
                        break

            # If the user is not in the array of OffenseProof, add them with 1 fault
            if not user_exists:
                OffenseProof.append([usernme, 1])
                await self.highrise.send_whisper(user.id, f"Dear {user.username}, \n\nYou are being warned 1 time. \nOffensive language & Hate speech is not allowed in this room. Please refrain from using those bad words. \nContinuing to use offensive language may lead to consequences. \n\nSincerely,\nCare Taker\n(ANSH HOME)")
                print(f"User added to the array of OffenseProof")
            
            # Print the updated array of OffenseProof
            print(f"Array of OffenseProof:", OffenseProof)

        pass
    async def on_tip(self, sender: User, receiver: User, tip: Item) -> None:
        BotName = "IronManBot"
        if receiver.username == BotName:
            await self.highrise.chat(f"Thank you @{sender.username} for tipping {tip.amount} to Me\n But from now don't tip me because I'm a Bot and the Gold can't be taken from me back Later.\nThank You")
        else:
            await self.highrise.chat(f"Thank you {sender.username} for tipping {tip.amount} to {receiver.username}!")
        pass
