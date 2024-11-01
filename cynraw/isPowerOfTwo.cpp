#include<iostream>
using namespace std;

/*void powerOfTwo(){
  int num;
  cout<<"Enter the range of numbers you want to obtain the powers of 2"<<endl;
  cin>>num;
  for(int i =1; i<= num; i++){
    if((i & (i-1)) == 0){
        cout<< i <<endl;
    }
  }  
}
*/
bool isPowerOfTwo(int num){
        if (num > 0 && ((num & num -1) == 0) ){
            cout << num <<" is a power of two";
            return true;
        }
        else 
        cout << num << " is not a power of two" << endl;
        return false;
}

int main(){
    int n;
    cout<<"Enter a number you wish to check if its a power of two:";
    cin>>n;
    isPowerOfTwo(n);

    return 0;
}