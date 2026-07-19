no = 11     

def Display():
    global no
    no = 21
    print("from display: ",no)

print("before: ",no )
Display()
print("after: ",no)
