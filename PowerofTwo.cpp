/*
Power of Two
Write a program that takes an integer as input and returns true if the input is a power of two.

Examples:

8=> returns true
6=> returns false
*/
#include<iostream>
using namespace std;
bool power(int x)
{
    //x has to be greater than 0
    if ((x>0)&&(x&(x-1))==0)
    {
        return true;
    }
    else
    {
        return false;
    }


}
int main()
{
    int n;
    cout<<"Enter an integer:\n";
    cin>>n;
    if (power(n)==true)
    {
        cout<<"True\n";
    }
    else
    {
       cout<<"False\n";
    }
    return 0;
}


