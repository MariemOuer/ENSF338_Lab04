 These approaches are designed to deal with different types of measurement noise. Think about what happens when we try to time a program, and which types of issues may result in an incorrect measurement. Reflect on how the two approaches (timeit and repeat) attempt to address these issues. Discuss when it is appropriate to use one or the other. [0.5 pts]

    For the timeit function we can utilize the use of the parameter "number" this allows the devleoper to have control over the number of iteration that occur thereby giving a precise reading for the time 

    As for repeat, it allows the developer to essentially gather various samples of data. It allows the devleoper to see the variation in the time it take for the code to implement for various implementations

    All in all, the timeit approach allows for the calculation of the time and the number of iterations the devleoper would like to see whereas the repeat approach allows for the variation between implementations to be made observable. 


Typically, the output of timeit is post-processed to compute some sort of aggregate statistics. Let’s only consider three: average, min, and max. Which one is the appropriate statistic to apply to the output of timeit timeit()? What is the appropriate statistics to apply to the output of timeit.repeat()? Discuss why. [0.5 pts]

    For timeit.timeit the only appropriate statistic is the average one. As there is very little information we can get in terms of the iterations that will be useful. One could argue that getting a minimum value or maximum value would be useful for calculating the best/worst case scenarios but that is not how this is implemented as the only data available is from x amount of iterations therefore the only useful statistic is the average.

    For timeit.repeat it si benificial to use any of the statistics as the average allows developers to see how the overall performance of the code is, min allows developers to see the best-case scenario and max allows the devveloper to see the worst case scenario. This si because the repeat allows variation within the data collected. 

    To note: according to the documentation provided the most common statistic used in timeit.repeat is the min (minimum time) thereby suggesting that the only appropriate statistic is the min one but it has just as many uses as the max statistic (in my opinion) so I would argue that all of the statistics are appropriate.