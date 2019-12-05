import java.io.*;
import java.util.*;
import java.lang.*;

public class Combination 
{
	public static void main(String[] args)
	{
		int[] containers = {50,44,11,49,42,46,18,32,26,40,21,7,18,43,10,47,36,24,22,40};
		int N = containers.length;
		int countOfCombination = 0; //first part
		int minContainers = N, minContainersCount = 0; //second part
		
		System.out.println(Math.pow(2, N));
		for (int i=0; i<Math.pow(2, N); ++i)
		{
			ArrayList<Integer> combination = new ArrayList<Integer>();
			for (int j=0; j<N; ++j)
			{
				if ((i & (1<<j)) != 0) //j. bit's value
					combination.add(containers[j]);
			}
			int sum = 0;
			for (int j=0; j<combination.size(); ++j)
			{
				sum+=combination.get(j);
			}
			if (sum==150) 
			{
				++countOfCombination; //first part
				//second part:
				if (combination.size() == minContainers)
				{
					++minContainersCount;
				}
				else if (combination.size() < minContainers) 
				{
					minContainers = combination.size();
					minContainersCount = 1; 
				}
			}
			
		}
		System.out.println(countOfCombination);
		System.out.println(minContainersCount);
	}
}
