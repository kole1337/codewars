import java.util.stream.IntStream;
public class Kata {
  public static int[][] matrixAddition(int[][] a, int[][] b) {
    IntStream.range(0, a.length * a.length)
                 .forEach(n -> a[n / a.length][n % a.length] += b[n / a.length][n % a.length]);
        return a;
  }
}
//https://www.codewars.com/kata/526233aefd4764272800036f/train/python