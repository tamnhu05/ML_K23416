import pandas as pd

def top3_products_sold(df, by_value=False):

    if by_value:
        df["SalesValue"] = df["UnitPrice"] * df["Quantity"] * (1 - df["Discount"])
        product_totals = df.groupby("ProductID")["SalesValue"].sum()
    else:
        product_totals = df.groupby("ProductID")["Quantity"].sum()

    top3 = product_totals.sort_values(ascending=False).head(3).reset_index()
    return top3

df = pd.read_csv("../datasets/SalesTransactions/SalesTransactions.csv")

print("Top 3 sản phẩm theo số lượng:")
print(top3_products_sold(df, by_value=False))

print("\nTop 3 sản phẩm theo doanh thu:")
print(top3_products_sold(df, by_value=True))
