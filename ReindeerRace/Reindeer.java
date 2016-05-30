import java.io.*;
import java.util.*;

public class Reindeer 
{
	//private final int speed, maxFlyTime, maxRestTime;
	private int speed, flyTime, maxFlyTime, restTime, maxRestTime, distance;
	private String name;
	
	public Reindeer() { this.distance = 0; this.name = "";}
	
	public Reindeer(String name, int speed, int maxFlyTime, int maxRestTime)
	{
		this.speed = speed;
		this.maxFlyTime = this.flyTime = maxFlyTime;
		this.maxRestTime = maxRestTime;
		this.distance = 0;
		this.restTime = 0;
		this.name = name;
	}
	
	public int getDistance()
	{
		return this.distance;
	}
	public String getName()
	{
		return this.name;
	}
	
	public void doAction()
	{
		if (flyTime > 0)
		{
		//	System.out.println("Running! Current distance: "+distance+" km");
			distance+=speed;
			--flyTime;
			if (flyTime==0) //if finish flying, starting to rest
				restTime = 0;
		}
		else 
		{
			//System.out.println("Resting..."+(maxRestTime-restTime)+" seconds remaining");
			++restTime;
			if (restTime == maxRestTime)
				flyTime = maxFlyTime;
		}
	}
	
	public String toString()
	{
		String back = "Name: "+name+" is in "+distance+" km (speed: "+speed+" km/s for "+maxFlyTime+" s, then rest "+maxRestTime+" s)\n";
		return back;
	}
}
