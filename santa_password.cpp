#include <iostream>
using namespace std;

long long text_to_value(string str)
{
    long long result = 0;
    for (int i = 0; i<str.size(); i++)
    {
		result*=26;
        result+= (str[i] - 'a' )+1;
    }
    return result-1;
}

string value_to_text(long long value)
{
    string result = "";
    while (value >= 0)
    {
        result = (char)('a' + value%26) + result;
        value /= 26;
        --value;
    }
    return result;
}

bool is_valid(string text)
{
	bool isOK = false;
	if (text[0]=='i' || text[0]=='o' || text[0]=='l'|| text[1]=='i' || text[1]=='o' || text[1]=='l')
		return false;
	for (int i=2; i<text.size(); i++)
	{
		if (text[i]=='i' || text[i]=='o' || text[i]=='l')
			return false;
		
		if (text[i-2]==text[i-1]-1 && text[i-1]==text[i]-1)
			isOK = true;
	}
	if (!isOK)
		return false;
	
	isOK = false;	
	for (int i=0; i<text.size()-1; ++i)
		{
			for (int j=i+2; j<text.size()-1; ++j)
			{
				if (text[i]==text[i+1] && text[j]==text[j+1] )
					isOK = true;
			}
		}	
	return isOK;
}

int main(int argc, char ** argv)
{
	if (argc < 2)
	{
		cout<<"Usage: "<<argv[0]<<" <starter_password> "<<endl;
		return -1;
	}
		
	string current_text(argv[1]);
	cout<<"Megyen....\n";
	long long current_num = text_to_value(argv[1]);
	do
	{
		cout<<current_text<<endl;
		++current_num;
		current_text = value_to_text(current_num);
	}
	while (!is_valid(current_text));
	cout<<current_text<<endl;
	return 0;
}
