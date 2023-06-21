import pandas as pd

df = pd.read_csv('C:/Users/nebas/source/repos/list_of_brands/catalog_of_brands.csv', sep='\t')
df_list = list(df['brand'])

# Enter searching brand
print('Enter brand you want to search')
searching_word = input()

# Settle with search result
if searching_word in df_list:
    print('Brand you have searched is already in list. Nothing to add')
else:
    print('Brand you have searched is not in list. Press "Y" if you want to add it to list of brands or another key to skip this operation')
    decision = input()
    if decision == 'Y':
        df_list.append(searching_word)
        df_list = sorted(df_list)
        df_out = pd.DataFrame(list(zip(df_list)), columns=['brand'])
        df_out.to_csv('C:/Users/nebas/source/repos/list_of_brands/catalog_of_brands.csv', sep='\t', index=False)
        print('Brand was added to list of brands')