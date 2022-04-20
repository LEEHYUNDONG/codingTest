# import re

# s = input()
# s = list(s.split('</div>'))
# patTitle = re.compile('<div title=\"(\S+)\">')
# patPara = re.compile('<p>(.+)</p>')

# def checkTag(st):
#     if len(st) % 2 != 0: # 문단에 포함할 수 없음
#         return False
#     else: # 답에 포함 가능
#         tmp = []
#         for i in range(len(st)):
#             if '/' not in st[i]:
#                 tmp.append(st[i])
#             if tmp and st[i].startswith('/'):
#                 if tmp[-1] == st[i].replace('/', ''):
#                     tmp.pop()
#         if len(tmp):
#             return False
#         return True


# answer = []
# for div in s:
#     t = re.findall(patTitle, div)
#     para = re.findall(patPara, div)
#     if t != []: # 타이틀 넣기
#         answer.append('title : {}'.format(t[0]))
#     if para != []: # 문단 넣기
#         para = list(para[0].split('</p>'))
#         st = []
#         for p in para:
#             if '<p>' in p or '</p>' in p:
#                 tagP = re.compile('<([a-zA-Z\s/]+)>')
#                 for tag in re.findall(tagP, p): # 태그 갯수 맞추기
#                     tag = tag.strip()
#                     if tag == 'p' or tag == 'br': 
#                         continue
#                     st.append(tag)
                
#                 tmp = checkTag(st)
#                 if tmp:
#                     p = re.sub(r'<p>', '', p)
#                     p = re.sub(r'</p>', '', p)
#                     p = re.sub(r'</?[\w ]*>', '', p)
#                     p = re.sub(r' ?\n ?', '', p)
#                     p = re.sub(r' {2,}', ' ', p)
                    
#                     answer.append(p.strip())
#             else:
#                 answer.append(p.strip())

# for i in answer:
#     print(i)


import re
s = input()

s = s[len('<main>'): -len('</main>')]
s = re.sub(r'<div +title="([\w ]*)">', r'title : \1\n', s)
s = re.sub(r'</div>', '', s)
s = re.sub(r'<p>', '', s)
s = re.sub(r'</p>', '\n', s)
s = re.sub(r'</?[\w ]*>', '', s)
s = re.sub(r' ?\n ?', '\n', s)
s = re.sub(r' {2,}', ' ', s)

print(s)