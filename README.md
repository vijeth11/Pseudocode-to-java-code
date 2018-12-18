# Pseudocode-to-java-code

This is a program which takes the pseudo code instructions and create a executable java code. It is still in development now it is able to
write for loop, if else and elsif condition and print statements. 


ex:<br />
enter the file nametest3<br />
enter the code<br />

for 5 times<br />
if 'for1 eq 2'<br />
print ' if condition working'<br />
End if<br />
elif 'for1 eq 3'<br />
print 'else if is working'<br />
End else if<br />
else<br />
print 'else is Working'<br />
End else<br />
End for<br />
End<br />
<br />
output code:<br />
public class test3 {<br />
<br />
  public static void main(String[] args) <br />
   { <br />
     for( int D=0;D<5;D++) <br />
     {<br />
        if (D == 2)<br />
        {<br />
          System.out.println(" if condition working");<br />
        }<br />
        else if (D == 3) <br />
        {<br />
          System.out.println("else if is working");<br />
        }<br />
        else <br />
        {<br />
           System.out.println("else is Working");<br />
        }<br />
      }<br />
    }<br />
}<br />
