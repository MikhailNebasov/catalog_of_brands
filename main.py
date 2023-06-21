import pandas as pd

df = pd.read_csv('C:/Users/nebas/source/repos/catalog_of_brands/catalog_of_brands.csv', sep='\t')
df_list1 = list(df['brand'])
df_list2 = list(df['alt_brand'])


# Enter searching brand
print('Enter brand you want to search')
searching_word = input()

# Settle with search result
if searching_word in df_list1:
    print('Brand you have searched is already in list. Nothing to add')
else:
    print('Brand you have searched is not in list. Press "Y" if you want to add it to list of brands or another key to skip this operation')
    decision = input()
    if decision == 'Y':
        df_list1.append(searching_word)
        print('Enter also alternative writing of brand using russian language')
        alt_brand = input()
        df_list2.append(alt_brand)
        df_out = pd.DataFrame(list(zip(df_list1, df_list2)), columns=['brand', 'alt_brand'])
        df_out.to_csv('C:/Users/nebas/source/repos/catalog_of_brands/catalog_of_brands.csv', sep='\t', index=False)
        print('Brand was added to list of brands')