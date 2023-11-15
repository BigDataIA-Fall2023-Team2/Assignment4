import streamlit as st
import snowflake.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Snowflake connection parameters
conn_params = {
    'user': '*******',
    'password': '*******',
    'account': '*******',
    'warehouse': '*******',
    'database': '*******',
    'schema': '*******'
}

# Establish a connection
conn = snowflake.connector.connect(**conn_params)
st.set_option('deprecation.showPyplotGlobalUse', False)


# Query data from Snowflake
query = """
SELECT
    a.AGE_RANGE,
    SUM(CASE WHEN c.sports_fan = 'Y' THEN 1 ELSE 0 END) AS sports_fan_count
FROM
    BIGDATA.PUBLIC.APP_USAGE a
JOIN
    BIGDATA.PUBLIC.CONSUMER_DATA c 
ON 
    a.STATE = c.STATE
WHERE  
    c.sports_fan = 'Y'
GROUP BY 
    a.AGE_RANGE;
"""

result = conn.cursor().execute(query).fetchall()

# Convert the result to a DataFrame
df = pd.DataFrame(result, columns=['AGE_RANGE', 'sports_fan_count'])

# Close the Snowflake connection
conn.close()

# Streamlit app
st.title("Sports Fan Count by Age Range")

# Display the fetched data

st.subheader("Data from Snowflake")
st.subheader("Interactive Bar Chart")
fig = px.bar(df, x='AGE_RANGE', y='sports_fan_count', labels={'sports_fan_count': 'Sports Fan Count'})
st.plotly_chart(fig)
