#!/usr/bin/env python
import nltk, random, csv, sys
import re
import json
from nltk.corpus import names
from nltk.tokenize import word_tokenize
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

def get_tweet_sentiment(tweet_dict):
    score = 0.0
    text = ""
    tweetWords=""
    if u'text' in tweet_dict:
        utf8_text = tweet_dict[u'text']
        text = utf8_text
        print text
	result=cl.classify(text)
    print "Sentiment of the tweet:", (result)
    return result

def selectTweets(row):
    tweetWords = []
    words = row[0].split()
    for i in words:
        i = i.lower()
        i = i.strip('@#\'"?,.!')
        tweetWords.append(i)
    row[0] = tweetWords

    if counter <= 499:
        trainTweets.append(row)
    else:
        testTweets.append(row)

trainTweets = []
testTweets = []



while True:
    
    
    filename =  str(raw_input("> Please enter a filename (.csv): "))
    
    
    if filename.endswith(".csv"):
        
        try:
            
          
            with open(filename, 'rb') as csvfile: 
                reader = csv.reader(csvfile, delimiter=';', quotechar='|')
                
             
                print "> File opened successfully!"
                
                counter = 0
                for row in reader:
                    selectTweets(row)
                    counter += 1
                    
                print "> Wait a sec for the results..."
                    
                cl = NaiveBayesClassifier(trainTweets)
                
                print("Accuracy of the classifier: {0}".format(cl.accuracy(testTweets)))
                cl.show_informative_features(10)
                
                while True:
                
                    
                    tweetfile =  str(raw_input("Please enter the file name of the data file(.json) "))
		    with open(tweetfile) as tf:
			nop=0
			non=0
        		for line in tf:
			    tweetwords=[]
			    text = ""
            		    if line:
				tweet = json.loads(line)
				result = get_tweet_sentiment(tweet)
				if result=="positive":
				    nop=nop+1
				if result=="negative":
				    non=non+1
		        print "\nThe number of Positive tweets are : ", nop
                        print "\nThe number of Negative tweets are : ", non		
         
        except IOError:
            print "File does not exist."
            
    
    else:
        print "Please open a file that ends with .csv"


