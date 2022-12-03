public class JomoPipi {
 
    public static char[][] shift(char[][] m, int n) {
        n = n % (m.length * m[0].length);
        for(int i = 0; i < n; i++){
            m = oneMove(m);
        }
        return m;
    }

    public static char[][] oneMove(char[][] m) {
        char[][] res = new char[m.length][m[0].length];
        for (int i = 0; i < m.length; i++) {
            for (int j = 0; j < m[i].length; j++) {
                if (j != m[i].length - 1) {
                    res[i][j + 1] = m[i][j];
                } else if (i != m.length - 1) {
                    res[i + 1][0] = m[i][j];
                } else {
                    res[0][0] = m[i][j];
                }
            }
        }
        return res;
    }
}
//https://www.codewars.com/kata/5afd3c451839f13b95000132/train/java