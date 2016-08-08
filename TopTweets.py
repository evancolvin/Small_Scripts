import tweepy


# Your Twitter OAuth Here:
auth = tweepy.OAuthHandler('', '')

auth.set_access_token('', '')

api = tweepy.API(auth)

def top_tweets(user, tweets = 10):
    """This function will return the 10 most favorited tweets by a specified user.
    To get more or less tweets returned, change the number following the
    'tweets argument.
    """

    print "Connecting to Twitter...\n"
    # If there's a problem connecting it will throw an error here
    user_tweets = api.user_timeline(user, count = 200)
    print "Connected\nFinding {}'s best Tweets...\n".format(api.get_user(user).name)

    # Pulls up to the next 3000 tweets
    for i in range(15):

        # Get new tweets and adds them to the list
        new_tweets = api.user_timeline(user, count = 200,
                                            max_id = user_tweets[-1].id - 1)
        user_tweets.extend(new_tweets)

    tweet_list = [] # this will hold the data I actually want

    # Makes tweets a list of lists where each list has the text of the tweet,
    # favorite count, retweet count, and the date the tweet was written
    for i in range(len(user_tweets)):

        tweet_list.append([user_tweets[i].text,
                    user_tweets[i].favorite_count,
                    user_tweets[i].retweet_count,
                    user_tweets[i].created_at])

    del user_tweets[:] # clearing unneeded list

    # Sorts the tweets by the number of times favorited, brings the most
    # favorited ones to the front, and truncates to the number of specified tweets
    tweet_list = sorted(tweet_list, key = lambda x: x[1], reverse = True)[:tweets]

    # Reformatting the tweets so they're not a such a mess
    for i in range(tweets):
        tweet_list[i][1] = "Favorited {} times".format(tweet_list[i][1])
        tweet_list[i][2] = "Retweeted {} times".format(tweet_list[i][2])
        tweet_list[i][3] = "Tweeted on {}".format(tweet_list[i][3])

    return tweet_list

if __name__ == '__main__':
    A = top_tweets(raw_input('What user would you like? '))
    for foo in A:
        for bar in foo:
            print bar
        print "\n"
