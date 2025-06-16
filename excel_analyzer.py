import pandas as pd

def analyze_excel_data(file_path):
    """
    Reads an Excel file, calculates family_id frequencies and average price per provider_name,
    and prints the results.
    """
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)

        print("--- DataFrame Head ---")
        print(df.head())
        print("\n")

        # Calculate the frequency of each family_id
        print("--- Family ID Frequencies ---")
        if 'family_id' in df.columns:
            family_id_counts = df['family_id'].value_counts()
            print(family_id_counts)
        else:
            print("Error: 'family_id' column not found.")
        print("\n")

        # Calculate the average price per provider_name
        print("--- Average Price Per Provider Name ---")
        if 'provider_name' in df.columns and 'price' in df.columns:
            # Ensure 'price' column is numeric, coercing errors to NaN
            df['price'] = pd.to_numeric(df['price'], errors='coerce')

            # Drop rows where price became NaN if they should not be part of the mean
            # df.dropna(subset=['price'], inplace=True) # Optional: if you want to remove rows with non-numeric prices

            average_price_per_provider = df.groupby('provider_name')['price'].mean()
            print(average_price_per_provider)
        elif 'provider_name' not in df.columns:
            print("Error: 'provider_name' column not found.")
        elif 'price' not in df.columns:
            print("Error: 'price' column not found.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Ensure openpyxl is installed by pandas when reading .xlsx
    # No direct import of openpyxl is needed in the script itself
    # as pandas handles it.
    excel_file = 'منفعة الحمل.xlsx'
    analyze_excel_data(excel_file)
