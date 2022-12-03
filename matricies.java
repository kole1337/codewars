public class Matrices {
  public static int[][] multiply(int[][] a, int[][] b) {
    return a[0].length != b.length
        ? null
        : java.util.stream.IntStream.range(0, a.length).mapToObj(r ->
          java.util.stream.IntStream.range(0, b[0].length).map(c ->
            java.util.stream.IntStream.range(0, b.length).map(i ->
              a[r][i] * b[i][c]
            ).sum()
          ).toArray()
        ).toArray(int[][]::new);
  }
}
//https://www.codewars.com/kata/59e779513d09a7b1090000b1/train/java