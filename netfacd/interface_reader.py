import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('/n************details of interface - ' + i + ' ************')
    try:
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) 
    except:
        print('could not collect adapter information')