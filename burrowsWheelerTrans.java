import java.util.Arrays;

public class BurrowsWheeler {
    
  
    public static BWT encode(String s) {
    String[] list = new String[s.length()];
    int counter = 0;

    for (int i = 0; i < s.length(); ++i){
      list[i] = s.substring(i) + s.substring(0, i);
    }

    Arrays.sort(list);

    StringBuilder builder = new StringBuilder();

    for (int i = 0; i < list.length; ++i){
      builder.append(list[i].charAt(list[i].length() - 1));
      if (list[i].equals(s)) counter = i;
    }
    return new BWT(builder.toString(), counter);
  }

  public static String decode(String s, int n) {
    if (s.length() == 0) return "";

    String[] list = s.split("");
    Arrays.sort(list);

    for (int j = 0; j < list.length - 1; j++){
      for (int i = 0; i < list.length; i++) {
        list[i] = s.charAt(i) + list[i];
      }
      Arrays.sort(list);
    }
    return list[n];
  }
}
//https://www.codewars.com/kata/54ce4c6804fcc440a1000ecb/train/python