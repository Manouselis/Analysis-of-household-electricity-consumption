# Libraries
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from random import randint
from math import ceil

# Constants
num_of_appliances = 9

# Directory
directory = 'C:/Users/Yuri/Desktop/SES_MILTON/Team4/'

# Reading the directory
house = pd.read_csv(directory + 'Team4.csv')

'''Preprocessing'''
# Removing samples with issues column set to 1 (sum of the sub-metering (IAMs) is greater than the household aggregate)
pos = house.iloc[:, -1] == 0
house_prepro = house[pos]

# NaN removal (Dropping Samples who contain NaN values)
house_prepro = house_prepro.dropna()

# Converting the dates from object to datetime
house_prepro['Time'] = pd.to_datetime(house_prepro['Time'])

''' Question 1'''

'''Subquestion a (Difference between working and off days)'''
# Calculating the mean usage per day for the whole dataset (In watts)
mean_usage = house_prepro.groupby([house_prepro['Time'].dt.weekday])['Aggregate'].mean()

# Plotting mean aggregate and days
ax1 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Bar plot (discrete data)
plt.bar(ax1, mean_usage)
plt.get_current_fig_manager().window.showMaximized()
plt.tight_layout()
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)
plt.ylabel('Aggregated Mean (Watt)', fontsize=22, fontweight='bold')
plt.xlabel('Day', fontsize=22, fontweight='bold')
plt.pause(1)
plt.tight_layout()

for i in range(len(ax1)):
    plt.text(i, float("{:.2f}".format(mean_usage[i])), "{:.2f}".format(mean_usage[i]), fontsize=18, horizontalalignment='center')

plt.savefig(os.path.join(os.path.expanduser('~'), str(directory) + 'Pictures', 'Question 1(a)'))
plt.close()

'''Subquestion b (Difference between seasons)'''
# Creating month to season Dictionary
month_num_to_season = {1: 'WINT', 2: 'WINT', 3: 'SPRING', 4: 'SPRING', 5: 'SPRING', 6: 'SUM', 7: 'SUM', 8: 'SUM',
                       9: 'FALL',
                       10: 'FALL', 11: 'FALL', 12: 'WINT'}

# Creating Season Column to group data with
house_prepro['Season'] = [month_num_to_season.get(t_stamp.month) for t_stamp in house_prepro['Time']]

# Calculating the mean usage per season for the whole dataset (In watts)
mean_usage_season = house_prepro.groupby([house_prepro['Season']])['Aggregate'].mean()

# Changing the order of the Seasons from alphabetical to natural
mean_usage_season = mean_usage_season.reindex(index=['FALL', 'WINT', 'SPRING', 'SUM'])
# Plotting mean aggregate compared to Season
ax1 = ['Fall', 'Winter', 'Spring', 'Summer']

# Bar plot (discrete data)
plt.bar(ax1, mean_usage_season)
plt.get_current_fig_manager().window.showMaximized()
plt.tight_layout()
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)
plt.ylabel('Aggregated Mean (Watt)', fontsize=22, fontweight='bold')
plt.xlabel('Season', fontsize=22, fontweight='bold')
plt.pause(1)
plt.tight_layout()

for i in range(len(ax1)):
    plt.text(i, float("{:.2f}".format(mean_usage_season[i])), "{:.2f}".format(mean_usage_season[i]), fontsize=18, horizontalalignment='center')

plt.savefig(os.path.join(os.path.expanduser('~'), str(directory) + 'Pictures', 'Question 1(b)'))
plt.close()


'''Subquestion c (Difference between day time zones i.e. morning, afternoon, night)'''
# Creating day timezone Dictionary
day_time_to_timezone = {1: 'Night', 2: 'Night', 3: 'Night', 4: 'Night', 5: 'Morning', 6: 'Morning', 7: 'Morning',
                        8: 'Morning',
                        9: 'Morning', 10: 'Morning', 11: 'Morning', 12: 'Afternoon', 13: 'Afternoon', 14: 'Afternoon',
                        15: 'Afternoon', 16: 'Afternoon',
                        17: 'Evening', 18: 'Evening', 19: 'Evening', 20: 'Evening', 21: 'Night', 22: 'Night',
                        23: 'Night', 00: 'Night'}

