''' 5.15 Tuples representing Invoices
        Use tuples to represent hardware store invoices that consist of four pieces of data:
            - ID: String
            - Description : String
            - Quantity : Integer
            - Item price : Float

    Part Number(ID)         Part Description        Quantity        Price
        83                   Electric sander            7           $57.98
        24                   Power saw                 18           $99.99
        7                    Sledge Hammer             11           $21.50
        77                   Hammer                    76           $11.99
        39                   Jig saw                    3           $79.50

    '''

from operator import itemgetter

invoices = [
    ('83', 'Electric sander', 7, 57.98),
    ('24', 'Power saw', 18, 99.99),
    ('7', 'Sledge Hammer', 11, 21.50),
    ('77', 'Hammer', 76, 11.99),
    ('39', 'Jig saw', 3, 79.50)
]

# a) Sort the invoices based on the first element (ID)
sorted_invoices_descr = sorted(invoices, key=itemgetter(1))
print("Part Number(ID)   Part Description   Quantity   Price")
for invoice in sorted_invoices_descr:
    print(f"    {invoice[0]}            {invoice[1]:<20} {invoice[2]}         ${invoice[3]:.2f}")

print()
# b)  Sort the invoices based on the fourth element (Price)
sorted_invoices_price = sorted(invoices, key=itemgetter(3))
print("Part Number(ID)   Part Description   Quantity   Price")
for invoice in sorted_invoices_price:
    print(f"    {invoice[0]}            {invoice[1]:<20} {invoice[2]}         ${invoice[3]:.2f}")

print()
# c)
# Map each invoice tuple to a tuple containing the part description and quantity
part_desc_quantity = map(lambda invoice: (invoice[1], invoice[2]), invoices)

# Sort the results by quantity
sorted_part_desc_quantity = sorted(part_desc_quantity, key=lambda x: x[1])

# Display the sorted results
print("Part Description   Quantity")
for item in sorted_part_desc_quantity:
    print(f"    {item[0]:<20} {item[1]}")
