import java.util.Arrays;
import java.util.stream.Collectors;

public class Fracts {

    public static String convertFrac(long[][] lst) {
        final Long dividor = Arrays.stream(lst)
                .map(pair -> new Long[]{pair[0], pair[1]})
                .map(Fracts::divideByGreatestCommonDivider)
                .map(longs -> longs[1])
                .reduce(1L, Fracts::leastCommonMultiple);

        return Arrays.stream(lst)
                .map(pair -> pair[0] * dividor / pair[1])
                .map(aLong -> String.format("(%d,%d)", aLong, dividor))
                .collect(Collectors.joining());
    }

    private static Long greatestCommonDivider(Long a, Long b) {
        return b == 0 ? a : greatestCommonDivider(b, a % b);
    }

    private static Long[] divideByGreatestCommonDivider(Long[] pair) {
        Long gcd = greatestCommonDivider(pair[0], pair[1]);
        return new Long[]{pair[0] / gcd, pair[1] / gcd};
    }

    private static Long leastCommonMultiple(Long a, Long b) {
        return Math.abs(a * b) / greatestCommonDivider(a, b);
    }
}

//https://www.codewars.com/kata/54d7660d2daf68c619000d95/train/java