# Creating TimeZone Column to group data with
house_prepro['TimeZone'] = [day_time_to_timezone.get(t_stamp.hour) for t_stamp in house_prepro['Time']]

# Calculating the mean usage per timezone for the whole dataset (In watts)
mean_usage_timezone = house_prepro.groupby([house_prepro['TimeZone']])['Aggregate'].mean()

# Changing the order of the Timezone from alphabetical to natural
mean_usage_timezone = mean_usage_timezone.reindex(index=['Morning', 'Afternoon', 'Evening', 'Night'])
# Plotting mean aggregate compared to Season
ax1 = ['Morning', 'Afternoon', 'Evening', 'Night']

# Bar plot (discrete data)
plt.bar(ax1, mean_usage_timezone)
plt.get_current_fig_manager().window.showMaximized()
plt.tight_layout()
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)
plt.ylabel('Aggregated Mean (Watt)', fontsize=22, fontweight='bold')
plt.xlabel('Time of Day', fontsize=22, fontweight='bold')
plt.pause(1)
plt.tight_layout()

for i in range(len(ax1)):
    plt.text(i, float("{:.2f}".format(mean_usage_timezone[i])), "{:.2f}".format(mean_usage_timezone[i]), fontsize=18, horizontalalignment='center')

plt.savefig(os.path.join(os.path.expanduser('~'), str(directory) + 'Pictures', 'Question 1(c)'))
plt.close()




''' Question 2'''

'''Subquestion a (Analyzing each appliance)'''

appli_col = ['Aggregate', 'Appliance1', 'Appliance2', 'Appliance3', 'Appliance4', 'Appliance5', 'Appliance6', 'Appliance7', 'Appliance8', 'Appliance9']

# Selecting only the appliances and Aggregate columns
house_summed = house_prepro[appli_col]

# Calculating the sum Wattage of each appliance
house_summed = house_summed.sum(axis=0, skipna=False)

# Percentage Consumption of each appliance
percentage_appliance = []
for i in range(num_of_appliances):
    percentage_appliance.append(100*house_summed[i+1]/house_summed[0])


# Plotting Percentage Consumption of each Appliance
ax1 = ['Appliance 1', 'Appliance 2', 'Appliance 3', 'Appliance 4', 'Appliance 5', 'Appliance 6', 'Appliance 7', 'Appliance 8', 'Appliance 9']

# Dead code ahead
plt.bar(ax1, percentage_appliance)
plt.get_current_fig_manager().window.showMaximized()
plt.pause(1)
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)
plt.pause(1)
plt.ylabel('Consumption of Each Appliance (%)', fontsize=20, fontweight='bold')
plt.xlabel('Appliances', fontsize=20, fontweight='bold')
plt.pause(5)
plt.tight_layout()
plt.close()

# Bar plot (discrete data)
plt.bar(ax1, percentage_appliance)
plt.get_current_fig_manager().window.showMaximized()
plt.pause(1)
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)
plt.pause(1)
plt.ylabel('Consumption of Each Appliance (%)', fontsize=20, fontweight='bold')
plt.xlabel('Appliances', fontsize=20, fontweight='bold')
plt.pause(1)
plt.tight_layout()

for i in range(len(ax1)):
    plt.text(i, float("{:.2f}".format(percentage_appliance[i])), "{:.2f}".format(percentage_appliance[i]), fontsize=18, horizontalalignment='center')

plt.savefig(os.path.join(os.path.expanduser('~'), str(directory) + 'Pictures', 'Question 2(a)(1)'))
plt.close()

# Setting Datetime As index for our dataframe
house_prepro_datetime = house_prepro.set_index('Time')

#Resampling the Dataframe to another frequency (weekly mean usage of each appliance)
house_prepro_weekly = house_prepro_datetime.resample("W").mean()[appli_col]

'''
SOS SOS SOS SOS 

NOTICE THAT THE DATAFRAME house_prepro_weekly has some NaN values
This is not a fault, this happens due to the fact that some weeks were not recorded at all
Must add at the project report

SOS SOS SOS SOS
'''

