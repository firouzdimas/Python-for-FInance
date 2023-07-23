import pandas as pd
import matplotlib.pyplot as plt

def main():
 
    file_name = input("Enter the CSV file name: ")

    
    try:
        df = pd.read_csv(file_name)
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return
    except Exception as e:
        print("Error reading CSV file:", e)
        return

    
    print("Available columns:")
    print(df.columns)
    
   
    selected_columns = input("Enter column names (comma-separated): ").split(',')

    
    selected_columns = [col.strip().upper() for col in selected_columns]

    
    for col in selected_columns:
        if col not in df.columns:
            print(f"Column '{col}' not found in the data.")
            continue

        print(f"\nAnalysis for '{col}':")
        print("Mean:", df[col].mean())
        print("Median:", df[col].median())
        print("Standard Deviation:", df[col].std())

   
        df[col].plot(kind='hist', title=f"Histogram for '{col}'")
        plt.xlabel(col)
        plt.show()

     
        create_scatter = input(f"Do you want to create a scatter plot for '{col}'? (y/n): ").lower()
        if create_scatter == 'y':
            selected_x = input("Enter the X-axis column name: ").strip().upper()
            if selected_x not in df.columns:
                print(f"Column '{selected_x}' not found in the data.")
                continue
            df.plot(kind='scatter', x=selected_x, y=col, title=f"Scatter plot for '{col}' vs '{selected_x}'")
            plt.xlabel(selected_x)
            plt.ylabel(col)
            plt.show()

if __name__ == "__main__":
    main()
