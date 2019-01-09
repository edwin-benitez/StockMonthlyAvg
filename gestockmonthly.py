import requests
import mysql.connector


f = open("apikey.txt", "r")
d = open("dbalogin.txt", "r") 
API_KEY = f.readline()
r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=GE&apikey=' + API_KEY)
result = r.json()
monthly = result['Monthly Time Series']

#Enter the last date of the month to get the average for that month
#Format year-month-day
month = input("Enter the month you want to check the average for (year-month-day): ")
avgMonth = monthly[month]


mydb = mysql.connector.connect(
  host= d.readline(),
  user= d.readline(),
  password=d.readline(9),
  database=d.read()
)

mycursor = mydb.cursor()

sql = "INSERT INTO stockAvgMonth (month, openAvg, highAvg, lowAvg, closeAvg, volumeAvg) VALUES (%s, %s, %s, %s, %s, %s)"
val = (month, avgMonth['1. open'], avgMonth['2. high'], avgMonth['3. low'], avgMonth['4. close'], avgMonth['5. volume'])
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
