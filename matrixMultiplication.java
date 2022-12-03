public class Kata {

  public static int[][] matrixMultiplication(int[][] a, int[][] b) {
    int n = a.length;
    int[][] res = new int[n][n];
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        for (int k = 0; k < n; k++) {
          res[i][j] += a[i][k] * b[k][j];
        }
      }
    }
    return res;
  }
}