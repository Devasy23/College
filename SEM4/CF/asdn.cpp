#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int n,b,r, ratio=0;
        cin>>n>>r>>b;
        ratio=r/b+1;
        for(int i=0; i<n;i++ ){
            for (int i = 0; i < ceil(r/b+1); i++)
            {
                if(r>0){
                    cout<<'R';
                    r--;
                }
                // else break;
            }
            if(b>0){
            cout<<'B';
            b--;
            }
            // else break;
        }
        cout<<endl;

	}
	return 0;
}