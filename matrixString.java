import java.util.Arrays;
import java.util.stream.IntStream;

public class Matrix {
    
    private int[][] m;
    
    public Matrix(String mStr){
        m = Arrays.stream( mStr.split("\n") )
                  .map( line -> Arrays.stream(line.split(" "))
                                      .mapToInt( s -> Integer.parseInt(s) )
                                      .toArray() )
                  .toArray(int[][]::new);
    }

    public int[] getColumn(int c) { return IntStream.range(0,m.length).map( r -> m[r][c] ).toArray(); }
    public int[] getRow(int r)    { return Arrays.copyOf(m[r], m[0].length); }
    
    public int getRowsCount()     { return m.length;    }
    public int getColumnsCount()  { return m[0].length; }
}
//https://www.codewars.com/kata/58b9ac455927cd595a0000d4/train/java