from json import load,dump
from os import write

class Cache:

    def __init__(self,file) -> None:
        self.file = file
        self.loadCache()

    def loadCache(self):
        with open(self.file,"r") as fp:
            self.cache = load(fp)

    def writeCache(self):
        with open(self.file,"w") as fp:
            dump(self.cache,fp)

    def get(self,key):
        return self.cache[key] if key in self.cache else None

    def put(self,key,value):
        self.cache[key]=value
        self.writeCache()

    def keys(self):
        return list(self.cache.keys())

    def clear(self):
        self.cache = {}
        self.writeCache()
