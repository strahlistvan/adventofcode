#include <iostream>
using namespace std;

int main()
{
	const int PRESENT_LIMIT = 33100000; 
	int house = 1, house_present = 0;
	while (house_present < PRESENT_LIMIT)
	{
		house_present = 0;
		for (int num=1; num<=house; ++num)
		{
			if (house%num==0 && house<=50*num)
				house_present+=11*num;
		}
		if (house%10000==0) 
			cout<<"House "<<house<<" got "<<house_present<<" presents."<<endl;
		++house;
	}
	cout<<"House "<<(house-1)<<" got "<<house_present<<" presents."<<endl;
}
