# # <!-- convert given list of codes onto dictionary into counter (iterator method). We will have a dictionary having candidate names
# # as keys and freq as values. Since more than one candidate may get the same num of votes and in this situation we need to print 
# # lexicographically smaller name, so now we will create another dictionary  by traversing prev created dictionary count of votes
# # will be key and candidate names will be values. Now find the value of maximum  set for a candidate and get list of candidates 
# # mapped on that count file. Now sort list of candidates having same number of maximum votes and print first element of sorted list
# # In order to print lexicographically smaller plane. -->


# from collections import Counter

# def winner(arr):
# 	votes=Counter(arr)
# 	dict = {}
# 	for value in votes.values():
# 		dict[value] = []
# 	for (key,value) in votes.items():
# 		dict[value].append(key)
  
# 	maxVote = sorted(dict.keys(),reverse=True)[0]
 
# 	if len(dict[maxVote])>1:
# 		print (sorted(dict[maxVote])[0])
# 	else:
# 		print (dict[maxVote][0])
  
# if __name__ == "__main__":
# 	arr=['john','johnny','john','john','johnny','jamie','johnny','john']
# 	winner(arr)
 
# votes_count=Counter(votes)
# max_votes=max(votes_count.values())

#----------------------------------------

# function to mirror characters 

def mirrorChars(input,k):
	original = 'abcdefghijklmnopqrstuvwxyz'
	reverse = 'zyxwvutsrqponmlkjihgfedcba'
	dictChars = dict(zip(original,reverse))
	prefix = input[0:k-1]
	suffix = input[k-1:]
	mirror = ''
	for i in range(0,len(suffix)):
		mirror = mirror + dictChars[suffix[i]]
	print (prefix+mirror)
if __name__ == "__main__":
	input = 'paradox'
	k = 3
	mirrorChars(input,k)

#-----------------------------------------------

def CounterFreq(my_list):
    freq=[]
    for item in my_list:
        if(item in freq):
            freq[item]+=1
        else:
            freq[item]=1
if __name__=="__name__":
    my_list=[1,1,1,5,5,3,1,3,3,1,4,4,4,2,2,2,2]
    CounterFreq(my_list)
    
#------------------------------------------------

jack=["name"]
dylan=["name": "Dylan Rhodes","assignment":[77,82]]