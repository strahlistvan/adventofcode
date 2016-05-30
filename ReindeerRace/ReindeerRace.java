import java.io.*;
import java.util.*;

public class ReindeerRace 
{
	public static ArrayList<Reindeer> Reindeers = new ArrayList<Reindeer>();
	public static Hashtable<String, Integer> ReindeerScore = new Hashtable<String, Integer>();
	
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
				ArrayList<String> leadersName = getLeadersName();
				for (int i=0; i<leadersName.size(); ++i)
				{
					int leaderScore = ReindeerScore.get(leadersName.get(i)) + 1;
					ReindeerScore.put(leadersName.get(i), leaderScore);
				}
			}
			//Print the final distances
			System.out.println(Reindeers);
			//Print the final scores
			System.out.println(ReindeerScore);
			
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
			ReindeerScore.put(name, 0); //for the second part
			line = reader.readLine();
		}
		reader.close();
	}
	
	public static ArrayList<String> getLeadersName()
	{
		int maxDistance = Reindeers.get(0).getDistance();
		ArrayList<String> leadersName = new ArrayList<String>();
		
		for (int i=0; i<Reindeers.size(); ++i)
		{
			if (Reindeers.get(i).getDistance() == maxDistance) 	//multiple lead
			{
				leadersName.add(Reindeers.get(i).getName());
			}
			else if (Reindeers.get(i).getDistance() > maxDistance) //new leader
			{
				maxDistance = Reindeers.get(i).getDistance();
				leadersName.clear();
				leadersName.add(Reindeers.get(i).getName());
			}
		}
		return leadersName;
	}
}
