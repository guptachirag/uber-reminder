# uber-reminder
It reminds to book Uber according to availability and traffic

###Solution - 

The application takes 4 inputs
####Source, Destination, Time and Email

Follow the steps below

1. It gets the time for uberGO using Uber API
2. It find the time to travel between Source and Destination using Maps API

3. It calculates the difference between current time and time given by user,
#####call that remaining time.

4. It calculates the sum of uberGO time and maps time + 1h, {Here 1 hour is taken to handle traffic variations}
#####call that sum

5. t calculates the new remaining time i.e. remaining time - sum

6. If the remaining time > 0, then it waits for the remaining time and recursively follow the above steps else sends the email to book the uberGo to the input email.
