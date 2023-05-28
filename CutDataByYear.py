import pandas as pd

pd.set_option('display.max_columns', None)
source_path = "/Users/vasiliykhaninev/Downloads/Crimes_-_2001_to_Present.csv"

df = pd.read_csv(source_path)

# Changes data type of columns "Date" and "Updated on" to datetime64(YYYY-MM-DD HH:MM:SS),
# so we can find min and max values correctly.
df["Date"] = df["Date"].astype("datetime64")
df["Updated On"] = df["Updated On"].astype("datetime64")

# Creates a copy of dataset and changes column "Date" to be year
a = df.copy()
a["Date"] = a["Date"].dt.year

# Extracts minimum and maximum value for column "Date" from the copy of our dataset, so we can use them for a loop
start = a.Date.min()
end = a.Date.max() + 1
iteration = start

# Loop that separates and saves data by the year
while True:
    df = df.set_index("Date")
    b = df.loc[str(iteration)]
    b.to_csv('Crimes_{}.csv'.format(iteration), sep=',')
    df = df.reset_index()
    iteration = iteration + 1
    if iteration == end:
        break


