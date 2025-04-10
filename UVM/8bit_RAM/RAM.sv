module ram (
	input [3:0] addr,
	input clk,
	input wr,
	input [7:0] din,
	output reg [7:0] dout
);

/// Memory declaration 
// 16 element memory array, each element is 8 bits wide
reg [7:0] mem [15:0]; 

always@(posedge clk)
	begin
		/// Write enable
		if (wr)	
			begin 
				/// Din write 
				mem[addr] <= din;
			end
		/// Read enable
		else 
			begin	/// Read dout
				dout <= mem[addr];
			end
	end

endmodule


/////_____Interface_____/////

interface ram_if;

logic [3:0] addr;
logic wr;
logic clk;
logic [7:0] din;
logic [7:0] dout;

endinterface
