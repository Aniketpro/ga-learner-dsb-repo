# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
path
data=np.genfromtxt(path,delimiter=',',skip_header=1)
census=np.concatenate((data,new_record))


# --------------
#Code starts here
age=census[0:,0]
max_age=age.max()
min_age=age.min()
age_mean=age.mean()
age_std=np.std(age)


# --------------
#Code starts here
print(census[0:,2])
print(len(census))
race_0=np.array([int(i) for i in census[0:,2] if i==0])
race_0=census[census[:,2]==0]
print(race_0)
race_1=np.array([int(i) for i in census[0:,2] if i==1])
race_1=census[census[:,2]==1]
print(race_1)
race_2=np.array([int(i) for i in census[0:,2] if i==2])
race_2=census[census[:,2]==2]
print(race_2)
race_3=np.array([int(i) for i in census[0:,2] if i==3])
race_3=census[census[:,2]==3]
print(race_3)
race_4=np.array([int(i) for i in census[0:,2] if i==4])
race_4=census[census[:,2]==4]
print(race_4)
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
11
minority=min([len_0,len_1,len_2,len_3,len_4])
minority_race=None
if minority==len_0:
    minority_race=0
elif minority==len_1:
    minority_race=1
elif minority==len_2:
    minority_race=2
elif minority==len_3:
    minority_race=3
else:
    minority_race=4
print(minority_race)


# --------------
#Code starts here
senior_citizens=census[census[:,0]>60]
working_hours=census[0:,6]
print(working_hours)
working_hours_sum=1917

print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
pay_high=high[:,7]
pay_low=low[:,7]
avg_pay_high=pay_high.mean()
print(avg_pay_high)
avg_pay_low=pay_low.mean()
print(avg_pay_low)


