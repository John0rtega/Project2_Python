import pandas as pd
from sklearn.linear_model import LinearRegression

# Read Excel file containing student data
df = pd.read_excel('C:/Users/admin/Desktop/student_scores.xlsx')

# Separate input (quiz scores) from output (final scores)
X = df.iloc[:, 1:11]
y = df.iloc[:, 11]

# Train linear regression model
model = LinearRegression()
model.fit(X, y)

# Read new Excel file containing quiz scores for new students
new_df = pd.read_excel('C:/Users/admin/Desktop/new_student_scores.xlsx')

# Use model to predict final scores for new students
new_X = new_df.iloc[:, 1:11]
predicted_scores = model.predict(new_X)

# Print predicted scores
print(predicted_scores)


