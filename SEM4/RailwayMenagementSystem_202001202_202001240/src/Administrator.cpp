#include "Administrator.h"

string Administrator::getPassword(void)
{
    return password;
}
Administrator::Administrator(void) {}
void Administrator::displayTrainDetails(void)
{
    fstream fin; // FILE pointer to read data
    fin.open("TrainDetails.csv", ios::in); // open "TrainDetails.csv" in read mode by fstream FILE pointer
    vector<string> row;
    string line, word, temp;
    cout << "Train Details :-" << endl << endl;
    while (!fin.eof()) // This loop will run until it reach the end of the file
    {
        // print data row by row
        row.clear();
        getline(fin, line);
        stringstream s(line);
        // storing data of train in row vector
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
    fin.close(); // close FILE
}
void Administrator::addTrainDetails(void)
{
    fstream fout; // FILE pointer to write data
    fout.open("TrainDetails.csv", ios::out | ios::app);
    getchar();
    cout << "Enter train name : ";
    getline(cin, name); // Take space separated input
    fstream fin;
    fin.open("TrainDetails.csv", ios::in); // FILE pointer to read data
    vector<string> row;
    string line, word, temp;
    // Code from line 45 to line 58 is returning the id of new train
    id = 10000;
    while (!fin.eof())
    {
        row.clear();
        getline(fin, line);
        stringstream s(line);
        while (getline(s, word, ','))
        {
            row.push_back(word);
        }
        if (row[1] != "Id")
            id = stoi(row[1], nullptr, 10);
    }
    id = id + 1;
    cout << "New train ID : " << id << endl;
    cout << "Enter route : ";
    getline(cin, route);
    cout << "Enter time (According to a 24 hour clock): ";
    getline(cin, time);
    cout << "Enter price : ";
    cin >> price;
    // Write Train data in "TrainDetails.csv" file
    fout << "\n"
         << name << "," << id << "," << route << "," << time << "," << price;
    cout << name << " added...." << endl;
    fout.close();
    fin.close();
}
void Administrator::updateTrainDetails(void)
{
    fstream fin, fout;
    fin.open("TrainDetails.csv", ios::in);
    fout.open("TrainDetailsNew.csv", ios::out);
    string line, word;
    vector<string> row;
    string id;
    cout << "Enter Train ID : ";
    cin >> id;
    int a = 0, temp = 0;
    while (!fin.eof())
    {
        row.clear();
        getline(fin, line);
        stringstream s(line);
        while (getline(s, word, ','))
        {
            row.push_back(word);
        }
        if (row[1] == id) // comparing train id and user inputed id
        {
            temp = 1;
            a++;
            int iter;
            do
            {
                cout << "What do you want to update?" << endl;
                cout << "1. Name" << endl
                     << "2. Route" << endl
                     << "3. Time" << endl
                     << "4. Price" << endl
                     << "5. Exit" << endl;
                cin >> iter;
                getchar();
                switch (iter)
                {
                case 1:
                {
                    string n;
                    cout << "Enter new Name : " << endl;
                    getline(cin, n);
                    row[0] = n;
                    break;
                }
                case 2:
                {
                    string n;
                    cout << "Enter Route : " << endl;
                    getline(cin, n);
                    row[2] = n;
                    break;
                }
                case 3:
                {
                    string n;
                    cout << "Enter new Time : " << endl;
                    getline(cin, n);
                    row[3] = n;
                    break;
                }
                case 4:
                {
                    string n;
                    cout << "Enter new Price : " << endl;
                    getline(cin, n);
                    row[4] = n;
                    break;
                }
                case 5:
                {
                    cout << "";
                    break;
                }
                default:
                    cout << "invalid input" << endl;
                    break;
                }
            }
            while (iter != 5);
            if (a == 1) // condition to write data of first line in "TrainDetails.csv"
            {
                fout << row[0] << ",";
                for (int i = 1; i <= 3; i++)
                {
                    fout << row[i] << ",";
                }
                fout << row[4];
            }
            else
            {
                fout << "\n"
                     << row[0] << ",";
                for (int i = 1; i <= 3; i++)
                {
                    fout << row[i] << ",";
                }
                fout << row[4];
            }
        }
        else
        {
            a++;
            if (a == 1) // condition to write data of first line in "TrainDetails.csv"
            {
                fout << row[0] << ",";
                for (int i = 1; i <= 3; i++)
                {
                    fout << row[i] << ",";
                }
                fout << row[4];
            }
            else
            {
                fout << "\n"
                     << row[0] << ",";
                for (int i = 1; i <= 3; i++)
                {
                    fout << row[i] << ",";
                }
                fout << row[4];
            }
        }
    }
    if (temp != 1)
    {
        cout << "Train Record not Found !!" << endl;
    }
    fin.close();
    fout.close();
    remove("TrainDetails.csv"); // delete file
    rename("TrainDetailsNew.csv", "TrainDetails.csv"); // rename first file to second file
}
void Administrator::readTrainDetails()
{
    fstream fin;
    fin.open("TrainDetails.csv", ios::in);
    string word, line, id;
    cout << "Enter Train Id : ";
    cin >> id;
    int count = 0;
    vector<string> row;
    while (!fin.eof())
    {
        row.clear();
        getline(fin, line);
        stringstream s(line);
        while (getline(s, word, ','))
        {
            row.push_back(word);
        }
        if (id == row[1])
        {
            count = 1;
            cout << "Name : " << row[0] << endl;
            cout << "Id : " << row[1] << endl;
            cout << "Route : " << row[2] << endl;
            cout << "Time : " << row[3] << endl;
            cout << "Ticket Price : " << row[4] << "/-" << endl;
        }
    }
    if (count != 1)
    {
        cout << "Train Record not Found !!" << endl;
    }
}
void Administrator::deleteTrainDetails(void)
{
    fstream fin, fout;
    fin.open("TrainDetails.csv", ios::in);
    fout.open("TrainDetailsNew.csv", ios::out);
    string line, word;
    vector<string> row;
    string id;
    cout << "Enter Train ID : ";
    cin >> id;
    int a = 0;
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
        if (row[1] == id)
        {
            count = 1;
            a++;
            cout << "Train data has been deleted !!" << endl;
        }
        else
        {
            a++;
            if (a == 1)
            {
                fout << row[0] << ",";
                for (int i = 1; i <= 3; i++)
                {
                    fout << row[i] << ",";
                }
                fout << row[4];
            }
            else
            {
                fout << "\n"
                     << row[0] << ",";
                for (int i = 1; i <= 3; i++)
                {
                    fout << row[i] << ",";
                }
                fout << row[4];
            }
        }
    }
    if (count != 1)
    {
        cout << "Train Record not Found !!" << endl;
    }
    fin.close();
    fout.close();
    remove("TrainDetails.csv");
    rename("TrainDetailsNew.csv", "TrainDetails.csv");
}
