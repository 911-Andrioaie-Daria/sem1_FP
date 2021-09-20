# Airplane!
Write a console-based application to help air traffic control monitor all domestic flights taking place during one day (`00:00 – 23:59`). The application must include the following features:
1.	Flight information is kept in a text file. The `input.txt` file included in this repository provides a suitable example. When the program starts, flight information is read from the input file **[1p]**. Modifications are persisted to the text file **[1p]**.
2.	Add a new flight. Each flight has an `identifier`, a `departure city` and ` departure time`, and an `arrival city` and `arrival time`. Flight identifiers are unique; flight times are between 15 and 90 minutes; an airport can handle a single operation (departure or arrival) during each minute (e.g. *two planes cannot leave the same airport at say 15:40, just as one plane cannot depart within the same minute during which another one arrives*) **[1.5p]**. 
3.	Delete a flight. The user provides the flight identifier. If it does not exist, an error message is displayed **[1p]**.
4.	List the airports, in decreasing order of activity (total number of departures and arrivals) **[1p]**.
5.	List the time intervals during which no flights are airborne, in decreasing order of their length. **[1p]**.
6.	List all time intervals during which the maximum number of flights are airborne **[1p]**.
7.	The tracking radar suffers a failure and is unavailaboe for the duration of the day. The backup radar can be used, but it can only track a single flight at a time. Determine the maximum number of flights that can proceed as planned. List them using the format below **[1.5p]**:\
`05:45 | 06:40 | RO650 | Cluj - Bucuresti`

## Non-functional requirements:
- Implement an object-oriented, layered architecture solution using the Python language. 
- Provide specification and PyUnit tests for Repository/Controller functions related with functionality 2 (*add a new flight*). In case specification or tests are missing, the functionality will not be graded.
- For maximum grade, implement all requirements using algorithms that have polynomial complexity.

### default [1p].
