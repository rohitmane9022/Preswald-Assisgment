from preswald import connect, get_df, query, table, text, slider, plotly
import plotly.express as px


connect()  
df = get_df("budget_csv")  

sql = "SELECT * FROM budget_csv WHERE Budget > 50"
filtered_df = query(sql, "budget_csv")


text("# My Budget Analysis App")
table(filtered_df, title="Filtered Data (Budget > 50)")


threshold = slider("Budget Threshold", min_val=0, max_val=1500, default=50)
table(df[df["Budget"] > threshold], title="Dynamic Budget View")


fig = px.scatter(df, x="Category", y="Budget", text="Category", title="Category vs Budget")
fig.update_traces(textposition='top center', marker=dict(size=12, color='lightblue'))
fig.update_layout(template='plotly_white')
plotly(fig)


text(f"Total Budget: ${df['Budget'].sum()}")