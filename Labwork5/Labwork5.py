import pandas as pd

# PART 1. DATA MANIPULATION
print("--- PART 1. DATA MANIPULATION ---")
# 1. Load the dataset
df_students = pd.read_csv('students.csv')

# 2. Display first 5 rows
print("\n- First 5 students -\n", df_students.head())

# 3. Find number of rows and columns
rows, columns = df_students.shape
print(f"\n- Rows: {rows}, Columns: {columns} -")

# 4. Select name and GPA
name_gpa = df_students[["name", "GPA"]]
print("\n- Name and GPA are selected -\n", name_gpa)

# 5. Find students with GPA >= 3.5
good_students = df_students[(df_students["GPA"] == 3.5) & (df_students["GPA"] > 3.5)]
print("\n- Good students with GPA >= 3.5 -\n", good_students)

# 6. Sort students by GPA
sorted1 = df_students.sort_values("GPA") # Low -> High
print("\n- Sort from Low to High -\n", sorted1)

sorted2 = df_students.sort_values("GPA", ascending = False) # High -> Low
print("\n- Sort from High to Low -\n", sorted2)

# 7. Find average GPA by major
average = df_students.groupby("major") ["GPA"].mean()
print("\n- Average GPA by major -\n", average)

# PART 2. FROM RAW DATA TO USEFUL INFO
print("\n\n--- PART 2. FROM RAW DATA TO USEFUL INFO")
# 1. Load both files
df_marks = pd.read_csv("scores.csv")

# 2. Check missing values
print("\n- Missing values -\n")
print("+ Students: \n", df_students.isna().sum())
print("+ Marks: \n", df_marks.isna().sum())

# 3. Fill or remove missing data appropriately
df_students.dropna(inplace = True)
df_marks.fillna(0, inplace = True)

# 4. Merge the 2 datasets
merge_df = pd.merge(df_students, df_marks, on = "student_id")

# 5. Calculate each student's average score
merge_df['avg_score'] = merge_df[['python', 'math', 'database']].mean(axis = 1)
print("\n- Student's average score -\n", merge_df['avg_score'])

# 6. Find the top 5 students
top = merge_df.sort_values(by = 'avg_score', ascending = False).head(5)
print("\n- Top 5 students have highest GPA -\n", top)

# 7. Compute average score by major
average = merge_df.groupby('major')['avg_score'].mean()
print("\n- Average score by major -\n", average)

# PART 3. EXTRA
print("\n\n--- PART 3. EXTRA ---")
def custom_query():
    df_students = pd.read_csv('students.csv')
    df_marks = pd.read_csv('scores.csv')
    df_course = pd.read_csv('courses.csv')

    print("\n- Search student -\n")

    user_condition = input("Enter the condition to search: \n(Suggest: name == 'Kate' or GPA > 3.0)\n")

    try:
        result = df_students.query(user_condition)

        if result.empty:
            print("Cannot find the student.\n")
        else:
            print(result)
    except:
        print("ERROR. Try again !")

if __name__ == '__main__':
    custom_query()