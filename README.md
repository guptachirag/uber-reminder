# uber-reminder
It reminds to book Uber according to availability and traffic

### Solution - 

The application takes 4 inputs
#### Source, Destination, Time and Email

Follow the steps below

1. Get the time for uberGO using Uber API
2. Find the time to travel between Source and Destination using Maps API

3. Calculate the difference between current time and time given by user,
#####call that remaining time.

4. Calculate the sum of uberGO time and maps time + 1h, {Here 1 hour is taken to handle traffic variations}
#####call that estimated_journey_duration

5. Calculate the new remaining time i.e. remaining time - estimated_journey_duration

6. If the remaining time > 0, then wait for the remaining time and recursively follow the above steps else sends the email to book the uberGo to the input email.
