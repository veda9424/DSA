def most_updated_menu(menu):
    num_items = len(menus[0])

    max_prices = max[max(item_prices) for item_prices in zip(*menus)]    #zip(*menus) transposes the list — it groups prices by item across all menus.

    max_good_count = -1    #We initialize with -1 so even if a menu has 0 good prices, it will still be considered better than -1 and the comparison will work.
    best_avg = -1    #Starting with -1 means any real average will be larger, and the comparison will work as expected when breaking ties.
    best_index = -1   # because we also have to consider the menu at the 0 index position

    for i,menu in enumerate(menus):
        good_count = sum(menu[j] == max_price[j])