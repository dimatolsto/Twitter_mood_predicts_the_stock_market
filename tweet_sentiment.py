import sys
import json

##def hw():
##    print 'Hello, world!'
##
##def lines(fp):
##    print str(len(fp.readlines()))

def sent2dict(tab_file):
    scores = {}
    for line in tab_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores
    #print scores

def sentiment_score(line,scores):
    sent_score = 0
    tweet = json.loads(line)        
    if 'text' in tweet.keys():
        tweet_message = tweet['text']
        #print tweet_message
        words = tweet_message.split()
        for word in words:
            encoded_word = word.encode('utf-8')
            if encoded_word in scores:
                sent_score = sent_score + scores[encoded_word]
        return float(sent_score)
    else:
        return 0.0  

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
##    hw()
##    lines(sent_file)
##    lines(tweet_file)
    scores = sent2dict(sent_file)  
    #print scores
    for line in tweet_file:
        print sentiment_score(line,scores)            
    

if __name__ == '__main__':
    main()


   
