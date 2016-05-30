public class LookAndSay
{
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
}
