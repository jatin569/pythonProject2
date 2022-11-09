'''
REQ:
Get highest sold out product of specific month
'''
data = {'A': [100, 80], 'B': [200, 140], 'C': [150, 100], 'D': [250, 230], 'E': [225, 215]}

months = {'A': [['Jan', 10], ['Mar', 2]],
          'E': ['Feb', 5],
          'C': ['Mar', 25],
          'D': ['Jan', 5],
          'B': ['Feb', 15]
          }

def get_highest(months, data):
    # I. Get profit of each product
    di = {}
    for p, sales in data.items():
        di[p] = sales[0] - sales[1]
    print("Profit of each product            : ", di)

    # II. Get month wise product profits
    fdi = {}
    for product, sales in months.items():
        if type(sales[0]) != list:
            p_profit = di[product] * sales[1]
            if sales[0] not in fdi.keys():
                fdi[sales[0]] = [[product, p_profit]]
            else:
                fdi[sales[0]].append([product, p_profit])
        else:
            for rec in sales:
                # print("RECORD : ", rec)
                p_profit = di[product] * rec[1]
                # print("DETAILS : ", product, rec[0], p_profit)
                if rec[0] not in fdi.keys():
                    fdi[rec[0]] = [[product, p_profit]]
                else:
                    fdi[rec[0]].append([product, p_profit])
    print("Monthwise product sales           : ", fdi)
    # III. Monthly wise highest sales
    monthly = {}
    p_max_sale = 0
    p_prod = None
    for month, sales in fdi.items():
        for pr, val in sales:
            if val >= p_max_sale:
                p_max_sale = val
                p_prod = pr
        monthly[month] = [p_prod, p_max_sale]
    print("Monthly highest sales             : ", monthly)
    # IV. Highest sold out product details of all months
    high_val = 0
    high_prod = None
    month = None
    for mon, sales in monthly.items():
        if sales[1] > high_val:
            high_prod, high_val = sales[0], sales[1]
            month = mon
    print("Monthly highest sold product      : ", month, high_val, high_prod)
    print("Product wise highest sold in year : ", p_max_sale, p_prod)

get_highest(months, data)
