public class Kata {
    public static int[][] rotateCounterclockwise(int[][] matrix, int times) {
        for (int i = 0; i < times % 4; i++) {
            matrix = rotateOneTime(matrix);
        }
        return matrix;
    }

    private static int[][] rotateOneTime(int[][] matrix) {
        int[][] result = new int[matrix.length][matrix[0].length];
        for (int i = matrix.length - 1, a = 0; i >= 0; i--, a++) {
            for (int j = 0; j < matrix[0].length; j++) {
                result[i][j] = matrix[j][a];
            }
        }
        return result;
    }
}
//https://www.codewars.com/kata/5919f3bf6589022915000023/train/python