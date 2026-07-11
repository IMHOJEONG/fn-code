import org.junit.Test;

import static org.hamcrest.Matchers.is;
import static org.junit.Assert.assertThat;

public class BowlingGameTest {

    @Test
    public void scoreStartsAtZero() {
        assertThat(new BowlingGame().score(), is(0));
    }
}
