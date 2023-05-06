#ifndef CUSTOMER_H
#define CUSTOMER_H

#include <bits/stdc++.h>
using namespace std;
class customer
{
private:
    // Private members for customer details
    string password, name, phoneNumber;
    int tickets, age, id, trainNumber, price;

public:
    customer(void);                   // constructor
    void addCustomerDetails(void);    // Take customer details and save them into "customerDetails.csv" File
    void updateCustomerDetails(void); // Update customer details except customer ID
    void readCustomerDetails(void);   // Read customer data by taking his/her ID and PASSWORD from "customerDetails.csv" File
    void deleteCustomerDetails(void); // Delete customer data by taking his/her ID and PASSWORD from "customerDetails.csv" File
    void displayTrainDetails(void);   // Display all trains that are available from "TrainDetails.csv"
    void printTicket(void);           // Print tickets with customer details and train details
};

#endif // CUSTOMER_H