# The below paragraph of code generates the percentage consumption of each appliance each week
percentage_appliance_weekly = pd.DataFrame()
for i in range(num_of_appliances):
    percentage_appliance_weekly['Perc. Appliance ' + str(i+1)] = house_prepro_weekly.iloc[:, i+1] / house_prepro_weekly.iloc[:, 0]

percentage_appliance_weekly = percentage_appliance_weekly*100


# Plotting Percentage Consumption of each Appliance for different weeks
ax1 = ['Appliance 1', 'Appliance 2', 'Appliance 3', 'Appliance 4', 'Appliance 5', 'Appliance 6', 'Appliance 7', 'Appliance 8', 'Appliance 9']

# Indicative number of weeks to plot
num_weeks = 4

# Plotting Percentage Consumption of each Appliance for different indicative number of weeks (here 4 random generated weeks)
for i in range(num_weeks):
    # Bar plot (discrete data)
    week = randint(0, len(percentage_appliance_weekly))
    plt.bar(ax1, percentage_appliance_weekly.iloc[week, :])
    plt.get_current_fig_manager().window.showMaximized()
    plt.tight_layout()
    plt.rc('xtick', labelsize=12)
    plt.rc('ytick', labelsize=12)
    plt.ylabel('Consumption of Each Appliance (%) for week ' + str(week), fontsize=15, fontweight='bold')
    plt.xlabel('Appliances', fontsize=20, fontweight='bold')
    plt.pause(1)
    plt.tight_layout()

    for j in range(len(ax1)):
        plt.text(j, float("{:.2f}".format(percentage_appliance_weekly.iloc[week, j])), "{:.2f}".format(percentage_appliance_weekly.iloc[week, j]),
                 fontsize=18, horizontalalignment='center')

    plt.savefig(os.path.join(os.path.expanduser('~'), str(directory) + 'Pictures', 'Question 2(a)(' + str(2+i) + ')'))
    plt.close()



# Calculating and ploting consumption of appliances in random time samples in order to find the house
for i in range(10):
    # Bar plot (discrete data)
    sampl = randint(10000, len(house_prepro_datetime))
    house_prepro_datetime[appli_col].iloc[sampl-10000:sampl, 1:].plot()
    plt.get_current_fig_manager().window.showMaximized()
    plt.tight_layout()
    plt.rc('xtick', labelsize=12)
    plt.rc('ytick', labelsize=12)
    plt.ylabel('Consumption of Each Appliance in time for sample ' + str(sampl), fontsize=10, fontweight='bold')
    plt.xlabel('Appliances', fontsize=20, fontweight='bold')
    plt.pause(1)
    plt.tight_layout()

    plt.savefig(os.path.join(os.path.expanduser('~'), str(directory) + 'Pictures', 'Find House (' + str(i) + ')'))
    plt.close()



'''Subquestion b (Difference between working and off days in each appliance)'''

appli_only_col = ['Appliance1', 'Appliance2', 'Appliance3', 'Appliance4', 'Appliance5', 'Appliance6', 'Appliance7', 'Appliance8', 'Appliance9']

# Calculating the mean usage per day for each appliance in the whole dataset (In watts)
mean_usage_applications = house_prepro.groupby([house_prepro['Time'].dt.weekday])[appli_only_col].mean()

# Plotting mean usage of each appliance and days
ax1 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Y Labels to use in for loop
ylabel_list = ['Freezer Mean Usage (Watt)', 'Washing Machine Mean Usage (Watt)', 'Dishwasher Mean Usage (Watt)', 'MJY Computer Mean Usage (Watt)', 'TV/Satellite Mean Usage (Watt)', 'Microwave Mean Usage (Watt)', 'Kettle Mean Usage (Watt)', 'Toaster Mean Usage (Watt)', 'PGM Computer Mean Usage (Watt)']

