---
b: https://blendedfeelings.com/software/low-level/assembly-language/directives.md
---

# Assembly code directives 
also known as pseudo-operations or assembler directives, are instructions that are not executed by the CPU but are used by the assembler during the assembly process. They provide guidance to the assembler on how to process the assembly code, manage the assembly environment, or control the layout of the generated machine code.

Here are some common assembly directives used in various assembly languages:

1. **Data Definition Directives:**
   - `.DB` or `BYTE`: Define a byte of data.
   - `.DW` or `WORD`: Define a word of data (typically 2 bytes).
   - `.DD` or `DWORD`: Define a double word of data (typically 4 bytes).
   - `.DQ` or `QWORD`: Define a quad word of data (typically 8 bytes).
   - `.DT` or `TBYTE`: Define a ten-byte (80-bit) data.

2. **Section Directives:**
   - `.SECTION` or `.SEGMENT`: Define a new section or segment in the code, such as `.data` for data segment, `.text` for code segment, or `.bss` for uninitialized data.

3. **Macro and Procedure Directives:**
   - `MACRO` and `ENDM`: Define and end a macro.
   - `PROC` and `ENDP`: Define and end a procedure.

4. **Equates and Variables:**
   - `EQU`: Define a constant value.
   - `=`: Alias for `EQU` in some assemblers.

5. **Control Directives:**
   - `.IF`, `.ELSE`, `.ENDIF`: Conditional assembly directives.
   - `.REPEAT` or `.REPT`, `.ENDR`: Repeat a block of code a specified number of times.
   - `.INCLUDE`: Include external files into the source code.

6. **Alignment and Padding Directives:**
   - `ALIGN`: Align the next instruction or data on a specified byte boundary.
   - `ORG`: Set the origin address for the following code or data.

7. **Other Directives:**
   - `GLOBAL` or `EXTERN`: Declare global labels or external references.
   - `END`: Indicate the end of the source file.

Different assemblers might use slightly different syntax or names for these directives, and some directives may be specific to a particular assembler. It's important to consult the documentation for the assembler you are using to understand the exact syntax and semantics of the directives it supports.


```plaintext
Assembly Program Pseudocode:

// Define a section for data
Data Section:
    // Define an array of integers with predefined values
    ARRAY: .DW 10, 20, 30, 40, 50

    // Define a variable to store the sum of the array elements
    SUM: .DW 0

// Define a section for code
Code Section:
    // Start of the main program code
    MAIN:
        // Load the address of the ARRAY into a register (e.g., BX)
        MOV BX, OFFSET ARRAY

        // Load the array size into a register (e.g., CX)
        MOV CX, 5  // Assuming the array has 5 elements

        // Clear the accumulator register (e.g., AX) to store the sum
        XOR AX, AX

    // Loop to iterate over the array and calculate the sum
    SUM_LOOP:
        // Check if the loop counter (CX) is zero (end of array)
        // If zero, jump to the end of the loop
        JZ END_LOOP

        // Add the value pointed by BX to AX
        ADD AX, [BX]

        // Increment the pointer to the next array element
        ADD BX, 2  // Assuming each integer is 2 bytes

        // Decrement the loop counter
        DEC CX

        // Jump back to the start of the loop
        JMP SUM_LOOP

    // End of the loop
    END_LOOP:
        // Store the sum (AX) into the SUM variable
        MOV [SUM], AX

        // Print the sum (This would be done using a system call or an interrupt)
        PRINT "The sum of the array is: ", AX

    // End the program
    END MAIN
```

This pseudocode represents a simple assembly program that calculates the sum of an array of integers. The actual assembly syntax will vary depending on the specific architecture and assembler being used. The `PRINT` operation is not an actual assembly instruction but represents a hypothetical system call or interrupt to output the result.