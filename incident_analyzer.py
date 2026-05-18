import pandas as pd

df = pd.read_csv("safety_incident.csv")

print("--- Safety Incident Summary ---\n")

rows = df.shape[0]
print("Total incidents: ", rows, "\n")


print("Incidents by severity: ")

low = df[df["Severity"] == "Low"].shape[0]
med = df[df["Severity"] == "Medium"].shape[0]
high = df[df["Severity"] == "High"].shape[0]

print("Low: ", low)
print("Medium: ", med)
print("High: ", high, "\n")


lost_time = df[df["Lost Time?"] == "Yes"].shape[0]
print("Lost time incidents: ", lost_time, "\n")

common = df["Incident Type"].value_counts().idxmax()
print("Most common incident types: ", common)

department = df["Department"].value_counts().idxmax()
print("Department with the most incidents: ", department)