n = input()

tmpOne = n.split('1')
tmpZ = n.split('0')

print(min(len(tmpOne)-tmpOne.count(''), len(tmpZ)-tmpZ.count('')))

