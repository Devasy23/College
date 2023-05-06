#include <bits/stdc++.h>
using namespace std;
int input[32];
int code[32];
int ham_calc(int,int);
int main()
{
	int n,i,p_n = 0,c_l,j,k, c_e=0;
	cout<<("Please enter the length of the Data Word: ");
	cin>>n;
	cout<<("Please enter the Data Word:\n");
	for(i=0;i<n;i++)
	{
		cin>>input[i];
	}

	i=0;
	while(n>(int)pow(2,i)-(i+1))
	{
		p_n++;
		i++;
	}
		
	c_l = p_n + n;
	int call[c_l];
	j=k=0;
	for(i=0;i<c_l;i++)
	{
		
		if(i==((int)pow(2,k)-1))
		{
			code[i]=0;
			k++;
		}
		else
		{
			code[i]=input[j];
			j++;
		}
	}
	for(i=0;i<p_n;i++)
	{
		int position = (int)pow(2,i);
		int value = ham_calc(position,c_l);
		code[position-1]=value;
	}
	cout<<("\nThe calculated Code Word is: ");
	for(i=0;i<c_l;i++)
		cout<<code[i]<<" ";
	cout<<endl;
	cout<<("Please enter the received Code Word:\n");
	int temp=0;
	for(i=0;i<c_l;i++){
		cin>>temp;
		if(code[i]!=temp) c_e++;
		code[i]=temp;}
	int error_pos = 0;
	for(i=0;i<p_n;i++)
	{
		int position = (int)pow(2,i);
		int value = ham_calc(position,c_l);
		if(value != 0)
			error_pos+=position;
	}
    int pos_of_orisig, pos_of_redsig = 0;
    int static rem[1000000]={};
    if (error_pos != 0 || c_e>0){
        cout<<"Error detected!! \n";
        if(code[error_pos-1]==1) code[error_pos-1]=0;
        else code[error_pos-1]=1;
        // for(int i=0; i<p_n; i++ ){
        //     if(i==((int)pow(2,pos_of_orisig)-1)){
        //          pos_of_orisig++; }
        //     else
        //     {
        //         rem[pos_of_redsig]=code[i];
        //         pos_of_redsig++;
        //     }
        // }
        cout<<"corrected code is "<<endl;
    	for(int j=0; j<c_l; j++) cout<<code[j]<<" ";
    }
	else {
		cout<<"NO error detected"<<endl;
    for(int i=0;i < p_n; i++)
    {
        if(i==((int)pow(2,pos_of_orisig)-1))
        { pos_of_orisig++; }
        else
        {   rem[pos_of_redsig]=code[i];
            pos_of_redsig++;} 
    }}
    
    // if(error_pos == 1)
	// 	cout<<("The received Code Word is correct.\n");
	// else
	// 	cout<<("Error at bit position: %d\n",error_pos);
}
int ham_calc(int position,int c_l)
{
	int count=0,i,j;
	i=position-1;
	while(i<c_l)
	{
		for(j=i;j<i+position;j++)
		{
			if(code[j] == 1)
				count++;
		}
		i=i+2*position;
	}
	if(count%2 == 0)
		return 0;
	else
		return 1;
}