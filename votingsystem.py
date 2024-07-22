nominee1 = input(" Enter the name of the first nominee: ")
nominee2 = input(" Enter the name of the second name: ")

nm1_vote = 0
nm2_vote = 0


voter_id = [1,2,3,4,5,6,7,8,9,10]

no_of_voter = len(voter_id)


while True:
    if voter_id ==[]:
        print("Voting session is over !!!")
        if nm1_vote> nm2_vote:
            percent= (nm1_vote/no_of_voter)*100
            print(nominee1, "has won the election with",percent,"% of votes")
            break
        elif nm1_vote < nm2_vote:
            percent= (nm2_vote/no_of_voter)*100
            print(nominee2, "has won th eelction",percent, "% of the votes")
            break
        else:
            print("Both the candidates have equal number of votes !! Government will decide an action on it")
            break
                
    voter = int(input("Enter your voter id: "))
    if voter in voter_id:
        print ("you are a voter")
        voter_id.remove(voter)
        print("--------------------------------")
        print("To give vote to", nominee1, "Press 1")
        print("to give vote to",nominee2, "Press 2")
        print("---------------------------------")
        vote = int(input("Enter your precious vote :"))
        if vote == 1:
            nm1_vote +=1
            print(nominee1, "Thanks to your important vote !!")
        elif vote ==2:
            nm2_vote +=1    
            print(nominee2, "Thanks to your important vote !!")
        elif vote > 2:
            print("Please Check your pressed key!")
        else :
            print(" You are not a voter or You already voted!!")    
            
        