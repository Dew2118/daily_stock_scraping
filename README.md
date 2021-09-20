# daily_stock_scraping
## How do I use it
1. open ubuntu terminal
2. cd to the project
3. heroku login
4. heroku run bash
    4.1 python siam_chart.py
    4.2 ls
    4.3 curl -F "file=@filename.csv" file.io
    4.4 exit
5. curl file.io_link > filename.csv
6. cp filename.csv temp
7. rm filename.csv 
8. mv temp filename.csv
6-8 is to remove file.io time limit
##In case of push files
1. git add filename(s)
2. git commit -m "message"
3. git push heroku main
4.heroku run bash