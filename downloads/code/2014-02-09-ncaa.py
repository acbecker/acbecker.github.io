import os
import numpy as np
from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "td" and attrs == [('class', 'year')]:
            self.doreset()
            self.attr = "year"
        elif tag == "td" and attrs == [('class', 'round')]:
            self.attr = "round"
        elif tag == "td" and attrs == [('class', 'seed')]:
            self.attr = "seed"
        elif tag == "td" and attrs == [('class', 'score')]:
            self.attr = "score"
        elif tag == "td":
            self.attr = None

    def doreset(self):
        if self.year is None:
            return
        
        if not self.counter.has_key(self.year):
            self.counter[self.year] = {}
            for round in self.rounds:
                self.counter[self.year][round] = []
        if self.round in self.rounds:
            self.counter[self.year][self.round].append((self.seed, self.score))
            
        self.year = None
        self.round = None
        self.seed = []
        self.score = []
        
    def handle_data(self, data):
        if self.attr == "year":
            self.year = data
            self.attr = None
        elif self.attr == "round":
            self.round = data
            self.attr = None
        elif self.attr == "seed":
            self.seed.append(int(data))
            self.attr = None
        elif self.attr == "score":
            self.score.append(int(data))
            self.attr = None
            
        #if self.attr is not None:
        #    print self.attr, data
            

    def feed(self, data):
        self.rounds  = ["First Round", "Second Round", "Sweet 16", "Elite Eight", "Final Four", "National Championship"]
        self.attr    = None
        self.counter = {}

        self.year  = None
        self.round = None
        self.seed  = []
        self.score = []
        
        HTMLParser.feed(self, data)
        self.doreset() # Get the last score in there
        import pdb; pdb.set_trace()
        self.parseByYear()
        self.parseByRound()
        self.parseAll()

    def domatchup(self, pair):
        (rank1, rank2), (score1, score2) = pair
        if rank1 < rank2 and score1 > score2:
            # Favorite wins
            return 1
        elif rank1 == rank2:
            # Ignore for now
            return -1
        return 0

    def parseMat(self):
        mattot = np.zeros((16, 16))
        matfav = np.zeros((16, 16))
        years = self.counter.keys()
        years.sort()
        for year in years:
            for round in self.counter[year]:
                for matchup in self.counter[year][round]:
                    (rank1, rank2), (score1, score2) = matchup
                    idx1 = min(rank1, rank2) - 1
                    idx2 = max(rank1, rank2) - 1
                    mattot[idx1, idx2] += 1
                    if rank1 < rank2 and score1 > score2:
                        matfav[idx1, idx2] += 1
        print "ALL", mattot, matfav, matfav/mattot
        return matfav/mattot
        
        
    def parseAll(self):
        ntot = 0
        nfav = 0
        years = self.counter.keys()
        years.sort()
        for year in years:
            for round in self.counter[year]:
                for matchup in self.counter[year][round]:
                    res = self.domatchup(matchup)
                    if res == -1:
                        continue
                    ntot += 1
                    nfav += res
        print "ALL", ntot, nfav, 1.0 * nfav / ntot

    def parseByYear(self):
        years = self.counter.keys()
        years.sort()
        for year in years:
            ntot = 0
            nfav = 0
            for round in self.counter[year]:
                for matchup in self.counter[year][round]:
                    res = self.domatchup(matchup)
                    if res == -1:
                        continue
                    ntot += 1
                    nfav += res
            print year, ntot, nfav, 1.0 * nfav / ntot

    def parseByRound(self):
        years = self.counter.keys()
        years.sort()
        for round in self.rounds:
            ntot = 0
            nfav = 0
            for year in years:
                for matchup in self.counter[year][round]:
                    res = self.domatchup(matchup)
                    if res == -1:
                        continue
                    ntot += 1
                    nfav += res
            print round, ntot, nfav, 1.0 * nfav / ntot
            
# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
data   = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../data/2014-02-09-ncaa.html")
parser.feed("\n".join(open(data).readlines()))
