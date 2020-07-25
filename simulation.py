import csv

CSV_FILE = "MSFT.csv"
CASH = 3000
CHANGE = 0
EXIT_BARRIER = 0.98
BUY_PRECENTAGE = 1.01
SELL_PRECENTAGE = 0.99
AMOUNT_OF_STOCKS = 0
COMISSION = 0.00065
PURCHASED_STOCK_VALUE = 0.0

def main():
    trade()


def trade():
    global CASH

    first_trade = True
    with open(CSV_FILE) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            current_value = float(row[3])
            if first_trade:
                buy_stock(current_value)
                first_trade = False
            else:
                test_stock_oscillation(current_value)

        sell_stock(current_value)
        print ("After all trading the amount of cash is: " + str(CASH))


def buy_stock(current_value):
    global CASH
    global AMOUNT_OF_STOCKS
    global PURCHASED_STOCK_VALUE
    if AMOUNT_OF_STOCKS == 0:
        print("----------------------------")
        print ("Buying stock at value: " + str(current_value))
        AMOUNT_OF_STOCKS = int (CASH / current_value )
        CHANGE = CASH % current_value - (AMOUNT_OF_STOCKS*current_value*COMISSION)
        PURCHASED_STOCK_VALUE = current_value
        print ("After buying stocks,")
        print ("Amount of stocks:" + str(AMOUNT_OF_STOCKS))
        print ("Amount of change:" + str(CHANGE))
    return()


def sell_stock(current_value):
    global AMOUNT_OF_STOCKS
    global CASH
    if AMOUNT_OF_STOCKS != 0:
        print("----------------------------")
        print ("Selling stock at value: " + str(current_value))
        CASH = current_value*AMOUNT_OF_STOCKS + CHANGE - (AMOUNT_OF_STOCKS*current_value*COMISSION)
        AMOUNT_OF_STOCKS = 0
        print("After selling stocks,")
        print("Amount of cash:" + str(CASH))

    return()


def test_stock_oscillation(current_value):
    oscillation = current_value/PURCHASED_STOCK_VALUE
    if oscillation <= EXIT_BARRIER:
        sell_stock(current_value)
        exit()
    else:
        if oscillation <=  SELL_PRECENTAGE:
            sell_stock(current_value)
        if oscillation >= BUY_PRECENTAGE:
            buy_stock(current_value)
    return()


if __name__ == "__main__":
        main()