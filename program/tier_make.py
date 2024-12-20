

import pandas as pd
df = pd.read_csv(r'C:\Users\nissh\Desktop\program\tier_maker\ANGEL_project\csv\test.csv')


df_grouped= df.groupby('name',as_index=False).mean(numeric_only=True)

df_sorted = df_grouped.sort_values('point')



html_text ='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ranking Table</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }
        th, td {
            border: 1px solid #ccc;
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #f4f4f4;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        tr:hover {
            background-color: #f1f1f1;
        }
    </style>
</head>
<body>
    <h1>Ranking Table</h1>
    <table>
        <thead>
            <tr>
                <th>Rank</th>
                <th>Name</th>
                <th>Score</th>
            </tr>
        </thead>
        <tbody>

'''

for k in range (df_sorted.shape[0]):
 html_text=html_text+'''
 
            <tr>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>
 '''.format(k+1,str(df_sorted['name'][k]),df_sorted['point'][k])

html_text=html_text+'''
            </tr>
        </tbody>
    </table>
 </body>
 </html>
 '''