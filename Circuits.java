import java.io.*;
import java.util.*;

public class Circuits
{
	static Hashtable<String, Short> wires = new Hashtable<String, Short>();
	
	public static void main(String[] args)
	{
		String fileName = ""; //input file name from args
		ArrayList<String[]> allRules = new ArrayList<String[]>();
		try 
		{
			fileName = args[0];
			BufferedReader reader = new BufferedReader(new FileReader(fileName));
			String line = reader.readLine();
			while (line!=null)
			{
				String[] array = line.split("\\s");
				initWires(array);
				allRules.add(array);
				line = reader.readLine();
			}
			reader.close();
			
			for (int i=0; i<allRules.size(); ++i)
			{
				setWires(allRules.get(i));
			}
			printWireValue("a");

		}
		catch (FileNotFoundException ex)
		{
			System.out.println("File not found: "+fileName);
			ex.printStackTrace();
		}
		catch (Exception ex)
		{
			System.out.println("Fatal error: "+ex);
			ex.printStackTrace();
		}
	}
	
	public static void printWireValue(String wireNum)
	{
		System.out.println(wires);
		int result = (int)wires.get(wireNum);
		if (result<0)
			result = result + 65536;
		if (result!=0)
			System.out.println("Az eredmeny: "+result);
	}
	
	public static boolean isNumeric(String str)  
	{  
	  return str.matches("\\d+"); 
	}
		
	public static void initWires(String[] rules_arr)
	{
		short value = 0;
		String key = rules_arr[rules_arr.length-1];
		wires.put(key, value);
		if (!isNumeric(rules_arr[0]) && !rules_arr[0].equals("NOT"))
			wires.put(rules_arr[0], value);
		if (!isNumeric(rules_arr[2]) && !rules_arr[2].equals("->"))
			wires.put(rules_arr[2], value);
	}
	
	public static short getValue(String str)
	{
		if (isNumeric(str))
			return Short.parseShort(str);
		else
			return wires.get(str);
	}
	
	public static void setWires(String[] rules_arr) throws Exception
	{
		String key = rules_arr[rules_arr.length-1];
		short value = 0;
	
		if (rules_arr.length == 3) //put value to wire
		{
			value = getValue(rules_arr[0]);
			//System.out.println(key+"-be Beleteszi: "+value);
		}
		else if (rules_arr.length == 4) //put negated value to wire
		{
			//System.out.println(key+"-be: NEM "+rules_arr[1]);
			value = getValue(rules_arr[1]);
			value =(short) ~value; //binary not
		}
		else if (rules_arr.length == 5)
		{
			//System.out.println(key+"-be "+rules_arr[0] +" "+ rules_arr[1] +" "+ rules_arr[2]);
			String opr = rules_arr[1];
			short op1 = getValue(rules_arr[0]);
			
			if (opr.equals("RSHIFT"))
			{
				short op2 = Short.parseShort(rules_arr[2]);
				value = (short) (op1 >> op2);
			}
			else if (opr.equals("LSHIFT"))
			{
				short op2 = Short.parseShort(rules_arr[2]);
				value = (short) (op1 << op2);
			}
			else if (opr.equals("AND"))
			{
				short op2 = getValue(rules_arr[2]);
				value = (short) (op1 & op2);
			}
			else if (opr.equals("OR"))
			{
				short op2 = getValue(rules_arr[2]);
				value = (short) (op1 | op2);
			}
		}
		wires.put(key, value); //add the new value to wires
	}
}
