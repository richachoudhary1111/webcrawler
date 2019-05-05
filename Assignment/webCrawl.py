
#Richa Choudhary 2019/05/05

#Class to read feeds information
class CrawlFeeds:
    def __init__(self):
        self.curr=None
    def getFeeds(self,text):
        return text

#Class introduce to add new type
class Type:
    # constructor
    def __init__(self):
        self.typeinfo={
            "Entity":"strong",
            "Link":"a",
            "Twitter":"a"
        }

    def addType(self,type,htmltag):
        self.typeinfo[type]=htmltag

#Class to extract feed info
class FeedInfo:
    #constructor
    def __init__(self):
        self.create_obj={}

    def createFeedinfo(self,st,en,type,feeds):
        word=''
        for i in range(0, len(feeds)):
            if i>=st and i<en:
                word+=feeds[i]

        self.create_obj[word]=type

#Class to get htmltag-inehritance : Base class
class HashTag(object):
    # constructor
    def __init__(self,typeinfo):
        self.typeinfo=typeinfo

#Derived class
class Tag(HashTag):
    # constructor
    def __init__(self,typeinfo):
        HashTag.__init__(self,typeinfo)

    def addTag(self,type):
        try:
            if type in self.typeinfo:
                if type.startswith("Twitter"):
                    return "<" + self.typeinfo[type] + " href='http://twitter.com/-'" + ">" + '-' + "</" + self.typeinfo[type] + ">"
                elif type.startswith("Link"):
                    return "<" + self.typeinfo[type] + " href='-'" + ">" + '-' + "</" + self.typeinfo[type] + ">"
                else:
                    return "<" + self.typeinfo[type] + ">" + '-' + "</" + self.typeinfo[type] + ">"
        except KeyError as error:
           print error
        except Exception as exception:
            print  exception

#Class to wrap data with htmltag
class WrapData:
    def __init__(self):
        pass

    def getResponse(self,text,worddic):
        word = '';res='';i=0
        while i<len(text):
            if text[i] == '@':
                res += text[i] + ' '
            if text[i]!=' ':
                word += feeds[i]
            else:
                res=self.searchData(word,worddic,res)
                word = ''
                res += ' '
            i += 1

        res = self.searchData(word, worddic, res)
        return res

    def searchData(self,word,worddic,res):
        flag = 1
        try:
            for key, value in worddic.iteritems():
                if key == word:
                    if(key[0]=='@'):
                        key=key[1:]
                    res += value.replace('-', key)
                    flag = 0
            if (flag):
                res += word
            return res
        except AttributeError as error:
            print error
        except ValueError as ve:
            print ve
        except Exception as exception:
            print exception


if __name__ == '__main__':

    # will crawl the facebook,twitter feeds
    crobj=CrawlFeeds()
    typeobj=Type()
    feedobj=FeedInfo()
    txt=raw_input("Enter crawl feeds: ")
    feeds=crobj.getFeeds(txt)

    print "Current Type & tag---",typeobj.typeinfo

    # Extend property to add new type & tag
    m = raw_input("Do you want to add new htmltag:Y/N ")
    alltype='Entity/Link/Twitter'
    if (m.lower() == 'y'):
        type = raw_input("Enter new type:")
        tag = raw_input("Enter new tag:")
        typeobj.addType(type, tag)
        print "Current Type & tag---", typeobj.typeinfo
        alltype = (typeobj.typeinfo.keys())
        alltype = '/'.join(alltype)


    # Extract information from feed
    n = input("No of information you want to extract: ")
    for i in range(n):
        type=raw_input("Enter " + alltype + ': ')
        startpos=input("Starting position:")
        endpos =input("Ending position:")
        feedobj.createFeedinfo(startpos,endpos,type,feeds)

    worddic={}


    hashobj = Tag(typeobj.typeinfo)
    for key,value in feedobj.create_obj.iteritems():
        tagresponse=hashobj.addTag(value)
        worddic[key]=tagresponse

    wrobj=WrapData()
    response=wrobj.getResponse(feeds,worddic)
    print "Response---",response

