# team_dynamics.py

class TeamMember:
    def __init__(self, name, role, communication, productivity, morale):
        """
        Initialize a team member with name, role, communication, productivity, and morale levels.
        :param name: str, the name of the team member
        :param role: str, the role of the team member
        :param communication: int, communication skill level (1-10)
        :param productivity: int, productivity level (1-10)
        :param morale: int, morale level (1-10)
        """
        self.name = name
        self.role = role
        self.communication = communication
        self.productivity = productivity
        self.morale = morale
    
    def __repr__(self):
        return f"{self.name} ({self.role}) - Comm: {self.communication}, Prod: {self.productivity}, Morale: {self.morale}"


class TeamDynamics:
    def __init__(self, team_members):
        """
        Initialize a team with a list of TeamMember objects.
        :param team_members: list, a list of TeamMember objects
        """
        self.team_members = team_members
    
    def average_performance(self):
        """
        Calculate the average team performance based on communication, productivity, and morale.
        :return: dict, with average communication, productivity, and morale
        """
        total_communication = sum([member.communication for member in self.team_members])
        total_productivity = sum([member.productivity for member in self.team_members])
        total_morale = sum([member.morale for member in self.team_members])

        avg_communication = total_communication / len(self.team_members)
        avg_productivity = total_productivity / len(self.team_members)
        avg_morale = total_morale / len(self.team_members)
        
        return {
            "average_communication": avg_communication,
            "average_productivity": avg_productivity,
            "average_morale": avg_morale
        }

    def team_status(self):
        """
        Return the overall team status based on average performance.
        :return: str, a status message
        """
        performance = self.average_performance()

        if performance["average_morale"] >= 8 and performance["average_productivity"] >= 8:
            return "The team is highly productive and motivated."
        elif performance["average_morale"] >= 5 and performance["average_productivity"] >= 5:
            return "The team is doing well, but there's room for improvement."
        else:
            return "The team is struggling with low morale and productivity."

    def print_team_details(self):
        """
        Print the details of all team members.
        """
        for member in self.team_members:
            print(member)


# Example usage:
if __name__ == "__main__":
    # Create team members
    member1 = TeamMember("Alice", "Developer", 8, 7, 9)
    member2 = TeamMember("Bob", "Designer", 6, 6, 6)
    member3 = TeamMember("Charlie", "Manager", 9, 8, 8)

    # Initialize team dynamics with team members
    team = TeamDynamics([member1, member2, member3])

    # Print the average performance
    print("Team Performance:", team.average_performance())

    # Get team status
    print("Team Status:", team.team_status())

    # Print team details
    team.print_team_details()