for j in range(mean_usage_applications.shape[-1]):
    # Bar plot (discrete data)
    plt.bar(ax1, mean_usage_applications.iloc[:, j])
    plt.get_current_fig_manager().window.showMaximized()
    plt.tight_layout()
    plt.rc('xtick', labelsize=18)
    plt.rc('ytick', labelsize=18)
    plt.ylabel(ylabel_list[j], fontsize=20, fontweight='bold')
    plt.xlabel('Day', fontsize=20, fontweight='bold')
    plt.ylim(bottom=int(mean_usage_applications.iloc[:, j].min())-2, top=int(mean_usage_applications.iloc[:, j].max())+2)
    plt.pause(1)
    plt.tight_layout()

    for i in range(len(ax1)):
        plt.text(i, float("{:.2f}".format(mean_usage_applications.iloc[i, j])), "{:.2f}".format(mean_usage_applications.iloc[i, j]), fontsize=18, horizontalalignment='center')


    plt.savefig(os.path.join(os.path.expanduser('~'), str(directory) + 'Pictures', 'Question 2(b)(' + str(j+1) + ')'))
    plt.close()





'''Subquestion b (2) (Difference between seasons in each appliance)'''

# Calculating the mean usage per season for each appliance in the whole dataset (In watts)
mean_usage_season_application = house_prepro.groupby([house_prepro['Season']])[appli_only_col].mean()

# Changing the order of the Seasons from alphabetical to natural
mean_usage_season_application = mean_usage_season_application.reindex(index=['FALL', 'WINT', 'SPRING', 'SUM'])

# Plotting mean usage of each appliance compared to Season
ax1 = ['Fall', 'Winter', 'Spring', 'Summer']

for j in range(mean_usage_season_application.shape[-1]):
    # Bar plot (discrete data)
    plt.bar(ax1, mean_usage_season_application.iloc[:, j])
    plt.get_current_fig_manager().window.showMaximized()
    plt.tight_layout()
    plt.rc('xtick', labelsize=18)
    plt.rc('ytick', labelsize=18)
    plt.ylabel(ylabel_list[j], fontsize=20, fontweight='bold')
    plt.xlabel('Season', fontsize=20, fontweight='bold')
    plt.ylim(bottom=max(int(mean_usage_season_application.iloc[:, j].min())-2, 0), top=int(mean_usage_season_application.iloc[:, j].max())+2)
    plt.pause(1)
    plt.tight_layout()

    for i in range(len(ax1)):
        plt.text(i, float("{:.2f}".format(mean_usage_season_application.iloc[i, j])), "{:.2f}".format(mean_usage_season_application.iloc[i, j]), fontsize=18, horizontalalignment='center')

    plt.savefig(os.path.join(os.path.expanduser('~'), str(directory) + 'Pictures', 'Question 2(b)(sec)(' + str(j+1) + ')'))
    plt.close()




'''Subquestion b (3) (Difference between seasons and days in each appliance)'''

mean_usage_season_day = house_prepro.groupby(['Season', house_prepro['Time'].dt.weekday])[appli_only_col].mean()

dict = []
seas = ['FALL', 'WINT', 'SPRING', 'SUM']
day = [0, 1, 2, 3, 4, 5, 6]
for i in range(len(seas)):
    for j in range(len(day)):
        dict.append((str(seas[i]), day[j]))

mean_usage_season_day = mean_usage_season_day.reindex(index=dict)

ax1 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

ylabel_list2 = [ylabel_list[i] + ', per day and season' for i in range(len(ylabel_list))]
for k in range(mean_usage_season_day.shape[-1]):
    # Bar plot (discrete data)
    ax = mean_usage_season_day.iloc[:, k].unstack(level=0).reindex(columns=seas).plot(kind='bar', subplots=True, rot=0, figsize=(9, 7), layout=(1, 4), title=ylabel_list2[k], legend=False, xlabel='Day', backend='matplotlib')
    fig = plt.gcf()
    ax_list = fig.axes

    for axes in ax_list:
        axes.set_xticks(np.arange(len(ax1)))
        axes.set_xticklabels(ax1, fontsize = 'x-small', rotation=45)
        axes.tick_params(axis='y', labelsize='medium')


    plt.get_current_fig_manager().window.showMaximized()
    plt.tight_layout()
    plt.ylim(bottom=max(int(mean_usage_season_day.iloc[:, k].min())-2, 0), top=int(mean_usage_season_day.iloc[:, k].max())+2)
    plt.pause(1)
    plt.tight_layout()



    plt.savefig(os.path.join(os.path.expanduser('~'), str(directory) + 'Pictures', 'Question 2(b)(third)(' + str(k+1) + ')'))
    plt.close()


print('Breakpoint')