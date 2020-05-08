
n = int(input())
m = int(input())
vote_num_of = {}
votes_of = {}
for i in range(n):
    person_name, nb_vote = input().split()
    nb_vote = int(nb_vote)
    vote_num_of[person_name] = nb_vote
    votes_of[person_name] = [0, 0, 0]

for i in range(m):
    voter_name, vote_value = input().split()
    if voter_name in votes_of:
        if vote_value == "Yes":
            votes_of[voter_name][0] += 1
        elif vote_value == "No":
            votes_of[voter_name][1] += 1
        else:
            votes_of[voter_name][2] += 1

yes, no = 0, 0
for voter in votes_of:
    if sum(votes_of[voter]) <= vote_num_of[voter]:
        yes, no = yes + votes_of[voter][0], no + votes_of[voter][1]

print("{} {}".format(yes, no))
