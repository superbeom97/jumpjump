### 6.3 ggplot

from ggplot import *

print(mtcars.head())
plt1 = ggplot(aes(x='mpg'), data=mtcars +
              geom_histogram(fill='darkblue', binwidth=2) +
              xlim(10, 35) + ylim(0, 10) +
              xlab("MPG") + ylab("Frequency") +
              ggtitle("Histogram of MPG"))
print(plt1)

print(meat.head())
plt2 = ggplot(aes(x='date', y='beef'), data=meat) + \
        geom_line(color='purple', size=1.5, alpha=0.75) + \
        xlab("Year") + ylab("Head of Cattle Slaughtered") + \
        ggtitle("Beef Consumption Over Time")
print(plt2)

print(diamonds.head())
plt3 = ggplot(diamonds, aes(x='carat', y='price', colour='cut')) + \
        geom_point(alpha=0.5) + \
        scale_color_gradient(low='#05D9F6', high='#5011D1') + \
        xlim(0, 6) + ylab("Price") + \
        ggtitle("Diamond Price by Carat and Cut") + \
        theme_gray()
print(plt3)

plt3.save("ggplot_plots.png")
