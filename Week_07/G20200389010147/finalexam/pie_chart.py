import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'positive', 'negative'
sizes = [5,3]
explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode,labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


#         title emo
# 0  test_title  正向
# 1  test_title  正向
# 2  test_title  正向
# 3  test_title  負向
# 4  test_title  負向
# 5  test_title  正向
# 6  test_title  正向
# 7  test_title  負向