import pymysql
from sql import host,user,password,dbname


try:
    conn = pymysql.connect(host=host,user=user,port=3306, passwd=password,database=dbname)
    print('successfully connected to database')

    while True:
        try:

            imp = input('Введите номер заказа:')
            if imp == '':
                break
            imp=int(imp)
            with conn.cursor() as cursor:
                cursor.execute('SELECT id FROM shops.order')
                id_orders = cursor.fetchall()
                found = False

                for id_order in id_orders:
                    if id_order[0] == imp:
                        found = True
                        break

                if found != True:
                    print('Номер заказа введен не верно, попробуйте снова или нажмите enter чтобы выйти')

                if found == True:
                    cursor.execute(
                        'SELECT shops.order.id, count, device.name, rack.stellage, rack_dop.stil_dop FROM shops.order INNER JOIN shops.main ON product_id = articul INNER JOIN shops.device ON device_id=device.id INNER JOIN shops.rack ON rack_main_id=rack.id INNER JOIN shops.rack_dop ON rack_dop_id=rack_dop.id '
                        'WHERE shops.order.id = %s', (imp,))

                    shoping = cursor.fetchall()
                    for shop in shoping:
                           print(f"\n=== Стеллаж {shop[3]}")
                        print(f"{shop[2]}")
                        print(f"заказ {shop[0]}, {shop[1]} шт")
                        print(f"доп стеллаж: {shop[4]}")



        except Exception as ex:
            print('not successful')


finally:
    conn.close()



