a=[1,2,3]
b=['11','22','33']
c=[True,False,True]

listinfo=[]

listinfo = [{'number':aa,'str':bb,'bool':cc} for aa,bb,cc in zip(a, b, c)]

# for aa,bb,cc in zip(a,b,c):
#     listinfo.append({'number':aa,'str':bb,'bool':cc})


print (listinfo)


