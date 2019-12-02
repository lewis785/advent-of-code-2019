import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

public class Task1
{
    public static void main(String[] args)
    {
        System.out.println(Arrays.toString(runIntcodes(getInitialIntcode())));
    }


    private static int[] runIntcodes(int[] intcodes)
    {
        int instructionPosition = 0;
        int instruction = intcodes[instructionPosition];
        while (instruction != 99) {
            int readPos1 = intcodes[instructionPosition + 1];
            int readPos2 = intcodes[instructionPosition + 2];
            int writePos = intcodes[instructionPosition + 3];

            if (instruction == 1) {
                intcodes[writePos] = intcodes[readPos1] + intcodes[readPos2];
            }

            if (instruction == 2) {
                intcodes[writePos] = intcodes[readPos1] * intcodes[readPos2];
            }

            instructionPosition += 4;
            instruction = intcodes[instructionPosition];
        }

        return intcodes;
    }

    private static int[] getInitialIntcode()
    {
        try {
            BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
            String line = reader.readLine();

            String[] opcodeStrings = line.split(",");
            int[] opcodes = new int[opcodeStrings.length];

            for (int i = 0; i < opcodeStrings.length; i++) {
                opcodes[i] = Integer.parseInt(opcodeStrings[i]);
            }

            return opcodes;
        } catch (IOException e) {
            e.printStackTrace();
            return new int[0];
        }
    }
}
