from flask import Flask,render_template, url_for
import pymysql
import pandas as pd


app = Flask(__name__)
app.jinja_env.filters['zip'] = zip

def conn_db():
    conn = pymysql.connect(host="    ", user="your_username", password="your_password", db="your_database", charset="utf8")
    return conn

def get_data(conn=conn_db(), n=10):
    # Get the top10 products
    sql = "select ProductMName, date_format(FeedbackDate, '%Y-%m') Month, count(FeedBack) Count from Feedbacks group by ProductMName, Month order by Count desc, Month asc"
    df = pd.read_sql(sql, conn)
    conn.close()
    product_count = []
    for index, value in enumerate(df["ProductMName"].unique()):
        product_count.append([value, index+1])
    product_count = dict(product_count)
    df["Rank"] = df["ProductMName"].map(lambda x: product_count[x])
    df = df[df["Rank"]<=n][["ProductMName", "Month", "Count"]]
    df.sort_values(by="Month", inplace=True)
    df_TotleCount = df.groupby(["ProductMName"])["Count"].sum()
    df_TotleCount.sort_values(ascending=False, inplace=True)
    df_pivot = pd.pivot_table(df, index="ProductMName", columns="Month", values="Count", fill_value=0)
    return df_TotleCount, df_pivot

@app.route('/')
def display_FeedbackCountByProject():
    df_TotleCount, df_pivot = get_data(n=10)
    TotleCount = df_TotleCount.values
    ProductMName = df_pivot.index.tolist()
    Month = df_pivot.columns.tolist()
    Count = df_pivot.values.tolist()
    return render_template('just.html', ProductMName=ProductMName, Month=Month, Count=Count, TotleCount=TotleCount)

if __name__ == "__main__":
    app.run(debug = True)
