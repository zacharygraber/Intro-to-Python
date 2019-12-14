#INPUT huffman tree, current code taken from edges
#OUTPUT build dictionary of words and code
#NOTHING is explicitly returned, it should fill in the dictionary d
#RECURSIVE FUNCTION
def make_code(xlst,code):
#TO DO:IMPLEMENT

#INPUT list of word, count pairs
#OUTPUT huffman tree with a single node
#[node, [0 or 1, [node]]]
def make_tree(xlst):
    #INPUT a list
    #RETURN a tuple with the two smallest values
    def twoMins(xlst):
        tempList = xlst
        min1 = xlst[0]
        min2 = xlst[1]
        for i in tempList:
            if i < min1:
                min1 = i
        tempList.remove(min1)
        for i in tempList:
            if i < min2:
                min2 = i
        return (min1, min2)

    while len(xlst > 1):
        x,y = twoMins([i[1] for i in xlst])
        node = x+y
        



###DATA
xlst = [['w',7],['u',12],['x',15],['v',18],['y',20]]
d = {}
f = lambda x: x[1] if type(x[0]) == str else x[0]
xlst.sort(key=f) #sorts either original or new nodes 
print(xlst)

make_tree(xlst)
make_code(xlst[0],"")

print(d)