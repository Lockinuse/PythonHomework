#***************************************************************
#
#  Author:            Breanna Plimpton
#
#  Program #:         6
#
#  File Name:         Program6.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          06/27/2016
#
#  Instructor:        Fred Kumi 
#
#  Chapter:           Chapter #6
#
#  Description:
#   This program gives you the occupancy rate for each hotel
#
#***************************************************************

#***************************************************************
#
#  Function:     main
# 
#  Description:  The main function of the program
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************


def main():

    NumberOfFloors = int(input("How many floors does this Hotel have? "))
    Floor = 1
    TotalRoomsTogether = 0
    TotalRoomsOccupied = 0
    TotalRoomsUnoccupied = 0

    while Floor <= NumberOfFloors:
        Floor = Floor + 1
        RoomsOnFloor = int(input("How many rooms are on this floor? "))
        RoomsOccupied = int(input("How many rooms are occupied on this floor? "))
        TotalRoomsTogether = TotalRoomsTogether + RoomsOnFloor
        TotalRoomsOccupied = TotalRoomsOccupied + RoomsOccupied
        TotalRoomsUnoccupied = TotalRoomsUnoccupied + (RoomsOnFloor - RoomsOccupied)

    print("This Hotel has", TotalRoomsTogether, "rooms in total.")
    print("This Hotel has", TotalRoomsOccupied, "rooms occupied.")
    print("This Hotel has", TotalRoomsUnoccupied, "rooms unoccupied.")

    OccupancyRate = (TotalRoomsOccupied / TotalRoomsTogether) * 100
    print("This Hotel's occupancy rate is at", format(OccupancyRate, '.2f'), "%.")

    # End of main
    
#***************************************************************
#
#  Function:     userInfo
# 
#  Description:  Prints Programmer's information
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************


def userInfo():
    print('Name:     Breanna Plimpton')
    print('Course:   Programming Fundamentals I')
    print('Program:  6')
    print()
    # End of userInfo


# Call functions
userInfo()
main()

# End of Program 6
