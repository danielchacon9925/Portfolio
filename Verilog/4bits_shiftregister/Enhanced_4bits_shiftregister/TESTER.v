module tester(
    // Inputs
    output reg CLK,
    output reg ENB,
    output reg DIR,
    output reg S_IN,
    output reg [1:0] MODO,
    output reg [3:0] D,
    // Outputs
    input [3:0] Q,
    input S_OUT
);

// CLK generator logic
initial begin
    CLK = 0;
end
always begin
    #1 CLK <= !CLK;
    
end

initial begin
    // Display
    $dumpfile("Test_4bits_shiftregister.vcd");
    $dumpvars(0, testbench);
    $display("\t\t------------------------------------------");
    $display("\t\tTime\| clk \|  DIR  \|  S_IN \|  MODO  \| S_OUT");
    $display("\t\t------------------------------------------");
    $monitor( $time, "|\t%b |\t%b |\t%b |\t%b |\t%b ", CLK, DIR, S_IN, MODO, S_OUT);

    ENB = 0;
    #8
    ENB = 1;
    //////////////////
    // RESET PRETEST//
    //////////////////
    // Delay to complete 1 period
    #2
    // RESET MODE ON
    MODO[1:0] = 2'b11;
    // Delay to complete 1 period
    #2

    //////////////////////////
    // TEST 1: Left ROTATION//
    //////////////////////////
    // PARALEL INITIAL
    MODO[1:0] = 2'b10;
    // Left direction
    DIR = 1'b0;
    S_IN = 1'b1;
    D[3:0] = 4'b0000;
    // Delay to complete 4 period
    #10
    // Shift
    MODO[1:0] = 2'b00;
    // Delay to complete 4 period
    #10

    ///////////////////////////////////
    ////////////// RESET ////////////// 
    ///////////////////////////////////
    // RESET MODE ON
    MODO[1:0] = 2'b11;
    // Delay to complete 1 period
    #2

    ///////////////////////////
    // TEST 2: Right ROTATION//
    ///////////////////////////
    // PARALEL INITIAL after reset 
    MODO[1:0] = 2'b10;
    #10
    // Right direction
    DIR = 1'b1;
    S_IN = 1'b1;
    #2
    // Shift
    MODO[1:0] = 2'b00;
    // Delay to complete 4 period
    #10

    ///////////////////////////////////
    ////////////// RESET ////////////// 
    ///////////////////////////////////
    // RESET MODE ON
    MODO[1:0] = 2'b11;
    // Delay to complete 1 period
    #2

    ///////////////////////////////////
    // TEST 3: CIRCULAR LEFT ROTATION//
    ///////////////////////////////////
    // PARALEL INITIAL
    MODO[1:0] = 2'b10;
    #2
    D[3:0] = 4'b1010;
    // Delay to complete 4 period
    #10
    // CIRCULAR LEFT
    DIR = 1'b0;
    MODO[1:0] = 2'b01;
    #10

    ///////////////////////////////////
    ////////////// RESET ////////////// 
    ///////////////////////////////////
    // RESET MODE ON
    MODO[1:0] = 2'b11;
    // Delay to complete 1 period
    #2

    ///////////////////////////////////
    // TEST 4: CIRCULAR RIGHT ROTATION//
    ///////////////////////////////////
    // PARALEL INITIAL
    MODO[1:0] = 2'b10;
    #2
    D[3:0] = 4'b1010;
    // Delay to complete 4 period
    #10
    // CIRCULAR RIGHT
    DIR = 1'b1;
    MODO[1:0] = 2'b01;
    #10

    ///////////////////////////////////
    ////////////// RESET ////////////// 
    ///////////////////////////////////
    // RESET MODE ON
    MODO[1:0] = 2'b11;
    // Delay to complete 1 period
    #2

    ///////////////////
    // TEST 5:PARALEL//
    ///////////////////
    // PARALEL INITIAL
    MODO[1:0] = 2'b10;
    #2
    DIR = 1'b1; 
    D[3:0] = 4'b0000;
    #10
    DIR = 1'b0; 
    D[3:0] = 4'b1111;
    #10
    ENB = 0;
    #300 
    $finish;
end


endmodule