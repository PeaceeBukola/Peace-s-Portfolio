#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

import gspread 


import panel as pn
pn.extension('tabulator')
import hvplot.pandas
import holoviews as hv
hv.extension('bokeh', config=dict(future_deprecations=True))






# In[2]:


import gspread

credentials =  {"type": "service_account",
  "project_id": "python-budget-417223",
  "private_key_id": "19ac0bf7e471af10380eb099ec49407506ddf12e",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDOzpr2VIT5RgPC\n7poHNVCWY2MGkt2fIA1yogf3/UhiBoDpHs/oZjmveaB2UzgxTKaZiLHgtPNzAGMl\n0TIcFSFcvwj8RsqhaU7DWaG059okiRmW6A/ARynQwamV3yPnPsNa1IPhj+ylrFAT\nMJhevEpNRtag6H+k1VYdE8A1saWZer2RdE4jXPSrDVMby4aAsuf+/qkFI7xEc+0u\nvXhmveKRW+mqxYKATF6gxH8jV9a/jwm8RKI17v1wsg+UnhusvTKuFqlgO/0GBnKr\nxUJZ7t/HtYrbK6TMfDQ21HZmi2D3QYw5/QaL/yFO92iWibDw7lmX7bqBvjROpPSF\nctohUDlbAgMBAAECggEAEyN5ocxGlg8NsA+Gv54GfDRsaKJU0jIULISkOiX9edzi\nNzC7yuUS95NI70paS+2tCU5mL8ZvNThW9Jv8iC7IbJ3dRgODIxbszBVSarx+Kp1p\neda2BnRPgVs6x3zkBLWBPLmoDsrT+q0MqAn6P+Iq+iXRHQkHLwjzNDOsuQtcqOxR\nXJHIukFmXhfT6oeWH9c1XJTUDvg1pJFGxWLhPYttJjwfA1g5Hkeg03iwsfsoHSl4\nBbl2q4La1p6AkJfeYq1HI1DOvZoD3WtQiEzBiSDJu/Kstfj2hPK2NbEjaGj/OxBf\nVw1LiqsNE1IuCaHxVOf2SaWxK324MmcVXsxx5z85eQKBgQDtuzXYeHLGuaeYzG8Z\n8/tbKpHEFfHYKUWpMeaE3hdApSBL7AqPUvb9RlfskQx2X/mXzPYtxt5AjFBIQgVK\noBKsNDx1Wol4Ggbymwkgm0RKZvAme2/49+b9EVYkNy7m6sZC4gMQAEKBqCF9pmjN\nLJhHqqwSWNvIXnTZpA/o+hKInwKBgQDeswkCj5mTTyLeIXVMyklVNOh01bBosf+R\nVFq+q3INccWhZcj8cSHsLPwpcRT267yQvU9d5SUnB1vyKUFxrOg+RdpJBneo3a51\n0yOi3kR8GxDrSkMkgsV0P6YJLorLrd1oAxEGzErLs94XWacd+uaLbAMcOlJU+J4y\nWpPVRBCJxQKBgD+fIXrsSTM7zkmLNJSKghNU4ivK/60s5nKwYxPd5/Up++m1ouHW\nfzkrES7DZsVrS/2/IYcAuMwngPjFimr9SeICHMf/Udjthjx5F0k9pFoREGYMFNxZ\nY90IPbh1eDzeSe7uU4l9uE7Asy3QUi3OqHZNi71hQHhwJu90A7oC6uDbAoGAX+1y\n5h2BI8kk1dZHtso0CHX/48Pgd1ilI67YX+Vt/YiSftFfYA5DdH50KE3DoBEvapGB\nTIrWFBfBbXCD9jlq2NgyDN6yUJUc/zfx08g2a9ck1JVqkqGZ+FcqaC4aL143TwRz\nIyCA33odIqXFrM5U3J2sQU6GBIALdNk7cNQe45kCgYEA0Efj4grDB26z8e3F6cKQ\nZWuwyiu0e4vNuBMgn81J0MSRbiNRHTTq+rol7QrpjgmGA6Z9emIvPf6D/z3pRyR5\nHKVG4osKOSVEK8huP1GE56JpCfzCCgJsjrnE7FvP5SBTIXqdztlWgeMTjiugMiJf\nqQhvsy2DadsUa798X2ibvTg=\n-----END PRIVATE KEY-----\n",
  "client_email": "python-budget@python-budget-417223.iam.gserviceaccount.com",
  "client_id": "103001024330856260488",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/python-budget%40python-budget-417223.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"}

gc = gspread.service_account_from_dict(credentials)

sh = gc.open("BUDGET DATASET")


# In[3]:


ws = sh.worksheet('Sheet1')
df = pd.DataFrame(ws.get_all_records())
df.head()


# In[4]:


df = df[['Start Date', 'Description', 'Amount', 'Balance']] #keep only desired columns
df['Description'] = df['Description'].map(str.lower) #lower case of descriptions

df = df.rename(columns={'Start Date': 'Date'})   #rename columns
df['Category'] = 'unassigned'                        #add category column

df.head()


# In[55]:


#income
#Electricity
#Water
#Disposal Services
#Food
#Outfits and accessories
#Rent
#Skincare
#Appliance
#Books





#income

import numpy as np

df['Category'] = np.where(df['Description'].str.contains(
    'salary|transfer|eoa foundation|firm'), 
    'income', df['Category'], )
    
# Water

df['Category'] = np.where(df['Description'].str.contains(
    'water|waterworks|public'), 
    'Water Supply', df['Category'], )
    
# Electricity

df['Category'] = np.where(df['Description'].str.contains(
    'light|phcn|electricity'), 
    'Electricity', df['Category'],)
                          
# Food

df['Category'] = np.where(df['Description'].str.contains(
    'restaurant|kfc|chicken|food|spoon|plate'), 
    'Food', df['Category'], )
    
# Outfits & accessories
    
df['Category'] = np.where(df['Description'].str.contains(
    'purple|pendant|spray|heel|dress|stiloutte|pin rollers|pins|hair|sanitary'), 
    'Outfits/accessories', df['Category'], )


# Disposal Service
    
df['Category'] = np.where(df['Description'].str.contains(
    'waste|sewage'), 
    'Disposal Service', df['Category'], )

#Rent
df['Category'] = np.where(df['Description'].str.contains(
    'rent|apartment|rentals|roof|security'), 
    'Rent', df['Category'],)

#Skincare
df['Category'] = np.where(df['Description'].str.contains(
    'skincare beauty|creams|jumia'), 
    'Skincare', df['Category'],)

#Appliance
df['Category'] = np.where(df['Description'].str.contains(
    'fan roller|fridge|microwave'), 
    'Appliances', df['Category'],)

#Books
df['Category'] = np.where(df['Description'].str.contains(
    'textbook|book'), 
    'Books', df['Category'],)
                           

# Convert the "Date" column to a datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Extract the month and year information
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
pd.options.display.max_rows = 93
df.head(93)


# In[ ]:


#TOP BANNER TITLE


# In[57]:


## Create Top Banner for a summary of March's income, recurring expenses, non-recurring expenses and savings

# Get the March month and year
latest_month = df['Month'].max()
latest_year = df['Year'].max()

# Filter the dataframe to include only transactions from the latest month
last_month_expenses = df[(df['Month'] == latest_month) & (df['Year'] == latest_year)]



# In[58]:


last_month_expenses = last_month_expenses.groupby('Category')['Amount'].sum().reset_index()

last_month_expenses['Amount']=last_month_expenses['Amount'].astype('str')
last_month_expenses['Amount']=last_month_expenses['Amount'].str.replace('-','')
last_month_expenses['Amount']=last_month_expenses['Amount'].astype('float')        #get absolute figures

last_month_expenses = last_month_expenses[last_month_expenses["Category"].str.contains("Excluded|unassigned") == False]    #exclude "excluded" category
last_month_expenses = last_month_expenses.sort_values(by='Amount', ascending=False)    #sort values
last_month_expenses['Amount'] = last_month_expenses['Amount'].round().astype(int)      #round values

last_month_expenses


# In[59]:


last_month_expenses_tot = last_month_expenses['Amount'].sum()
last_month_expenses_tot


# In[60]:


def calculate_difference(event):
    income = float(income_widget.value)
    recurring_expenses = float(recurring_expenses_widget.value)
    monthly_expenses = float(monthly_expenses_widget.value)
    difference = income - recurring_expenses - monthly_expenses
    difference_widget.value = str(difference)

income_widget = pn.widgets.TextInput(name="Income", value="0")
recurring_expenses_widget = pn.widgets.TextInput(name="Recurring Expenses", value="0")
monthly_expenses_widget = pn.widgets.TextInput(name="Non-Recurring Expenses", value=str(last_month_expenses_tot))
difference_widget = pn.widgets.TextInput(name="Last Month's Savings", value="0")

income_widget.param.watch(calculate_difference, "value")
recurring_expenses_widget.param.watch(calculate_difference, "value")
monthly_expenses_widget.param.watch(calculate_difference, "value")

pn.Row(income_widget, recurring_expenses_widget, monthly_expenses_widget, difference_widget).show() 


# In[ ]:


### Create last month expenses bar chart 



# In[108]:


last_month_expenses_chart = last_month_expenses.hvplot.bar(
    x='Category', 
    y='Amount', 
    height=200, 
    width=870, 
    title="Last Month Expenses",
    ylim=(0, 4000))

last_month_expenses_chart


# In[ ]:


### Create monthly expenses trend bar chart 


# In[81]:


df['Date'] = pd.to_datetime(df['Date'])            # convert the 'Date' column to a datetime object
df['Month-Year'] = df['Date'].dt.to_period('M')    # extract the month and year from the 'Date' column and create a new column 'Month-Year'
monthly_expenses_trend_by_cat = df.groupby(['Month-Year', 'Category'])['Amount'].sum().reset_index()

monthly_expenses_trend_by_cat['Amount']=monthly_expenses_trend_by_cat['Amount'].astype('str')
monthly_expenses_trend_by_cat['Amount']=monthly_expenses_trend_by_cat['Amount'].str.replace('-','')
monthly_expenses_trend_by_cat['Amount']=monthly_expenses_trend_by_cat['Amount'].astype('float')
monthly_expenses_trend_by_cat = monthly_expenses_trend_by_cat[monthly_expenses_trend_by_cat["Category"].str.contains("Excluded") == False]

monthly_expenses_trend_by_cat = monthly_expenses_trend_by_cat.sort_values(by='Amount', ascending=False)
monthly_expenses_trend_by_cat['Amount'] = monthly_expenses_trend_by_cat['Amount'].round().astype(int)
monthly_expenses_trend_by_cat['Month-Year'] = monthly_expenses_trend_by_cat['Month-Year'].astype(str)
monthly_expenses_trend_by_cat = monthly_expenses_trend_by_cat.rename(columns={'Amount': 'Amount '})

monthly_expenses_trend_by_cat



# In[82]:


select_category1 = pn.widgets.Select(name='Select Category', options=[
#Electricity
#Water
#Disposal Services
#Food
#Outfits and accessories
#Rent
#Skincare
#Appliance
#Books 
    'All',
    'Skincare',
    'Water Supply',
    'Disposal Service',
    'Food',
    'Outfits/accessories',
    'Rent',
    'Appliances',
    'Books'
    ])

select_category1


# In[83]:


# define plot function
def plot_expenses(category):
    if category == 'All':
        plot_df = monthly_expenses_trend_by_cat.groupby('Month-Year').sum()
    else:
        plot_df = monthly_expenses_trend_by_cat[monthly_expenses_trend_by_cat['Category'] == category].groupby('Month-Year').sum()
    plot = plot_df.hvplot.bar(x='Month-Year', y='Amount ')
    return plot

# define callback function
@pn.depends(select_category1.param.value)
def update_plot(category):
    plot = plot_expenses(category)
    return plot

# create layout
monthly_expenses_trend_by_cat_chart = pn.Row(select_category1, update_plot)
monthly_expenses_trend_by_cat_chart[1].width = 300

monthly_expenses_trend_by_cat_chart


# In[171]:


df = df[['Date', 'Category', 'Description', 'Amount']]
df['Amount']=df['Amount'].astype('str')
df['Amount']=df['Amount'].str.replace('-','')
df['Amount']=df['Amount'].astype('float')        #get absolute figures

df = df[df["Category"].str.contains("Excluded") == False]    #exclude "excluded" category
df['Amount'] = df['Amount'].round().astype(int)      #round values
df


# In[172]:


#Define a function to filter the dataframe based on the selected category
def filter_df(category):
    if category == 'All':
        return df
    return df[df['Category'] == category]


# In[173]:


# Create a DataFrame widget that updates based on the category filter
summary_table = pn.widgets.DataFrame(filter_df('All'), height = 300,width=400)


# In[174]:


# Define a callback that updates the dataframe widget when the category filter is changed
def update_summary_table(event):
    summary_table.value = filter_df(event.new)


# In[175]:


# Add the callback function to the category widget
select_category1.param.watch(update_summary_table, 'value')
summary_table


# In[140]:


import os
cwd=os.getcwd()
cwd


# In[184]:


# Define the template, select_category1, and other necessary components


# Create the template
template = pn.template.FastListTemplate(
    title="Personal Finances Summary",
    sidebar=[
        pn.pane.Markdown("## *Money Management for Financial Freedom*"),
        pn.pane.PNG('cash.png', sizing_mode='scale_both'),
        pn.pane.Markdown(""),
        pn.pane.Markdown(""),
        select_category1
    ],
    main=[
        pn.Row(income_widget, recurring_expenses_widget, monthly_expenses_widget, difference_widget, width=300),
        pn.Row(last_month_expenses_chart, height=200),
        pn.GridBox(
            monthly_expenses_trend_by_cat_chart[1],
            summary_table,
            ncols=2,
            align='start',
            sizing_mode='stretch_width'
        )])

#Change background color of monthly expenses trend by category chart
for chart in monthly_expenses_trend_by_cat_chart:
    chart.line_color = 'red'  # Change to your desired color

# Display the template
template.show()


# In[159]:


#Change background color of monthly expenses trend by category chart
for chart in monthly_expenses_trend_by_cat_chart:
    chart.background_fill_color = 'red'  # Change to your desired color


# In[178]:


pn.serve(template)

