"""
Voting System

Task:
- Implement a simple voting system.
- Store candidates in a dictionary { "candidate_name": vote_count }
- Allow voters (by ID) to vote only once.
- Use *args to register multiple candidates at once.
- Use **kwargs to update candidate details like party, region.


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Candidate as a class.
- Voter as a class with has_voted flag.
- Election as a manager class.
"""

candidates = {}
voters = set() 

def register_candidates(*args, **kwargs):
    """Register candidates with optional metadata.
    """
    for candidate in args:
        candidates[candidate] = {"votes": 0, **kwargs}
    return f"Candidates registered: {', '.join(args)}"

def cast_vote(voter_id, candidate):
    """Cast vote if voter has not voted before.
        after all the vote logic is completeted sucessfully,
        return: Vote casted for {candidate}.
    """
    if voter_id in voters:
        return "You have already voted"
    if candidate not in candidates:
        return "Candidate not found"
    candidates[candidate]["votes"] += 1
    voters.add(voter_id)
    return f"Vote casted for {candidate}"

def election_result():
    """Return the winner(s)."""
    if not candidates:
        return "No candidates registered"
    max_votes = max(c["votes"] for c in candidates.values())
    winners = [name for name, data in candidates.items() if data["votes"] == max_votes]
    return {"winners": winners, "candidates": candidates}

print(register_candidates("tom", "jerry", "mimi", party="APC", region="North"))
print(cast_vote("v1", "tom"))
print(cast_vote("v2", "mimi"))  
print(election_result())

