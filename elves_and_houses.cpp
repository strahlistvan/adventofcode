#include <iostream>
#include <cmath>
using namespace std;

int sigma(int number);

int main()
{
	const int PRESENT_LIMIT = 33100000; 
	int house = 1, house_present = 0;
	while (house_present < PRESENT_LIMIT)
	{
		house_present = 10*sigma(house);
		if (house%10000==0) 
			cout<<"House "<<house<<" got "<<house_present<<" presents."<<endl;
		++house;
	}
	cout<<"House "<<(house-1)<<" got "<<house_present<<" presents."<<endl;
}

int sigma(int number)
{
	int prime = 2, mult = 0, result = 1;
	if (number<2) 
		return result;
	
	while (number>1)
	{
		while (number%prime==0)
		{
			++mult;
			number/=prime;
		}
		result*=(pow(prime,mult+1)-1)/(prime-1);
		mult = 0;
		++prime;	
	}
	return result;
}
