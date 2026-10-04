```python
import csv
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from scipy import stats
import matplotlib.pyplot as plt

# Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Custom module
import analytics_module


FILE = "Walmart_DataSet.csv"


# ============================================================
# 1. PYTHON CORE CONCEPTS
# ============================================================

def python_core():

    print("\n--- 1. Python Core Concepts ---")

    project = "Walmart Sales Analysis and Forecasting"

    # Read number of records from dataset
    records = len(df)

    print("Project:", project)
    print("Dataset Records:", records)

    if records > 0:
        print("Dataset contains Walmart sales records.")

    # Simple loop
    print("\nImportant Dataset Fields:")

    for item in ["Store", "Date", "Weekly_Sales",
                 "Temperature", "Fuel_Price", "CPI"]:
        print("-", item)

    # Simple condition
    average_sales = df["Weekly_Sales"].mean()

    if average_sales > 1000000:
        print("\nAverage weekly sales are above 1 million.")


# ============================================================
# 2. DATA STRUCTURES
# ============================================================

def data_structures():

    print("\n--- 2. Data Structures ---")

    # List
    concepts = [
        "Python",
        "Pandas",
        "NumPy"
    ]

    # Tuple
    years = (
        "2010",
        "2011",
        "2012"
    )

    # Set
    stores = set(df["Store"].head(10))

    # Dictionary
    sales_record = {
        "Store": int(df.iloc[0]["Store"]),
        "Weekly_Sales": float(df.iloc[0]["Weekly_Sales"])
    }

    concepts.append("SciPy")

    print("List:", concepts)
    print("Tuple:", years)
    print("Set:", stores)
    print("Dictionary:", sales_record)


# ============================================================
# 3. PYTHON LIBRARIES
# ============================================================

def python_libraries():

    print("\n--- 3. Python Libraries ---")

    print("NumPy Version:", np.__version__)
    print("Pandas Version:", pd.__version__)
    print("SciPy Version:", stats.__name__)

    print("Requests and BeautifulSoup imported successfully.")
    print("Matplotlib imported successfully.")
    print("Scikit-learn imported successfully.")


# ============================================================
# 4. CUSTOM MODULES
# ============================================================

def custom_modules():

    print("\n--- 4. Custom Modules ---")

    total_sales = df["Weekly_Sales"].head(10).sum()
    records = 10

    average = analytics_module.calculate_average_sales(
        total_sales,
        records
    )

    category = analytics_module.sales_category(average)

    print("Total Sales of First 10 Records:",
          round(total_sales, 2))

    print("Number of Records:", records)

    print("Average Sales:", round(average, 2))

    print("Sales Category:", category)


# ============================================================
# 5. EXCEPTION HANDLING
# ============================================================

def exception_handling():

    print("\n--- 5. Exception Handling ---")

    try:

        store = int(input("Enter Store Number: "))

        result = df[df["Store"] == store]

        if result.empty:
            raise ValueError("Store does not exist.")

        print(
            "Average Sales:",
            round(result["Weekly_Sales"].mean(), 2)
        )

    except ValueError as e:

        print("Error:", e)

    except Exception as e:

        print("Unexpected error:", e)


# ============================================================
# 6. WEB SCRAPING
# ============================================================

def web_scraping():

    print("\n--- 6. Web Scraping ---")

    try:

        url = "https://quotes.toscrape.com/"

        response = requests.get(
            url,
            timeout=10
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        quote = soup.find(
            "span",
            class_="text"
        )

        author = soup.find(
            "small",
            class_="author"
        )

        print(
            "Example Scraped Quote:",
            quote.get_text(strip=True)
        )

        print(
            "Author:",
            author.get_text(strip=True)
        )

    except requests.RequestException:

        print("Unable to access website.")


# ============================================================
# 7. FILE HANDLING
# ============================================================

def file_handling():

    print("\n--- 7. File Handling ---")

    try:

        with open(FILE, "r", encoding="utf-8") as file:

            reader = csv.reader(file)

            print("Columns:")
            print(next(reader))

            print("\nFirst Record:")
            print(next(reader))

    except FileNotFoundError:

        print("CSV file not found.")


# ============================================================
# 8. CRUD OPERATIONS
# ============================================================

def crud_operations(data):

    while True:

        print("\n--- 8. CRUD Operations ---")

        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Back to Main Menu")

        choice = input("Enter choice: ").strip()

        # ----------------------------------------------------
        # CREATE
        # ----------------------------------------------------

        if choice == "1":

            try:

                store = int(
                    input("Store Number: ")
                )

                weekly_sales = float(
                    input("Weekly Sales: ")
                )

                temperature = float(
                    input("Temperature: ")
                )

                fuel_price = float(
                    input("Fuel Price: ")
                )

                cpi = float(
                    input("CPI: ")
                )

                row = len(data)

                data.loc[row, "Store"] = store
                data.loc[row, "Date"] = "01-01-2013"
                data.loc[row, "Weekly_Sales"] = weekly_sales
                data.loc[row, "Temperature"] = temperature
                data.loc[row, "Fuel_Price"] = fuel_price
                data.loc[row, "CPI"] = cpi

                data.to_csv(
                    FILE,
                    index=False
                )

                print("Record created successfully.")

            except ValueError:

                print("Invalid input.")

        # ----------------------------------------------------
        # READ
        # ----------------------------------------------------

        elif choice == "2":

            try:

                store = int(
                    input("Enter Store Number: ")
                )

                result = data[
                    data["Store"] == store
                ]

                if result.empty:

                    print("Record not found.")

                else:

                    print(
                        result.head(10)
                        .to_string(index=False)
                    )

            except ValueError:

                print("Invalid Store Number.")

        # ----------------------------------------------------
        # UPDATE
        # ----------------------------------------------------

        elif choice == "3":

            try:

                store = int(
                    input("Enter Store Number: ")
                )

                sales = float(
                    input("New Weekly Sales: ")
                )

                index = data[
                    data["Store"] == store
                ].index

                if len(index) > 0:

                    data.loc[
                        index[0],
                        "Weekly_Sales"
                    ] = sales

                    data.to_csv(
                        FILE,
                        index=False
                    )

                    print(
                        "Record updated successfully."
                    )

                else:

                    print("Record not found.")

            except ValueError:

                print("Invalid input.")

        # ----------------------------------------------------
        # DELETE
        # ----------------------------------------------------

        elif choice == "4":

            try:

                store = int(
                    input("Enter Store Number: ")
                )

                index = data[
                    data["Store"] == store
                ].index

                if len(index) == 0:

                    print("Record not found.")

                else:

                    data.drop(
                        index[0],
                        inplace=True
                    )

                    data.reset_index(
                        drop=True,
                        inplace=True
                    )

                    data.to_csv(
                        FILE,
                        index=False
                    )

                    print(
                        "Record deleted successfully."
                    )

            except ValueError:

                print("Invalid Store Number.")

        elif choice == "5":

            break

        else:

            print("Invalid choice.")


# ============================================================
# 9. NUMPY
# ============================================================

def numpy_analysis(data):

    print("\n--- 9. NumPy ---")

    sales = np.array(
        data["Weekly_Sales"]
    )

    print(
        "Total Sales:",
        round(np.sum(sales), 2)
    )

    print(
        "Average Sales:",
        round(np.mean(sales), 2)
    )

    print(
        "Maximum Sales:",
        round(np.max(sales), 2)
    )

    print(
        "Minimum Sales:",
        round(np.min(sales), 2)
    )

    print(
        "Standard Deviation:",
        round(np.std(sales), 2)
    )


# ============================================================
# 10. SCIPY
# ============================================================

def scipy_analysis(data):

    print("\n--- 10. SciPy ---")

    sales = data[
        "Weekly_Sales"
    ].to_numpy()

    result = stats.describe(sales)

    print(
        "Mean:",
        round(result.mean, 2)
    )

    print(
        "Variance:",
        round(result.variance, 2)
    )

    print(
        "Minimum:",
        round(result.minmax[0], 2)
    )

    print(
        "Maximum:",
        round(result.minmax[1], 2)
    )


# ============================================================
# 11. PANDAS
# ============================================================

def pandas_analysis(data):

    print("\n--- 11. Pandas ---")

    print("\nFirst 5 Records:")

    print(
        data.head()
    )

    print("\nDataset Shape:")

    print(
        data.shape
    )

    print("\nMissing Values:")

    print(
        data.isnull().sum()
    )

    print("\nStore Count:")

    print(
        data["Store"]
        .value_counts()
        .head()
    )

    print("\nAverage Weekly Sales:")

    print(
        round(
            data["Weekly_Sales"].mean(),
            2
        )
    )


# ============================================================
# 12. DATA PREPROCESSING
# ============================================================

def data_preprocessing():

    print("\n--- 12. Data Preprocessing ---")

    data = df.copy()

    print(
        "Original Columns:"
    )

    print(
        data.columns.tolist()
    )

    # Remove unwanted columns
    data.drop(
        columns=[
            "Holiday_Flag",
            "Unemployment"
        ],
        errors="ignore",
        inplace=True
    )

    # Convert Date to datetime
    data["Date"] = pd.to_datetime(
        data["Date"],
        dayfirst=True,
        errors="coerce"
    )

    # Check missing values
    print("\nMissing Values Before Cleaning:")

    print(
        data.isnull().sum()
    )

    # Remove duplicate records
    data.drop_duplicates(
        inplace=True
    )

    # Fill missing numeric values
    numeric_columns = [
        "Weekly_Sales",
        "Temperature",
        "Fuel_Price",
        "CPI"
    ]

    for column in numeric_columns:

        data[column] = data[column].fillna(
            data[column].mean()
        )

    print(
        "\nColumns After Preprocessing:"
    )

    print(
        data.columns.tolist()
    )

    print(
        "\nMissing Values After Cleaning:"
    )

    print(
        data.isnull().sum()
    )

    print(
        "\nPreprocessing completed successfully."
    )


# ============================================================
# 13. DATA VISUALIZATION
# ============================================================

def data_visualization():

    print("\n--- 13. Data Visualization ---")

    data = df.copy()

    data["Date"] = pd.to_datetime(
        data["Date"],
        dayfirst=True
    )

    # Total sales by date
    daily_sales = (
        data.groupby("Date")["Weekly_Sales"]
        .sum()
    )

    # Line graph
    plt.figure(figsize=(10, 5))

    plt.plot(
        daily_sales.index,
        daily_sales.values
    )

    plt.title(
        "Walmart Total Weekly Sales"
    )

    plt.xlabel("Date")

    plt.ylabel("Weekly Sales")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()

    # Sales distribution
    plt.figure(figsize=(8, 5))

    plt.hist(
        data["Weekly_Sales"],
        bins=30
    )

    plt.title(
        "Distribution of Walmart Weekly Sales"
    )

    plt.xlabel("Weekly Sales")

    plt.ylabel("Frequency")

    plt.tight_layout()

    plt.show()


# ============================================================
# 14. STATISTICAL ANALYSIS
# ============================================================

def statistical_analysis():

    print("\n--- 14. Statistical Analysis ---")

    sales = df["Weekly_Sales"]

    print(
        "Mean:",
        round(sales.mean(), 2)
    )

    print(
        "Median:",
        round(sales.median(), 2)
    )

    print(
        "Mode:",
        round(sales.mode()[0], 2)
    )

    print(
        "Variance:",
        round(sales.var(), 2)
    )

    print(
        "Standard Deviation:",
        round(sales.std(), 2)
    )

    print(
        "Minimum:",
        round(sales.min(), 2)
    )

    print(
        "Maximum:",
        round(sales.max(), 2)
    )

    # Correlation
    print(
        "\nCorrelation between "
        "Temperature and Sales:"
    )

    print(
        round(
            df["Temperature"]
            .corr(df["Weekly_Sales"]),
            3
        )
    )

    print(
        "\nCorrelation between "
        "Fuel Price and Sales:"
    )

    print(
        round(
            df["Fuel_Price"]
            .corr(df["Weekly_Sales"]),
            3
        )
    )


# ============================================================
# 15. PROBABILITY
# ============================================================

def probability():

    print("\n--- 15. Probability ---")

    sales = df["Weekly_Sales"]

    average_sales = sales.mean()

    # Probability that a randomly selected
    # record has sales greater than average
    successful_records = (
        sales > average_sales
    ).sum()

    total_records = len(sales)

    probability_value = (
        successful_records /
        total_records
    )

    print(
        "Average Weekly Sales:",
        round(average_sales, 2)
    )

    print(
        "Records Above Average:",
        successful_records
    )

    print(
        "Total Records:",
        total_records
    )

    print(
        "Probability of Selecting "
        "Above-Average Sales:",
        round(probability_value, 3)
    )


# ============================================================
# 16. SAMPLING & INFERENCE
# ============================================================

def sampling_inference():

    print("\n--- 16. Sampling & Inference ---")

    sales = df["Weekly_Sales"]

    # Random sample of 100 records
    sample = sales.sample(
        n=100,
        random_state=42
    )

    sample_mean = sample.mean()

    population_mean = sales.mean()

    print(
        "Population Mean:",
        round(population_mean, 2)
    )

    print(
        "Sample Mean:",
        round(sample_mean, 2)
    )

    print(
        "Sample Size:",
        len(sample)
    )

    # Confidence interval
    confidence = 0.95

    standard_error = (
        stats.sem(sample)
    )

    interval = stats.t.interval(
        confidence,
        df=len(sample) - 1,
        loc=sample_mean,
        scale=standard_error
    )

    print(
        "\n95% Confidence Interval:"
    )

    print(
        "Lower:",
        round(interval[0], 2)
    )

    print(
        "Upper:",
        round(interval[1], 2)
    )


# ============================================================
# 17. HYPOTHESIS TESTING
# ============================================================

def hypothesis_testing():

    print("\n--- 17. Hypothesis Testing ---")

    sales = df["Weekly_Sales"]

    # H0:
    # Average weekly sales = 1,000,000
    #
    # H1:
    # Average weekly sales != 1,000,000

    test_value = 1000000

    result = stats.ttest_1samp(
        sales,
        test_value
    )

    print(
        "Hypothesized Mean:",
        test_value
    )

    print(
        "Calculated Mean:",
        round(sales.mean(), 2)
    )

    print(
        "T-Statistic:",
        round(result.statistic, 3)
    )

    print(
        "P-Value:",
        round(result.pvalue, 6)
    )

    significance_level = 0.05

    if result.pvalue < significance_level:

        print(
            "Result: Reject the null hypothesis."
        )

    else:

        print(
            "Result: Fail to reject "
            "the null hypothesis."
        )


# ============================================================
# 18. MACHINE LEARNING
# ============================================================

def machine_learning():

    print("\n--- 18. Machine Learning ---")

    data = df.copy()

    # Features
    X = data[
        [
            "Store",
            "Temperature",
            "Fuel_Price",
            "CPI"
        ]
    ]

    # Target
    y = data[
        "Weekly_Sales"
    ]

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    # Linear Regression model
    model = LinearRegression()

    model.fit(
        X_train,
        y_train
    )

    # Prediction
    predictions = model.predict(
        X_test
    )

    # Evaluation
    mae = mean_absolute_error(
        y_test,
        predictions
    )

    r2 = r2_score(
        y_test,
        predictions
    )

    print(
        "Training Records:",
        len(X_train)
    )

    print(
        "Testing Records:",
        len(X_test)
    )

    print(
        "Mean Absolute Error:",
        round(mae, 2)
    )

    print(
        "R² Score:",
        round(r2, 3)
    )

    # Example prediction
    example = pd.DataFrame({
        "Store": [1],
        "Temperature": [70],
        "Fuel_Price": [3.0],
        "CPI": [215]
    })

    predicted_sales = model.predict(
        example
    )

    print(
        "\nExample Predicted Weekly Sales:",
        round(predicted_sales[0], 2)
    )


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    global df

    try:

        df = pd.read_csv(FILE)

    except FileNotFoundError:

        print(
            "ERROR: CSV file not found."
        )

        print(
            "Put the Walmart CSV file "
            "in the same folder as main.py."
        )

        return

    # Remove unwanted columns
    df.drop(
        columns=[
            "Holiday_Flag",
            "Unemployment"
        ],
        errors="ignore",
        inplace=True
    )

    while True:

        print("\n" + "=" * 60)

        print(
            "       WALMART SALES ANALYSIS"
        )

        print("=" * 60)

        print("1.  Python Core Concepts")
        print("2.  Data Structures")
        print("3.  Python Libraries")
        print("4.  Custom Modules")
        print("5.  Exception Handling")
        print("6.  Web Scraping")
        print("7.  File Handling")
        print("8.  CRUD Operations")
        print("9.  NumPy")
        print("10. SciPy")
        print("11. Pandas")
        print("12. Data Preprocessing")
        print("13. Data Visualization")
        print("14. Statistical Analysis")
        print("15. Probability")
        print("16. Sampling & Inference")
        print("17. Hypothesis Testing")
        print("18. Machine Learning")
        print("19. Exit")

        print("=" * 60)

        choice = input(
            "Enter choice: "
        ).strip()

        if choice == "1":
            python_core()

        elif choice == "2":
            data_structures()

        elif choice == "3":
            python_libraries()

        elif choice == "4":
            custom_modules()

        elif choice == "5":
            exception_handling()

        elif choice == "6":
            web_scraping()

        elif choice == "7":
            file_handling()

        elif choice == "8":
            crud_operations(df)

        elif choice == "9":
            numpy_analysis(df)

        elif choice == "10":
            scipy_analysis(df)

        elif choice == "11":
            pandas_analysis(df)

        elif choice == "12":
            data_preprocessing()

        elif choice == "13":
            data_visualization()

        elif choice == "14":
            statistical_analysis()

        elif choice == "15":
            probability()

        elif choice == "16":
            sampling_inference()

        elif choice == "17":
            hypothesis_testing()

        elif choice == "18":
            machine_learning()

        elif choice == "19":

            print(
                "\nProgram finished."
            )

            break

        else:

            print(
                "\nInvalid choice."
            )


if __name__ == "__main__":
    main()