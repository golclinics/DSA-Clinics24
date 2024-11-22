#include <iostream>

using namespace std;
void fizzBuzz();
int main(){
    fizzBuzz();

    return 0;
}

void fizzBuzz(){
    for(int i=0;i<=100;i++){
        if (i%15 == 0){
            cout<<"FizzBuzz"<<endl;
        }
        else if(i%3 == 0){
            cout<<"Fizz"<<endl;
        }
        else if(i%5 == 0){
            cout<<"Buzz"<<endl;
        }
        else{
            cout<<i<<endl;
        }
    }
}
