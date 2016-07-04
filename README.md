# uber-reminder
It reminds to book Uber according to availability and traffic

###Solution - 

The application takes 4 inputs
####Source, Destination, Time and Email

It gets the time for uberGO using Uber API
It find the time to travel between Source and Destination using Maps API

After that 
It calculates the difference between current time and time given by user,
call that remaining time.

It calculates the difference the sum of uberGO time and maps time + 1h
{Here 1 hour is taken to handle traffic variations}

then the calculates new remaining time is remaining time - sum

After this it waits for the remaining time and recursively follow the above steps.
