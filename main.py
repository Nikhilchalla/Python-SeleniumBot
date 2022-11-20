from booking.booking1 import Booking

try:

    with Booking() as bot:
        bot.land_first_page()
        bot.currency_change(currency='USD')
        bot.search_place_to_go('NEW YORK')
        bot.select_dates(check_in='2022-11-16',
                         check_out='2022-11-19')
        bot.select_adult(1)
        bot.click_search()
        bot.apply_filtrations()

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;G:/SeleniumDrivers \n \n'
             )
    else:
        raise







