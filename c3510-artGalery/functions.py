import wget
import tweepy as tw
import json
import time
import os

#pessoas banidas
banidoArroba = [
'mar_de_nevoa'
]

def baixarEntidade(entidade):
    tweet_id = message.message_create["message_data"]["entities"]["urls"][0]['expanded_url'].split('/')[-1]
    tweet = api.get_status(tweet_id)
    if tweet.favorited == False:
        api.create_favorite(tweet_id)
    if 'media' in tweet.entities:
        counter = 0
        for image in tweet.entities['media']:
            print( tweet.entities['media'])
            counter +=1
            wget.download(image['media_url'])
            file_name = f"{tweet_id}@{tweet.user.screen_name}-{counter}.jpg"
            os.rename(image['media_url'].split('/')[-1],file_name)
            os.system(f"move {file_name} ./\"{entidade[-1]} {entidade}\"")
            confirmacao(file_name, f"{entidade[-1]} {entidade}")
    else:
        semImagem(f"{entidade}")

def baixarBruxinha():
    tweet_id = message.message_create["message_data"]["entities"]["urls"][0]['expanded_url'].split('/')[-1]
    tweet = api.get_status(tweet_id)
    salvar_tweet('a bruxinha',tweet_id )
    if tweet.favorited == False:
        api.create_favorite(tweet_id)
    if 'media' in tweet.entities:
        counter = 0
        for image in tweet.entities['media']:
            counter +=1
            wget.download(image['media_url'])
            file_name = f"{tweet_id}@{tweet.user.screen_name}-{counter}.jpg"
            os.rename(image['media_url'].split('/')[-1],file_name)
            os.system(f"move {file_name} ./\"a bruxinha\"")
            confirmacao(file_name, "a bruxinha")
    else:
        semImagem("bruxinha")

def baixarPistoleiro():
    tweet_id = message.message_create["message_data"]["entities"]["urls"][0]['expanded_url'].split('/')[-1]
    tweet = api.get_status(tweet_id)
    if tweet.favorited == False:
        api.create_favorite(tweet_id)
    if 'media' in tweet.entities:
        counter = 0
        for image in tweet.entities['media']:
            counter +=1
            wget.download(image['media_url'])
            file_name = f"{tweet_id}@{tweet.user.screen_name}-{counter}.jpg"
            os.rename(image['media_url'].split('/')[-1],file_name)
            os.system(f"move {file_name} ./\"o pistoleiro\"")
            confirmacao(file_name, "o pistoleiro")
    else:
        semImagem("pistoleiro")

#debugger

def confirmacao(file_name, entidade):
    print(f"confirmado {entidade}")
    directory = os.getcwd()
    media = api.media_upload(filename=f"{directory}/{entidade}/{file_name}")
    api.send_direct_message(recipient_id = oldest_user, text = f'obrigado pel{entidade}',attachment_type='media', attachment_media_id=media.media_id)

def semImagem(entidade):
    api.send_direct_message(recipient_id = oldest_user, text = f'não existe {entidade} ai')

def banirContas(usuarios):
    banido = []
    for arroba in usuarios:
        banido.append(api.get_user(screen_name = arroba).id_str)
    return banido

def salvar_tweet(entidade,instanceTweet):
    Tsalvar = api.get_status(instanceTweet)._json
    with open(f"{entidade}.txt", "a") as output:
        output.write(f"{json.dumps(Tsalvar)}\n\n")

def tts(say):
    import win32com.client
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    try:
        speaker.Speak(say)
    except:
        pass

#--------------------------------------------------
if __name__ == '__main__':
    with open ('key.txt', 'r') as tfile:
        consumer_key = tfile.readline().strip('\n')
        consumer_secret = tfile.readline().strip('\n')
        access_token = tfile.readline().strip('\n')
        access_secret = tfile.readline().strip('\n')
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tw.API(auth)

    print(api.rate_limit_status()['resources']['statuses'])
    # -----------------------------------------------------------------

    print('banidos =', banirContas(banidoArroba))
    direct_messages = api.get_direct_messages(count = 40)#count = 1)
    print(f'lidas {len(direct_messages)} mensagens')

    #oldest_id = direct_messages[-1].id
    with open('last_id.txt', 'r') as file:
        oldest_id = file.read()
    #print(oldest_id)
    banidos = banirContas(banidoArroba)
    while True:
        novasMen = 0
        novasBruxinhas = 0
        for message in reversed(direct_messages):
            if message.id <= oldest_id:
                continue
            novasMen += 1
            if message.message_create["sender_id"] in banidos:
                api.send_direct_message(recipient_id = message.message_create["sender_id"], text = f'você foi banido desculpa')
                oldest_id = message.id
                oldest_user = message.message_create["sender_id"]
                with open('last_id.txt', 'w') as file:
                    file.write(oldest_id)
                continue

            oldest_id = message.id
            oldest_user = message.message_create["sender_id"]
            with open('last_id.txt', 'w') as file:
                file.write(oldest_id)
            with open("teste.txt", "a") as output:
                output.write(f"{json.dumps(message._json)} \n")
            #print(message.message_create["message_data"]["text"])

            if message.message_create["message_data"]["text"][0:9] == "BRUXINHA!":
                baixarBruxinha()
                novasBruxinhas += 1
            elif message.message_create["message_data"]["text"][0:11] == "PISTOLEIRO!":
                baixarPistoleiro()
                novasBruxinhas += 1
            elif message.message_create["message_data"]["text"][0:15] == "CYBERPUNKZINHO!":
                baixarEntidade("cyberpunkzinho")

        if novasBruxinhas:
            s = "" if novasBruxinhas == 1 else "s"
            novasBruxinhas = "uma" if novasBruxinhas ==1 else novasBruxinhas
            novasBruxinhas = "duas" if novasBruxinhas ==2 else novasBruxinhas
            tts(f'você tem {novasBruxinhas} nova{s} bruxinha{s}')
        time.sleep(240)
        print("new_loop")
        direct_messages = api.get_direct_messages(count = 40)
        print(f'lidas {len(direct_messages)} mensagens')

    #[{'url': 'https://t.co/A3nn5vAtPb', 'expanded_url': 'https://twitter.com/F_RU12/status/1490318106475991042', 'display_url': 'twitter.com/F_RU12/status/…', 'indices': [10, 33]}]
