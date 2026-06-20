#anonymus auction
print("logo here")


more_person = True
big = 0
winner = ''
dic = {
        'name':[],
        'bid': []
        }

while more_person:
    
    
    name =  input("enter ur name:\n")
    bid = int(input('enter ur bid:\n'))

    dic['name'].append(name)
    dic['bid'].append(bid)
    
    

    more_bidder = input("is there more ppl to bid? yes or no:\n").lower()
    
    
    if more_bidder == "no":
        more_person = False
        print('\n'*100)
    else:
        print('\n'*100)
        
        
for i in range(len(dic['bid'])):
    if dic['bid'][i] > big:
        big = dic['bid'][i]
        winner = dic['name'][i]

print(f"Winner is {winner} with ₹{big}")


