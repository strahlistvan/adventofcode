#include <iostream>
#include <sstream>
using namespace std;

string to_string(int number)
{
    stringstream ss;
    ss<<number;
    return ss.str();
}

int main(int argc, char ** argv)
{
    string number = "1113122113";
    cout<<number<<endl;
    int maxCycles = 50, cycle = 1, i=0;

    for (cycle=1; cycle<=maxCycles; ++cycle)
    {
        string newNum = "";
        for (i=0; i<number.size(); )
        {
            char symbol = number[i];
            int symbolCount = 0;
            while (i<number.size() && number[i]==symbol)
            {
                ++i;
                ++symbolCount;
            }
          
            newNum += to_string(symbolCount);
            newNum += symbol;
        }
        number = newNum; //new number to current
        cout<<cycle<<". number length: "<<number.size()<<endl;
    }
    return 0;
}
/*
	public static void main(String args[])
	{
		String number = "1113122113";
		int maxCycles = 50;

		for (int cycle=1; cycle<=maxCycles; ++cycle)
		{
			String newNum = new String();
			for (int i=0; i<number.length(); )
			{
				char symbol = number.charAt(i);
				//System.out.println("Keresett symbol: "+symbol+" indexe:"+(i));
				int symbolCount = 0;
				while (i<number.length() && number.charAt(i)==symbol)
				{
					++i;
					++symbolCount;
				}
				newNum+=Integer.toString(symbolCount);
				newNum+=symbol;
			}
		//	System.out.println(newNum.length());
			number = newNum; //new number to current
			System.out.println(cycle+". number: "+number.length());
		}

	}
*/
