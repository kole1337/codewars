public class Kata {
  
    public static double[][] getMatrixProduct(double[][] a, double[][] b) {
    double[][] result;
    if (a[0].length == b.length) {
      result = new double[a.length][b[0].length];
      for (int i = 0; i < a.length; i++) {
        for (int j = 0; j < b[0].length; j++) {
          for (int k = 0; k < a[0].length; k++) {
            result[i][j] += a[i][k] * b[k][j];
          }
        }
      }
    } else {
      result = null;
    }

    return result;
  }
}
//https://www.codewars.com/kata/573248f48e531896770001f9/train/python