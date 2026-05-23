import org.junit.Test;

import static org.hamcrest.Matchers.contains;
import static org.hamcrest.Matchers.empty;
import static org.hamcrest.Matchers.is;
import static org.hamcrest.MatcherAssert.assertThat;;

public class PrimeFactorsTest {

    @Test
    public void factors() {
        assertThat(PrimeFactors.factorsOf(1), is(empty()));

        assertThat(PrimeFactors.factorsOf(3), contains(3));

        assertThat(PrimeFactors.factorsOf(4), contains(2,2));

        assertThat(PrimeFactors.factorsOf(5), contains(5));

        assertThat(PrimeFactors.factorsOf(6), contains(2,3));

        assertThat(PrimeFactors.factorsOf(7), contains(7));

        assertThat(PrimeFactors.factorsOf(8), contains(2,2,2));

        assertThat(PrimeFactors.factorsOf(9), contains(3,3));
    }
}
