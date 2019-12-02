import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Task2
{
    public static void main(String[] args)
    {
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                int[] initialIntcode = getInitialIntcode();
                initialIntcode[1] = i;
                initialIntcode[2] = j;

                if (runIntcode(initialIntcode)[0] == 19690720) {
                    System.out.println("noun: " + i + " verb: " + j);
                    return;
                }

            }
        }
    }

    private static int[] runIntcode(int[] intcode)
    {
        int instructionPosition = 0;
        int instruction = intcode[instructionPosition];
        while (instruction != 99) {
            int readPos1 = intcode[instructionPosition + 1];
            int readPos2 = intcode[instructionPosition + 2];
            int writePos = intcode[instructionPosition + 3];

            if (instruction == 1) {
                intcode[writePos] = intcode[readPos1] + intcode[readPos2];
            } else if (instruction == 2) {
                intcode[writePos] = intcode[readPos1] * intcode[readPos2];
            } else {
                System.out.println("Invalid instruction: " + instruction);
                return intcode;
            }

            instructionPosition += 4;
            instruction = intcode[instructionPosition];
        }

        return intcode;
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
