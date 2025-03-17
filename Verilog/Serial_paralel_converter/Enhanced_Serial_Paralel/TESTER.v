module TESTER(
    input P_VALID,
    input S_OUT,
    input [31:0] P_OUT,
    output reg CLK,
    output reg RESET,
    output reg S_START,
    output reg S_IN,
    output reg [31:0] P_IN
);

// CLK generator
initial begin
    CLK = 0;
end
always begin
    #1 CLK <= !CLK;
end


// TEST
initial begin
    // Display
    $dumpfile("seriestoparalel.vcd");
    $dumpvars(0, testbench); 
    $display("\t\t------------------------------------------");
    $display("\t\tTime\| CLK \|  S_START  \|  S_IN \|  S_OUT  \| P_OUT");
    $display("\t\t------------------------------------------");
    $monitor( $time, "|\t%b |\t%b |\t%b |\t%b |\t%b ", CLK, S_START, S_IN, S_OUT, P_OUT);

    RESET = 0;
    S_START = 0;   
    #2
    RESET = 1;
    #2
    // Paralel to series
    S_START = 1;
    P_IN = 32'b00000000000000001111111111111111;
    #64
    RESET = 0;
    // Series to paralel
    #1 
	S_IN <= 1;
    #1 
	S_IN <= 0;
    #1 
	S_IN <= 1;
    // Test de FSM en medio de 0X5A
    #1 
	S_IN <= 0;
    #1 
	S_IN <= 1;
    #1 
	S_IN <= 0;
    #1 
	S_IN <= 1;
    #1 
	S_IN <= 0;
    // Word of confirmation
    // Two PERIODS
    #4
	S_IN <= 1;
    #1 
	S_IN <= 0;
    #1 
	S_IN <= 1;
    #1 
	S_IN <= 0;
    #1 
	S_IN <= 1;
    #1 
	S_IN <= 0;
    #1 
	S_IN <= 1;
    #1 
	S_IN <= 0;
    #1 
	S_IN <= 1;
    #1 
	S_IN <= 0;
    #1 
	S_IN <= 1;
    #1 
	S_IN <= 0;
    #1 
	S_IN <= 1;
    #1 
	S_IN <= 0;
    #1 
	S_IN <= 1;
    #1 
	S_IN <= 0;
    #1 
    S_IN <= 1;
    #1 
	S_IN <= 0;
    #1 
	S_IN <= 1;
    #1 
	S_IN <= 0;
    #1 
	S_IN <= 1;
    #1 
	S_IN <= 0;
    #1 
	S_IN <= 1;
    #1 
	S_IN <= 0;
    #1 
	S_IN <= 1;
    #1 
	S_IN <= 0;
    #1 
	S_IN <= 1;
    #1 
	S_IN <= 0;
    #1 
	S_IN <= 1;
    #1 
	S_IN <= 0;
    #1 
	S_IN <= 1;
    #1 
	S_IN <= 0;

    #150
    RESET = 0;
    #5
    $finish;
end
endmodule
