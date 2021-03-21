import requests
import threading 

def getSimilarity(sentence_x,sentence_y,sentence_scores,threadLock):
    params =  {
    "text1": sentence_x,
    "text2": sentence_y,
    "token":"9bc923cfc260417daf46e1199092fd85"
    }
    response = requests.get('https://www.twinword.com/api/text/similarity/latest/',params=params)
    resp = response.json()
    # handling critical section
    threadLock.acquire() # get lock
    sentence_scores[sentence_x]=round(resp["similarity"],1) # will round value 0.25 to 0.3 to maintain 1 decimal
    threadLock.release() # release lock

def getBestMatchText(sentence_scores):
    max_score,best_text = 0,None
    for text,score in sentence_scores.items():
        if score > max_score :
            max_score,best_text = score,text
    return best_text

def getBestMatch(sentences,sentence_y):
    sentence_scores  = {}
    threadLock = threading.Lock()
    # getting similarity score for all keys at time using thread to reduce the latency
    threads =  [threading.Thread(target = getSimilarity,args = (sentence_x,sentence_y,sentence_scores,threadLock)) for sentence_x in sentences]
    # starting all threads
    [thread.start() for thread in threads]
    # waiting for threads to finish job
    [thread.join() for thread in threads]
    print(sentence_scores)
    return getBestMatchText(sentence_scores)
