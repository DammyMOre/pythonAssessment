class Register:
    def __init__(self):
        candidate= []
        voters = {}

        def register_voter(self, voter):
            if voter.voter_id not in self.voters:
                self.voters[voter.voter_id] = voter
                print(f"Voter {voter.name} registered successfully!")
            else:
                print("Voter already registered.")

        def verify_voter(self, voter_id):
            if voter_id in self.voters:
                voter = self.voters[voter_id]
                if voter.is_eligible():
                    return True
                else:
                    print(f"Voter {voter.name} is not eligible to vote.")
            else:
                print("Voter not found.")
            return False




