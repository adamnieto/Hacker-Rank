import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        for(int i=1; i <= t; i++){
            String answer = "";
            int a = scan.nextInt();
            int b = scan.nextInt();
            int n = scan.nextInt();
            int previousTerms = 0;
            for(int power = 0; power <= n-1; power++){
                if (power == 0){
                   int currentTerm = a + (int)(Math.pow(2,power)) * b;
                   int finalOutput = currentTerm + previousTerms;
                   previousTerms += currentTerm;
                   answer += Integer.toString(finalOutput) + " ";
                }
                else{
                     int currentTerm = (int)(Math.pow(2,power)) * b;
                     int finalOutput = currentTerm + previousTerms;
                     previousTerms += currentTerm;
                     answer += Integer.toString(finalOutput) + " ";
                }
                
                
            } 
            System.out.println(answer);
        }
        
    }
}