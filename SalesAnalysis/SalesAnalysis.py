import pandas as pd
import glob
import calendar
import matplotlib.pyplot as plt

all_data = pd.read_csv("all_months_data.csv")

# Task-1: Merging 12 months of data in a single file
def task_1_merge_all_months_data():
    l = [pd.read_csv(filename) for filename in glob.glob("./Sales_Data/*")]
    all_months_data = pd.concat(l, axis=0)
    all_months_data.to_csv("all_months_data.csv", index=False)

# Task-2: What was the best month for sales? How much was earned that month?
def task_2_best_month_for_sales(all_data):
    # Lets clean the data.
    # Add columns with proper values for months
    all_data["Month"] = all_data["Order Date"].str[0:2]

    # Find NaN values
    nan_df = all_data[all_data.isna().any(axis=1)]
    # print(nan_df.head())

    # drop nan rows & other garbage rows
    all_data = all_data.dropna(how='all')
    all_data = all_data[all_data["Order Date"].str[0:2] != "Or"]

    # Convert columns types to correct ones
    all_data["Month"] = all_data["Month"].astype("int32")
    # all_data["Month"] = all_data["Month"].apply(lambda x: calendar.month_abbr[x])
    all_data["Quantity Ordered"] = pd.to_numeric(all_data["Quantity Ordered"])
    all_data["Price Each"] = pd.to_numeric(all_data["Price Each"])

    # Now, lets look at sales for each row. Sales = Qty * Price
    all_data["Sales"] = all_data["Quantity Ordered"] * all_data["Price Each"]
    
    # ans for the questions:
    sum_all_data = all_data.groupby("Month").sum()
    print(sum_all_data)

    # lets visualize the analysis to get the ans easily.
    all_months = range(1,13)
    plt.bar(all_months, sum_all_data["Sales"])
    plt.xlabel("Month Number")
    plt.ylabel("Sales in USD ($)")
    plt.show()

# Task 3: What city had the highest number of sales?
def task_2_city_with_highest_number_of_sales(all_data):
    
    print(all_data.head())
    # Lets clean the data.
    # Add city column

task_2_city_with_highest_number_of_sales(all_data)