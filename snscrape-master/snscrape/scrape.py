import snscrape.modules.twitter as sntwitter
import csv

keyword = 'BlerDCon2021'
maxTweets = 30000

#Open/create a file to append data to
csvFile = open('BlerDCon2021.csv', 'a', newline='', encoding='utf8')

#Use csv writer
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['id','date','tweet'])

for i,tweet in enumerate(sntwitter.TwitterSearchScraper(keyword + ' since:2021-06-01 until:2021-12-16').get_items()) :
        if i > maxTweets :
            break
        csvWriter.writerow([tweet.id, tweet.date, tweet.renderedContent])
csvFile.close()