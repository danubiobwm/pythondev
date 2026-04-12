from dataset import ecom_sale
import plotly.express as px

bar_fig = px.bar(
                data_frame=ecom_sale,
                 y="Country",
                 x="Total Sales",
                 title="Total Sales by Country",
                 orientation="h"
                 )
bar_fig.update_layout({'bargap':0.5})
#bar_fig.show()