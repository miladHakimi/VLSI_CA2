`timescale 1ns/1ps

module part1TB();
	`define NULL 0    

	reg [7:0] A, B;
	wire [15:0] P;
	reg[7:0] A1, B1;
	reg clk = 1'b0;
	reg[15:0] captured_data;
	integer	data_file; // file handler
	integer	scan_file; // file handler
	
	part1 p1(A, B, P);
	

	initial begin
	  data_file = $fopen("input.txt", "r");
	  if (data_file == `NULL) begin
	    $display("data_file handle was NULL");
	    $finish;
	  end
	end

	always @(posedge clk) begin
	  scan_file = $fscanf(data_file, "%b\n", captured_data); 
	  if (!$feof(data_file)) begin
	  	{A, B} = captured_data;
	  end
	end

	initial begin
		repeat(103000)
			#20 clk = ~clk;
	end
endmodule