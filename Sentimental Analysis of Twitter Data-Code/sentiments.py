import re
import sys
import json

def get_tweet_sentiment(tweet_dict, weights):
    score = 0.0
    text = ""
    if u'text' in tweet_dict:
        utf8_text = tweet_dict[u'text']
        text = utf8_text
        toks = re.split('\s+', utf8_text.lower())
        for word in toks:
            word = re.sub('\W', '', word)
            if word in weights:
                score += weights[word]
        score = min(15, score)
        score = max(-15, score)
        for word in toks:
            word = re.sub('\W', '', word)
            if word not in weights and len(word) > 3:
                weights[word] = 0

    return score, text

def readWeights():
    weights = {}
    with open('sentiments.txt') as f:
        for line in f:
            toks = re.split('\s+', line.strip().lower()) 
            if len(toks) == 2:
                word = toks[0]
                word = re.sub('\W', '', word)
                weights[word] = float(toks[1])
    return weights

def main(tweet_file):
    nop=0
    non=0
    weights = readWeights()
    sentiments = []
    
    with open(tweet_file) as tf:
        for line in tf:
            if line:
                tweet = json.loads(line)
		
                score, tweet_text = get_tweet_sentiment(tweet, weights)
                if score > 2:
                    print "\"",tweet_text, "\" : Had score ", score
                    sentiments.append(score)
		    nop=nop+1
		if score <-2:
 		    print "\"",tweet_text, "\" : Had score ", score
               	    sentiments.append(score)
		    non=non+1

    total = 0.0
    for num in sentiments:
        total += num
	
    if (total/len(sentiments))>0.0:
	print "\n\nThe overall popularity of this mention is  POSITIVE : ",total/len(sentiments)
    else:
	print "\n\nThe overall popularity of this mention is  NEGATIVE : ",total/len(sentiments)

    print "\nThe number of Positive tweets are : ", nop
    print "\nThe number of Negetive tweets are : ", non
if __name__ == '__main__':
    main(sys.argv[1])
