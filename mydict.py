class Dict(dict):
    def __init__(self,**kw):
        super(Dict,self).__init__(**kw)   #**kw是关键字参数
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("Dict object has no attribute '%s'" %key)
    def __setattr__(self, key, value):
        self[key]=value

