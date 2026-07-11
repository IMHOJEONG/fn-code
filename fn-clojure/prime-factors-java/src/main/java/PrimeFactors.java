import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class PrimeFactors {

    /**
     *  1) 첫 번째 코드 
     *  ArrayList<Integer> factors = new ArrayList<>();
        if (n > 1) {
            factors.add(n);
            return factors;
        }
        
        return factors;


        ArrayList<Integer> factors = new ArrayList<>();
        if (n > 1) {

            //
            // 2) 두 번째 수정
            // if (n % 2 == 0) {
            //     factors.add(2);
            //     n /= 2;
            // }
            // 
            while (n % 2 == 0) {
                factors.add(2);
                n /= 2;
            }

        }
        if (n > 1) {
            factors.add(n);
        }
        return factors;

     */
    public static List<Integer> factorsOf(int n) {

        // if (n <= 1) {
        //     return Collections.emptyList();
        // }

        ArrayList<Integer> factors = new ArrayList<>();

        for (int divisor = 2; n > 1; divisor++) {
            for (; n % divisor == 0; n /= divisor) {
                factors.add(divisor);
            }
        }
        return factors;



        // throw new UnsupportedOperationException("Prime factorization is not implemented yet.");
    }
}
