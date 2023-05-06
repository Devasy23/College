#ifndef ADMINISTRATOR_H
#define ADMINISTRATOR_H

#include <bits/stdc++.h>
using namespace std;
class Administrator
{
private:
    // Administrator password for controlling whole system
    string password = "#D_202_240";
    // Train data
    string name, route, time;
    int price, id;

public:
    Administrator(void);
    string getPassword(void);       // return administrator password
    void displayTrainDetails(void); // Display all trains that are available from "TrainDetails.csv"
    void addTrainDetails(void);     // Take train details and save them into "TrainDetails.csv" File
    void updateTrainDetails(void);  // Update train details except train ID
    void readTrainDetails(void);    // Read train data by taking train ID from "TrainDetails.csv" File
    void deleteTrainDetails(void);  // Delete train data by taking train ID from "TrainDetails.csv" File
};

#endif // ADMINISTRATOR_H
