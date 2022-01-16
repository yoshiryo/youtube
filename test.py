import MeCab
import ipadic
m = MeCab.Tagger(ipadic.MECAB_ARGS)
comment ="おおおおお"
print(m.parse(comment))
node = m.parseToNode(comment)
while node:
    hin = node.feature.split(",")[0]
    s = node.surface
    if hin == "名詞":
        print(s)
    node = node.next