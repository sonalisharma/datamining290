from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
import itertools



class UserSimilarity(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    def extract_user_bus_id(self, _, record):
        if record['type'] == 'review':
            yield [record['user_id'],record['business_id']]
    ###
    # TODO: write the functions needed to
    # 1) find potential matches, 
    # 2) calculate the Jaccard between users, with a user defined as a set of
    # reviewed businesses
    ##/

    

    def combine_bus(self, user_id,business_id):
        yield [user_id,list(business_id)]

    def makepairs(self,user_id,business_ids):
        yield ["COM",[user_id,business_ids]]
    
    def makepairsred(self,stat,values):
        for x in itertools.combinations(list(values), 2):
            yield ["com" , x]
        
    def keypairs(self,stat,y):
        def jaccard(x,y):
            union =  (float)(len(list((set(x) | set(y)))))
            intersect = (float)(len(list((set(x) & set(y)))))
            jcoeff = (intersect/union)
            return jcoeff
        a=list(y)
        if (jaccard(a[0][1], a[1][1])) >= 0.5:
            yield [(a[0][0], a[1][0]), jaccard(a[0][1], a[1][1])]


    def steps(self):
        """TODO: Document what you expect each mapper and reducer to produce:
        mapper1: <line, record> => <key, value>
        reducer1: <key, [values]>
        mapper2: ...
        """
        return [self.mr(self.extract_user_bus_id,self.combine_bus), self.mr(self.makepairs, self.makepairsred),self.mr(self.keypairs)]
        #,self.mr(self.keypairs,self.jaccard)]


if __name__ == '__main__':
    UserSimilarity.run()
