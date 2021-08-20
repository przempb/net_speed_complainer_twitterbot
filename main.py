from twitter_class import InternetSpeedTwitterBot


#___SET VALUES OF INTERNET SPEED THAT ARE GUARANTEED
PROMISED_DOWN = 1500
PROMISED_UP = 100

bot = InternetSpeedTwitterBot()
internet_speed = bot.get_internet_speed()


if __name__ == "__main__":
    if float(internet_speed[0]) < PROMISED_DOWN or float(internet_speed[1]) < PROMISED_UP:
        tweet = f"Hej UPC, mój internet powinien mieć prędkość pobierania {PROMISED_DOWN}down/{PROMISED_UP}up." \
                f"W najnowszym teście speedtest.net jest tylko {internet_speed[0]}down/{internet_speed[1]}up Za co ja Wam płacę?!"
        twitter = bot.tweet_at_provider(message=tweet)

