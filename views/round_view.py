class RoundView:
    @staticmethod
    def display_round(round):
        print(f"Round: {round.name}")
        print(f"Start time: {round.start_time}, End time: {round.end_time}")
        for match in round.matches:
            MatchView.display_match(match)

    @staticmethod
    def input_start_and_end_times(round):
        round.start_time = input("Entrer l'heure de début du tour: ")
        round.end_time = input("Entrer l'heure de fin du tour: ")
