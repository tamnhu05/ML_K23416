import sqlite3
import pandas as pd
def customers_with_min_invoices(customers_df, invoices_df, N):
    invoice_stats = invoices_df.groupby("CustomerId").agg(
        InvoiceCount=("InvoiceId", "count"),
        InvoiceValue=("Total", "sum")
    ).reset_index()

    result = customers_df.merge(invoice_stats, on="CustomerId")
    result = result[result["InvoiceCount"] >= N]

    return result[["CustomerId", "InvoiceCount", "InvoiceValue"]]

conn = sqlite3.connect("../../databases/Chinook_Sqlite.sqlite")
customers = pd.read_sql_query("SELECT * FROM Customer", conn)
invoices = pd.read_sql_query("SELECT * FROM Invoice", conn)

conn.close()

df_result = customers_with_min_invoices(customers, invoices, N=2)
print(df_result)

