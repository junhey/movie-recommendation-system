# coding=utf-8
'''
基于项目的推荐系统，IBCF：
Created on 2018-03-07
@author: junhey
'''
import random
import math


class KNN:
    
    # 初始化相关参数
    def __init__(self):
        # 找到与目标用户兴趣相似的20个用户，为其推荐10部电影
        self.n_sim_user = 20
        self.n_rec_movie = 10

        # 将数据集划分为训练集和测试集
        self.traindata = {}
        self.testdata = {}

        # 用户相似度矩阵
        self.user_sim_matrix = {}
        self.movie_count = 0

        print('相似用户数：%d' % self.n_sim_user)
        print('推荐电影数：%d' % self.n_rec_movie)


    # 读文件得到“用户-电影”数据
    def get_dataset(self, filename, pivot=0.75):
        traindata_len = 0
        testdata_len = 0
        for line in self.load_file(filename):            
            userid, movieid, rating, timestamp = line.split(',')
            if random.random() < pivot:
                self.traindata.setdefault(userid, {})
                self.traindata[userid][movieid] = rating
                traindata_len += 1
            else:
                self.testdata.setdefault(userid, {})
                self.testdata[userid][movieid] = rating
                testdata_len += 1            
        
        print('分离训练集和测试集成功!')
        print('训练集数量:%s' % traindata_len)
        print('测试集数量:%s' % testdata_len)      



    # 读文件，返回文件的每一行
    def load_file(self, filename):
        with open(filename, 'r') as f:
            for i, line in enumerate(f):
                if i == 0:  # 去掉文件第一行的title
                    continue
                yield line.strip('\r\n')
        print('读取文件 %s 成功!' % filename)

    def ItemSim(self, train=None):
        train = self.traindata        
        ItemSimcount = dict()
        Item_count = dict()
        for _, items in train.items():
            for itemidi in items.keys():
                Item_count.setdefault(itemidi, 0)
                Item_count[itemidi] += 1
                for itemidj in items.keys():
                    if itemidi == itemidj:
                        continue
                    ItemSimcount.setdefault(itemidi, {})
                    ItemSimcount[itemidi].setdefault(itemidj, 0)
                    ItemSimcount[itemidi][itemidj] += 1
        self.ItemSimlist = dict()
        for itemidi, related_item in ItemSimcount.items():
            self.ItemSimlist.setdefault(itemidi, {})
            for itemidj, wij in related_item.items():
                self.ItemSimlist[itemidi].setdefault(itemidj, 0)
                self.ItemSimlist[itemidi][itemidj] = wij / math.sqrt(Item_count[itemidi] * Item_count[itemidj] * 1.0)

    def recommend(self, user, train=None, k=5, nitem=10):
        train = self.traindata
        recommendlist = dict()
        User_Itemlist = train.get(user, {})
        for i, ri in User_Itemlist.items():
            for j, wij in sorted(self.ItemSimlist[i].items(), key=lambda x: x[1], reverse=True)[0:k]:
                if j in User_Itemlist:
                    continue
                recommendlist.setdefault(j, 0)
                recommendlist[j] += float(ri) * wij
        return dict(sorted(recommendlist.items(), key=lambda x: x[1], reverse=True)[0:nitem])

    def recallAndPrecision(self, train=None, test=None, k=5, nitem=10):
        train = self.traindata
        test = self.testdata
        hit = 0
        recall = 0
        precision = 0
        for user in train.keys():
            tu = test.get(user, {})
            rank = self.recommend(user, train=train, k=k, nitem=nitem)
            for item, _ in rank.items():
                if item in tu:
                    hit += 1
            recall += len(tu)
            precision += self.n_rec_movie
        return (hit / (recall * 1.0), hit / (precision * 1.0))

    def coverage(self, train=None, test=None, k=5, nitem=10):
        train = self.traindata
        test = self.testdata
        recommend_items = set()
        all_items = set()
        for user in train.keys():
            for item in train[user].keys():
                all_items.add(item)
            rank = self.recommend(user, train=train, k=k, nitem=nitem)
            for item, _ in rank.items():
                recommend_items.add(item)
        return len(recommend_items) / (len(all_items) * 1.0)

    def popularity(self, train=None, test=None, k=5, nitem=10):
        train = self.traindata
        test = self.testdata
        item_popularity = dict()
        for user, items in train.items():
            for item in items.keys():
                item_popularity.setdefault(item, 0)
                item_popularity[item] += 1
        ret = 0
        n = 0
        for user in train.keys():
            rank = self.recommend(user, train=train, k=k, nitem=nitem)
            for item, _ in rank.items():
                if item in item_popularity:
                    ret += math.log(1 + item_popularity[item])
                    n += 1
        return ret / (n * 1.0)

    def RMSE(self, records):
        return math.sqrt( \
            sum([(rui - pui) * (rui - pui) for u, i, rui, pui in records]) \
            / float(len(records)))

    def MAE(self, records):
        return sum([abs(rui - pui) for u, i, rui, pui in records]) \
               / float(len(records))


if __name__ == "__main__":
    rating_file = './ml-latest-small/ratings.csv'
    cf = KNN()
    cf.get_dataset(rating_file)
    cf.ItemSim()
    print("%3s%20s%20s%20s%20s" % ('K', "precision精确度", 'recall召回率', 'coverage覆盖率', 'popularity流行度'))
    for k in [5,10,20,40,80,160]:
        recall, precision = cf.recallAndPrecision(k=k)
        coverage = cf.coverage(k=k)
        popularity = cf.popularity(k=k)       
        print("%3d%19.3f%%%19.3f%%%19.3f%%%20.3f" % (k, precision * 100, recall * 100, coverage * 100, popularity))


'''
  K           precision              recall            coverage          popularity
  5             24.516%              6.512%             12.500%               4.181
 10             25.872%              6.872%              9.934%               4.399
 20             27.243%              7.236%              8.578%               4.520
 40             27.213%              7.228%              7.710%               4.572
 80             26.438%              7.022%              6.745%               4.607
160             25.186%              6.690%              6.183%               4.562
'''