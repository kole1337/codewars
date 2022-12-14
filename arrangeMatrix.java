class JomoPipi {
  static char[][] diagonalSort(char[][] data) {
    char[][] sorted = new char[data.length][data[0].length];
    int x = 0, y = 0;
    for (char[] row : data)
      for (char el : row) {
        sorted[x--][y++] = el;
        if (x < 0 || y > row.length - 1) {
          x += y + 1;
          y = 0;
          if (x > data.length - 1) {
            y = x - data.length + 1;
            x -= y;
          }
        }
      }
    return sorted;
  }
}
//https://www.codewars.com/kata/5ab1f8d38d28f67410000090/train/python