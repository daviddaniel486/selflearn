def main():
    house_price = int(1000000)
    print('This house sale price is at $1,000,000')
    buyer_credit = int(input('What is your credit score? '))
    #set good credit
    is_good_credit = buyer_credit >= 700
    if is_good_credit:
        new_price = house_price * 0.9
        print('You can get the house for', new_price)
    else:
        new_price = house_price * 0.8
        print('You can get the house for $' + str(new_price))



























































if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
