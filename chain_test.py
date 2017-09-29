class Chain(object):
    def __init__(self,path=''):
        self._path=path

#    def __getattr__(self,path):
#        return Chain('%s/%s'%(self._path,path))
    def __getattr__(self,path):
        if self._path == '':
            return Chain('%s'%path)
        else:
            return Chain('%s.%s'%(self._path,path))

    def __str__(self):
        return self._path

    __repr__=__str__


dir1 = Chain().status.user.timeline.list.hh
date = Chain().year.mont.day.time
print dir1
print date
