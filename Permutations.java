import java.io.*;
import java.util.*;

public class ShortestPath
{	
	public static void main(String args[])
	{
		permute("","abcd");
	}
	
	public static void permute(String completed, String notCompleted)
	{
		if (notCompleted.length()==0)
			return;
		
		for (int i=0; i<notCompleted.length(); ++i)
		{
			String next = completed + notCompleted.charAt(i);
			String remaining = notCompleted.substring(0, i) + notCompleted.substring(i+1);
			System.out.println(completed+notCompleted);
			permute(next, remaining);
		}
	}
}
