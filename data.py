import pandas as pd

# Sample purchase data: 1 = bought, 0 = not bought
data = {
    'Product_A': [1, 0, 1, 0, 1],
    'Product_B': [0, 1, 0, 1, 0],
    'Product_C': [1, 1, 0, 0, 1],
    'Product_D': [0, 0, 1, 1, 0],
    'Product_E': [1, 0, 1, 0, 1],
}

customers = ['Cust_1', 'Cust_2', 'Cust_3', 'Cust_4', 'Cust_5']

purchase_df = pd.DataFrame(data, index=customers)

def get_purchase_data():
    return purchase_df
