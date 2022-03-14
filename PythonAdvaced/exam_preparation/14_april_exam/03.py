def flights(*args):
    flights_dict={}
    for i in range(len(args)):
        if args[i]=='Finish':
            break
        elif not str(args[i]).isdigit():
            if args[i] not in flights_dict:
                flights_dict[args[i]]=0
            if i+1<len(args):
                flights_dict[args[i]]+=int(args[i+1])

    return flights_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))