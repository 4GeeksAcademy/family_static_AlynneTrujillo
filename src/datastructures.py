
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members.  // might need something here to say which ID is next??
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["last_name"] = self.last_name
        member["id"] = self._generateId()
        member["lucky_numbers"] = list(member["lucky_numbers"])
        self._members.append(member)
        return member

    def delete_member(self, id):
        # FOR LOOP? --- has to be connected to ID?
        for id in range(len(self._members)):
            if self._members[id]["id"] == id:
                self._members.pop(id)
                return None

    def get_member(self, id):
        for one_member in self._members:
            if one_member ["id"] == int(id):
                return one_member
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
