#include <Administrator.h>
#include <customer.h>
#include <windows.h>

int main()
{
    system("cls");
    system("color B");
    int ch, iter;
    cout << endl
         << endl;
    cout << "         ----------------------------------------------------\n";
    cout << "         |            RAILWAY MANAGEMENT SYSTEM             |\n";
    cout << "         ----------------------------------------------------\n";
    cout << endl
         << endl;
    do
    {
        cout << "\n\n--> MAIN MENU\n\n";
        cout << "\t\t1. Administrator Menu\n\t\t2. User Menu\n\t\t3. Exit\n\n";
        cout << "\t\tEnter your choice : ";
        cin >> ch;
        cout << endl << endl;
        switch (ch)
        {
        case 1:
        {
            Administrator admin;
            string pass;
            cout << "\t\tEnter Administrator Password : ";
            cin >> pass;
            if (pass == admin.getPassword())
            {
                system("cls");
                system("color 2");
                do
                {
                    cout << "\n\n--> ADMINISTRATOR MENU\n\n";
                    cout << "\t\t1. Display All Train Details" << endl
                         << "\t\t2. Add New Train" << endl
                         << "\t\t3. Update Train Details" << endl
                         << "\t\t4. Search Train Details" << endl
                         << "\t\t5. Remove Train" << endl
                         << "\t\t6. Return to MAIN MENU" << endl
                         << endl
                         << "\t\tEnter your choice : ";
                    cin >> iter;
                    switch (iter)
                    {
                    case 1:
                    {
                        system("cls");
                        cout << endl
                             << endl;
                        admin.displayTrainDetails();
                        cout << endl
                             << endl;
                        cout << "Press ENTER to continue...." << endl
                             << endl
                             << endl;
                        getchar();
                        getchar();
                        break;
                    }
                    case 2:
                    {
                        system("cls");
                        cout << endl
                             << endl;
                        admin.addTrainDetails();
                        cout << endl
                             << endl;
                        cout << "Press ENTER to continue...." << endl
                             << endl
                             << endl;
                        getchar();
                        getchar();
                        break;
                    }
                    case 3:
                    {
                        system("cls");
                        cout << endl
                             << endl;
                        admin.updateTrainDetails();
                        cout << endl
                             << endl;
                        cout << "Press ENTER to continue...." << endl
                             << endl
                             << endl;
                        getchar();
                        getchar();
                        break;
                    }
                    case 4:
                    {
                        system("cls");
                        cout << endl
                             << endl;
                        admin.readTrainDetails();
                        cout << endl
                             << endl;
                        cout << "Press ENTER to continue...." << endl
                             << endl
                             << endl;
                        getchar();
                        getchar();
                        break;
                    }
                    case 5:
                    {
                        system("cls");
                        cout << endl
                             << endl;
                        admin.deleteTrainDetails();
                        cout << endl
                             << endl;
                        cout << "Press ENTER to continue...." << endl
                             << endl
                             << endl;
                        getchar();
                        getchar();
                        break;
                    }
                    case 6:
                        break;
                    default:
                        system("cls");
                        cout << endl
                             << endl;
                        cout << "INVALIDE INPUT !!" << endl
                             << endl;
                        cout << "Press ENTER to continue...." << endl
                             << endl
                             << endl;
                        getchar();
                        getchar();
                        break;
                    }
                    system("cls");
                }
                while (iter != 6);
                system("color B");
                break;
            }
            else
                cout << "WRONG PASSWORD !!" << endl;
        }
        case 2:
        {
            customer consumer;
            system("cls");
            system("color 2");
            do
            {
                cout << "--> USER MENU\n\n";
                cout << "\t\t1. Add New User" << endl
                     << "\t\t2. Update User Data" << endl
                     << "\t\t3. Display User Data" << endl
                     << "\t\t4. Cancel Ticket" << endl
                     << "\t\t5. Print Ticket" << endl
                     << "\t\t6. Return to MAIN MENU" << endl
                     << endl
                     << "\t\tEnter your choice : ";
                cin >> iter;
                switch (iter)
                {
                case 1:
                {
                    system("cls");
                    cout << endl
                         << endl;
                    consumer.addCustomerDetails();
                    cout << endl
                         << endl;
                    cout << "Press ENTER to continue...." << endl
                         << endl
                         << endl;
                    getchar();
                    getchar();
                    break;
                }
                case 2:
                {
                    system("cls");
                    cout << endl
                         << endl;
                    consumer.updateCustomerDetails();
                    cout << endl
                         << endl;
                    cout << "Press ENTER to continue...." << endl
                         << endl
                         << endl;
                    getchar();
                    getchar();
                    break;
                }
                case 3:
                {
                    system("cls");
                    cout << endl
                         << endl;
                    consumer.readCustomerDetails();
                    cout << endl
                         << endl;
                    cout << "Press ENTER to continue...." << endl
                         << endl
                         << endl;
                    getchar();
                    getchar();
                    break;
                }
                case 4:
                {
                    system("cls");
                    cout << endl
                         << endl;
                    consumer.deleteCustomerDetails();
                    cout << endl
                         << endl;
                    cout << "Press ENTER to continue...." << endl
                         << endl
                         << endl;
                    getchar();
                    getchar();
                    break;
                }
                case 5:
                {
                    system("cls");
                    cout << endl
                         << endl;
                    consumer.printTicket();
                    cout << endl
                         << endl;
                    cout << "Press ENTER to continue...." << endl
                         << endl
                         << endl;
                    getchar();
                    getchar();
                    break;
                }
                case 6:
                    break;
                default:
                    system("cls");
                    cout << endl
                         << endl;
                    cout << "INVALIDE INPUT !!" << endl
                         << endl;
                    cout << "Press ENTER to continue...." << endl
                         << endl
                         << endl;
                    getchar();
                    getchar();
                    break;
                }
                system("cls");
            }
            while (iter != 6);
            system("color B");
            break;
        }
        break;
        case 3:
            break;
        }
    }
    while (ch < 3);
    system("cls");
    system("color 74");
    cout << "\n\n";
    cout << "                              --------------------------------------------------------------------------------------------------------------" << endl
         << "                              |  This \"RAILWAY MANAGEMENT SYSTEM\" is developed by Virat Chaudhari(202001240) and Jaimin Satani(202001202)  |" << endl
         << "                              --------------------------------------------------------------------------------------------------------------" << endl;
    cout << "\n\n";
    return 0;
}
