class TimeMap:

    def __init__(self):
        self.store={}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=[(value,timestamp)]
        else:
            self.store[key]+=[(value,timestamp)]
    
    def get(self, key: str, timestamp: int) -> str:
        findIN=self.store.get(key,[])
        res="" 
        l , r = 0, len(findIN)-1  
        while(l<=r):
            mid = (l+r) // 2
            if findIN[mid][1]<=timestamp:
                res=findIN[mid][0]
                l=mid+1
            else:
                r=mid-1
        return res
