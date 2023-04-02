#######################################question1#######################################


# what are the numbers in the list?

numberslist = [84,16,1,75,44]

#find the minimum in an array
def findmin(l):
    if l ==[]:
        return None
    else:
        return findmin2(l, l[0])
        #return findmaxrecursive2(l, l[0])

def findmin2(l,min):
    if l == []:
        return min
    if l[0]<min:
        min=l[0]
    
    return findmin2(l[1:],min)

#find the max in an array list
def findmax(l):
    if l ==[]:
        return None
    else:
        return findmax2(l, l[0])

def findmax2(l,max):
    if l == []:
        return max
    if l[0]>max:
        max=l[0]
    
    return findmax2(l[1:],max)

#get the answers for the max and min

minx = findmin(numberslist)
maxx = findmax(numberslist)

print("the max number is ", maxx,", and the min number is", minx)


#######################################question2#######################################

#write a recursive function to reverse a lsit

#list we're using

problem2list = [24,12,4,2,55]

##define backwards recursive function
    
    #simple options:
        #problem2list.reverse()
        #print(problem2list)

        #problem2listreversed = problem2list[::-1]
        #print(problem2listreversed)

#def takeitbacknowyall, the actual recursiive function

def takeitbacknowyall(lst):
    if not lst:
        return[]
    return [lst[-1]] + takeitbacknowyall(lst[:-1])
    
reverselist = takeitbacknowyall(problem2list)
print(reverselist)
