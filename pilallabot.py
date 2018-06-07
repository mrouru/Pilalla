import sys, random, time, pickle
from time import sleep

try:
	#Twitter credentials
	CONSUMER_KEY = 'YOUR_CONSUMER_KEY'
	CONSUMER_SECRET = 'YOUR_CONSUMER_SECRET'
	ACCESS_KEY = 'YOUR_ACCESS_KEY'
	ACCESS_SECRET = 'YOUR_ACCESS_SECRET'

	#Setting up the authentication and API for Twitter
	#auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	#auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	#api = tweepy.API(auth)

	def main():
		while True:
			numberOfNouns = sum(1 for line in open('finnishnouns.txt', 'r'))
			
			#Create a pickle file for maintaining the 168 (7 * 24, one week) nouns
			pickle_file = open('nounfile.pickle', 'ab')
			try:
				lastWeekNouns = pickle.load(open('nounfile.pickle', 'rb'))
			except EOFError:
				lastWeekNouns = []

			#Get a random noun
			nounIndex = random.randint(0, numberOfNouns-1)
			while nounIndex in lastWeekNouns:
				nounIndex = random.randint(0, numberOfNouns-1)
		
			noun = open("finnishnouns.txt", "r").readlines()[nounIndex].rstrip('\n')

			#Check if the noun has already been tweeted
			if len(lastWeekNouns) < numberOfNouns:
					lastWeekNouns.append(nounIndex)
					with open ('nounfile.pickle', 'wb') as pickle_file:
						pickle.dump(lastWeekNouns, pickle_file)

			#Form the tweet
			tweet = noun + " on pilalla"
			
			print(tweet)
			sleep(1)
			#api.update_status(tweet)

	if __name__ == "__main__":
		main()
		
except Exception as e:
    print(e.message)