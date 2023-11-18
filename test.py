product_details=[[ 'Leather wallet',1100,18,1],
    ['Umbrella',900,12,4],
    ['Cigarette',200,28,3],
    ["Honey",100,0,2]]

max_gst_product=""

max_gst=0

total_amt=0

for i in product_details:
    gst=((i[1]*i[2])/100)*i[3]
    total_price=(i[1]*i[3])+gst
    if i[1]>=500:

        disc=((i[1]*5)/100)*i[3]
        total_price=(total_price)-disc
        total_amt=total_price+total_amt
    else:
        total_amt=total_price+total_amt
    if max_gst<gst:
        max_gst_product=i[0]
        max_gst=gst
print(f'the maximum best product is {max_gst_product}')
print(f'the total price is {total_amt}')
