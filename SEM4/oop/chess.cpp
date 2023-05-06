#include <bits/stdc++.h>
using namespace std;
void s1(int x, int y, int arr[][9]);
void s1d(int x, int y, int arr[][9]);
void s2(int x, int y, int arr[][9]);
void s2d(int x, int y, int arr[][9]);
void s3(int x, int y, int arr[][9]);
void s3d(int x, int y, int arr[][9]);
void s4(int x, int y, int arr[][9]);
void s4d(int x, int y, int arr[][9]);
void calcstep(int x_in, int y_in, int arr[][9]);

int main()
{
    int n;
    cout << "enter the size of board\n";
    std::cin >> n;
    int arr[9][9];
    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
            arr[i][j] = -2;
       
    }
    int x_in, y_in, x_out, y_out;
    cout << "Enter th starting coordinates\n";
    cin >> x_in >> y_in;
    arr[x_in][y_in] = 0;
    cout << "Enter th end coordinates\n";
    cin >> x_out >> y_out;
    //s1(x_in, y_in, arr);
    int mi=1;
    calcstep(x_in, y_in, arr);
    s3d(x_in, y_in, arr);
    s4d(x_in, y_in, arr);
    while(arr[x_out][y_out]==-2){
    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++){
            if(arr[i][j]==mi){
                calcstep(i, j, arr);
            }
        } 
            
    }
        mi++;
    }
    cout<<"\n The total no, of steps deeded from start to end is  : "<<arr[x_out][y_out]<<endl;
    //calcstep(x_in, y_in, arr);
    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++){
            if(arr[i][j]>-1){
                if((i==x_out)&&(j==y_out)) cout<<"$"<< arr[i][j]<<"|";
                else cout << arr[i][j] << " | ";
                 }
            else cout<<"# | ";
            }
        cout << endl;
    }
}
void calcstep(int x_in, int y_in, int arr[][9])
{
    s1(x_in, y_in, arr);
    s1d(x_in, y_in, arr);
    s2(x_in, y_in, arr);
    s2d(x_in, y_in, arr);
    s3(x_in, y_in, arr);
    s3d(x_in, y_in, arr);
    s4(x_in, y_in, arr);
    s4d(x_in, y_in, arr);
}
void s1(int x, int y, int arr[][9])
{
    int a, b, step;
    a = x + 2;
    b = y + 1;
    step = arr[x][y];
    
    
    if (((a >-1)&&(b>-1))&&(a&&b<9))
    {
        if (arr[a][b]==-2)
        {
            step++;
            arr[a][b] = step;
            
        }
    }
}
void s1d(int x, int y, int arr[][9])
{
    int a, b, step;
    a = x + 1;
    b = y + 2;
    step = arr[x][y];
    
    
    if (((a >-1)&&(b>-1))&&(a&&b<9))
    {
        if (arr[a][b]==-2)
        {
            step++;
            arr[a][b] = step;
            
        }
    }
}
void s2(int x, int y, int arr[][9])
{
    int a, b, step;
    a = x + 2;
    b = y - 1;
    step = arr[x][y];
    
    
    if (((a >-1)&&(b>-1))&&(a&&b<9))
    {
        if (arr[a][b]==-2)
        {
            step++;
            arr[a][b] = step;
            
        }
    }
    
}
void s2d(int x, int y, int arr[][9])
{
    int a, b, step;
    a = x + 1;
    b = y - 2;
    step = arr[x][y];
    
    
    if (((a >-1)&&(b>-1))&&(a&&b<9))
    {
        if (arr[a][b]==-2)
        {
            step++;
            arr[a][b] = step;
            
        }
    }
}
void s3(int x, int y, int arr[][9])
{
    int a, b, step;
    a = x - 2;
    b = y - 1;
    step = arr[x][y];
    
    
    if (((a >-1)&&(b>-1))&&(a&&b<9))
    {
        if (arr[a][b]==-2)
        {
            step++;
            arr[a][b] = step;
            
        }
    }
}
void s3d(int x, int y, int arr[][9])
{
    int a, b, step;
    a = x - 1;
    b = y - 2;
    step = arr[x][y];
    //cout<<a<<b;
    
    if (((a >-1)&&(b>-1))&&(a&&b<9))
    {
        if (arr[a][b]==-2)
        {
            step++;
            arr[a][b] = step;
            
            
        }
    }
}
void s4(int x, int y, int arr[][9])
{
    int a, b, step;
    a = x - 2;
    b = y + 1;
    step = arr[x][y];
    
    
    if (((a >-1)&&(b>-1))&&(a&&b<9))
    {
        if (arr[a][b]==-2)
        {
            step++;
            arr[a][b] = step;
            
        }
    }
}
void s4d(int x, int y, int arr[][9])
{
    int a, b, step;
    a = x - 1;
    b = y + 2;
    step = arr[x][y];
    //cout<<a<<b;
    
    if (((a >-1)&&(b>-1))&&(a&&b<9))
    {   
        if (arr[a][b]==-2)
        {
            step++;
            arr[a][b] = step;
            
            
        }
    }
}
