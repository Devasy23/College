#include "customer.h"

customer::customer(void) {}
void customer::printTicket(void)
{
    fstream fin, fint; // FILE pointers to read data
    fin.open("customerDetails.csv", ios::in);
    fint.open("TrainDetails.csv", ios::in);
    vector<string> row, row1;
    string line, line1, word, word1;
    string id;
    cout << "Enter your ID : ";
    cin >> id;
    cout << "Enter Password : ";
    cin >> password;
    int count = 0;
    // Print tickets
    while (!fin.eof())
    {
        row.clear();
        getline(fin, line);
        stringstream s(line);
        while (getline(s, word, ','))
        {
            row.push_back(word);
        }
        if (row[6] == id)
        {
            if (row[7] == password)
            {
                count = 1;
                cout << "---------------------------------------------------------------" << endl
                     << "|                                                             |" << endl
                     << "|                       CUSTOMER DETAILS                      |" << endl
                     << "|                                                             |" << endl
                     << "|  NAME : " << row[0] << setw(53 - row[0].size()) << " |" << endl
                     << "|  AGE : " << row[1] << "              PHONE NO. : " << row[2] << setw(16) << " |" << endl
                     << "|  CUSTOMER ID : " << row[6] << setw(42) << " |" << endl
                     << "|                                                             |" << endl
                     << "|                                                             |" << endl
                     << "|                         TRAIN DETAILS                       |" << endl
                     << "|                                                             |" << endl;
                // print train details
                while (!fint.eof())
                {
                    row1.clear();
                    getline(fint, line1);
                    stringstream s1(line1);
                    while (getline(s1, word1, ','))
                    {
                        row1.push_back(word1);
                    }
                    if (row1[1] == row[8])
                    {
                        cout << "|  NAME : " << row1[0] << setw(53 - row1[0].size()) << " |" << endl
                             << "|  TRAIN NUMBER : " << row1[1] << "         "
                             << "ROUTE : " << row1[2] << setw(23 - row1[2].size()) << " |" << endl
                             << "|  Time : " << row1[3] << setw(53 - row1[3].size()) << "  |" << endl
                             << "|  Tickets : " << row[3] << "         Total Amount : " << row[5] << "/-" << setw(24 - row[3].size() - row[5].size()) << " |" << endl;
                    }
                }
                cout << "|                                                             |" << endl
                     << "---------------------------------------------------------------" << endl;
            }
            else
            {
                cout << "Wrong password ! " << endl;
                goto end3;
            }
        }
    }
    if (count != 1)
    {
        cout << endl << "Record not found !!" << endl << endl;
    }
    // close files
    fin.close();
    fint.close();
end3:
    cout << "";
}
void customer::addCustomerDetails(void)
{
    fstream fout;
    fout.open("customerDetails.csv", ios::out | ios::app); // open "customerDetails.csv" in write mode by fstream FILE pointer
    getchar();
    cout << "Enter your name : ";
    getline(cin, name);
    cout << "Enter your age : ";
    cin >> age;
    cout << "Enter your phone number : ";
    cin >> phoneNumber;
    fstream finc;
    finc.open("customerDetails.csv", ios::in); // open "customerDetails.csv" in read mode by fstream FILE pointer
    vector<string> row;
    string line, word, temp;
    fout << "\n"
         << name << ","
         << age << ","
         << phoneNumber << ",";
    id = 1000;
    // Code from line 100 to line 112 is returning the id of new customer
    while (!finc.eof())
    {
        row.clear();
        getline(finc, line);
        stringstream s(line);
        while (getline(s, word, ','))
        {
            row.push_back(word);
        }
        if (row[6] != "Id")
            id = stoi(row[6], nullptr, 10);
    }
    id = id + 1;
    cout << "This is your ID : " << id << endl;
    cout << "Enter your password : ";
    cin >> password;
    cout << endl << endl;
up1:
    displayTrainDetails();
    cout << endl << endl;
    cout << "Enter train number : ";
    cin >> trainNumber;
    fstream fint;
    int c = 0;
    fint.open("TrainDetails.csv", ios::in);
    // Code from line 124 to line 140 is returning the price of selected train
    int tempTrainNumber;
    while (!fint.eof())
    {
        row.clear();
        getline(fint, line);
        stringstream s(line);
        while (getline(s, word, ','))
        {
            row.push_back(word);
        }
        if (row[1] != "Id")
        {
            tempTrainNumber = stoi(row[1], nullptr, 10);
            if (tempTrainNumber == trainNumber)
            {
                price = stoi(row[4], nullptr, 10);
                c = 1;
            }
        }
    }
    if(c == 1)
    {
        cout << "How many tickets do you want?" << endl;
        cin >> tickets;
        fout << tickets << ","
             << price << ","
             << tickets * price << ","
             << id << ","
             << password << ","
             << trainNumber;
        cout << "Total price : " << tickets * price << endl;
    }
    else
    {
        cout << "Invalid Train Number !! " << endl << endl;
        goto up1;
    }
    fout.close();
    fint.close();
    finc.close();
}
void customer::displayTrainDetails(void)
{
    fstream fin;
    fin.open("TrainDetails.csv", ios::in);
    vector<string> row;
    string line, word, temp;
    cout << "Train Details :-" << endl << endl;
    while (!fin.eof())
    {
        row.clear();
        getline(fin, line);
        stringstream s(line);
        while (getline(s, word, ','))
        {
            row.push_back(word);
        }
        cout << row[0] << setw(23 - row[0].size()) << " | ";
        cout << row[1] << setw(8 - row[1].size()) << " | ";
        cout << row[2] << setw(25 - row[2].size()) << " | ";
        cout << row[3] << setw(16 - row[3].size()) << " | ";
        cout << row[4] << endl;
    }
    fin.close();
}
void customer::updateCustomerDetails(void)
{
    fstream fin, fout;
    fin.open("customerDetails.csv", ios::in);
    fout.open("customerDetailsNew.csv", ios::out);
    string line, word;
    vector<string> row;
    string id;
    cout << "Enter your ID : ";
    cin >> id;
    cout << "Enter Password : ";
    cin >> password;
    int a = 0, count = 0;
    while (!fin.eof())
    {
        row.clear();
        getline(fin, line);
        stringstream s(line);
        while (getline(s, word, ','))
        {
            row.push_back(word);
        }
        if (row[6] == id)
        {
            if (row[7] == password)
            {
                a++;
                count = 1;
                int iter;
                do
                {
                    cout << "What do you want to update?" << endl;
                    cout << "1. Name" << endl
                         << "2. Age" << endl
                         << "3. Phone Number" << endl
                         << "4. Number of Tickets" << endl
                         << "5. Password" << endl
                         << "6. Exit" << endl;
                    cin >> iter;
                    switch (iter)
                    {
                    case 1:
                    {
                        string n;
                        cout << "Enter new Name : " << endl;
                        getchar();
                        getline(cin, n);
                        row[0] = n;
                        break;
                    }
                    case 2:
                    {
                        string n;
                        cout << "Enter Age : " << endl;
                        cin >> n;
                        row[1] = n;
                        break;
                    }
                    case 3:
                    {
                        string n;
                        cout << "Enter new phone number : " << endl;
                        cin >> n;
                        row[2] = n;
                        break;
                    }
                    case 4:
                    {
                        int num1, num2;
                        string n;
                        cout << "How many tickets do you want ? " << endl;
                        cin >> n;
                        row[3] = n;
                        num1 = stoi(row[4], nullptr, 10); // convert string to number (stoi (string, nullptr, base))
                        num2 = stoi(row[3], nullptr, 10);
                        num1 = num1 * num2;
                        row[5] = to_string(num1); // convert number to string
                        break;
                    }
                    case 5:
                    {
                        string n1, n2;
                        cout << "Enter new password : ";
                        cin >> n1;
pass:
                        cout << "Enter password again : ";
                        cin >> n2;
                        if (n1 == n2)
                        {
                            row[7] = n1;
                            cout << endl << "Password Updated !!" << endl;
                        }
                        else
                        {
                            cout << "Wrong Password !" << endl;
                            goto pass;
                        }
                        break;
                    }
                    case 6:
                        break;
                    default:
                        cout << "invalid input" << endl;
                        break;
                    }
                }
                while (iter != 6);
                if (a == 1)
                {
                    fout << row[0] << ",";
                    for (int i = 1; i <= 7; i++)
                    {
                        fout << row[i] << ",";
                    }
                    fout << row[8];
                }
                else
                {
                    fout << "\n"
                         << row[0] << ",";
                    for (int i = 1; i <= 7; i++)
                    {
                        fout << row[i] << ",";
                    }
                    fout << row[8];
                }
            }
            else
            {
                cout << " wrong password ! " << endl;
                fin.close();
                fout.close();
                remove("customerDetailsNew.csv");
                goto end2;
            }
        }
        else
        {
            a++;
            if (a == 1)
            {
                fout << row[0] << ",";
                for (int i = 1; i <= 7; i++)
                {
                    fout << row[i] << ",";
                }
                fout << row[8];
            }
            else
            {
                fout << "\n"
                     << row[0] << ",";
                for (int i = 1; i <= 7; i++)
                {
                    fout << row[i] << ",";
                }
                fout << row[8];
            }
        }
    }
    fin.close();
    fout.close();
    remove("customerDetails.csv");
    rename("customerDetailsNew.csv", "customerDetails.csv");
    if (count != 1)
    {
        cout << endl << "Record not found !!" << endl << endl;
    }
end2:
    cout << "";
}
void customer::readCustomerDetails(void)
{
    fstream fin;
    fin.open("customerDetails.csv", ios::in);
    vector<string> row;
    string line, word, temp;
    string id;
    cout << "Enter your ID : ";
    cin >> id;
    cout << "Enter Password : ";
    cin >> password;
    int count = 0;
    while (!fin.eof())
    {
        row.clear();
        getline(fin, line);
        stringstream s(line);
        while (getline(s, word, ','))
        {
            row.push_back(word);
        }
        if (row[6] == id)
        {
            if (row[7] == password)
            {
                count = 1;
                cout << "Name : " << row[0] << endl;
                cout << "Age : " << row[1] << endl;
                cout << "Phone Number : " << row[2] << endl;
                cout << "Number of tickets : " << row[3] << endl;
                cout << "Total Price : " << row[5] << endl;
            }
            else
            {
                cout << "Wrong password ! " << endl;
            }
        }
    }
    if (count != 1)
    {
        cout << endl << "Record not found !!" << endl << endl;
    }
    fin.close();
}
void customer::deleteCustomerDetails(void)
{
    fstream fin, fout;
    fin.open("customerDetails.csv", ios::in);
    fout.open("customerDetailsNew.csv", ios::out);
    string line, word;
    vector<string> row;
    string id;
    int a = 0, count = 0;
    cout << "Enter your ID : ";
    cin >> id;
    cout << "Enter Password : ";
    cin >> password;
    while (!fin.eof())
    {
        row.clear();
        getline(fin, line);
        stringstream s(line);
        while (getline(s, word, ','))
        {
            row.push_back(word);
        }
        if (row[6] == id)
        {
            if (row[7] == password)
            {
                count = 1;
                a++;
                cout << "Ticket Cancelled !!" << endl;
            }
            else
            {
                cout << "Wrong password !!" << endl;
                fin.close();
                fout.close();
                remove("customerDetailsNew.csv");
                goto end;
            }
        }
        else
        {
            a++;
            if (a == 1)
            {
                fout << row[0] << ",";
                for (int i = 1; i <= 7; i++)
                {
                    fout << row[i] << ",";
                }
                fout << row[8];
            }
            else
            {
                fout << "\n"
                     << row[0] << ",";
                for (int i = 1; i <= 7; i++)
                {
                    fout << row[i] << ",";
                }
                fout << row[8];
            }
        }
    }
    fin.close();
    fout.close();
    remove("customerDetails.csv");
    rename("customerDetailsNew.csv", "customerDetails.csv");
    if (count != 1)
    {
        cout << endl << "Record not found !!" << endl << endl;
    }
end:
    cout << "";
}
