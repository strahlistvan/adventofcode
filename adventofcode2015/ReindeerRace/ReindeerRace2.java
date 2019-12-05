import java.io.*;
import java.util.*;

public class ReindeerRace2
{
	public static ArrayList<Reindeer> Reindeers = new ArrayList<Reindeer>();
	
	public static void main (String[] args)
	{
		try 
		{
			String fileName = "input14_reindeers.txt";
			getReindeersFromFile(fileName);
			for (int time=1; time<=2503; ++time)
			{
				for (int i=0; i<Reindeers.size(); ++i)
				{
					Reindeers.get(i).doAction();
				}
			}
			//Print the final distances
			System.out.println(Reindeers);
			
		}
		catch (Exception ex) 
		{
			System.out.println("Fatal error: "+ex);
			ex.printStackTrace();
		}
	}
	
	public static void getReindeersFromFile(String fileName) throws Exception
	{
		BufferedReader reader = new BufferedReader(new FileReader(fileName));
		String line = reader.readLine();
		while (line!=null)
		{
			String[] arr = line.split(" ");
			String name = arr[0];
			int speed = Integer.parseInt(arr[3]);
			int maxFlyTime = Integer.parseInt(arr[6]);
			int maxRestTime = Integer.parseInt(arr[13]);
			Reindeer deer = new Reindeer(name, speed, maxFlyTime, maxRestTime);
			Reindeers.add(deer);
			line = reader.readLine();
		}
		reader.close();
	}
}