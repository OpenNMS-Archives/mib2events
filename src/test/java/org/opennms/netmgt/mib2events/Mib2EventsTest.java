package org.opennms.netmgt.mib2events;

import static org.junit.Assert.assertTrue;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import org.junit.Test;


/**
 * Unit test for simple App.
 */
public class Mib2EventsTest {

    @Test
    public void testConvertSimpleMibFile() throws Exception {
        Mib2Events convertor = new Mib2Events();
        convertor.convert("src/test/resources/UCD-SNMP-MIB.txt");
        
        final ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        final PrintStream printStream = new PrintStream(outputStream);
        
        convertor.printEvents(printStream);
        
        final String output = outputStream.toString("UTF8");
        
        System.err.println(output);

        assertTrue(output.contains("agent start"));
    }
}
