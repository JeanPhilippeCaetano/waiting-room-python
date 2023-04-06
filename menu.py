class Menu:
    def __init__(self):
        self.options = {"1": ("Add patient", self.option_1),
                        "2": ("Add doctor", self.option_2),
                        "3": ("Get most urgent patient", self.option_3)}

    def afficher_menu(self):
        print("Choisissez une option :")
        for key, value in self.options.items():
            print(f"{key}: {value[0]}")

    def executer_action(self, option):
        try:
            self.options[option][1]()
        except KeyError:
            print("Option invalide.")

    def option_1(self):
        print("Vous avez choisi l'option 1.")

    def option_2(self):
        print("Vous avez choisi l'option 2.")

    def option_3(self):
        print("Vous avez choisi l'option 3.")

menu = Menu()
menu.afficher_menu()
option = input("Entrez votre choix : ")
menu.executer_action(option)