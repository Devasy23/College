// code for hamming code of 4 bits
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int a[4], b[7], i, j, k, x, y, z;
    cout << "Enter 4 bits of data one by one" << endl;
    for (i = 0; i < 4; i++)
    {
        cin >> a[i];
    }
    b[0] = a[0];
    b[1] = a[1];
    b[3] = a[2];
    b[6] = a[3];
    b[4] = b[0] ^ b[1] ^ b[3];
    b[2] = b[0] ^ b[3] ^ b[6];
    b[5] = b[1] ^ b[3] ^ b[6];
    cout << "Encoded data is" << endl;
    for (i = 0; i < 7; i++)
    {
        cout << b[i];
    }
    cout << endl;
    cout << "Enter received data bits one by one" << endl;
    for (i = 0; i < 7; i++)
    {
        cin >> b[i];
    }
    x = b[6] ^ b[4] ^ b[2] ^ b[0];
    y = b[5] ^ b[4] ^ b[1] ^ b[0];
    z = b[3] ^ b[2] ^ b[1] ^ b[0];

    i = 3 * x + 2 * y + z;
    if (i == 0)
    {
        cout << "No error while transmission of data" << endl;
    }
    else
    {
        cout << "Error on position " << i << endl;
        cout << "Data sent : ";
        for (j = 0; j < 7; j++)
        {
            cout << b[j];
        }
        cout << endl;
        cout << "The correct message is : ";
        if (b[7 - i] == 0)
        {
            b[7 - i] = 1;
        }
        else
        {
            b[7 - i] = 0;
        }
        for (j = 0; j < 7; j++)
        {
            cout << b[j];
        }
    }
    return 0;
}