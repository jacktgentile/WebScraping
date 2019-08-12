from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import re

url = "https://www.twitter.com/BarackObama"
# url = "http://ethans_fake_twitter_site.surge.sh/"
response = urlopen(url)
soup = BeautifulSoup(response.read(),"html.parser")
tweetList = soup.find_all("div",class_="content")

tweetArr = []
for tweet in tweetList:
    countList = tweet.find_all('span', class_="ProfileTweet-actionCountForAria")
    tweetObj = {
        "date": tweet.find('small', class_="time").a['title'],
        "tweet": tweet.find('p', class_='TweetTextSize').text,
        "replies": countList[0].text[:-8],
        "retweets": countList[1].text[:-9],
        "likes": countList[2].text[:-6]
    }
    tweetArr.append(tweetObj)
with open("twitter_data.json", "w") as outfile:
    json.dump(tweetArr, outfile)
