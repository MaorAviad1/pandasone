import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['John', 'Jane', 'Mike', 'Lisa'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'Paris', 'London', 'Tokyo']
}
df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Perform some operations using Pandas
# Sort the DataFrame by age in descending order
df_sorted = df.sort_values('Age', ascending=False)

# Filter the DataFrame to include only people from New York
df_filtered = df[df['City'] == 'New York']

# Calculate the average age
avg_age = df['Age'].mean()

# Display the sorted DataFrame, filtered DataFrame, and average age
print("\nSorted DataFrame:")
print(df_sorted)

print("\nFiltered DataFrame:")
print(df_filtered)

print("\nAverage Age:", avg_age)
