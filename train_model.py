import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,r2_score

df = pd.read_csv("BTech_students_performance.csv")
label_enc = LabelEncoder()

print(df.head())
print(df.info())
print(df.describe())
print(df.corr())
print(df.isnull().sum())

df = df.drop(columns=["EAMCET"])
#df["Jee"] = df["Jee"].fillna(df["Jee"].mean())//filling missing values with mean

for i in df.columns:
    if df[i].dtype == "object":
        df[i] = label_enc.fit_transform(df[i])
        


#df = df.drop(columns=["Gender","Relationship", "Avg Screen Time"])

x=df.drop(columns=["CGPA"])
y=df["CGPA"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

print(f"X_train shape: {x_train.shape}, X_test shape: {x_test.shape}")

model = RandomForestRegressor(n_estimators=100,random_state=42)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

mae = mean_absolute_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

print(f"Mean Absolute Error: {mae:.2f}")
print(f"R² Score: {r2:.2f}")

joblib.dump(model, "student_performance_model.pkl")

print("🎉 Model saved successfully as 'student_performance_model.pkl'!")