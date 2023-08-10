module BUF(A, Y);
  input A;
  output Y;
  assign #1 Y = A;
endmodule

module NOT(A, Y);
  input A;
  output Y;
  assign #1 Y = ~A;
endmodule

module NAND(A, B, Y);
  input A, B;
  output Y;
  assign #2 Y = ~(A & B);
endmodule

module NOR(A, B, Y);
  input A, B;
  output Y;
  assign #2  Y = ~(A | B);
endmodule

module DFF(D, C, Q);
  input D;
  input C;
  output reg Q;
  always @(posedge C) Q <= #4 D;
endmodule