import pandas as pd
import matplotlib.pyplot as plt

def format_data(filepath):
    '''
    Helper function to format incoming data.
    ----------
    filepath: path to the data.
    
    Returns
    -------
    Formatted dataframe
    '''
    x = pd.read_csv(filepath)
    x.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'], inplace=True)
    x.set_index('Country Name', inplace=True)
    x.transpose()
    return x



def plot_imp_exp(df1, df2, region, df1_label='LABEL', df2_label='LABEL', title='SET A TITLE'):
    '''
    Helper function to plot imports and exports.
    ----------
    df1: dataframe.
    df2: dataframe.
    region: list of regions.
    
    Returns
    -------
    Plot.
    '''
    x_data = range(1960, 2021)
    y1_data = df1.loc[region]
    y2_data = df2.loc[region]
    
    fig = plt.figure()
    
    ax1 = fig.add_subplot(1, 1, 1) # or 211
    ax1.plot(x_data, y1_data, label=df1_label)
    ax1.set_title(title)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Percent')
    ax1.legend()
    
    ax2 = fig.add_subplot(1, 1, 1)
    ax2.plot(x_data, y2_data, color='b', label=df2_label)
    ax2.legend()
    
    

def plot_gdp_growth_rates(df, regions, colors, title='SET A TITLE'):
    '''
    Helper function to plot gdp growth rates.
    ----------
    df: dataframe.
    regions: list of regions.
    colors: list of colors for the plot.
    
    Returns
    -------
    Plot.
    '''
    x_data = range(1960, 2021)
    fig = plt.figure(figsize=(20,10))
    ax = fig.add_subplot(1, 1, 1)
    
    for idx, country in enumerate(regions):
        ax.plot(x_data, df.loc[country], label=country, color=colors[idx])
        
    plt.ylim(-6, 20) 
    ax.legend()
    ax.set_title('GDP Growth Rate')
    ax.set_xlabel('Year')
    ax.set_ylabel('Percent')


    
def plot_trade_rates(df, region_list, colors, title='SET A TITLE'):
    '''
    Helper function to plot trade rates.
    ----------
    df: dataframe.
    region_list: list of regions.
    colors: list of colors for the plot.
    
    Returns
    -------
    Plot.
    '''
    x_data = range(1959, 2021)
    fig = plt.figure(figsize=(20,10))
    ax = fig.add_subplot(1, 1, 1)
    
    for idx, region in enumerate(region_list):
        ax.plot(x_data, df.loc[region], label=region, color=colors[idx])
    
    plt.ylim(5, 45) 
    ax.legend()
    ax.set_title(title)
    ax.set_xlabel('Year')
    ax.set_ylabel('Percent')
    





