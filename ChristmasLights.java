import java.io.*;
import java.util.*;

public class ChristmasLights
{
	static int[][] lights = new int[1000][1000];
	static String fileName = "";
	static int mode = 1;

	/** Count total brightness (used in mode 2) */
	public static int totalBrightness()
	{
		int total = 0;
		for (int i=0; i<lights.length; ++i)
		{
			for (int j=0; j<lights[i].length; ++j)
			{
				total+=lights[i][j];
			}
	   }
	   return total;
	}
	
	/** Count lightnings (used in mode 1) */
	public static int countLightings()
	{
		int count = 0;
		for (int i=0; i<lights.length; ++i)
		{
			for (int j=0; j<lights[i].length; ++j)
			{
			   if (lights[i][j]==1)
			   	++count;
			 }
	   }
	   return count;
	}
	
	public static void changeLights(int start_x, int start_y, int end_x, int end_y, int sign, int mode)
	{
		for (int x=start_x; x<=end_x; ++x)
		{
			for (int y=start_y; y<=end_y; ++y)
			{
				if (mode==1)
				{
					if (sign==2)
					{
						if (lights[x][y]==1)
							lights[x][y] = -1;
						else 
							lights[x][y] = 1;
					}
					else 
						lights[x][y] = sign;
				}
				else if (mode==2) 
				{
					lights[x][y]+=sign;
					if (lights[x][y] < 0)
						lights[x][y] = 0;
				}
			}
		}
	}
	
	public static void main(String args[])
	{
		try 
		{
			fileName = args[0];
			mode = Integer.parseInt(args[1]);
			
			//reading input file
			BufferedReader reader = new BufferedReader(new FileReader(fileName));
			String line = "";
			while((line = reader.readLine()) != null) 
			{
				String[] arr = line.split("\\s|,"); //split line to array
				if (arr[0].equals("turn"))
				{
					int start_x = Integer.parseInt(arr[2]);
					int start_y = Integer.parseInt(arr[3]);
					int end_x   = Integer.parseInt(arr[5]);
					int end_y   = Integer.parseInt(arr[6]);
				
					if (arr[1].equals("on") ) //turn on
						changeLights(start_x, start_y, end_x, end_y, 1, mode);
					else  //turn off
						changeLights(start_x, start_y, end_x, end_y, -1, mode);
				}
				else //toggle
				{
					int start_x = Integer.parseInt(arr[1]);
					int start_y = Integer.parseInt(arr[2]);
					int end_x   = Integer.parseInt(arr[4]);
					int end_y   = Integer.parseInt(arr[5]);
					changeLights(start_x, start_y, end_x, end_y, 2, mode);
				}
		   }   
         reader.close();  
         if (mode==1)
         	System.out.println("Lighting lights: "+countLightings());
         else
         	System.out.println("Total brightness: "+totalBrightness() );
		}
		catch (FileNotFoundException ex)
		{
			System.out.println("File not found: "+fileName);
			ex.printStackTrace();
		}
		catch (IOException ex)
		{
			System.out.println("Error while reading file: "+fileName);
			ex.printStackTrace();
		}
		catch (IndexOutOfBoundsException ex)
		{
			System.out.println("Program's arguments: Input file name, Mode: 1 - count lights, 2 - count total brightness");
			ex.printStackTrace();
		}
		
		catch (Exception ex)
		{
			System.out.println("Fatal error!");
			ex.printStackTrace();
		}
	}
}
