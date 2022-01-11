import MeCab
 
m = MeCab.Tagger()
comment ="gg"
node = m.parseToNode(comment)
while node:
    hin = node.feature.split(",")
    print(hin)
    node = node.next