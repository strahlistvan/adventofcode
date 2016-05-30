import java.io.*;
import java.util.*;

public class NiceOrNaughty 
{
	
	public static boolean isNice1(String word)
	{
		String[] bad = {"ab", "cd", "pq", "xy"};
		String[] vowel = {"a", "e", "i", "o", "u"};
		int vovelCount = 0;
		boolean hasDouble = false;
		
		for (int i=0; i<word.length(); ++i)
		{
			if (Arrays.asList(vowel).contains(word.substring(i, i+1))) //i. char vowel?
				++vovelCount;
		}		
		if (vovelCount<3) 
			return false;
		
		for (int i=0; i<word.length()-1; ++i)
		{
			String sub = word.substring(i, i+2);
			if (Arrays.asList(bad).contains(sub)) //contains bad word?
				return false;
			if (sub.charAt(0)==sub.charAt(1))
				hasDouble = true;
		}
		
		return hasDouble;
	}
	
	public static boolean isNice2(String word)
	{
		boolean found = false;
		//check repeat with exactly 1 letter between them
		for (int i=0; i<word.length()-2; ++i)
		{
			String sub = word.substring(i, i+3);
			if (sub.charAt(0) == sub.charAt(2))
				found = true;
		}
		if (!found)
			return false;
			
		//check pairs without overlapping
		for (int i=0; i<word.length()-1; ++i)
		{
			for (int j=i+2; j<word.length()-1; ++j)
			{
				if (word.substring(i, i+2).equals(word.substring(j, j+2)) )
					return true;
			}
		}
		return false;
	}

public static void main (String[] args)
{
	String fileName = "";
	try 
	{
		fileName = args[0]; //fileName from argument!
		BufferedReader reader = new BufferedReader(new FileReader(fileName) );
		String line = reader.readLine();
		int nice1Count = 0, nice2Count = 0;
		while (line!=null)
		{
			if (isNice1(line)) 
				++nice1Count;
			if (isNice2(line))
			   ++nice2Count;
			line = reader.readLine();
		}
		System.out.println("Nice1 words in "+fileName+": "+nice1Count);
		System.out.println("Nice2 words in "+fileName+": "+nice2Count);
	}
	catch(ArrayIndexOutOfBoundsException ex)
	{
		System.out.println("Program argument: <input file name>");
		ex.printStackTrace();
	}
	catch (FileNotFoundException ex)
	{
		System.out.println("File not found: "+fileName);
		ex.printStackTrace();
	}
	catch(Exception ex)
	{
		System.out.println("Fatal error!");
		ex.printStackTrace();
	}
}
}
