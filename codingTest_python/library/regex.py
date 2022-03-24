import re

p = re.compile('[a-z]+')
f = p.finditer("python hello world 12word deram!!!")

# print(dir(re.Match))
for find in f:
    print(find, end=' ')
    print(find.span())


p = re.compile(r"[a-zA-Z0-9_-]+@[a-z]+.[a-zA-Z]+$")
s1 = "easttwave@gmail.com"
s2 = "e123123!!!@gmail.com"
s3 = "e123123@gmail.com123"

res = p.findall(s1)
print(res)
res = p.match(s2)
print(res)
res = p.match(s3)
print(res)

p = re.compile(r'(\w+)\s+(\d+[-]+\d+[-]\d+)')
res = p.search("leehyundong 010-1234-4321")
print(res.group(1))
print(res.group(2))

s = "korean american italian"
res = re.sub('n', '', s)
print(res)
