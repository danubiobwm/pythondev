import pandas as pd

ecom_sales = pd.read_csv(
    "./dados/ecom_sales.csv",
    )

#print(ecom_sales)
#print(ecom_sales.head())
ecom_sale=ecom_sales.groupby("Country")["OrderValue"].sum().reset_index(name="Total Sales").sort_values(by="Total Sales", ascending=False)
print(ecom_sale)