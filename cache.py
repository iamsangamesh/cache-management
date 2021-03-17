from json import load,dump

cache = {}

def loadCache():
    global cache
    with open("./db.json") as fp:
        cache = load(fp)

loadCache()

def writeCache():
    global cache
    with open("./db.json","w") as fp:
        dump(cache,fp)

def get(key):
    return cache[key] if key in cache else None

def put(key,value):
    cache[key]=value
    writeCache()
