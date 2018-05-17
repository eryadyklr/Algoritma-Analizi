using System;					
public class Program
{
	public static void Main()
	{
		 Console.Write("Küme boyutunu giriniz: ");
         int boyut = Convert.ToInt32(Console.ReadLine());
         int[] kume = new int[boyut];
         for (int i = 0; i < boyut; i++)
         {
             Console.Write(i + ".elemanı giriniz: ");
             kume[i] = Convert.ToInt32(Console.ReadLine());    
         }
         String s = "";
         for (int i = 0; i < Math.Pow(2, boyut); i++)
         {
             int b = i;
             s += "(";
             for (int j = 0; j < boyut; j++)
             {
                 if ((b & 1) == 1)
                     s += kume[j].ToString() + ",";
                 b = b >> 1;
             }
             s += "),  ";
         }
         Console.WriteLine(s);
         Console.ReadLine();
	}
}
