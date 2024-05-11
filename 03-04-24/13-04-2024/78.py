name='RAKESHRUSHITHA'
vowellist=["A",'E','I','O','U']
vowelcount=0
consonentscount=0
for i in name:
    if i in vowellist:
        vowelcount=vowelcount+1
    else:
        consonentscount=consonentscount+1
print(vowelcount)
print(consonentscount)