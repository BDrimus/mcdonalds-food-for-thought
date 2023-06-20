import time

import config
from gui import display_gui
from survey import fill_out_survey

print (config.email)

def main():
    start_time = time.time()
    entry_code, date_of_order, time_of_order, amount_spent = display_gui()

    fill_out_survey(entry_code, date_of_order, time_of_order, amount_spent)

    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()