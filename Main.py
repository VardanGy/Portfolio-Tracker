from Model import buy, sell, build_situation
from View import Display


while True:

    display = Display()

    choice = display.show_menu()

    if choice == "1":
        date, name, ticker, quantity, price, fees = display.ask_buy()

        buy(date, name, ticker, quantity, price, fees)

        print("Achat enregistré")

    elif choice == "2":
        date, name, ticker, quantity, price, fees = display.ask_sell()

        sell(date, name, ticker, quantity, price, fees)

        print("Vente enregistrée")

    elif choice == "3":
        situation = build_situation()

        display.display_situation(situation)

    elif choice == "4":
        break

    else:
        print("Choix invalide")